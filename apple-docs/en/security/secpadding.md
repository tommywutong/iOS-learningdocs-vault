---
title: SecPadding
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, macOS 10.6+（12.0 起废弃）, tvOS 4.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secpadding
source_url: 'https://developer.apple.com/documentation/security/secpadding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpadding.json'
content_hash: 'sha256:df16e9a8011d7e2a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPadding

<sub>Structure</sub>

The types of padding to use when you create or verify a digital signature.

> [!warning] Deprecated
> Replaced with SecKeyAlgorithm

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SecPadding
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<secpadding/init(rawvalue_).md>) _(deprecated)_

### Constants

- [kSecPaddingSigRaw](secpadding/sigraw.md) _(deprecated)_
- [kSecPaddingPKCS1](secpadding/pkcs1.md) — PKCS1 padding. _(deprecated)_
- [kSecPaddingOAEP](secpadding/oaep.md) _(deprecated)_
- [kSecPaddingPKCS1MD2](secpadding/pkcs1md2.md) — Data to be signed is an MD2 hash. _(deprecated)_
- [kSecPaddingPKCS1MD5](secpadding/pkcs1md5.md) — Data to be signed is an MD5 hash. _(deprecated)_
- [kSecPaddingPKCS1SHA1](secpadding/pkcs1sha1.md) — Data to be signed is a SHA1 hash. _(deprecated)_
- [kSecPaddingPKCS1SHA224](secpadding/pkcs1sha224.md) — Data to be signed is a SHA224 hash. _(deprecated)_
- [kSecPaddingPKCS1SHA256](secpadding/pkcs1sha256.md) — Data to be signed is a SHA256 hash. _(deprecated)_
- [kSecPaddingPKCS1SHA384](secpadding/pkcs1sha384.md) — Data to be signed is a SHA384 hash. _(deprecated)_
- [kSecPaddingPKCS1SHA512](secpadding/pkcs1sha512.md) — Data to be signed is a SHA512 hash. _(deprecated)_
