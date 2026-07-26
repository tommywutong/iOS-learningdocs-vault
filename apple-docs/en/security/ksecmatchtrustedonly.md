---
title: kSecMatchTrustedOnly
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecmatchtrustedonly
source_url: 'https://developer.apple.com/documentation/security/ksecmatchtrustedonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecmatchtrustedonly.json'
content_hash: 'sha256:31e4abab5372c829'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecMatchTrustedOnly

<sub>Global Variable</sub>

A key whose value is a Boolean indicating whether untrusted certificates should be returned.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecMatchTrustedOnly: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md). If this attribute is provided with a value of [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md), only certificates that can be verified back to a trusted anchor are returned. If this value is [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md) or the attribute is not provided, then both trusted and untrusted certificates may be returned.
