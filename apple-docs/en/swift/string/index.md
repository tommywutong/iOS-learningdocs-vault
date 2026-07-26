---
title: String.Index
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/index
source_url: 'https://developer.apple.com/documentation/swift/string/index'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/index.json'
content_hash: 'sha256:c9594ccb4754d238'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# String.Index

<sub>Structure</sub>

A position of a character or code unit in a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Index
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../bitwisecopyable.md), [Comparable](../comparable.md), [Copyable](../copyable.md), [CustomDebugStringConvertible](../customdebugstringconvertible.md), [Equatable](../equatable.md), [Escapable](../escapable.md), [Hashable](../hashable.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Initializers

- [init(_:within:)](<index/init(__within_)-2txd4.md>) — Creates an index in the given UTF-16 view that corresponds exactly to the specified string position.
- [init(_:within:)](<index/init(__within_)-2u3iq.md>) — Creates an index in the given string that corresponds exactly to the specified position.
- [init(_:within:)](<index/init(__within_)-379kg.md>)
- [init(_:within:)](<index/init(__within_)-3eir6.md>) — Creates an index in the given string that corresponds exactly to the specified position.
- [init(_:within:)](<index/init(__within_)-5lb6l.md>) — Creates an index in the given UTF-8 view that corresponds exactly to the specified `UTF16View` position.
- [init(_:within:)](<index/init(__within_)-7e1rw.md>) — Creates an index in the given Unicode scalars view that corresponds exactly to the specified `UTF16View` position.
- [init(encodedOffset:)](<index/init(encodedoffset_).md>) — Creates a new index at the specified code unit offset.
- [init(utf16Offset:in:)](<index/init(utf16offset_in_).md>) — Creates a new index at the specified UTF-16 code unit offset

### Instance Properties

- [encodedOffset](index/encodedoffset.md) — The offset into a string’s code units for this index.

### Instance Methods

- [samePosition(in:)](<index/sameposition(in_)-3mz95.md>) — Returns the position in the given UTF-8 view that corresponds exactly to this index.
- [samePosition(in:)](<index/sameposition(in_)-4yeo1.md>) — Returns the position in the given view of Unicode scalars that corresponds exactly to this index.
- [samePosition(in:)](<index/sameposition(in_)-6oxfv.md>) — Returns the position in the given string that corresponds exactly to this index.
- [samePosition(in:)](<index/sameposition(in_)-86cct.md>) — Returns the position in the given UTF-16 view that corresponds exactly to this index.
- [utf16Offset(in:)](<index/utf16offset(in_).md>) — The UTF-16 code unit offset corresponding to this index.

### Default Implementations

- [Comparable Implementations](index/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](index/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](index/equatable-implementations.md)
- [Hashable Implementations](index/hashable-implementations.md)

## See Also

### Related String Types

- [Substring](../substring.md) — A slice of a string.
- [StringProtocol](../stringprotocol.md) — A type that can represent a string as a collection of characters.
- [UnicodeScalarView](unicodescalarview.md) — A view of a string’s contents as a collection of Unicode scalar values.
- [UTF16View](utf16view.md) — A view of a string’s contents as a collection of UTF-16 code units.
- [UTF8View](utf8view.md) — A view of a string’s contents as a collection of UTF-8 code units.
- [Iterator](iterator.md) — A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [Encoding](encoding.md)
