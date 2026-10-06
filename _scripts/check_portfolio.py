"""Validate the committed portfolio snapshot and featured Jekyll pages."""
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / '_data/portfolio.json').read_text())
projects = {p['path']: p for p in data['projects']}
assert len(projects) == len(data['projects']), 'duplicate catalog paths'
families = {g['id'] for g in data['groups']}
assert all(p['family'] in families for p in projects.values())
for name in data['featured'] + ['hw-ml-tutorials']:
    text = (ROOT / '_projects' / (name + '.md')).read_text()
    assert 'portfolio_id: ' + name in text, name
    assert 'redirect:' not in text.split('---', 2)[1], name
    assert '{% include portfolio_project.liquid %}' in text, name
    assert name in projects, name
listed = set(re.findall(r'^  - zesun33/([^\s]+)$', (ROOT / '_data/repositories.yml').read_text(), re.M))
expected = {p['path'] for p in projects.values() if p['github']} | {'personal-projects', 'zesun33.github.io'}
assert listed == expected, (listed - expected, expected - listed)
assert 'portfolio_directory.liquid' in (ROOT / '_pages/repositories.md').read_text()
print(f'PASS: {len(projects)} catalog entries, all featured pages, and repository list')
