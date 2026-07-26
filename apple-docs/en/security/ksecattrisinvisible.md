---
title: kSecAttrIsInvisible
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrisinvisible
source_url: 'https://developer.apple.com/documentation/security/ksecattrisinvisible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrisinvisible.json'
content_hash: 'sha256:010e1268a81b46d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrIsInvisible

<sub>Global Variable</sub>

A key with a value that’s a Boolean indicating the item’s visibility.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrIsInvisible: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md) and is [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) if the item is invisible (that is, should not be displayed).
