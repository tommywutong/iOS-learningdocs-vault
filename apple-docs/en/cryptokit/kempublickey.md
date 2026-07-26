---
title: KEMPublicKey
framework: Apple CryptoKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/kempublickey
source_url: 'https://developer.apple.com/documentation/cryptokit/kempublickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/kempublickey.json'
content_hash: 'sha256:a897b1b5749984f5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# KEMPublicKey

<sub>Protocol</sub>

The public key for a key encapsulation mechanism.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol KEMPublicKey : Sendable
```

## Relationships

- **Inherits From**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Inherited By**: [HPKEKEMPublicKey](hpkekempublickey.md)

- **Conforming Types**: [PublicKey](mlkem1024/publickey.md), [PublicKey](mlkem768/publickey.md), [PublicKey](xwingmlkem768x25519/publickey.md)

## Topics

### Instance Methods

- [encapsulate()](<kempublickey/encapsulate().md>) — Generates and encapsulates a shared secret.

## See Also

### KEM keys

- [KEMPrivateKey](kemprivatekey.md) — The private key for a key encapsulation mechanism.
