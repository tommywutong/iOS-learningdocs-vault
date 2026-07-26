---
title: x963Representation
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/p384/signing/privatekey/x963representation
source_url: 'https://developer.apple.com/documentation/cryptokit/p384/signing/privatekey/x963representation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p384/signing/privatekey/x963representation.json'
content_hash: 'sha256:c01c220ddafdceb7'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P384](../../../p384.md) · [Signing](../../signing.md) · [PrivateKey](../privatekey.md)

# x963Representation

<sub>Instance Property</sub>

An ANSI x9.63 representation of the private key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var x963Representation: Data { get }
```

## See Also

### Representing the key

- [rawRepresentation](rawrepresentation.md) — A data representation of the private key.
- [derRepresentation](derrepresentation.md) — A Distinguished Encoding Rules (DER) encoded representation of the private key.
- [pemRepresentation](pemrepresentation.md) — A Privacy-Enhanced Mail (PEM) representation of the private key.
