---
title: HPKEDiffieHellmanPrivateKey
framework: Apple CryptoKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpkediffiehellmanprivatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/hpkediffiehellmanprivatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpkediffiehellmanprivatekey.json'
content_hash: 'sha256:eca4e060e3477d8c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# HPKEDiffieHellmanPrivateKey

<sub>Protocol</sub>

A type that represents the private key in a Diffie-Hellman key exchange.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol HPKEDiffieHellmanPrivateKey : DiffieHellmanKeyAgreement where Self.PublicKey : HPKEDiffieHellmanPublicKey
```

## Relationships

- **Inherits From**: [DiffieHellmanKeyAgreement](diffiehellmankeyagreement.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Inherited By**: [HPKEDiffieHellmanPrivateKeyGeneration](hpkediffiehellmanprivatekeygeneration.md)

- **Conforming Types**: [PrivateKey](curve25519/keyagreement/privatekey.md), [PrivateKey](p256/keyagreement/privatekey.md), [PrivateKey](p384/keyagreement/privatekey.md), [PrivateKey](p521/keyagreement/privatekey.md), [PrivateKey](secureenclave/p256/keyagreement/privatekey.md)
