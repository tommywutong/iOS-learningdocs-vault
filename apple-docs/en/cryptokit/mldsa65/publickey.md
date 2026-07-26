---
title: MLDSA65.PublicKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/mldsa65/publickey
source_url: 'https://developer.apple.com/documentation/cryptokit/mldsa65/publickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mldsa65/publickey.json'
content_hash: 'sha256:7da397d0ba541517'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [MLDSA65](../mldsa65.md)

# MLDSA65.PublicKey

<sub>Structure</sub>

The public key for MLDSA65.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PublicKey
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a public key

- [init(rawRepresentation:)](<publickey/init(rawrepresentation_).md>) — Parses a public key from a serialized representation.

### Getting the raw representation

- [rawRepresentation](publickey/rawrepresentation.md) — A serialized representation of the public key.

### Instance Methods

- [isValidSignature(_:for:)](<publickey/isvalidsignature(__for_).md>) — Verifies a MLDSA65 signature.
- [isValidSignature(_:for:context:)](<publickey/isvalidsignature(__for_context_).md>) — Verifies a MLDSA65 signature, in a specific context.

## See Also

### Keys

- [PrivateKey](privatekey.md) — The private key for MLDSA65.
