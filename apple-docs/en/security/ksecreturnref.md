---
title: kSecReturnRef
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecreturnref
source_url: 'https://developer.apple.com/documentation/security/ksecreturnref'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecreturnref.json'
content_hash: 'sha256:f2191e31352c2cbf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecReturnRef

<sub>Global Variable</sub>

A key whose value is a Boolean indicating whether or not to return a reference to an item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecReturnRef: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md). A value of [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) indicates that a reference should be returned. Depending on the item class requested, the returned references may be of type [SecKeychainItem](seckeychainitem.md), [SecKey](seckey.md), [SecCertificate](seccertificate.md), [SecIdentity](secidentity.md), or [CFData](../corefoundation/cfdata.md).
