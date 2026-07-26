---
title: PKCS1
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, macOS 10.6+（12.0 起废弃）, tvOS 4.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secpadding/pkcs1
source_url: 'https://developer.apple.com/documentation/security/secpadding/pkcs1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpadding/pkcs1.json'
content_hash: 'sha256:db6761a0172e2b65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecPadding](../secpadding.md)

# PKCS1

<sub>Type Property</sub>

PKCS1 padding.

> [!warning] Deprecated
> Replaced with SecKeyAlgorithm

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var PKCS1: SecPadding { get }
```

## Discussion

For elliptic curve, defaults to a signature in x9.62 DER encoding.
