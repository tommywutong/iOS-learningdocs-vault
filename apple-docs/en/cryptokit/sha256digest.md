---
title: SHA256Digest
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/sha256digest
source_url: 'https://developer.apple.com/documentation/cryptokit/sha256digest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/sha256digest.json'
content_hash: 'sha256:cc02c20c5ada08db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# SHA256Digest

<sub>Structure</sub>

The output of a Secure Hashing Algorithm 2 (SHA-2) hash with a 256-bit digest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SHA256Digest
```

## Relationships

- **Conforms To**: [ContiguousBytes](../foundation/contiguousbytes.md), [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Digest](digest.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Inspecting the digest length

- [byteCount](sha256digest/bytecount.md) — The number of bytes in the digest.

### Describing a digest

- [description](sha256digest/description.md) — A human-readable description of the digest.

### Hashing a digest

- [hash(into:)](<sha256digest/hash(into_).md>) — Hashes the essential components of the digest by feeding them into the given hash function.

## See Also

### Specifying the output type

- [Digest](sha256/digest.md) — The digest type for a SHA256 hash function.
