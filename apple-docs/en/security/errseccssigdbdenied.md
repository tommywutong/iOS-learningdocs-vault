---
title: errSecCSSigDBDenied
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/errseccssigdbdenied
source_url: 'https://developer.apple.com/documentation/security/errseccssigdbdenied'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/errseccssigdbdenied.json'
content_hash: 'sha256:f1269d4d3dad9e0f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# errSecCSSigDBDenied

<sub>Global Variable</sub>

Access to signature database denied.

<sub>Mac Catalyst, macOS</sub>

```swift
var errSecCSSigDBDenied: OSStatus { get }
```

## Discussion

This error is returned when the system is attempting to sign unsigned code ad-hoc and couldn’t write to the signature database because of a permission problem.
