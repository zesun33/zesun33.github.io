# Security Policy

## Supported Versions

This academic portfolio website is actively maintained with security updates applied to the following versions:

| Version | Supported      |
| ------- | -------------- |
| 2.x.x   | ✅ Yes         |
| 1.x.x   | ❌ No (Legacy) |

## Security Considerations

### Website Security

This is a **static website** hosted on **GitHub Pages** with the following security measures:

- **HTTPS Enforcement**: All traffic is encrypted via GitHub Pages SSL
- **Content Security Policy**: Implemented to prevent XSS attacks
- **No Server-Side Processing**: Static site reduces attack surface
- **Dependency Scanning**: Automated vulnerability detection via GitHub Security
- **Regular Updates**: Dependencies updated via Dependabot

### Data Privacy

- **No Personal Data Collection**: Website does not collect or store personal information
- **Third-Party Services**: Limited to academic platforms (Google Scholar, ORCID)
- **Analytics**: No tracking or analytics beyond GitHub Pages basic metrics
- **Comments**: Giscus integration uses GitHub authentication (user-controlled)

### Content Security

- **Academic Integrity**: All research content is original or properly attributed
- **Publication Rights**: Only authorized publications are shared
- **Image Rights**: All images are owned, licensed, or used under fair use
- **Contact Information**: Only professional contact details are displayed

## Reporting a Vulnerability

If you discover a security vulnerability in this website, please report it responsibly:

### Preferred Method: Private Security Advisory

1. Go to the [Security tab](https://github.com/zesun33/zesun33.github.io/security) of this repository
2. Click "Report a vulnerability"
3. Provide detailed information about the vulnerability
4. Include steps to reproduce if applicable

### Alternative Method: Email

Send an email to: **zesun.ahmed@psu.edu**

**Subject**: `[SECURITY] Website Vulnerability Report`

**Include**:

- Description of the vulnerability
- Steps to reproduce
- Potential impact assessment
- Suggested mitigation (if known)

### What to Expect

- **Acknowledgment**: Within 48 hours of report
- **Initial Assessment**: Within 1 week
- **Resolution Timeline**: Depends on severity
  - **Critical**: Within 24-48 hours
  - **High**: Within 1 week
  - **Medium**: Within 2 weeks
  - **Low**: Next scheduled update

### Responsible Disclosure

Please follow responsible disclosure practices:

- **Do not** publicly disclose the vulnerability until it's resolved
- **Do not** access or modify data beyond what's necessary to demonstrate the issue
- **Do not** perform actions that could harm the website or its users
- **Do** provide sufficient detail for reproduction and assessment

## Security Best Practices

### For Contributors

When contributing to this repository:

1. **Dependency Updates**:

   - Keep Ruby gems updated via `bundle update`
   - Update Node.js packages via `npm audit fix`
   - Monitor security advisories for Jekyll and plugins

2. **Code Security**:

   - Avoid hardcoding sensitive information
   - Use secure coding practices for any JavaScript
   - Validate and sanitize any user inputs (if added)

3. **Content Security**:
   - Verify all external links are legitimate
   - Ensure uploaded files are safe and appropriate
   - Check image metadata for sensitive information

### For Users

When interacting with the website:

1. **Comments (Giscus)**:

   - Uses your GitHub account for authentication
   - Comments are stored in GitHub Discussions
   - Follow GitHub's community guidelines

2. **External Links**:
   - External links open in new tabs for security
   - Verify destination before clicking
   - Report suspicious or broken links

## Security Features

### Automated Security Measures

- **GitHub Security Advisories**: Automatic vulnerability scanning
- **Dependabot**: Automated dependency updates
- **CodeQL Analysis**: Static code analysis for security issues
- **Link Validation**: Automated checking for malicious links

### Manual Security Reviews

- **Content Review**: All content changes are reviewed
- **Dependency Audit**: Regular manual review of dependencies
- **Access Control**: Repository access limited to authorized contributors
- **Backup Strategy**: Git history provides complete backup

## Compliance and Standards

### Academic Standards

- **Research Ethics**: All research content follows academic integrity guidelines
- **Copyright Compliance**: Proper attribution and fair use practices
- **Privacy Protection**: No unauthorized personal information sharing

### Technical Standards

- **Web Security**: Follows OWASP guidelines for static sites
- **Accessibility**: WCAG 2.1 AA compliance for inclusive access
- **Performance**: Security measures don't compromise site performance

## Contact Information

For security-related questions or concerns:

- **Primary Contact**: zesun.ahmed@psu.edu
- **Institution**: Pennsylvania State University
- **GitHub**: [@zesun33](https://github.com/zesun33)

## Acknowledgments

We appreciate the security research community and responsible disclosure practices. Contributors who report valid security issues will be acknowledged (with permission) in our security advisories.

---

**Last Updated**: January 17, 2025  
**Next Review**: July 17, 2025
