---
title: MLKEM1024.PublicKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/mlkem1024/publickey
source_url: 'https://developer.apple.com/documentation/cryptokit/mlkem1024/publickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mlkem1024/publickey.json'
content_hash: 'sha256:0074456084963c08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [MLKEM1024](../mlkem1024.md)

# MLKEM1024.PublicKey

<sub>Structure</sub>

A public key you use to encapsulate shared secrets with the Module-Lattice key encapsulation mechanism.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PublicKey
```

## Relationships

- **Conforms To**: [KEMPublicKey](../kempublickey.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a public key

- [init(rawRepresentation:)](<publickey/init(rawrepresentation_).md>) — Initializes a public key from a raw representation.

### Accessing a key’s raw representation

- [rawRepresentation](publickey/rawrepresentation.md) — A serialized representation of the public key.

### Encapsulating a shared secret

- [encapsulate()](<publickey/encapsulate().md>) — Generates and encapsulates a shared secret.

## See Also

### Keys

- [PrivateKey](privatekey.md) — A private key you use to decapsulate shared secrets with the Module-Lattice key encapsulation mechanism.
