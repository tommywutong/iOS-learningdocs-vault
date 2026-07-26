---
title: UInt128.Words
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint128/words-swift.struct
source_url: 'https://developer.apple.com/documentation/swift/uint128/words-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/words-swift.struct.json'
content_hash: 'sha256:0a537a7e27b2058f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt128](../uint128.md)

# UInt128.Words

<sub>Structure</sub>

A type that represents the words of a binary integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Words
```

## Overview

The `Words` type must conform to the `RandomAccessCollection` protocol with an `Element` type of `UInt` and `Index` type of `Int`.

## Relationships

- **Conforms To**: [BidirectionalCollection](../bidirectionalcollection.md), [BitwiseCopyable](../bitwisecopyable.md), [Collection](../collection.md), [Copyable](../copyable.md), [Escapable](../escapable.md), [RandomAccessCollection](../randomaccesscollection.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md), [Sequence](../sequence.md)

## Topics

### Default Implementations

- [BidirectionalCollection Implementations](words-swift.struct/bidirectionalcollection-implementations.md)
- [Collection Implementations](words-swift.struct/collection-implementations.md)
- [RandomAccessCollection Implementations](words-swift.struct/randomaccesscollection-implementations.md)
- [Sequence Implementations](words-swift.struct/sequence-implementations.md)
