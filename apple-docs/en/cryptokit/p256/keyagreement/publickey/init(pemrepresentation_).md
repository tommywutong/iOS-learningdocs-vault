---
title: 'init(pemRepresentation:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/p256/keyagreement/publickey/init(pemrepresentation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/p256/keyagreement/publickey/init(pemrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p256/keyagreement/publickey/init%28pemrepresentation%3A%29.json'
content_hash: 'sha256:eafe9e0805c2a903'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P256](../../../p256.md) · [KeyAgreement](../../keyagreement.md) · [PublicKey](../publickey.md)

# init(pemRepresentation:)

<sub>Initializer</sub>

Creates a P-256 public key for key agreement from a Privacy-Enhanced Mail (PEM) representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(pemRepresentation: String) throws
```

## Parameters

- `pemRepresentation` — A PEM representation of the key.

## See Also

### Creating a public key

- [init(rawRepresentation:)](<init(rawrepresentation_).md>) — Creates a P-256 public key for key agreement from a collection of bytes.
- [init(compactRepresentation:)](<init(compactrepresentation_).md>) — Creates a P-256 public key for key agreement from a compact representation of the key.
- [init(derRepresentation:)](<init(derrepresentation_).md>) — Creates a P-256 public key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(x963Representation:)](<init(x963representation_).md>) — Creates a P-256 public key for key agreement from an ANSI x9.63 representation.
- [init(compressedRepresentation:)](<init(compressedrepresentation_).md>) — Creates a P-256 public key for key agreement from a compressed representation of the key.
