---
title: String.Iterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/iterator
source_url: 'https://developer.apple.com/documentation/swift/string/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/iterator.json'
content_hash: 'sha256:cfdff386a28370ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# String.Iterator

<sub>Structure</sub>

A type that provides the collection’s iteration interface and encapsulates its iteration state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Iterator
```

## Overview

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.

## Relationships

- **Conforms To**: [IteratorProtocol](../iteratorprotocol.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Instance Methods

- [next()](<iterator/next().md>) — Advances to the next element and returns it, or `nil` if no next element exists.

### Type Aliases

- [Element](iterator/element.md) — The type of element traversed by the iterator.

## See Also

### Related String Types

- [Substring](../substring.md) — A slice of a string.
- [StringProtocol](../stringprotocol.md) — A type that can represent a string as a collection of characters.
- [Index](index.md) — A position of a character or code unit in a string.
- [UnicodeScalarView](unicodescalarview.md) — A view of a string’s contents as a collection of Unicode scalar values.
- [UTF16View](utf16view.md) — A view of a string’s contents as a collection of UTF-16 code units.
- [UTF8View](utf8view.md) — A view of a string’s contents as a collection of UTF-8 code units.
- [Encoding](encoding.md)
