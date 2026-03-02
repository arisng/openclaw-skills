# CrawSecure

**CrawSecure** is a security analysis skill designed to help users evaluate potential risks in ClawHub / OpenClaw skills **before installing or trusting them**.

It combines **local static analysis** with an **optional web-based visualization** layer to improve transparency, understanding, and decision-making.

---

## What CrawSecure Does

CrawSecure analyzes skill-related files and metadata to surface potential security concerns.

It helps users:
- Understand what a skill may do before installing it
- Identify risky or unsafe code patterns
- Make informed trust decisions

### Key Capabilities
- Static analysis of skill files
- Detection of potentially dangerous patterns
- Clear, structured risk reporting
- Optional web-based visualization of results

---

## Risk Signals Analyzed

CrawSecure looks for indicators such as:

- Dangerous or destructive command patterns
- Execution-related behavior (e.g. shell calls, eval-like usage)
- References to sensitive files or credentials
- Indicators of unsafe or misleading practices
- Inconsistencies between declared purpose and actual behavior

> CrawSecure performs **read-only analysis** and does **not modify any files**.

---

## Security Philosophy

CrawSecure is built around the following principles:

- **Read-only analysis**
- **No file modification**
- **No persistence**
- **No privilege escalation**
- **No automatic execution of third-party code**

The goal is to increase **trust and transparency** inside the ClawHub ecosystem.

---

## Execution Model

CrawSecure provides a **local CLI scanner** that users run manually.

- The scan itself is performed locally
- No files are modified
- No skill code is executed

After a scan completes, CrawSecure may output an **optional URL** that allows the user to view the scan results in a browser.

This web page:
- Displays the scan report in a human-readable format
- May require user authentication
- Does **not** execute or install any skill code

---

## Network & Data Usage

- CrawSecure does **not** require network access to perform local analysis
- If the user chooses to open the provided report URL:
  - Only scan metadata and findings are displayed
  - No source files or secrets are uploaded automatically
  - No background network activity occurs without user action

---

## Intended Usage

CrawSecure is intended to be used:
- Before installing a skill
- As a verification step for security-conscious users
- As an educational tool to understand common risk patterns

It does **not** replace full manual code review, but complements it.

---

## Transparency Notice

CrawSecure exists to promote safer usage of third-party skills.

Users are encouraged to:
- Review skill source code manually
- Verify publishers and repositories
- Understand what they run in their environments

Security is layered — CrawSecure is one of those layers.

---

## License

MIT