---
title: kSecCodeInfoPlatformIdentifier
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfoplatformidentifier
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfoplatformidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfoplatformidentifier.json'
content_hash: 'sha256:bb85ef8bcef20244'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoPlatformIdentifier

<sub>Global Variable</sub>

A key whose value identifies the operating system release with which the code is associated, if any.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoPlatformIdentifier: CFString
```

## Discussion

If this code was signed as part of an operating system release, the value identifies that release.
