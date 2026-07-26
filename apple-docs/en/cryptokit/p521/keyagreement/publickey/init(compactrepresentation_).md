---
title: 'init(compactRepresentation:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/p521/keyagreement/publickey/init(compactrepresentation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/p521/keyagreement/publickey/init(compactrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p521/keyagreement/publickey/init%28compactrepresentation%3A%29.json'
content_hash: 'sha256:bf165c1763cf2bc4'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P521](../../../p521.md) · [KeyAgreement](../../keyagreement.md) · [PublicKey](../publickey.md)

# init(compactRepresentation:)

<sub>Initializer</sub>

Creates a P-521 public key for key agreement from a compact representation of the key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Bytes>(compactRepresentation: Bytes) throws where Bytes : ContiguousBytes
```

## Parameters

- `compactRepresentation` — A compact representation of the key as a collection of contiguous bytes.

## See Also

### Creating a public key

- [init(rawRepresentation:)](<init(rawrepresentation_).md>) — Creates a P-521 public key for key agreement from a collection of bytes.
- [init(derRepresentation:)](<init(derrepresentation_).md>) — Creates a P-521 public key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation:)](<init(pemrepresentation_).md>) — Creates a P-521 public key for key agreement from a Privacy-Enhanced Mail (PEM) representation.
- [init(x963Representation:)](<init(x963representation_).md>) — Creates a P-521 public key for key agreement from an ANSI x9.63 representation.
- [init(compressedRepresentation:)](<init(compressedrepresentation_).md>) — Creates a P-521 public key for key agreement from a compressed representation of the key.
