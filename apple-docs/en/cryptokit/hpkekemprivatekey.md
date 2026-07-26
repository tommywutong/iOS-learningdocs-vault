---
title: HPKEKEMPrivateKey
framework: Apple CryptoKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpkekemprivatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/hpkekemprivatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpkekemprivatekey.json'
content_hash: 'sha256:7591ba651ef70e05'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# HPKEKEMPrivateKey

<sub>Protocol</sub>

A type that represents the private key in HPKE.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol HPKEKEMPrivateKey : KEMPrivateKey where Self.PublicKey : HPKEKEMPublicKey
```

## Relationships

- **Inherits From**: [KEMPrivateKey](kemprivatekey.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Inherited By**: [HPKEKEMPrivateKeyGeneration](hpkekemprivatekeygeneration.md)

- **Conforming Types**: [PrivateKey](xwingmlkem768x25519/privatekey.md)
