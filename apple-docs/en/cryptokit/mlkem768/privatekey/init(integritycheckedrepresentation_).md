---
title: 'init(integrityCheckedRepresentation:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/mlkem768/privatekey/init(integritycheckedrepresentation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/mlkem768/privatekey/init(integritycheckedrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mlkem768/privatekey/init%28integritycheckedrepresentation%3A%29.json'
content_hash: 'sha256:1ea497b187edaacc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLKEM768](../../mlkem768.md) · [PrivateKey](../privatekey.md)

# init(integrityCheckedRepresentation:)

<sub>Initializer</sub>

Initializes a private key from an integrity-checked representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(integrityCheckedRepresentation: D) throws where D : DataProtocol
```

## Parameters

- `integrityCheckedRepresentation` — A representation of the private key that includes the seed value, and a hash of the corresponding public key.

## See Also

### Creating a private key

- [generate()](<generate().md>) — Generates a new, random private key.
- [init()](<init().md>) — Initializes a random private key.
- [init(seedRepresentation:publicKey:)](<init(seedrepresentation_publickey_).md>) — Initializes a private key from a seed representation and optional public key.
