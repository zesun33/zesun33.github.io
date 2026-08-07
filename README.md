# Md Zesun Ahmed Mia - Academic Portfolio Website

[![Deploy site](https://github.com/zesun33/zesun33.github.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/zesun33/zesun33.github.io/actions/workflows/deploy.yml)
[![Accessibility](https://github.com/zesun33/zesun33.github.io/actions/workflows/axe.yml/badge.svg)](https://github.com/zesun33/zesun33.github.io/actions/workflows/axe.yml)
[![Link Check](https://github.com/zesun33/zesun33.github.io/actions/workflows/broken-links.yml/badge.svg)](https://github.com/zesun33/zesun33.github.io/actions/workflows/broken-links.yml)

This repository contains the source code for my personal academic website, hosted at **[https://zesun33.github.io](https://zesun33.github.io)**.

## 👨‍🎓 About

I am a **PhD candidate in Electrical Engineering** at **Pennsylvania State University**, specializing in cutting-edge research areas:

- **Neuromorphic Computing** & Brain-Inspired AI
- **Machine Learning Hardware** & AI Accelerators  
- **Emerging Semiconductor Devices** (FeFET, Spintronics)
- **Device-Circuit Co-design** & Process Integration

Former **Graduate Technical Intern at Intel Corporation** (May-July 2025), where I contributed to advanced semiconductor manufacturing through Design of Experiments (DOE) for thin film deposition, process integration tools, and AI/ML predictive frameworks for semiconductor process optimization.

## 🌟 Website Features

### 📚 **Academic Content Management**
- **Publications**: Automatically generated from BibTeX with citation metrics
- **Research Projects**: Detailed project portfolios with images and descriptions
- **CV**: Dynamic curriculum vitae with timeline layouts
- **News & Updates**: Research announcements and academic milestones

### 🔬 **Research Showcase**
- **Interactive Publication Browser** with filtering and search
- **Project Categories**: Research, coursework, and collaboration projects
- **Teaching Portfolio**: Course materials and mentoring experience
- **Blog**: Technical insights and research discussions

### 🎨 **Modern Web Features**
- **Responsive Design**: Optimized for all devices and screen sizes
- **Dark/Light Mode**: Automatic theme switching with user preference
- **Search Functionality**: Full-text search across all content
- **Social Integration**: Google Scholar, ORCID, LinkedIn profiles
- **Performance Optimized**: Fast loading with image optimization and CSS purging

## 🛠️ Technical Stack

### **Core Technologies**
- **[Jekyll 4.x](https://jekyllrb.com/)** - Static site generator with future posts support
- **[al-folio Theme](https://github.com/alshedivat/al-folio)** - Academic portfolio theme (customized)
- **[GitHub Pages](https://pages.github.com/)** - Hosting and deployment
- **[GitHub Actions](https://github.com/features/actions)** - CI/CD pipeline with automated quality checks
- **[Husky](https://typicode.github.io/husky/)** - Git hooks for automated code quality enforcement
- **[Prettier](https://prettier.io/)** - Code formatting with automated pre-commit checks

### **Frontend Technologies**
- **HTML5** with semantic markup and accessibility features
- **SCSS/CSS3** with responsive design and modern layouts
- **JavaScript (ES6+)** for interactive features
- **Bootstrap 5** for responsive grid and components

### **Content Management**
- **[Jekyll-Scholar](https://github.com/inukshuk/jekyll-scholar)** - BibTeX publication management
- **YAML Front Matter** - Structured content metadata
- **Markdown** - Content authoring with extended syntax
- **Liquid Templates** - Dynamic content generation

### **Development Tools**
- **Ruby 3.3.5** with Bundler for dependency management
- **Node.js & npm** for frontend tooling
- **Python 3.13** for Jupyter notebook integration
- **ImageMagick** for responsive image processing

## 🔧 Development Workflow

### **Automated Quality Assurance**
This project enforces strict code quality standards with automated workflows:

- **Pre-commit Hooks**: Prettier formatting checks run automatically before every commit
- **GitHub Push Approval**: All deployments require explicit approval for production safety
- **CI/CD Pipeline**: Comprehensive testing including Prettier, broken links, and accessibility checks
- **Documentation Standards**: All changes must include updated documentation

### **Development Commands**
```bash
# Format checking and fixing
npm run format:check    # Check code formatting
npm run format         # Auto-fix formatting issues
npm run pre-push-check # Pre-deployment verification (Prettier)

# Development server
npm run preview:docker # Docker preview (Windows / no Ruby on PATH) → http://127.0.0.1:4000/
npm run dev           # Jekyll via Ruby/Bundler (if installed)
npm run build         # Build production site
```

### **Before push**
1. `npm run format:check`
2. Launch local preview (`npm run preview:docker` or `npm run dev`) and check changed pages
3. Ask for explicit push approval

See [`.workspace-rules.md`](.workspace-rules.md) and [DEVELOPMENT.md](DEVELOPMENT.md) (Docker on Windows).

### **Workflow Rules**
See [`.workspace-rules.md`](.workspace-rules.md) for comprehensive development workflow requirements.

## 🚀 Quick Start

### Prerequisites
- Ruby 3.3.5+
- Node.js 18+
- Python 3.13+
- ImageMagick

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/zesun33/zesun33.github.io.git
   cd zesun33.github.io
   ```

2. **Install dependencies:**
   ```bash
   # Ruby dependencies
   bundle install
   
   # Node.js dependencies  
   npm install
   
   # Python dependencies
   pip install -r requirements.txt
   ```

3. **Start development server:**
   ```bash
   # Preferred on Windows when Ruby/Bundler are not on PATH:
   npm run preview:docker

   # Or, if Ruby/Bundler work locally:
   npm run dev
   # / bundle exec jekyll serve --livereload
   ```

4. **Open in browser:**
   Navigate to `http://127.0.0.1:4000` (Docker) or `http://localhost:4000`

   Docker preview needs a one-time junction `C:\zesun-site` → this repo; see [DEVELOPMENT.md](DEVELOPMENT.md).

### VS Code Development Environment

The repository includes a pre-configured workspace file (`zesun-academic-website.code-workspace`) optimized for Jekyll development:

- **🖥️ Git Bash Terminal**: Default terminal set to Git Bash for Windows
- **🔧 Jekyll Tasks**: Pre-configured tasks for serve, build, and clean operations
- **📦 Extension Recommendations**: Curated list of helpful extensions for Jekyll development
- **⚙️ Code Formatting**: Prettier integration with Jekyll-specific settings
- **🔍 File Associations**: Proper syntax highlighting for Liquid, YAML, and BibTeX files

**Quick Start with VS Code:**
1. Open the workspace file: `File > Open Workspace from File > zesun-academic-website.code-workspace`
2. Install recommended extensions when prompted
3. Use `Ctrl+Shift+P` and run `🚀 Jekyll: Serve (Development)` to start the development server

## 📖 Documentation

- **[DEVELOPMENT.md](DEVELOPMENT.md)** - Comprehensive development guide
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines and standards
- **[al-folio Documentation](https://github.com/alshedivat/al-folio)** - Theme-specific documentation

## 🔄 Deployment

The website automatically deploys via **GitHub Actions** when changes are pushed to the `main` branch:

1. **Automated Build Process**: Ruby/Jekyll environment setup with all dependencies
2. **Quality Assurance**: Accessibility testing, link validation, and code quality checks  
3. **Performance Optimization**: CSS purging, image optimization, and minification
4. **GitHub Pages Deployment**: Automatic deployment with custom domain support

## 📊 Quality Assurance

The repository includes comprehensive automated testing:

- **🔍 Accessibility Testing** (axe-core)
- **🔗 Link Validation** (internal and external)
- **📈 Performance Monitoring** (Lighthouse)
- **🎨 Code Formatting** (Prettier)
- **🛡️ Security Scanning** (CodeQL)

## 🚀 Recent Updates (August 2025)

### **Major System Improvements**
- **Workflow Automation**: Implemented Prettier pre-commit hooks and push approval system
- **CV Data Synchronization**: Fixed resume.json vs _data/cv.yml discrepancy for accurate CV display
- **Future Posts Support**: Enabled Jekyll future post display for 2025-dated content

### **Content Updates**
- **Intel Internship Completion**: Updated with detailed technical contributions and correct dates
- **Modern Skills Integration**: Added AI tools proficiency (Cursor, Copilot, VSCode, Cline)
- **Publications Enhancement**: Added Neuromorphic Cybersecurity paper and updated URLs
- **Awards Section**: Complete fellowship and recognition history (2014-2025)

### **Technical Enhancements**
- **Zero Prettier Failures**: Automated code formatting with pre-commit enforcement  
- **Enhanced Documentation**: Comprehensive workflow rules and development guides
- **Performance Optimizations**: Improved loading times and Core Web Vitals scores
- **Contact Information**: Added phone number and ORCID integration

## 📞 Contact & Academic Profiles

- **📧 Email**: [zesun.ahmed@psu.edu](mailto:zesun.ahmed@psu.edu)
- **🆔 ORCID**: [0009-0004-3509-8455](https://orcid.org/0009-0004-3509-8455)
- **🎓 Google Scholar**: [View Publications](https://scholar.google.com/citations?user=j-zfUj8AAAAJ&hl=en&oi=ao)
- **💼 LinkedIn**: [Connect with me](https://www.linkedin.com/in/zesun-ahmed/)
- **🔬 ResearchGate**: [Research Profile](https://www.researchgate.net/profile/Md-Zesun-Ahmed-Mia-2/)

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Content updates and corrections
- Feature enhancements
- Bug fixes and improvements
- Documentation updates

## 📄 License

- **Website Content**: © 2025 Md Zesun Ahmed Mia. All rights reserved.
- **al-folio Theme**: [MIT License](https://github.com/alshedivat/al-folio/blob/master/LICENSE)
- **Code Contributions**: MIT License (for theme-related code)

## 🏷️ Keywords

`neuromorphic computing` `machine learning hardware` `spintronics` `semiconductor devices` `AI accelerators` `brain-inspired computing` `emerging devices` `FeFET` `Penn State` `electrical engineering` `PhD research` `Intel Corporation` `academic portfolio` `Jekyll` `GitHub Pages`

---

**⭐ Star this repository** if you find it useful for your own academic website development!
