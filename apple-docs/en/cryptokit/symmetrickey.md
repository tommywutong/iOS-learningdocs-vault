---
title: SymmetricKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/symmetrickey
source_url: 'https://developer.apple.com/documentation/cryptokit/symmetrickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/symmetrickey.json'
content_hash: 'sha256:2cb4f000b11a4ba0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# SymmetricKey

<sub>Structure</sub>

A symmetric cryptographic key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SymmetricKey
```

## Overview

You typically derive a symmetric key from an instance of a shared secret ([SharedSecret](sharedsecret.md)) that you obtain through key agreement. You use a symmetric key to compute a message authentication code like [HMAC](hmac.md), or to open and close a sealed box ([SealedBox](chachapoly/sealedbox.md) or [SealedBox](aes/gcm/sealedbox.md)) using a cipher like [ChaChaPoly](chachapoly.md) or [AES](aes.md).

## Relationships

- **Conforms To**: [ContiguousBytes](../foundation/contiguousbytes.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a key

- [init(data:)](<symmetrickey/init(data_).md>) — Creates a key from the given data.
- [init(size:)](<symmetrickey/init(size_).md>) — Generates a new random key of the given size.

### Getting the key length

- [bitCount](symmetrickey/bitcount.md) — The number of bits in the key.

### Initializers

- [init(copying:)](<symmetrickey/init(copying_).md>) — Creates a key from the given data.
- [init(copyingWithZeroing:)](<symmetrickey/init(copyingwithzeroing_).md>) — Creates a key from the given data, zeroing out the bytes afterward. _(beta)_
- [init(size:initializingWith:)](<symmetrickey/init(size_initializingwith_).md>) — Creates a new key of the given size where the key contents are initialized via a callback. _(beta)_

### Instance Properties

- [bytes](symmetrickey/bytes.md) — Access the raw bytes of the key. _(beta)_

## See Also

### Message authentication codes

- [HMAC](hmac.md) — A hash-based message authentication algorithm.
- [SymmetricKeySize](symmetrickeysize.md) — The sizes that a symmetric cryptographic key can take.
