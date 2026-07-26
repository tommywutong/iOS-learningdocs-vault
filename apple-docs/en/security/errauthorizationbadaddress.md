---
title: errAuthorizationBadAddress
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/errauthorizationbadaddress
source_url: 'https://developer.apple.com/documentation/security/errauthorizationbadaddress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/errauthorizationbadaddress.json'
content_hash: 'sha256:cf19685d783d8086'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# errAuthorizationBadAddress

<sub>Global Variable</sub>

The requested socket address is invalid.

<sub>Mac Catalyst, macOS</sub>

```swift
var errAuthorizationBadAddress: OSStatus { get }
```

## Discussion

The socket address must be in the range (0, 1023) inclusive.
