---
title: kSecUseAuthenticationUISkip
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecuseauthenticationuiskip
source_url: 'https://developer.apple.com/documentation/security/ksecuseauthenticationuiskip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecuseauthenticationuiskip.json'
content_hash: 'sha256:0b0fcc8e3c93c681'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecUseAuthenticationUISkip

<sub>Global Variable</sub>

A value that indicates items requiring user authentication should be skipped.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecUseAuthenticationUISkip: CFString
```

## Discussion

Silently skip any items that require user authentication. Only use this value with the [SecItemCopyMatching](<secitemcopymatching(____).md>) function.
