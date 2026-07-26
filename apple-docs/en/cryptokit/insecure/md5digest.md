---
title: Insecure.MD5Digest
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/insecure/md5digest
source_url: 'https://developer.apple.com/documentation/cryptokit/insecure/md5digest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/insecure/md5digest.json'
content_hash: 'sha256:0604a66eb2d3eded'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [Insecure](../insecure.md)

# Insecure.MD5Digest

<sub>Structure</sub>

The output of a MD5 hash.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MD5Digest
```

## Relationships

- **Conforms To**: [ContiguousBytes](../../foundation/contiguousbytes.md), [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Digest](../digest.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [Sequence](../../swift/sequence.md)

## Topics

### Inspecting the digest length

- [byteCount](md5digest/bytecount.md) — The number of bytes in the digest.

### Describing a digest

- [description](md5digest/description.md) — A human-readable description of the digest.

### Hashing a digest

- [hash(into:)](<md5digest/hash(into_).md>) — Hashes the essential components of the digest by feeding them into the given hash function.

## See Also

### Specifying the output type

- [Digest](md5/digest.md) — The digest type for a MD5 hash function.
