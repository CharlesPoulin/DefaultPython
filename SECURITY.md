# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.x.x   | :white_check_mark: |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please follow these steps:

### Do NOT

- Open a public GitHub issue describing the vulnerability
- Disclose the vulnerability publicly before it has been addressed

### Do

1. **Email**: Send details to `security@example.com` (replace with your email)
2. **Include**:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Any suggested fixes (optional)

### What to Expect

- **Acknowledgment**: Within 48 hours of your report
- **Status Update**: Within 7 days with our assessment
- **Resolution**: We aim to address critical vulnerabilities within 30 days

### After Resolution

- We will credit you in the release notes (unless you prefer anonymity)
- We may ask you to verify the fix

## Security Best Practices

When contributing to this project:

- Never commit secrets, API keys, or credentials
- Use environment variables for sensitive configuration
- Keep dependencies updated (we use Dependabot)
- Follow secure coding guidelines

## Automated Security

This project uses:

- **Bandit** for Python security linting
- **Dependabot** for dependency updates
- **Pre-commit hooks** for code quality checks

Thank you for helping keep this project secure!
