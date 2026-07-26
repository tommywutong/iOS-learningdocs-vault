---
title: kSecMatchCaseInsensitive
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecmatchcaseinsensitive
source_url: 'https://developer.apple.com/documentation/security/ksecmatchcaseinsensitive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecmatchcaseinsensitive.json'
content_hash: 'sha256:6d074519a18844f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecMatchCaseInsensitive

<sub>Global Variable</sub>

A key whose value is a Boolean indicating whether case-insensitive matching is performed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecMatchCaseInsensitive: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md). If this value is [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md), or if this attribute is not provided, then case-sensitive string matching is performed.
