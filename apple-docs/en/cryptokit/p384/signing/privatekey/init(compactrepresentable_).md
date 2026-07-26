---
title: 'init(compactRepresentable:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/p384/signing/privatekey/init(compactrepresentable:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/p384/signing/privatekey/init(compactrepresentable:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p384/signing/privatekey/init%28compactrepresentable%3A%29.json'
content_hash: 'sha256:dd28622a8c69602a'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P384](../../../p384.md) · [Signing](../../signing.md) · [PrivateKey](../privatekey.md)

# init(compactRepresentable:)

<sub>Initializer</sub>

Creates a random P-384 private key for signing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(compactRepresentable: Bool = true)
```

## Parameters

- `compactRepresentable` — A Boolean value that indicates whether CryptoKit creates the key with the structure to enable compact point encoding.

## Discussion

Keys that use a compact point encoding enable shorter public keys, but aren’t compliant with FIPS certification. If your app requires FIPS certification, create a key with [init(rawRepresentation:)](<init(rawrepresentation_).md>).

## See Also

### Creating a private key

- [init(rawRepresentation:)](<init(rawrepresentation_).md>) — Creates a P-384 private key for signing from a collection of bytes.
- [init(derRepresentation:)](<init(derrepresentation_).md>) — Creates a P-384 private key for signing from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation:)](<init(pemrepresentation_).md>) — Creates a P-384 private key for signing from a Privacy-Enhanced Mail PEM) representation.
- [init(x963Representation:)](<init(x963representation_).md>) — Creates a P-384 private key for signing from an ANSI x9.63 representation.
