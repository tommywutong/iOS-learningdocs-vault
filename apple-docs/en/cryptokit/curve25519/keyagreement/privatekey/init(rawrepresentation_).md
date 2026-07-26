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
doc_path: '/documentation/cryptokit/curve25519/keyagreement/privatekey/init(rawrepresentation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/curve25519/keyagreement/privatekey/init(rawrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/curve25519/keyagreement/privatekey/init%28rawrepresentation%3A%29.json'
content_hash: 'sha256:c3f847f93833a1dd'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [Curve25519](../../../curve25519.md) · [KeyAgreement](../../keyagreement.md) · [PrivateKey](../privatekey.md)

# init(rawRepresentation:)

<sub>Initializer</sub>

Creates a Curve25519 private key for key agreement from a collection of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(rawRepresentation: D) throws where D : ContiguousBytes
```

## Parameters

- `rawRepresentation` — A raw representation of the key as a collection of contiguous bytes.

## See Also

### Creating a private key

- [init()](<init().md>) — Creates a random Curve25519 private key for key agreement.
