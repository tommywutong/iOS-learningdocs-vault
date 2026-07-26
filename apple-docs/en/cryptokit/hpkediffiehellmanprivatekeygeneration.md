---
title: HPKEDiffieHellmanPrivateKeyGeneration
framework: Apple CryptoKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpkediffiehellmanprivatekeygeneration
source_url: 'https://developer.apple.com/documentation/cryptokit/hpkediffiehellmanprivatekeygeneration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpkediffiehellmanprivatekeygeneration.json'
content_hash: 'sha256:5940a124741fcca4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# HPKEDiffieHellmanPrivateKeyGeneration

<sub>Protocol</sub>

A type that represents the generation of private keys in a Diffie-Hellman key exchange.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol HPKEDiffieHellmanPrivateKeyGeneration : HPKEDiffieHellmanPrivateKey
```

## Relationships

- **Inherits From**: [DiffieHellmanKeyAgreement](diffiehellmankeyagreement.md), [HPKEDiffieHellmanPrivateKey](hpkediffiehellmanprivatekey.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [PrivateKey](curve25519/keyagreement/privatekey.md), [PrivateKey](p256/keyagreement/privatekey.md), [PrivateKey](p384/keyagreement/privatekey.md), [PrivateKey](p521/keyagreement/privatekey.md)

## Topics

### Initializers

- [init()](<hpkediffiehellmanprivatekeygeneration/init().md>) — Creates a private key generator.
