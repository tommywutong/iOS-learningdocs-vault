---
title: KEMOneTimePrivateKey
framework: Apple CryptoKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/cryptokit/kemonetimeprivatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/kemonetimeprivatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/kemonetimeprivatekey.json'
content_hash: 'sha256:305353f4275b746c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# KEMOneTimePrivateKey

<sub>Protocol</sub>

A one-time private key for a key encapsulation mechanism, which can only decapsulate once but it does so faster.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol KEMOneTimePrivateKey : Sendable, ~Copyable
```

## Relationships

- **Inherits From**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [OneTimePrivateKey](mlkem1024/onetimeprivatekey.md), [OneTimePrivateKey](mlkem768/onetimeprivatekey.md), [OneTimePrivateKey](xwingmlkem768x25519/onetimeprivatekey.md)

## Topics

### Associated Types

- [PublicKey](kemonetimeprivatekey/publickey-swift.associatedtype.md) _(beta)_

### Instance Properties

- [publicKey](kemonetimeprivatekey/publickey-swift.property.md) — The associated public key. _(beta)_

### Instance Methods

- [decapsulate(_:)](<kemonetimeprivatekey/decapsulate(__).md>) — Recovers a shared secret from an encapsulated representation. _(beta)_

### Type Methods

- [generate()](<kemonetimeprivatekey/generate().md>) — Generates a new random private key. _(beta)_
