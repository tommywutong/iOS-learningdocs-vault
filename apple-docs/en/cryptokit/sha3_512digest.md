---
title: SHA3_512Digest
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/sha3_512digest
source_url: 'https://developer.apple.com/documentation/cryptokit/sha3_512digest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/sha3_512digest.json'
content_hash: 'sha256:ea82a9e05746e226'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# SHA3_512Digest

<sub>Structure</sub>

The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 512-bit digest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SHA3_512Digest
```

## Relationships

- **Conforms To**: [ContiguousBytes](../foundation/contiguousbytes.md), [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Digest](digest.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Instance Properties

- [description](sha3_512digest/description.md) — A human-readable description of the digest.

### Instance Methods

- [hash(into:)](<sha3_512digest/hash(into_).md>) — Hashes the essential components of the digest by feeding them into the given hash function.

### Type Properties

- [byteCount](sha3_512digest/bytecount.md) — The number of bytes in the digest.
