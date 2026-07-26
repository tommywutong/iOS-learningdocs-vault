---
title: Insecure.SHA1Digest
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/insecure/sha1digest
source_url: 'https://developer.apple.com/documentation/cryptokit/insecure/sha1digest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/insecure/sha1digest.json'
content_hash: 'sha256:fdca9224a0245284'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [Insecure](../insecure.md)

# Insecure.SHA1Digest

<sub>Structure</sub>

The output of a SHA1 hash.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SHA1Digest
```

## Relationships

- **Conforms To**: [ContiguousBytes](../../foundation/contiguousbytes.md), [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Digest](../digest.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [Sequence](../../swift/sequence.md)

## Topics

### Inspecting the digest length

- [byteCount](sha1digest/bytecount.md) — The number of bytes in the digest.

### Describing a digest

- [description](sha1digest/description.md) — A human-readable description of the digest.

### Hasing a digest

- [hash(into:)](<sha1digest/hash(into_).md>) — Hashes the essential components of the digest by feeding them into the given hash function.

## See Also

### Specifying the output type

- [Digest](sha1/digest.md) — The digest type for a SHA1 hash function.
