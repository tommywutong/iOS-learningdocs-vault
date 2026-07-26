---
title: HPKEKEMPublicKey
framework: Apple CryptoKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpkekempublickey
source_url: 'https://developer.apple.com/documentation/cryptokit/hpkekempublickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpkekempublickey.json'
content_hash: 'sha256:96b4c8118849ffed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# HPKEKEMPublicKey

<sub>Protocol</sub>

A type that represents the public key in HPKE

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol HPKEKEMPublicKey : HPKEPublicKeySerialization, KEMPublicKey
```

## Relationships

- **Inherits From**: [HPKEPublicKeySerialization](hpkepublickeyserialization.md), [KEMPublicKey](kempublickey.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [PublicKey](xwingmlkem768x25519/publickey.md)

## Topics

### Associated Types

- [EphemeralPrivateKey](hpkekempublickey/ephemeralprivatekey.md) — The type of the ephemeral private key.
