---
title: kSecReturnAttributes
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecreturnattributes
source_url: 'https://developer.apple.com/documentation/security/ksecreturnattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecreturnattributes.json'
content_hash: 'sha256:2158afcb8397c181'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecReturnAttributes

<sub>Global Variable</sub>

A key whose value is a Boolean indicating whether or not to return item attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecReturnAttributes: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md). A value of [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) indicates that a dictionary of the (unencrypted) attributes of an item should be returned in the form of a [CFDictionary](../corefoundation/cfdictionary.md) using the keys and values defined in [Item attribute keys and values](item-attribute-keys-and-values.md).
