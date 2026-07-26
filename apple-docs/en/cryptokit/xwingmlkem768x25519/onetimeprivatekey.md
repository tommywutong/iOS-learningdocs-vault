---
title: XWingMLKEM768X25519.OneTimePrivateKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/cryptokit/xwingmlkem768x25519/onetimeprivatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/onetimeprivatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/xwingmlkem768x25519/onetimeprivatekey.json'
content_hash: 'sha256:19d92b678c7f1687'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [XWingMLKEM768X25519](../xwingmlkem768x25519.md)

# XWingMLKEM768X25519.OneTimePrivateKey

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct OneTimePrivateKey
```

## Relationships

- **Conforms To**: [KEMOneTimePrivateKey](../kemonetimeprivatekey.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [publicKey](onetimeprivatekey/publickey.md) — The corresponding public key. _(beta)_

### Instance Methods

- [decapsulate(_:)](<onetimeprivatekey/decapsulate(__).md>) — Decapsulate a shared secret. _(beta)_

### Type Methods

- [generate()](<onetimeprivatekey/generate().md>) — Generates a new, random one-time-use private key. _(beta)_
