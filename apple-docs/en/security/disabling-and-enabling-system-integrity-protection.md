---
title: Disabling and Enabling System Integrity Protection
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/disabling-and-enabling-system-integrity-protection
source_url: 'https://developer.apple.com/documentation/security/disabling-and-enabling-system-integrity-protection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/disabling-and-enabling-system-integrity-protection.json'
content_hash: 'sha256:646c1b4efaf69dc1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# Disabling and Enabling System Integrity Protection

<sub>Article</sub>

Disable system protections only temporarily during development to test drivers, kernel extensions, and other low-level code.

## Overview

System Integrity Protection (SIP) in macOS protects the entire system by preventing the execution of unauthorized code. The system automatically authorizes apps that the user downloads from the App Store. The system also authorizes apps that a developer notarizes and distributes directly to users. The system prevents the launching of all other apps by default.

During development, it may be necessary for you to disable SIP temporarily to install and test your code. You don’t need to disable SIP to run and debug apps from Xcode, but you might need to disable it to install system extensions, such as DriverKit drivers.

### Disable System Integrity Protection Temporarily

To disable SIP, do the following:

1. Restart your computer in [Recovery mode](https://support.apple.com/en-us/HT201314).
2. Launch Terminal from the Utilities menu.
3. Run the command `csrutil disable`.
4. Restart your computer.

> [!warning] Warning
> Disable SIP only temporarily to perform necessary tasks, and reenable it as soon as possible. Failure to reenable SIP when you are done testing leaves your computer vulnerable to malicious code.

### Enable System Integrity Protection

To reenable SIP, do the following:

1. Restart your computer in [Recovery mode](https://support.apple.com/en-us/HT201314).
2. Launch Terminal from the Utilities menu.
3. Run the command `csrutil enable`.
4. Restart your computer.
