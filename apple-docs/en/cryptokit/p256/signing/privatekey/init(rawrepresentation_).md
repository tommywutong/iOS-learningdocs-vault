---
title: 'init(rawRepresentation:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/p256/signing/privatekey/init(rawrepresentation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/p256/signing/privatekey/init(rawrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p256/signing/privatekey/init%28rawrepresentation%3A%29.json'
content_hash: 'sha256:0950d901be97a7ef'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P256](../../../p256.md) · [Signing](../../signing.md) · [PrivateKey](../privatekey.md)

# init(rawRepresentation:)

<sub>Initializer</sub>

Creates a P-256 private key for signing from a collection of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Bytes>(rawRepresentation: Bytes) throws where Bytes : ContiguousBytes
```

## Parameters

- `rawRepresentation` — A raw representation of the key as a collection of contiguous bytes.

## See Also

### Creating a private key

- [init(compactRepresentable:)](<init(compactrepresentable_).md>) — Creates a random P-256 private key for signing.
- [init(derRepresentation:)](<init(derrepresentation_).md>) — Creates a P-256 private key for signing from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation:)](<init(pemrepresentation_).md>) — Creates a P-256 private key for signing from a Privacy-Enhanced Mail PEM) representation.
- [init(x963Representation:)](<init(x963representation_).md>) — Creates a P-256 private key for signing from an ANSI x9.63 representation.
