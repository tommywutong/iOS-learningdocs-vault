---
title: MLKEM768.OneTimePrivateKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/cryptokit/mlkem768/onetimeprivatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/mlkem768/onetimeprivatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mlkem768/onetimeprivatekey.json'
content_hash: 'sha256:428eff3fc9d22323'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [MLKEM768](../mlkem768.md)

# MLKEM768.OneTimePrivateKey

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct OneTimePrivateKey
```

## Relationships

- **Conforms To**: [KEMOneTimePrivateKey](../kemonetimeprivatekey.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init()](<onetimeprivatekey/init().md>) — Initializes a random one-time-use private key. _(beta)_

### Instance Properties

- [publicKey](onetimeprivatekey/publickey.md) — The corresponding public key. _(beta)_

### Instance Methods

- [decapsulate(_:)](<onetimeprivatekey/decapsulate(__).md>) — Decapsulate a shared secret. _(beta)_

### Type Methods

- [generate()](<onetimeprivatekey/generate().md>) — Generates a new, random one-time-use private key. _(beta)_
