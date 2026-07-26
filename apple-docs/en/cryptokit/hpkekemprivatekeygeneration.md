---
title: HPKEKEMPrivateKeyGeneration
framework: Apple CryptoKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpkekemprivatekeygeneration
source_url: 'https://developer.apple.com/documentation/cryptokit/hpkekemprivatekeygeneration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpkekemprivatekeygeneration.json'
content_hash: 'sha256:8b17399dc9e2c800'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# HPKEKEMPrivateKeyGeneration

<sub>Protocol</sub>

A type that represents the generation of private keys in HPKE

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol HPKEKEMPrivateKeyGeneration : HPKEKEMPrivateKey
```

## Relationships

- **Inherits From**: [HPKEKEMPrivateKey](hpkekemprivatekey.md), [KEMPrivateKey](kemprivatekey.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [PrivateKey](xwingmlkem768x25519/privatekey.md)

## Topics

### Initializers

- [init()](<hpkekemprivatekeygeneration/init().md>) — Creates a private key generator.
