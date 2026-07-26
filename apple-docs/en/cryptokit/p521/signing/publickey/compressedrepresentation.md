---
title: compressedRepresentation
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/p521/signing/publickey/compressedrepresentation
source_url: 'https://developer.apple.com/documentation/cryptokit/p521/signing/publickey/compressedrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p521/signing/publickey/compressedrepresentation.json'
content_hash: 'sha256:5035e0af661aa812'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P521](../../../p521.md) · [Signing](../../signing.md) · [PublicKey](../publickey.md)

# compressedRepresentation

<sub>Instance Property</sub>

A compressed representation of the public key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var compressedRepresentation: Data { get }
```

## See Also

### Representing the key

- [rawRepresentation](rawrepresentation.md) — A full representation of the public key.
- [compactRepresentation](compactrepresentation.md) — A compact representation of the public key.
- [derRepresentation](derrepresentation.md) — A Distinguished Encoding Rules (DER) encoded representation of the public key.
- [pemRepresentation](pemrepresentation.md) — A Privacy-Enhanced Mail (PEM) representation of the public key.
- [x963Representation](x963representation.md) — An ANSI x9.63 representation of the public key.
