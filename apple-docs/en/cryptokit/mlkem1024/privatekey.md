---
title: MLKEM1024.PrivateKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/mlkem1024/privatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/mlkem1024/privatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mlkem1024/privatekey.json'
content_hash: 'sha256:d6d9d6a5e31107e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [MLKEM1024](../mlkem1024.md)

# MLKEM1024.PrivateKey

<sub>Structure</sub>

A private key you use to decapsulate shared secrets with the Module-Lattice key encapsulation mechanism.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PrivateKey
```

## Relationships

- **Conforms To**: [KEMPrivateKey](../kemprivatekey.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a private key

- [generate()](<privatekey/generate().md>) — Generates a new, random private key.
- [init()](<privatekey/init().md>) — Initializes a random private key.
- [init(integrityCheckedRepresentation:)](<privatekey/init(integritycheckedrepresentation_).md>) — Initializes a private key from an integrity-checked representation.
- [init(seedRepresentation:publicKey:)](<privatekey/init(seedrepresentation_publickey_).md>) — Initializes a private key from a seed representation and optional public key.

### Inspecting a private key’s properties

- [integrityCheckedRepresentation](privatekey/integritycheckedrepresentation.md) — An integrity-checked representation of the private key.
- [publicKey](privatekey/publickey.md) — The corresponding public key.
- [seedRepresentation](privatekey/seedrepresentation.md) — The private key’s seed representation.

### Decapsulating shared secrets

- [decapsulate(_:)](<privatekey/decapsulate(__).md>) — Decapsulate a shared secret.

## See Also

### Keys

- [PublicKey](publickey.md) — A public key you use to encapsulate shared secrets with the Module-Lattice key encapsulation mechanism.
