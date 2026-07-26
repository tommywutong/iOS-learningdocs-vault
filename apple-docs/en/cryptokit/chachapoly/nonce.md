---
title: ChaChaPoly.Nonce
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/chachapoly/nonce
source_url: 'https://developer.apple.com/documentation/cryptokit/chachapoly/nonce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/chachapoly/nonce.json'
content_hash: 'sha256:37db9c007a6ae5bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [ChaChaPoly](../chachapoly.md)

# ChaChaPoly.Nonce

<sub>Structure</sub>

A value used once during a cryptographic operation and then discarded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Nonce
```

## Overview

Don’t reuse the same nonce for multiple calls to encryption APIs. It’s critical that nonces are unique per call to encryption APIs in order to protect the integrity of the encryption.

## Relationships

- **Conforms To**: [ContiguousBytes](../../foundation/contiguousbytes.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [Sequence](../../swift/sequence.md)

## Topics

### Creating a nonce

- [init()](<nonce/init().md>) — Creates a new random nonce.
- [init(data:)](<nonce/init(data_).md>) — Creates a nonce from the given data.

### Iterating over a nonce’s bytes

- [makeIterator()](<nonce/makeiterator().md>) — Returns an iterator over the elements of the nonce.

### Initializers

- [init(copying:)](<nonce/init(copying_).md>) — Creates a nonce from the given data. _(beta)_

### Instance Properties

- [bytes](nonce/bytes.md) — The bytes stored in the nonce.
- [count](nonce/count.md) — The number of bytes stored in the nonce.
