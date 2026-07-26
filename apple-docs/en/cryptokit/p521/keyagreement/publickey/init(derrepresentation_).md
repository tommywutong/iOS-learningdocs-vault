---
title: 'init(derRepresentation:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/p521/keyagreement/publickey/init(derrepresentation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/p521/keyagreement/publickey/init(derrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p521/keyagreement/publickey/init%28derrepresentation%3A%29.json'
content_hash: 'sha256:caf4666910c48b0f'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P521](../../../p521.md) · [KeyAgreement](../../keyagreement.md) · [PublicKey](../publickey.md)

# init(derRepresentation:)

<sub>Initializer</sub>

Creates a P-521 public key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Bytes>(derRepresentation: Bytes) throws where Bytes : RandomAccessCollection, Bytes.Element == UInt8
```

## Parameters

- `derRepresentation` — A DER-encoded representation of the key.

## See Also

### Creating a public key

- [init(rawRepresentation:)](<init(rawrepresentation_).md>) — Creates a P-521 public key for key agreement from a collection of bytes.
- [init(compactRepresentation:)](<init(compactrepresentation_).md>) — Creates a P-521 public key for key agreement from a compact representation of the key.
- [init(pemRepresentation:)](<init(pemrepresentation_).md>) — Creates a P-521 public key for key agreement from a Privacy-Enhanced Mail (PEM) representation.
- [init(x963Representation:)](<init(x963representation_).md>) — Creates a P-521 public key for key agreement from an ANSI x9.63 representation.
- [init(compressedRepresentation:)](<init(compressedrepresentation_).md>) — Creates a P-521 public key for key agreement from a compressed representation of the key.
