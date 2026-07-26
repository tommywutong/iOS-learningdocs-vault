---
title: Insecure.MD5
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/insecure/md5
source_url: 'https://developer.apple.com/documentation/cryptokit/insecure/md5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/insecure/md5.json'
content_hash: 'sha256:992146c81b814907'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [Insecure](../insecure.md)

# Insecure.MD5

<sub>Structure</sub>

An implementation of MD5 hashing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MD5
```

## Overview

The [MD5](md5.md) hash implements the [HashFunction](../hashfunction.md) protocol to produce an MD5 digest ([MD5Digest](md5digest.md)).

You can compute the digest by calling the static `hash(data:)` method once. Alternatively, if the data that you want to hash is too large to fit in memory, you can compute the digest iteratively by creating a new hash instance, calling the `update(data:)` method repeatedly with blocks of data, and then calling the [finalize()](<md5/finalize().md>) method to get the result.

> [!important] Important
> This hash algorithm isn’t considered cryptographically secure, but is provided for backward compatibility with older services that require it. For new services, prefer one of the secure hashes, like [SHA512](../sha512.md).

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Escapable](../../swift/escapable.md), [HashFunction](../hashfunction.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Specifying the output type

- [Digest](md5/digest.md) — The digest type for a MD5 hash function.
- [MD5Digest](md5digest.md) — The output of a MD5 hash.

### Reporting the hash length

- [byteCount](md5/bytecount.md) — The number of bytes in an MD5 digest.

### Computing a hash iteratively

- [init()](<md5/init().md>) — Creates a MD5 hash function.
- [update(bufferPointer:)](<md5/update(bufferpointer_).md>) — Incrementally updates the hash function with the contents of the buffer.
- [finalize()](<md5/finalize().md>) — Finalizes the hash function and returns the computed digest.

### Reporting hash function information

- [blockByteCount](md5/blockbytecount.md) — The number of bytes that represents the hash function’s internal state.

## See Also

### Hashes

- [SHA1](sha1.md) — An implementation of SHA1 hashing.
