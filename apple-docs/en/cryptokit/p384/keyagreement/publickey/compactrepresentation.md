---
title: compactRepresentation
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/p384/keyagreement/publickey/compactrepresentation
source_url: 'https://developer.apple.com/documentation/cryptokit/p384/keyagreement/publickey/compactrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p384/keyagreement/publickey/compactrepresentation.json'
content_hash: 'sha256:a9494321a32bab58'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P384](../../../p384.md) · [KeyAgreement](../../keyagreement.md) · [PublicKey](../publickey.md)

# compactRepresentation

<sub>Instance Property</sub>

A compact representation of the public key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var compactRepresentation: Data? { get }
```

## See Also

### Representing the key

- [rawRepresentation](rawrepresentation.md) — A full representation of the public key.
- [derRepresentation](derrepresentation.md) — A Distinguished Encoding Rules (DER) encoded representation of the public key.
- [pemRepresentation](pemrepresentation.md) — A Privacy-Enhanced Mail (PEM) representation of the public key.
- [x963Representation](x963representation.md) — An ANSI x9.63 representation of the public key.
- [compressedRepresentation](compressedrepresentation.md) — A compressed representation of the public key.
