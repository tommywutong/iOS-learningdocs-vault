---
title: XWingMLKEM768X25519.PublicKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/xwingmlkem768x25519/publickey
source_url: 'https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/publickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/xwingmlkem768x25519/publickey.json'
content_hash: 'sha256:9a804226b92f73f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [XWingMLKEM768X25519](../xwingmlkem768x25519.md)

# XWingMLKEM768X25519.PublicKey

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PublicKey
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Escapable](../../swift/escapable.md), [HPKEKEMPublicKey](../hpkekempublickey.md), [HPKEPublicKeySerialization](../hpkepublickeyserialization.md), [KEMPublicKey](../kempublickey.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Accessing a key’s raw representation

- [rawRepresentation](publickey/rawrepresentation.md)

### Accessing the corresponding private key type

- [HPKEEphemeralPrivateKey](publickey/hpkeephemeralprivatekey.md) — The type of the ephemeral private key associated with this public key.

### Initializers

- [init(rawRepresentation:)](<publickey/init(rawrepresentation_).md>)

### Default Implementations

- [HPKEKEMPublicKey Implementations](publickey/hpkekempublickey-implementations.md)
- [HPKEPublicKeySerialization Implementations](publickey/hpkepublickeyserialization-implementations.md)

## See Also

### Keys

- [PrivateKey](privatekey.md)
