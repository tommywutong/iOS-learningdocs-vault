---
title: MLDSA65.PrivateKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/mldsa65/privatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/mldsa65/privatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mldsa65/privatekey.json'
content_hash: 'sha256:286b0c76c1b39673'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [MLDSA65](../mldsa65.md)

# MLDSA65.PrivateKey

<sub>Structure</sub>

The private key for MLDSA65.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PrivateKey
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a private key

- [init()](<privatekey/init().md>) — Creates a random MLDSA65 private key.
- [init(integrityCheckedRepresentation:)](<privatekey/init(integritycheckedrepresentation_).md>) — Initializes a private key from an integrity-checked data representation.
- [init(seedRepresentation:publicKey:)](<privatekey/init(seedrepresentation_publickey_).md>) — Initializes a private key from the seed representation.

### Inspecting a private key’s properties

- [integrityCheckedRepresentation](privatekey/integritycheckedrepresentation.md) — The integrity-checked data representation of the private key.
- [publicKey](privatekey/publickey.md) — The associated public key.
- [seedRepresentation](privatekey/seedrepresentation.md) — The seed representation of the private key.

### Signing data

- [signature(for:)](<privatekey/signature(for_).md>) — Generates a MLDSA65 signature.
- [signature(for:context:)](<privatekey/signature(for_context_).md>) — Generates a MLDSA65 signature, with context.

## See Also

### Keys

- [PublicKey](publickey.md) — The public key for MLDSA65.
