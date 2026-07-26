---
title: MessageAuthenticationCode
framework: Apple CryptoKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/messageauthenticationcode
source_url: 'https://developer.apple.com/documentation/cryptokit/messageauthenticationcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/messageauthenticationcode.json'
content_hash: 'sha256:d965f7fa51c96f05'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# MessageAuthenticationCode

<sub>Protocol</sub>

A type that represents a message authentication code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol MessageAuthenticationCode : ContiguousBytes, CustomStringConvertible, Hashable, Sendable, Sequence where Self.Element == UInt8
```

## Relationships

- **Inherits From**: [ContiguousBytes](../foundation/contiguousbytes.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

- **Conforming Types**: [HashedAuthenticationCode](hashedauthenticationcode.md)

## Topics

### Retrieving the code length

- [byteCount](messageauthenticationcode/bytecount.md) — The number of bytes in the message authentication code.

### Comparing codes

- [==(_:_:)](<messageauthenticationcode/==(____)-3rxc4.md>) — Returns a Boolean value indicating whether a message authentication code is equivalent to a collection of binary data.
- [==(_:_:)](<messageauthenticationcode/==(____)-b90.md>) — Returns a Boolean value indicating whether two message authentication codes are equal.

### Default Implementations

- [CustomStringConvertible Implementations](messageauthenticationcode/customstringconvertible-implementations.md)

## See Also

### Working with codes

- [MAC](hmac/mac.md) — An alias for a hash-based message authentication code.
- [HashedAuthenticationCode](hashedauthenticationcode.md) — A hash-based message authentication code.
