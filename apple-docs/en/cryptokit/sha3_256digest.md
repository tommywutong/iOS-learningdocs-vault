---
title: SHA3_256Digest
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/sha3_256digest
source_url: 'https://developer.apple.com/documentation/cryptokit/sha3_256digest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/sha3_256digest.json'
content_hash: 'sha256:ac576f1bcdbe6175'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# SHA3_256Digest

<sub>Structure</sub>

The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 256-bit digest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SHA3_256Digest
```

## Relationships

- **Conforms To**: [ContiguousBytes](../foundation/contiguousbytes.md), [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Digest](digest.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Instance Properties

- [description](sha3_256digest/description.md) — A human-readable description of the digest.

### Instance Methods

- [hash(into:)](<sha3_256digest/hash(into_).md>) — Hashes the essential components of the digest by feeding them into the given hash function.

### Type Properties

- [byteCount](sha3_256digest/bytecount.md) — The number of bytes in the digest.
