---
title: PKCS1SHA512
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, macOS 10.6+（12.0 起废弃）, tvOS 4.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secpadding/pkcs1sha512
source_url: 'https://developer.apple.com/documentation/security/secpadding/pkcs1sha512'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpadding/pkcs1sha512.json'
content_hash: 'sha256:b7b25d5132760a10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecPadding](../secpadding.md)

# PKCS1SHA512

<sub>Type Property</sub>

Data to be signed is a SHA512 hash.

> [!warning] Deprecated
> Replaced with SecKeyAlgorithm

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var PKCS1SHA512: SecPadding { get }
```

## Discussion

Standard ASN.1 padding will be done, as well as PKCS1 padding of the underlying RSA operation. Used with [SecKeyRawSign](<../seckeyrawsign(____________).md>) and [SecKeyRawVerify](<../seckeyrawverify(____________).md>) only.
