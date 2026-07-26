---
title: HashedAuthenticationCode
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hashedauthenticationcode
source_url: 'https://developer.apple.com/documentation/cryptokit/hashedauthenticationcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hashedauthenticationcode.json'
content_hash: 'sha256:1bd8d0072ac3d92c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# HashedAuthenticationCode

<sub>Structure</sub>

A hash-based message authentication code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct HashedAuthenticationCode<H> where H : HashFunction
```

## Relationships

- **Conforms To**: [ContiguousBytes](../foundation/contiguousbytes.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MessageAuthenticationCode](messageauthenticationcode.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Retrieving the code length

- [byteCount](hashedauthenticationcode/bytecount.md) — The number of bytes in the message authentication code.

### Describing a code

- [description](hashedauthenticationcode/description.md) — A human-readable description of the code.

## See Also

### Working with codes

- [MAC](hmac/mac.md) — An alias for a hash-based message authentication code.
- [MessageAuthenticationCode](messageauthenticationcode.md) — A type that represents a message authentication code.
