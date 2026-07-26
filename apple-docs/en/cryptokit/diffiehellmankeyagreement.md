---
title: DiffieHellmanKeyAgreement
framework: Apple CryptoKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/diffiehellmankeyagreement
source_url: 'https://developer.apple.com/documentation/cryptokit/diffiehellmankeyagreement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/diffiehellmankeyagreement.json'
content_hash: 'sha256:223266fc60848b5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# DiffieHellmanKeyAgreement

<sub>Protocol</sub>

A Diffie-Hellman Key Agreement Key

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol DiffieHellmanKeyAgreement : Sendable
```

## Relationships

- **Inherits From**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Inherited By**: [HPKEDiffieHellmanPrivateKey](hpkediffiehellmanprivatekey.md), [HPKEDiffieHellmanPrivateKeyGeneration](hpkediffiehellmanprivatekeygeneration.md)

- **Conforming Types**: [PrivateKey](curve25519/keyagreement/privatekey.md), [PrivateKey](p256/keyagreement/privatekey.md), [PrivateKey](p384/keyagreement/privatekey.md), [PrivateKey](p521/keyagreement/privatekey.md), [PrivateKey](secureenclave/p256/keyagreement/privatekey.md)

## Topics

### Associated Types

- [PublicKey](diffiehellmankeyagreement/publickey-swift.associatedtype.md) — The public key share type to perform the DH Key Agreement

### Instance Properties

- [publicKey](diffiehellmankeyagreement/publickey-swift.property.md)

### Instance Methods

- [sharedSecretFromKeyAgreement(with:)](<diffiehellmankeyagreement/sharedsecretfromkeyagreement(with_).md>) — Performs a Diffie-Hellman Key Agreement.
