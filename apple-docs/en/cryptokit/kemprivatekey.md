---
title: KEMPrivateKey
framework: Apple CryptoKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/kemprivatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/kemprivatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/kemprivatekey.json'
content_hash: 'sha256:f92b351d2d36cb1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# KEMPrivateKey

<sub>Protocol</sub>

The private key for a key encapsulation mechanism.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol KEMPrivateKey : Sendable
```

## Relationships

- **Inherits From**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Inherited By**: [HPKEKEMPrivateKey](hpkekemprivatekey.md), [HPKEKEMPrivateKeyGeneration](hpkekemprivatekeygeneration.md)

- **Conforming Types**: [PrivateKey](mlkem1024/privatekey.md), [PrivateKey](mlkem768/privatekey.md), [PrivateKey](secureenclave/mlkem1024/privatekey.md), [PrivateKey](secureenclave/mlkem768/privatekey.md), [PrivateKey](xwingmlkem768x25519/privatekey.md)

## Topics

### Associated Types

- [PublicKey](kemprivatekey/publickey-swift.associatedtype.md)

### Instance Properties

- [publicKey](kemprivatekey/publickey-swift.property.md) — The associated public key.

### Instance Methods

- [decapsulate(_:)](<kemprivatekey/decapsulate(__).md>) — Recovers a shared secret from an encapsulated representation.

### Type Methods

- [generate()](<kemprivatekey/generate().md>) — Generates a new random private key.

## See Also

### KEM keys

- [KEMPublicKey](kempublickey.md) — The public key for a key encapsulation mechanism.
