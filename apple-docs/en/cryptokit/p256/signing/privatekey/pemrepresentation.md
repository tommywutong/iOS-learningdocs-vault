---
title: pemRepresentation
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/p256/signing/privatekey/pemrepresentation
source_url: 'https://developer.apple.com/documentation/cryptokit/p256/signing/privatekey/pemrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p256/signing/privatekey/pemrepresentation.json'
content_hash: 'sha256:be93da7bbf53c27a'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P256](../../../p256.md) · [Signing](../../signing.md) · [PrivateKey](../privatekey.md)

# pemRepresentation

<sub>Instance Property</sub>

A Privacy-Enhanced Mail (PEM) representation of the private key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var pemRepresentation: String { get }
```

## See Also

### Representing the key

- [rawRepresentation](rawrepresentation.md) — A data representation of the private key.
- [derRepresentation](derrepresentation.md) — A Distinguished Encoding Rules (DER) encoded representation of the private key.
- [x963Representation](x963representation.md) — An ANSI x9.63 representation of the private key.
