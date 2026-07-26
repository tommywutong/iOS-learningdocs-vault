---
title: PKCS1MD5
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, macOS 10.6+（12.0 起废弃）, tvOS 4.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secpadding/pkcs1md5
source_url: 'https://developer.apple.com/documentation/security/secpadding/pkcs1md5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpadding/pkcs1md5.json'
content_hash: 'sha256:c8f671f3c4504dbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecPadding](../secpadding.md)

# PKCS1MD5

<sub>Type Property</sub>

Data to be signed is an MD5 hash.

> [!warning] Deprecated
> Replaced with SecKeyAlgorithm

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var PKCS1MD5: SecPadding { get }
```

## Discussion

Standard ASN.1 padding is done, as well as PKCS1 padding of the underlying RSA operation. Used with [SecKeyRawSign](<../seckeyrawsign(____________).md>) and [SecKeyRawVerify](<../seckeyrawverify(____________).md>) only.
