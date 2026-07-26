---
title: MLDSA87.PublicKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/mldsa87/publickey
source_url: 'https://developer.apple.com/documentation/cryptokit/mldsa87/publickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mldsa87/publickey.json'
content_hash: 'sha256:ad0c8ef68b2e02a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [MLDSA87](../mldsa87.md)

# MLDSA87.PublicKey

<sub>Structure</sub>

The public key for MLDSA87.

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

- [isValidSignature(_:for:)](<publickey/isvalidsignature(__for_).md>) — Verifies a MLDSA87 signature.
- [isValidSignature(_:for:context:)](<publickey/isvalidsignature(__for_context_).md>) — Verifies a MLDSA87 signature, in a specific context.

## See Also

### Keys

- [PrivateKey](privatekey.md) — The private key for MLDSA87.
