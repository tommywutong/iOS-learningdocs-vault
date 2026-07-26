---
title: considerExpiration
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccsflags/considerexpiration
source_url: 'https://developer.apple.com/documentation/security/seccsflags/considerexpiration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccsflags/considerexpiration.json'
content_hash: 'sha256:7f1f7ca1a5497261'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecCSFlags](../seccsflags.md)

# considerExpiration

<sub>Type Property</sub>

Consider expired certificates invalid.

<sub>Mac Catalyst, macOS</sub>

```swift
static var considerExpiration: SecCSFlags { get }
```

## Discussion

When passed to a function that performs code validation, this flag requests that code signatures made by expired certificates be rejected. By default, expiration of participating certificates is not automatic grounds for rejection.
