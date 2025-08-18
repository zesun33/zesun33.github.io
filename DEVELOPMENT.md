# Development Guide

This document provides detailed information for developers working on Md Zesun Ahmed Mia's academic website.

## Architecture Overview

### Technology Stack

- **Static Site Generator**: Jekyll 4.x
- **Theme**: al-folio (academic portfolio theme)
- **Hosting**: GitHub Pages
- **CI/CD**: GitHub Actions
- **Frontend**: HTML5, SCSS, JavaScript (ES6+)
- **Backend**: Ruby (Jekyll plugins)
- **Content Management**: Markdown, YAML, BibTeX

### Directory Structure

```
├── _bibliography/          # BibTeX files for publications
├── _books/                # Book reviews and reading lists
├── _data/                 # YAML data files (CV, social links, etc.)
├── _includes/             # Reusable HTML components
├── _layouts/              # Page layout templates
├── _news/                 # News and announcement posts
├── _pages/                # Static pages (About, CV, etc.)
├── _plugins/              # Custom Jekyll plugins
├── _posts/                # Blog posts
├── _projects/             # Research projects
├── _sass/                 # SCSS stylesheets
├── _scripts/              # Build and utility scripts
├── assets/                # Static assets (images, CSS, JS)
├── .github/workflows/     # GitHub Actions CI/CD
├── _config.yml            # Jekyll configuration
├── Gemfile                # Ruby dependencies
├── package.json           # Node.js dependencies
└── requirements.txt       # Python dependencies
```

## Development Environment Setup

### System Requirements

- **Ruby**: 3.3.5+ (managed via rbenv/rvm recommended)
- **Node.js**: 18+ with npm
- **Python**: 3.13+ with pip
- **ImageMagick**: For image processing
- **Git**: For version control
- **Git Bash**: Recommended terminal for Windows development

### IDE Configuration

The repository includes a pre-configured VS Code workspace (`zesun-academic-website.code-workspace`) with:

- **Git Bash as default terminal** for Windows development
- **Jekyll-specific file associations** (Liquid, YAML, BibTeX)
- **Recommended extensions** for Jekyll, Ruby, and web development
- **Code formatting settings** with Prettier integration
- **Search exclusions** for build artifacts and dependencies
- **Pre-configured tasks** for common development operations

#### Recommended VS Code Extensions

The workspace automatically suggests these extensions:

- **Jekyll & Static Sites**: Jekyll syntax, Liquid templates
- **Web Development**: Prettier, Tailwind CSS, auto-rename tags
- **Markdown**: All-in-one Markdown support with Mermaid diagrams
- **Git & GitHub**: Pull requests, Copilot, GitLens
- **Code Quality**: Spell checker, ESLint, accessibility linter

#### Development Tasks

Pre-configured tasks available via Command Palette (`Ctrl+Shift+P`):

- `🚀 Jekyll: Serve (Development)` - Start development server with live reload
- `🏗️ Jekyll: Build (Production)` - Build for production deployment
- `🧹 Jekyll: Clean` - Clean build artifacts
- `💎 Bundle: Install Dependencies` - Install Ruby gems
- `📦 NPM: Install Dependencies` - Install Node.js packages
- `🎨 Prettier: Format Code` - Format all code files

### Installation Steps

1. **Install Ruby dependencies:**

   ```bash
   bundle install
   ```

2. **Install Node.js dependencies:**

   ```bash
   npm install
   ```

3. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install system dependencies (Ubuntu/Debian):**
   ```bash
   sudo apt-get update
   sudo apt-get install imagemagick
   ```

### Local Development

**Start development server:**

```bash
bundle exec jekyll serve --livereload --drafts
```

**Build for production:**

```bash
JEKYLL_ENV=production bundle exec jekyll build
```

**Run with Docker (alternative):**

```bash
docker run -it --rm -v "$PWD":/usr/src/app -p "4000:4000" starefossen/github-pages
```

## Key Features and Components

### Publication Management

Publications are managed via BibTeX in `_bibliography/papers.bib`:

- **Jekyll-Scholar plugin** processes BibTeX entries
- **Automatic citation formatting** with APA style
- **Publication badges** (Altmetric, Dimensions, Google Scholar)
- **PDF links and abstracts** support
- **Filtering and grouping** by year, type, etc.

### CV System

Dynamic CV generation from `_data/cv.yml`:

- **Structured YAML data** for easy maintenance
- **Responsive timeline layout** for experience
- **Automatic formatting** for education, skills, etc.
- **Print-friendly styling** for PDF generation

### Search and Navigation

- **Full-text search** across posts, publications, and pages
- **Tag-based filtering** for blog posts and projects
- **Responsive navigation** with mobile-friendly design
- **Breadcrumb navigation** for better UX

### Performance Optimization

- **PurgeCSS integration** removes unused CSS
- **Image optimization** with responsive images
- **Lazy loading** for images and heavy content
- **Minification** of CSS and JavaScript
- **CDN integration** for external libraries

## Customization Guide

### Theme Customization

The site uses the al-folio theme with customizations:

1. **Colors and Typography:**

   - Edit `_sass/_variables.scss`
   - Customize color schemes in `_sass/_themes.scss`

2. **Layout Modifications:**

   - Override layouts in `_layouts/`
   - Customize includes in `_includes/`

3. **Adding New Sections:**
   - Create new page templates
   - Update navigation in `_data/navigation.yml`

### Content Management

1. **Adding Publications:**

   ```bibtex
   @article{key2024,
     title={Your Paper Title},
     author={Author, Name and Mia, Md Zesun Ahmed},
     journal={Journal Name},
     year={2024},
     bibtex_show={true},
     selected={true},
     pdf={paper.pdf},
     abstract={Your abstract here...}
   }
   ```

2. **Adding Projects:**

   ```yaml
   ---
   layout: page
   title: Project Name
   description: Brief description
   img: assets/img/project-image.jpg
   category: research
   ---
   ```

3. **Adding News:**
   ```markdown
   ---
   layout: post
   date: 2024-01-15
   inline: true
   ---

   Your news content here.
   ```

## Deployment and CI/CD

### GitHub Actions Workflow

The site uses automated deployment via GitHub Actions:

1. **Build Process:**

   - Ruby/Jekyll environment setup
   - Python dependencies for Jupyter notebooks
   - ImageMagick for image processing
   - CSS purging for optimization

2. **Quality Checks:**

   - Accessibility testing (axe-core)
   - Broken link detection
   - Code quality analysis (CodeQL)
   - HTML/CSS formatting (Prettier)

3. **Deployment:**
   - Automatic deployment to GitHub Pages
   - Custom domain support
   - HTTPS enforcement

### Manual Deployment

For manual deployment or testing:

```bash
# Build the site
JEKYLL_ENV=production bundle exec jekyll build

# Test the build
bundle exec htmlproofer ./_site --disable-external

# Deploy (if using custom hosting)
rsync -avz --delete _site/ user@server:/path/to/webroot/
```

## Troubleshooting

### Common Issues

1. **Bundle install fails:**

   ```bash
   # Update RubyGems and Bundler
   gem update --system
   gem install bundler
   bundle update
   ```

2. **ImageMagick errors:**

   ```bash
   # Ubuntu/Debian
   sudo apt-get install imagemagick libmagickwand-dev

   # macOS
   brew install imagemagick
   ```

3. **Jekyll build fails:**

   ```bash
   # Clear cache and rebuild
   bundle exec jekyll clean
   bundle exec jekyll build --verbose
   ```

4. **JavaScript/CSS not loading:**
   - Check `_config.yml` baseurl settings
   - Verify asset paths in templates
   - Clear browser cache

### Performance Issues

1. **Slow build times:**

   - Use `--incremental` flag for development
   - Exclude unnecessary files in `_config.yml`
   - Optimize image sizes

2. **Large site size:**
   - Enable PurgeCSS
   - Optimize images with ImageMagick
   - Remove unused assets

## Testing

### Local Testing

```bash
# Test site build
bundle exec jekyll build

# Test links (internal only)
bundle exec htmlproofer ./_site --disable-external

# Test accessibility
npm run test:accessibility

# Test performance
npm run test:lighthouse
```

### Automated Testing

The repository includes comprehensive testing:

- **Unit tests** for custom plugins
- **Integration tests** for site functionality
- **Accessibility tests** with axe-core
- **Performance tests** with Lighthouse
- **Link validation** for internal and external links

## Security Considerations

1. **Content Security Policy** headers configured
2. **HTTPS enforcement** via GitHub Pages
3. **Dependency scanning** via GitHub Security
4. **No sensitive data** in repository
5. **Regular dependency updates** via Dependabot

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## Support and Resources

- **Jekyll Documentation**: https://jekyllrb.com/docs/
- **al-folio Theme**: https://github.com/alshedivat/al-folio
- **GitHub Pages**: https://docs.github.com/en/pages
- **Jekyll-Scholar**: https://github.com/inukshuk/jekyll-scholar
