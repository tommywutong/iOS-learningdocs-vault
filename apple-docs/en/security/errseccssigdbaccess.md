---
title: errSecCSSigDBAccess
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/errseccssigdbaccess
source_url: 'https://developer.apple.com/documentation/security/errseccssigdbaccess'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/errseccssigdbaccess.json'
content_hash: 'sha256:5f18b4a8106bbffc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# errSecCSSigDBAccess

<sub>Global Variable</sub>

Can’t access signature database.

<sub>Mac Catalyst, macOS</sub>

```swift
var errSecCSSigDBAccess: OSStatus { get }
```

## Discussion

This error is returned when the system is attempting to sign unsigned code ad-hoc and couldn’t write to the signature database because of some problem other than a permission problem. For example, the signature database might be missing or corrupted.
