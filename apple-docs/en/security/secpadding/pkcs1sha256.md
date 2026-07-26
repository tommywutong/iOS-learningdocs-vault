---
title: PKCS1SHA256
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, macOS 10.6+（12.0 起废弃）, tvOS 4.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secpadding/pkcs1sha256
source_url: 'https://developer.apple.com/documentation/security/secpadding/pkcs1sha256'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpadding/pkcs1sha256.json'
content_hash: 'sha256:1f0bb636e715407e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecPadding](../secpadding.md)

# PKCS1SHA256

<sub>Type Property</sub>

Data to be signed is a SHA256 hash.

> [!warning] Deprecated
> Replaced with SecKeyAlgorithm

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var PKCS1SHA256: SecPadding { get }
```

## Discussion

Standard ASN.1 padding will be done, as well as PKCS1 padding of the underlying RSA operation. Used with [SecKeyRawSign](<../seckeyrawsign(____________).md>) and [SecKeyRawVerify](<../seckeyrawverify(____________).md>) only.
