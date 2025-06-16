# pyright: reportMissingImports=false
#!/usr/bin/env python
"""Extract abstracts from all PDF files located under the two directories provided
by the user and save them into a markdown file for easy review.

Usage:
    python scripts/extract_abstracts.py

Dependencies:
    pip install pdfminer.six
"""
import os
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    from pdfminer.high_level import extract_text
except ImportError:
    sys.stderr.write("[ERROR] pdfminer.six is required. Install it via 'pip install pdfminer.six'\n")
    sys.exit(1)

# Directories containing the papers (update paths if needed)
BASE_DIRS = [
    r"C:\\Users\\zesun\\OneDrive - The Pennsylvania State University\\Study\\PSU\\Research\\Papers",
    r"C:\\Users\\zesun\\OneDrive - The Pennsylvania State University\\Study\\Paper work",
]

# Output file will be placed in the script's directory
OUTPUT_PATH = Path(__file__).resolve().parent / "extracted_abstracts.md"

ABSTRACT_HEADING_RE = re.compile(r"\babstract\b[:.\-\s]*", re.IGNORECASE)
SECTION_BREAK_RE = re.compile(r"\n\s*\n")


def extract_abstract_from_text(text: str) -> str | None:
    """Attempt to extract the abstract from the given PDF text."""
    match = ABSTRACT_HEADING_RE.search(text)
    if not match:
        return None

    # Text after the heading
    remainder = text[match.end():]

    # Stop at the first blank line or common section heading
    end_match = SECTION_BREAK_RE.search(remainder)
    if end_match:
        abstract = remainder[: end_match.start()].strip()
    else:
        abstract = remainder.strip()

    # Fallback: truncate very long snippets
    MAX_LEN = 4000
    if len(abstract) > MAX_LEN:
        abstract = abstract[:MAX_LEN].rsplit(" ", 1)[0] + " …"
    return abstract if abstract else None


def process_pdf(pdf_path: Path) -> str | None:
    """Extract text from the PDF (first 2 pages) and get the abstract."""
    try:
        text = extract_text(str(pdf_path), maxpages=2)  # only first couple pages for speed
    except Exception as e:
        sys.stderr.write(f"[WARN] Failed to read '{pdf_path}': {e}\n")
        return None
    return extract_abstract_from_text(text)


def main() -> None:
    abstracts: list[tuple[str, str]] = []  # (file, abstract)

    for base in BASE_DIRS:
        for root, _dirs, files in os.walk(base):
            for filename in files:
                if not filename.lower().endswith(".pdf"):
                    continue
                pdf_path = Path(root) / filename
                sys.stdout.write(f"Processing {pdf_path}\n")
                abstract = process_pdf(pdf_path)
                if abstract:
                    abstracts.append((str(pdf_path), abstract))
                else:
                    sys.stdout.write(f"    -> No abstract found\n")

    # Write output
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(f"# Extracted Abstracts\n\nGenerated on {datetime.now().isoformat(timespec='seconds')}\n\n")
        if not abstracts:
            f.write("No abstracts found.\n")
        for path, abstract in abstracts:
            rel_path = path.replace(os.sep, "/")
            f.write(f"## {os.path.basename(path)}\n")
            f.write(f"*Source*: `{rel_path}`\n\n")
            f.write(abstract.replace("\r", "") + "\n\n---\n\n")

    print(f"Completed. Extracted {len(abstracts)} abstracts. See '{OUTPUT_PATH}'.")


if __name__ == "__main__":
    main() 