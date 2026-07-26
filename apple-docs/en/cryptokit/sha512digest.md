---
title: SHA512Digest
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/sha512digest
source_url: 'https://developer.apple.com/documentation/cryptokit/sha512digest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/sha512digest.json'
content_hash: 'sha256:e2a0a6f2de4c0a0a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# SHA512Digest

<sub>Structure</sub>

The output of a Secure Hashing Algorithm 2 (SHA-2) hash with a 512-bit digest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SHA512Digest
```

## Relationships

- **Conforms To**: [ContiguousBytes](../foundation/contiguousbytes.md), [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Digest](digest.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Inspecting the digest length

- [byteCount](sha512digest/bytecount.md) — The number of bytes in the digest.

### Describing a digest

- [description](sha512digest/description.md) — A human-readable description of the digest.

### Hashing a digest

- [hash(into:)](<sha512digest/hash(into_).md>) — Hashes the essential components of the digest by feeding them into the given hash function.

## See Also

### Specifying the output type

- [Digest](sha512/digest.md) — The digest type for a SHA512 hash function.
