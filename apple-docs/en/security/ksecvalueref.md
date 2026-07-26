---
title: kSecValueRef
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecvalueref
source_url: 'https://developer.apple.com/documentation/security/ksecvalueref'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecvalueref.json'
content_hash: 'sha256:d1e75319ab5e6e1f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecValueRef

<sub>Global Variable</sub>

A key whose value is a reference to the item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecValueRef: CFString
```

## Discussion

The corresponding value, depending on the item class requested, is of type [SecKeychainItem](seckeychainitem.md), [SecKey](seckey.md), [SecCertificate](seccertificate.md), or [SecIdentity](secidentity.md).
