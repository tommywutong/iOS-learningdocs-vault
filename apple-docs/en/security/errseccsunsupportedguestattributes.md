---
title: errSecCSUnsupportedGuestAttributes
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/errseccsunsupportedguestattributes
source_url: 'https://developer.apple.com/documentation/security/errseccsunsupportedguestattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/errseccsunsupportedguestattributes.json'
content_hash: 'sha256:dc20231789c86484'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# errSecCSUnsupportedGuestAttributes

<sub>Global Variable</sub>

Cannot locate guest code using this attribute set.

<sub>Mac Catalyst, macOS</sub>

```swift
var errSecCSUnsupportedGuestAttributes: OSStatus { get }
```

## Discussion

When calling the [SecHostCreateGuest](sechostcreateguest.md) function or the [SecCodeCopyGuestWithAttributes](<seccodecopyguestwithattributes(________).md>) function, you passed a key that either isn’t understood, recognized, or supported.
