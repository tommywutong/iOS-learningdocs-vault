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
doc_path: '/documentation/cryptokit/p384/signing/publickey/init(derrepresentation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/p384/signing/publickey/init(derrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p384/signing/publickey/init%28derrepresentation%3A%29.json'
content_hash: 'sha256:98bbc87f972eab8c'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P384](../../../p384.md) · [Signing](../../signing.md) · [PublicKey](../publickey.md)

# init(derRepresentation:)

<sub>Initializer</sub>

Creates a P-384 public key for signing from a Distinguished Encoding Rules (DER) encoded representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Bytes>(derRepresentation: Bytes) throws where Bytes : RandomAccessCollection, Bytes.Element == UInt8
```

## Parameters

- `derRepresentation` — A DER-encoded representation of the key.

## See Also

### Creating a key

- [init(rawRepresentation:)](<init(rawrepresentation_).md>) — Creates a P-384 public key for signing from a collection of bytes.
- [init(compactRepresentation:)](<init(compactrepresentation_).md>) — Creates a P-384 public key for signing from a compact representation of the key.
- [init(compressedRepresentation:)](<init(compressedrepresentation_).md>) — Creates a P-384 public key for signing from a compressed representation of the key.
- [init(pemRepresentation:)](<init(pemrepresentation_).md>) — Creates a P-384 public key for signing from a Privacy-Enhanced Mail (PEM) representation.
- [init(x963Representation:)](<init(x963representation_).md>) — Creates a P-384 public key for signing from an ANSI x9.63 representation.
