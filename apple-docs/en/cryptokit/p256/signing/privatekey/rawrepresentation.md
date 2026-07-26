---
title: rawRepresentation
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/p256/signing/privatekey/rawrepresentation
source_url: 'https://developer.apple.com/documentation/cryptokit/p256/signing/privatekey/rawrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p256/signing/privatekey/rawrepresentation.json'
content_hash: 'sha256:13b7a25e4121c044'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P256](../../../p256.md) · [Signing](../../signing.md) · [PrivateKey](../privatekey.md)

# rawRepresentation

<sub>Instance Property</sub>

A data representation of the private key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var rawRepresentation: Data { get }
```

## See Also

### Representing the key

- [derRepresentation](derrepresentation.md) — A Distinguished Encoding Rules (DER) encoded representation of the private key.
- [pemRepresentation](pemrepresentation.md) — A Privacy-Enhanced Mail (PEM) representation of the private key.
- [x963Representation](x963representation.md) — An ANSI x9.63 representation of the private key.
