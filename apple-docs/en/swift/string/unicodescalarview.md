---
title: String.UnicodeScalarView
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/unicodescalarview
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview.json'
content_hash: 'sha256:6206b53ca3230ce0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# String.UnicodeScalarView

<sub>Structure</sub>

A view of a string’s contents as a collection of Unicode scalar values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UnicodeScalarView
```

## Overview

You can access a string’s view of Unicode scalar values by using its `unicodeScalars` property. Unicode scalar values are the 21-bit codes that are the basic unit of Unicode. Each scalar value is represented by a `Unicode.Scalar` instance and is equivalent to a UTF-32 code unit.

```swift
let flowers = "Flowers 💐"
for v in flowers.unicodeScalars {
    print(v.value)
}
// 70
// 108
// 111
// 119
// 101
// 114
// 115
// 32
// 128144
```

Some characters that are visible in a string are made up of more than one Unicode scalar value. In that case, a string’s `unicodeScalars` view contains more elements than the string itself.

```swift
let flag = "🇵🇷"
for c in flag {
    print(c)
}
// 🇵🇷

for v in flag.unicodeScalars {
    print(v.value)
}
// 127477
// 127479
```

You can convert a `String.UnicodeScalarView` instance back into a string using the `String` type’s `init(_:)` initializer.

```swift
let favemoji = "My favorite emoji is 🎉"
if let i = favemoji.unicodeScalars.firstIndex(where: { $0.value >= 128 }) {
    let asciiPrefix = String(favemoji.unicodeScalars[..<i])
    print(asciiPrefix)
}
// Prints "My favorite emoji is "
```

## Relationships

- **Conforms To**: [BidirectionalCollection](../bidirectionalcollection.md), [Collection](../collection.md), [Copyable](../copyable.md), [CustomDebugStringConvertible](../customdebugstringconvertible.md), [CustomReflectable](../customreflectable.md), [CustomStringConvertible](../customstringconvertible.md), [Escapable](../escapable.md), [RangeReplaceableCollection](../rangereplaceablecollection.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md), [Sequence](../sequence.md)

## Topics

### Instance Properties

- [customPlaygroundQuickLook](unicodescalarview/customplaygroundquicklook.md) — A custom playground Quick Look for this instance.

### Instance Methods

- [isTriviallyIdentical(to:)](<unicodescalarview/istriviallyidentical(to_).md>) — Returns a boolean value indicating whether this unicode scalar view is trivially identical to `other`. _(beta)_

### Default Implementations

- [BidirectionalCollection Implementations](unicodescalarview/bidirectionalcollection-implementations.md)
- [Collection Implementations](unicodescalarview/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](unicodescalarview/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](unicodescalarview/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](unicodescalarview/customstringconvertible-implementations.md)
- [RangeReplaceableCollection Implementations](unicodescalarview/rangereplaceablecollection-implementations.md)
- [Sequence Implementations](unicodescalarview/sequence-implementations.md)

## See Also

### Related String Types

- [Substring](../substring.md) — A slice of a string.
- [StringProtocol](../stringprotocol.md) — A type that can represent a string as a collection of characters.
- [Index](index.md) — A position of a character or code unit in a string.
- [UTF16View](utf16view.md) — A view of a string’s contents as a collection of UTF-16 code units.
- [UTF8View](utf8view.md) — A view of a string’s contents as a collection of UTF-8 code units.
- [Iterator](iterator.md) — A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [Encoding](encoding.md)
