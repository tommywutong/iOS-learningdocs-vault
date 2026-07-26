---
title: 'init(seedRepresentation:publicKey:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/mlkem768/privatekey/init(seedrepresentation:publickey:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/mlkem768/privatekey/init(seedrepresentation:publickey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mlkem768/privatekey/init%28seedrepresentation%3Apublickey%3A%29.json'
content_hash: 'sha256:2645742eecb1974c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLKEM768](../../mlkem768.md) · [PrivateKey](../privatekey.md)

# init(seedRepresentation:publicKey:)

<sub>Initializer</sub>

Initializes a private key from a seed representation and optional public key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(seedRepresentation: D, publicKey: MLKEM768.PublicKey?) throws where D : DataProtocol
```

## Parameters

- `seedRepresentation` — The seed representation `d||z`, as specified in the `ML-KEM.KeyGen_internal(d,z)` algorithm (Algorithm 16) of FIPS 203.

- `publicKey` — An optional public key. Pass this to check that the initialized private key is consistent with the public key. The initializer throws if the public key doesn’t match the expected value.

## See Also

### Creating a private key

- [generate()](<generate().md>) — Generates a new, random private key.
- [init()](<init().md>) — Initializes a random private key.
- [init(integrityCheckedRepresentation:)](<init(integritycheckedrepresentation_).md>) — Initializes a private key from an integrity-checked representation.
