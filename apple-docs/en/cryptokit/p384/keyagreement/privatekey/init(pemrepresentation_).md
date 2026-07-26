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
doc_path: '/documentation/cryptokit/p384/keyagreement/privatekey/init(pemrepresentation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/p384/keyagreement/privatekey/init(pemrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p384/keyagreement/privatekey/init%28pemrepresentation%3A%29.json'
content_hash: 'sha256:7f1c40f04b171141'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P384](../../../p384.md) · [KeyAgreement](../../keyagreement.md) · [PrivateKey](../privatekey.md)

# init(pemRepresentation:)

<sub>Initializer</sub>

Creates a P-384 private key for key agreement from a Privacy-Enhanced Mail PEM) representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(pemRepresentation: String) throws
```

## Parameters

- `pemRepresentation` — A PEM representation of the key.

## See Also

### Creating a private key

- [init(rawRepresentation:)](<init(rawrepresentation_).md>) — Creates a P-384 private key for key agreement from a collection of bytes.
- [init(compactRepresentable:)](<init(compactrepresentable_).md>) — Creates a random P-384 private key for key agreement.
- [init(derRepresentation:)](<init(derrepresentation_).md>) — Creates a P-384 private key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(x963Representation:)](<init(x963representation_).md>) — Creates a P-384 private key for key agreement from an ANSI x9.63 representation.
