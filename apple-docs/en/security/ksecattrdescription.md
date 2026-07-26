---
title: kSecAttrDescription
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrdescription
source_url: 'https://developer.apple.com/documentation/security/ksecattrdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrdescription.json'
content_hash: 'sha256:1a7a0a2ce7423c6e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrDescription

<sub>Global Variable</sub>

A key with a value that’s a string indicating the item’s description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrDescription: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md) and specifies a user-visible string describing this kind of item (for example, “Disk image password”).
