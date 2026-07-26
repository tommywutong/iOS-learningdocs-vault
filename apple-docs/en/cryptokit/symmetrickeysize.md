---
title: SymmetricKeySize
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/symmetrickeysize
source_url: 'https://developer.apple.com/documentation/cryptokit/symmetrickeysize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/symmetrickeysize.json'
content_hash: 'sha256:5f20a372c44eb366'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# SymmetricKeySize

<sub>Structure</sub>

The sizes that a symmetric cryptographic key can take.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SymmetricKeySize
```

## Overview

When creating a new [SymmetricKey](symmetrickey.md) instance with a call to its [init(size:)](<symmetrickey/init(size_).md>) initializer, you typically use one of the standard key sizes, like [bits128](symmetrickeysize/bits128.md), [bits192](symmetrickeysize/bits192.md), or [bits256](symmetrickeysize/bits256.md). When you need a key with a non-standard length, use the [init(bitCount:)](<symmetrickeysize/init(bitcount_).md>) initializer to create a `SymmetricKeySize` instance with a custom bit count.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Using standard key lengths

- [bits128](symmetrickeysize/bits128.md) — A size of 128 bits.
- [bits192](symmetrickeysize/bits192.md) — A size of 192 bits.
- [bits256](symmetrickeysize/bits256.md) — A size of 256 bits.

### Creating a nonstandard key length

- [init(bitCount:)](<symmetrickeysize/init(bitcount_).md>) — Creates a new key size of the given length.

### Getting the length

- [bitCount](symmetrickeysize/bitcount.md) — The number of bits in the key.

## See Also

### Message authentication codes

- [HMAC](hmac.md) — A hash-based message authentication algorithm.
- [SymmetricKey](symmetrickey.md) — A symmetric cryptographic key.
