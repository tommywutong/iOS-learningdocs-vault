---
title: 'init(x963Representation:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/p521/signing/publickey/init(x963representation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/p521/signing/publickey/init(x963representation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p521/signing/publickey/init%28x963representation%3A%29.json'
content_hash: 'sha256:82570cfce5ae65b2'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P521](../../../p521.md) · [Signing](../../signing.md) · [PublicKey](../publickey.md)

# init(x963Representation:)

<sub>Initializer</sub>

Creates a P-521 public key for signing from an ANSI x9.63 representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Bytes>(x963Representation: Bytes) throws where Bytes : ContiguousBytes
```

## Parameters

- `x963Representation` — An ANSI x9.63 representation of the key.

## See Also

### Creating a key

- [init(rawRepresentation:)](<init(rawrepresentation_).md>) — Creates a P-521 public key for signing from a collection of bytes.
- [init(compactRepresentation:)](<init(compactrepresentation_).md>) — Creates a P-521 public key for signing from a compact representation of the key.
- [init(compressedRepresentation:)](<init(compressedrepresentation_).md>) — Creates a P-521 public key for signing from a compressed representation of the key.
- [init(derRepresentation:)](<init(derrepresentation_).md>) — Creates a P-521 public key for signing from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation:)](<init(pemrepresentation_).md>) — Creates a P-521 public key for signing from a Privacy-Enhanced Mail (PEM) representation.
