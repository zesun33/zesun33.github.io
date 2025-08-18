# Deployment Guide

This guide provides comprehensive instructions for deploying and maintaining Md Zesun Ahmed Mia's academic portfolio website.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Local Development](#local-development)
- [Production Deployment](#production-deployment)
- [Environment Configuration](#environment-configuration)
- [Troubleshooting](#troubleshooting)
- [Maintenance](#maintenance)

## Overview

The website uses a **static site generation** approach with **Jekyll** and is automatically deployed to **GitHub Pages** via **GitHub Actions**. This setup provides:

- ✅ **Zero-cost hosting** via GitHub Pages
- ✅ **Automatic SSL/HTTPS** with custom domain support
- ✅ **Global CDN distribution** for fast loading
- ✅ **Automated deployments** on every commit
- ✅ **Version control** for all content and code

## Prerequisites

### System Requirements

| Component       | Version | Purpose           |
| --------------- | ------- | ----------------- |
| **Ruby**        | 3.3.5+  | Jekyll runtime    |
| **Node.js**     | 18+     | Frontend tooling  |
| **Python**      | 3.13+   | Jupyter notebooks |
| **Git**         | 2.0+    | Version control   |
| **ImageMagick** | 7.0+    | Image processing  |

### Account Requirements

- **GitHub Account** with repository access
- **Domain Name** (optional, for custom domain)
- **Google Analytics** (optional, for tracking)

## Local Development

### Initial Setup

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

5. **Install system dependencies:**

   **Ubuntu/Debian:**

   ```bash
   sudo apt-get update
   sudo apt-get install imagemagick libmagickwand-dev
   ```

   **macOS:**

   ```bash
   brew install imagemagick
   ```

   **Windows:**

   ```bash
   # Use Windows Subsystem for Linux (WSL) or
   # Download ImageMagick from official website
   ```

### Development Server

**Start the development server:**

```bash
bundle exec jekyll serve --livereload --drafts
```

**Available options:**

- `--livereload`: Auto-refresh browser on changes
- `--drafts`: Include draft posts
- `--incremental`: Faster builds (experimental)
- `--host 0.0.0.0`: Allow external connections

**Access the site:**

- Local: `http://localhost:4000`
- Network: `http://[your-ip]:4000`

### Development Workflow

1. **Create a feature branch:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make changes and test locally:**

   ```bash
   bundle exec jekyll serve --livereload
   ```

3. **Build for production testing:**

   ```bash
   JEKYLL_ENV=production bundle exec jekyll build
   ```

4. **Commit and push changes:**

   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin feature/your-feature-name
   ```

5. **Create pull request** via GitHub interface

## Production Deployment

### Automatic Deployment (Recommended)

The site automatically deploys when changes are pushed to the `main` branch:

1. **Push to main branch:**

   ```bash
   git checkout main
   git merge feature/your-feature-name
   git push origin main
   ```

2. **Monitor deployment:**

   - Visit the [Actions tab](https://github.com/zesun33/zesun33.github.io/actions)
   - Check the "Deploy site" workflow status
   - Deployment typically takes 2-5 minutes

3. **Verify deployment:**
   - Visit [https://zesun33.github.io](https://zesun33.github.io)
   - Check that changes are live
   - Test functionality across devices

### Manual Deployment (Alternative)

For custom hosting or manual deployment:

1. **Build the site:**

   ```bash
   JEKYLL_ENV=production bundle exec jekyll build
   ```

2. **Test the build:**

   ```bash
   bundle exec htmlproofer ./_site --disable-external
   ```

3. **Deploy to server:**
   ```bash
   # Example for custom server
   rsync -avz --delete _site/ user@server:/path/to/webroot/
   ```

### GitHub Pages Configuration

The repository is configured for GitHub Pages deployment:

1. **Repository Settings:**

   - Go to Settings → Pages
   - Source: "GitHub Actions"
   - Custom domain: `zesun33.github.io` (or custom domain)

2. **Branch Protection:**
   - Main branch is protected
   - Requires pull request reviews
   - Status checks must pass

## Environment Configuration

### Jekyll Configuration

**Development (`_config.yml`):**

```yaml
url: "http://localhost:4000"
baseurl: ""
environment: development
```

**Production (GitHub Actions):**

```yaml
url: "https://zesun33.github.io"
baseurl: ""
environment: production
```

### Environment Variables

**GitHub Actions Secrets:**

- No sensitive secrets required for basic deployment
- Optional: `GOOGLE_ANALYTICS_ID` for tracking

**Local Development:**

```bash
export JEKYLL_ENV=development
export BUNDLE_PATH=vendor/bundle
```

### Custom Domain Setup

If using a custom domain:

1. **Add CNAME file:**

   ```bash
   echo "yourdomain.com" > CNAME
   git add CNAME
   git commit -m "Add custom domain"
   git push origin main
   ```

2. **Configure DNS:**

   ```
   # A records
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153

   # Or CNAME record
   yourdomain.com → zesun33.github.io
   ```

3. **Enable HTTPS:**
   - GitHub Pages automatically provides SSL
   - May take up to 24 hours to activate

## Troubleshooting

### Common Build Issues

**1. Bundle install fails:**

```bash
# Clear bundle cache
bundle clean --force
rm -rf vendor/bundle
bundle install
```

**2. Jekyll build fails:**

```bash
# Clear Jekyll cache
bundle exec jekyll clean
bundle exec jekyll build --verbose
```

**3. ImageMagick errors:**

```bash
# Ubuntu/Debian
sudo apt-get install imagemagick libmagickwand-dev

# macOS
brew reinstall imagemagick

# Check installation
convert --version
```

**4. Node.js/npm issues:**

```bash
# Clear npm cache
npm cache clean --force
rm -rf node_modules
npm install
```

### Deployment Issues

**1. GitHub Actions failing:**

- Check the Actions tab for error logs
- Verify all required files are committed
- Check for syntax errors in YAML files

**2. Site not updating:**

- Clear browser cache
- Check GitHub Pages settings
- Verify deployment completed successfully

**3. Custom domain issues:**

- Verify DNS configuration
- Check CNAME file content
- Wait for DNS propagation (up to 48 hours)

### Performance Issues

**1. Slow build times:**

```bash
# Use incremental builds for development
bundle exec jekyll serve --incremental

# Exclude unnecessary files
# Add to _config.yml:
exclude:
  - node_modules/
  - vendor/
  - .git/
```

**2. Large site size:**

```bash
# Run PurgeCSS
npm run build:css

# Optimize images
# Check assets/img/ for large files
```

## Maintenance

### Regular Tasks

**Weekly:**

- [ ] Check for broken links
- [ ] Review site performance metrics
- [ ] Monitor GitHub Actions status

**Monthly:**

- [ ] Update Ruby gems: `bundle update`
- [ ] Update Node.js packages: `npm update`
- [ ] Review and update content
- [ ] Check accessibility compliance

**Quarterly:**

- [ ] Review and update dependencies
- [ ] Performance audit with Lighthouse
- [ ] Security review and updates
- [ ] Backup verification

### Dependency Updates

**Ruby Gems:**

```bash
# Check outdated gems
bundle outdated

# Update all gems
bundle update

# Update specific gem
bundle update jekyll
```

**Node.js Packages:**

```bash
# Check outdated packages
npm outdated

# Update packages
npm update

# Check for security vulnerabilities
npm audit
npm audit fix
```

**Python Packages:**

```bash
# Check outdated packages
pip list --outdated

# Update packages
pip install --upgrade -r requirements.txt
```

### Backup Strategy

**Automated Backups:**

- Git repository serves as primary backup
- GitHub provides redundant storage
- All content is version-controlled

**Manual Backups:**

```bash
# Clone repository to backup location
git clone --mirror https://github.com/zesun33/zesun33.github.io.git backup/

# Export site data
bundle exec jekyll build
tar -czf site-backup-$(date +%Y%m%d).tar.gz _site/
```

### Monitoring

**Automated Monitoring:**

- GitHub Actions for build status
- Dependabot for security updates
- Link checker for broken links

**Manual Monitoring:**

- Google Search Console for SEO
- Web Vitals for performance
- Accessibility testing tools

### Recovery Procedures

**Site Recovery:**

1. Identify the issue (build failure, content error, etc.)
2. Revert to last known good commit if necessary
3. Fix the issue in a feature branch
4. Test thoroughly before merging to main

**Data Recovery:**

1. All content is in Git history
2. Use `git log` and `git checkout` to recover files
3. Publications are backed up in BibTeX format
4. CV data is in structured YAML format

## Support and Resources

### Documentation

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [al-folio Theme Guide](https://github.com/alshedivat/al-folio)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

### Community Support

- [Jekyll Community Forum](https://talk.jekyllrb.com/)
- [GitHub Community](https://github.community/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/jekyll)

### Professional Support

- Contact: zesun.ahmed@psu.edu
- GitHub Issues: [Report problems](https://github.com/zesun33/zesun33.github.io/issues)

---

**Last Updated**: January 17, 2025  
**Next Review**: July 17, 2025
