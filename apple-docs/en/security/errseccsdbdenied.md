---
title: errSecCSDBDenied
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/errseccsdbdenied
source_url: 'https://developer.apple.com/documentation/security/errseccsdbdenied'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/errseccsdbdenied.json'
content_hash: 'sha256:d8d7977ee3865b49'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# errSecCSDBDenied

<sub>Global Variable</sub>

Access to signature database denied.

<sub>Mac Catalyst, macOS</sub>

```swift
var errSecCSDBDenied: OSStatus { get }
```

## Database

This error is returned when the system is attempting to sign unsigned code ad-hoc and couldn’t write to the signature database because of a permission problem.
