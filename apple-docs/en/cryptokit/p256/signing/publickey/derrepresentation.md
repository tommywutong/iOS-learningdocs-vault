---
title: derRepresentation
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/p256/signing/publickey/derrepresentation
source_url: 'https://developer.apple.com/documentation/cryptokit/p256/signing/publickey/derrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p256/signing/publickey/derrepresentation.json'
content_hash: 'sha256:baa74dc7fdb34524'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P256](../../../p256.md) · [Signing](../../signing.md) · [PublicKey](../publickey.md)

# derRepresentation

<sub>Instance Property</sub>

A Distinguished Encoding Rules (DER) encoded representation of the public key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var derRepresentation: Data { get }
```

## See Also

### Representing the key

- [rawRepresentation](rawrepresentation.md) — A full representation of the public key.
- [compactRepresentation](compactrepresentation.md) — A compact representation of the public key.
- [compressedRepresentation](compressedrepresentation.md) — A compressed representation of the public key.
- [pemRepresentation](pemrepresentation.md) — A Privacy-Enhanced Mail (PEM) representation of the public key.
- [x963Representation](x963representation.md) — An ANSI x9.63 representation of the public key.
