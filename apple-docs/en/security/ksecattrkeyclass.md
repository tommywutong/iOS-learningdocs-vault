---
title: kSecAttrKeyClass
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrkeyclass
source_url: 'https://developer.apple.com/documentation/security/ksecattrkeyclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrkeyclass.json'
content_hash: 'sha256:71de83a27619ebf4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrKeyClass

<sub>Global Variable</sub>

A key whose value indicates the item’s cryptographic key class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrKeyClass: CFString
```

## Discussion

The corresponding value is of type [CFTypeRef](../corefoundation/cftyperef.md) and specifies a type of cryptographic key. Possible values are listed in [Key Class Values](item-attribute-keys-and-values.md#Key-Class-Values). Read only.

> [!note] Note
> Don’t confuse this attribute with the more general [kSecClass](ksecclass.md) attribute that indicates an item’s class (for example password, certificate, or cryptographic key). The [kSecAttrKeyClass](ksecattrkeyclass.md) attribute described here applies only to items of class [kSecClassKey](ksecclasskey.md), indicating what category a cryptographic key fits into (for example, public, private, or symmetric).
