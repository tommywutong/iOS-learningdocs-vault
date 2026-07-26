---
title: Digest
framework: Apple CryptoKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/digest
source_url: 'https://developer.apple.com/documentation/cryptokit/digest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/digest.json'
content_hash: 'sha256:b6779447838d8c26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# Digest

<sub>Protocol</sub>

A type that represents the output of a hash.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol Digest : ContiguousBytes, CustomStringConvertible, Hashable, Sendable, Sequence where Self.Element == UInt8
```

## Relationships

- **Inherits From**: [ContiguousBytes](../foundation/contiguousbytes.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

- **Conforming Types**: [MD5Digest](insecure/md5digest.md), [SHA1Digest](insecure/sha1digest.md), [SHA256Digest](sha256digest.md), [SHA384Digest](sha384digest.md), [SHA3_256Digest](sha3_256digest.md), [SHA3_384Digest](sha3_384digest.md), [SHA3_512Digest](sha3_512digest.md), [SHA512Digest](sha512digest.md)

## Topics

### Getting the digest length

- [byteCount](digest/bytecount.md) — The number of bytes in the digest.

### Comparing digests

- [==(_:_:)](<digest/==(____)-7yz3z.md>) — Determines whether a digest is equivalent to a collection of contiguous bytes.
- [==(_:_:)](<digest/==(____)-6m59k.md>) — Determines whether two digests are equal.

### Default Implementations

- [CustomStringConvertible Implementations](digest/customstringconvertible-implementations.md)

## See Also

### Specifying the output type

- [Digest](hashfunction/digest.md)
