# Contributing to Md Zesun Ahmed Mia's Academic Website

Thank you for your interest in contributing to this academic portfolio website. This document provides guidelines for contributing to the site's development and content.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Content Guidelines](#content-guidelines)
- [Code Standards](#code-standards)
- [Submission Process](#submission-process)

## Getting Started

This website is built with Jekyll using the al-folio academic theme and is hosted on GitHub Pages. The site automatically deploys when changes are pushed to the main branch.

### Prerequisites

- Ruby 3.3.5 or higher
- Bundler gem
- Node.js and npm (for frontend tooling)
- Python 3.13 (for Jupyter notebook conversion)
- ImageMagick (for image processing)

## Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/zesun33/zesun33.github.io.git
   cd zesun33.github.io
   ```

2. **Install Ruby dependencies:**
   ```bash
   bundle install
   ```

3. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

4. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Serve the site locally:**
   ```bash
   bundle exec jekyll serve --livereload
   ```

The site will be available at `http://localhost:4000`.

## Content Guidelines

### Publications

Publications are managed through BibTeX in `_bibliography/papers.bib`. When adding new publications:

- Use proper BibTeX formatting
- Include `bibtex_show={true}` for display
- Add `selected={true}` for featured publications
- Include PDF files in the repository when possible
- Add abstracts and relevant metadata

### CV Updates

The CV is managed through `_data/cv.yml`. Follow the existing YAML structure:

- Use consistent formatting for dates
- Include proper institution names and locations
- Add descriptions as YAML lists for better formatting
- Maintain chronological order (most recent first)

### News and Announcements

Add news items to the `_news/` directory:

- Use the format: `YYYY-MM-DD-title.md`
- Include proper front matter with date and inline settings
- Keep announcements concise and professional

### Projects

Projects are managed in the `_projects/` directory:

- Include proper front matter with title, description, and category
- Add relevant images to `assets/img/`
- Use consistent formatting and professional language

## Code Standards

### Jekyll/Liquid Templates

- Use semantic HTML5 elements
- Follow accessibility best practices
- Maintain consistent indentation (2 spaces)
- Comment complex Liquid logic

### CSS/SCSS

- Follow the existing SCSS structure in `_sass/`
- Use BEM methodology for CSS classes when possible
- Ensure responsive design principles
- Test across different screen sizes

### JavaScript

- Use modern ES6+ syntax
- Ensure compatibility with the site's browser support
- Minimize external dependencies
- Follow the existing code style

## Submission Process

### For Content Updates

1. **Create a feature branch:**
   ```bash
   git checkout -b update/content-description
   ```

2. **Make your changes:**
   - Update relevant files
   - Test locally with `bundle exec jekyll serve`
   - Verify all links and formatting

3. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Update: Brief description of changes"
   ```

4. **Push and create a pull request:**
   ```bash
   git push origin update/content-description
   ```

### For Code Changes

1. **Follow the same branching strategy**
2. **Ensure all tests pass:**
   - Check with `bundle exec jekyll build`
   - Verify no broken links
   - Test responsive design

3. **Update documentation if needed**
4. **Submit pull request with detailed description**

## Quality Assurance

The repository includes automated checks for:

- **Accessibility** (axe-core testing)
- **Broken links** (internal and external)
- **Code quality** (CodeQL analysis)
- **HTML/CSS formatting** (Prettier)
- **Performance** (Lighthouse scoring)

Ensure your contributions pass these automated checks.

## Content Review Process

All content changes undergo review for:

- **Academic accuracy** and professional presentation
- **Technical correctness** of research descriptions
- **Consistency** with existing site structure and style
- **SEO optimization** and metadata completeness

## Questions and Support

For questions about contributing:

- Review existing issues and pull requests
- Check the [al-folio documentation](https://github.com/alshedivat/al-folio)
- Contact the site maintainer for academic content questions

## License

By contributing to this repository, you agree that your contributions will be licensed under the same terms as the project (MIT License for the theme, with content copyright retained by the author).