---
title: Insecure.SHA1
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/insecure/sha1
source_url: 'https://developer.apple.com/documentation/cryptokit/insecure/sha1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/insecure/sha1.json'
content_hash: 'sha256:f35cab1fe0904ed6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [Insecure](../insecure.md)

# Insecure.SHA1

<sub>Structure</sub>

An implementation of SHA1 hashing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SHA1
```

## Overview

The [SHA1](sha1.md) hash implements the [HashFunction](../hashfunction.md) protocol to produce a SHA1 digest ([SHA1Digest](sha1digest.md)).

You can compute the digest by calling the static `hash(data:)` method once. Alternatively, if the data that you want to hash is too large to fit in memory, you can compute the digest iteratively by creating a new hash instance, calling the `update(data:)` method repeatedly with blocks of data, and then calling the [finalize()](<sha1/finalize().md>) method to get the result.

> [!important] Important
> This hash algorithm isn’t considered cryptographically secure, but is provided for backward compatibility with older services that require it. For new services, prefer one of the secure hashes, like [SHA512](../sha512.md).

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Escapable](../../swift/escapable.md), [HashFunction](../hashfunction.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Specifying the output type

- [Digest](sha1/digest.md) — The digest type for a SHA1 hash function.
- [SHA1Digest](sha1digest.md) — The output of a SHA1 hash.

### Reporting the hash length

- [byteCount](sha1/bytecount.md) — The number of bytes in a SHA1 digest.

### Computing a hash iteratively

- [init()](<sha1/init().md>) — Creates a SHA1 hash function.
- [update(bufferPointer:)](<sha1/update(bufferpointer_).md>) — Incrementally updates the hash function with the contents of the buffer.
- [finalize()](<sha1/finalize().md>) — Finalizes the hash function and returns the computed digest.

### Reporting hash function information

- [blockByteCount](sha1/blockbytecount.md) — The number of bytes that represents the hash function’s internal state.

## See Also

### Hashes

- [MD5](md5.md) — An implementation of MD5 hashing.
