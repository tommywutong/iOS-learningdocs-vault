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
doc_path: '/documentation/cryptokit/mldsa65/privatekey/init(seedrepresentation:publickey:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/mldsa65/privatekey/init(seedrepresentation:publickey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mldsa65/privatekey/init%28seedrepresentation%3Apublickey%3A%29.json'
content_hash: 'sha256:c552fb95be2604d8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLDSA65](../../mldsa65.md) · [PrivateKey](../privatekey.md)

# init(seedRepresentation:publicKey:)

<sub>Initializer</sub>

Initializes a private key from the seed representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(seedRepresentation: D, publicKey: MLDSA65.PublicKey?) throws where D : DataProtocol
```

## Parameters

- `seedRepresentation` — The seed representation of the private key. This parameter needs to be 32 bytes long.

- `publicKey` — The public key associated with the secret key.

## Discussion

This initializer implements the `ML-DSA.KeyGen_internal` algorithm (Algorithm 16) of FIPS 204.

If a public key is provided, a consistency check is performed between it and the derived public key.

## See Also

### Creating a private key

- [init()](<init().md>) — Creates a random MLDSA65 private key.
- [init(integrityCheckedRepresentation:)](<init(integritycheckedrepresentation_).md>) — Initializes a private key from an integrity-checked data representation.
