---
title: kSecAttrApplicationLabel
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrapplicationlabel
source_url: 'https://developer.apple.com/documentation/security/ksecattrapplicationlabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrapplicationlabel.json'
content_hash: 'sha256:e9fb0a13dd4c5c5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrApplicationLabel

<sub>Global Variable</sub>

A key whose value indicates the item’s application label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrApplicationLabel: CFString
```

## Discussion

The corresponding value is of type [CFData](../corefoundation/cfdata.md) and contains a label for this item. This attribute is different from the [kSecAttrLabel](ksecattrlabel.md) attribute, which is intended to be human-readable. Instead, this attribute is used to look up a key programmatically; in particular, for keys of class [kSecAttrKeyClassPublic](ksecattrkeyclasspublic.md) and [kSecAttrKeyClassPrivate](ksecattrkeyclassprivate.md), the value of this attribute is the hash of the public key.
