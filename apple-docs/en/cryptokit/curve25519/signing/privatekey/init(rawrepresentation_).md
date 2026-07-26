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
doc_path: '/documentation/cryptokit/curve25519/signing/privatekey/init(rawrepresentation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/curve25519/signing/privatekey/init(rawrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/curve25519/signing/privatekey/init%28rawrepresentation%3A%29.json'
content_hash: 'sha256:26f9993cb204e4bd'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [Curve25519](../../../curve25519.md) · [Signing](../../signing.md) · [PrivateKey](../privatekey.md)

# init(rawRepresentation:)

<sub>Initializer</sub>

Creates a Curve25519 private key for signing from a data representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(rawRepresentation data: D) throws where D : ContiguousBytes
```

## Parameters

- `data` — A representation of the key as contiguous bytes from which to create the key.

## See Also

### Creating a private key

- [init()](<init().md>) — Creates a random Curve25519 private key for signing.
