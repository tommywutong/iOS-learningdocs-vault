---
title: kSecReturnPersistentRef
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecreturnpersistentref
source_url: 'https://developer.apple.com/documentation/security/ksecreturnpersistentref'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecreturnpersistentref.json'
content_hash: 'sha256:b2b3f4f79ad9e347'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecReturnPersistentRef

<sub>Global Variable</sub>

A key whose value is a Boolean indicating whether or not to return a persistent reference to an item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecReturnPersistentRef: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md). A value of [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) indicates that a persistent reference to an item should be returned as a [CFData](../corefoundation/cfdata.md) object. Unlike normal references, a persistent reference may be stored on disk or passed between processes.
