---
title: Substring
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/substring
source_url: 'https://developer.apple.com/documentation/swift/substring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring.json'
content_hash: 'sha256:aa12017d9d184470'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Substring

<sub>Structure</sub>

A slice of a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Substring
```

## Overview

When you create a slice of a string, a `Substring` instance is the result. Operating on substrings is fast and efficient because a substring shares its storage with the original string. The `Substring` type presents the same interface as `String`, so you can avoid or defer any copying of the string’s contents.

The following example creates a `greeting` string, and then finds the substring of the first sentence:

```swift
let greeting = "Hi there! It's nice to meet you! 👋"
let endOfSentence = greeting.firstIndex(of: "!")!
let firstSentence = greeting[...endOfSentence]
// firstSentence == "Hi there!"
```

You can perform many string operations on a substring. Here, we find the length of the first sentence and create an uppercase version.

```swift
print("'\(firstSentence)' is \(firstSentence.count) characters long.")
// Prints "'Hi there!' is 9 characters long."

let shoutingSentence = firstSentence.uppercased()
// shoutingSentence == "HI THERE!"
```

## Converting a Substring to a String

This example defines a `rawData` string with some unstructured data, and then uses the string’s `prefix(while:)` method to create a substring of the numeric prefix:

```swift
let rawInput = "126 a.b 22219 zzzzzz"
let numericPrefix = rawInput.prefix(while: { "0"..."9" ~= $0 })
// numericPrefix is the substring "126"
```

When you need to store a substring or pass it to a function that requires a `String` instance, you can convert it to a `String` by using the `String(_:)` initializer. Calling this initializer copies the contents of the substring to a new string.

```swift
func parseAndAddOne(_ s: String) -> Int {
    return Int(s, radix: 10)! + 1
}
_ = parseAndAddOne(numericPrefix)
// error: cannot convert value...
let incrementedPrefix = parseAndAddOne(String(numericPrefix))
// incrementedPrefix == 127
```

Alternatively, you can convert the function that takes a `String` to one that is generic over the `StringProtocol` protocol. The following code declares a generic version of the `parseAndAddOne(_:)` function:

```swift
func genericParseAndAddOne<S: StringProtocol>(_ s: S) -> Int {
    return Int(s, radix: 10)! + 1
}
let genericallyIncremented = genericParseAndAddOne(numericPrefix)
// genericallyIncremented == 127
```

You can call this generic function with an instance of either `String` or `Substring`.

> [!important] Important
> Don’t store substrings longer than you need them to perform a specific operation. A substring holds a reference to the entire storage of the string it comes from, not just to the portion it presents, even when there is no other reference to the original string. Storing substrings may, therefore, prolong the lifetime of string data that is no longer otherwise accessible, which can appear to be memory leakage.

## Relationships

- **Conforms To**: [Attachable](../testing/attachable.md), [BidirectionalCollection](bidirectionalcollection.md), [Collection](collection.md), [Comparable](comparable.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [CustomTestStringConvertible](../testing/customteststringconvertible.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md), [ExpressibleByStringLiteral](expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md), [Hashable](hashable.md), [LosslessStringConvertible](losslessstringconvertible.md), [RangeReplaceableCollection](rangereplaceablecollection.md), [RegexComponent](regexcomponent.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Sequence](sequence.md), [StringProtocol](stringprotocol.md), [TextOutputStream](textoutputstream.md), [TextOutputStreamable](textoutputstreamable.md)

## Topics

### Operators

- [~=(_:_:)](<substring/~=(____).md>)

### Initializers

- [init()](<substring/init().md>) — Creates an empty substring.
- [init(_:)](<substring/init(__)-4njms.md>) — Creates a Substring having the given content.
- [init(_:)](<substring/init(__)-61zpv.md>) — Creates a Substring having the given content.
- [init(_:)](<substring/init(__)-7k0au.md>) — Creates a Substring having the given content.

### Instance Properties

- [base](substring/base.md) — Returns the underlying string from which this substring was derived.
- [characters](substring/characters.md) — A view of the string’s contents as a collection of characters.
- [customPlaygroundQuickLook](substring/customplaygroundquicklook.md) — A custom playground Quick Look for this instance.
- [isContiguousUTF8](substring/iscontiguousutf8.md) — Returns whether this string’s storage contains validly-encoded UTF-8 contents in contiguous memory.
- [utf8Span](substring/utf8span.md) — A UTF-8 span over the code units that make up this substring.

### Instance Methods

- [filter(_:)](<substring/filter(__).md>)
- [isTriviallyIdentical(to:)](<substring/istriviallyidentical(to_).md>) — Returns a boolean value indicating whether this substring is identical to `other`. _(beta)_
- [makeContiguousUTF8()](<substring/makecontiguousutf8().md>) — If this string is not contiguous, make it so. If this mutates the substring, it will invalidate any pre-existing indices.
- [replaceSubrange(_:with:)](<substring/replacesubrange(__with_)-mfwu.md>)
- [withMutableCharacters(_:)](<substring/withmutablecharacters(__).md>) — Applies the given closure to a mutable view of the string’s characters.
- [withUTF8(_:)](<substring/withutf8(__).md>) — Runs `body` over the content of this substring in contiguous memory. If this substring is not contiguous, this will first make it contiguous, which will also speed up subsequent access. If this mutates the substring, it will invalidate any pre-existing indices.

### Type Aliases

- [CharacterView](substring/characterview.md) — A view of a string’s contents as a collection of characters.
- [Output](substring/output.md)

### Default Implementations

- [Attachable Implementations](substring/attachable-implementations.md)
- [BidirectionalCollection Implementations](substring/bidirectionalcollection-implementations.md)
- [Collection Implementations](substring/collection-implementations.md)
- [Comparable Implementations](substring/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](substring/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](substring/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](substring/customstringconvertible-implementations.md)
- [Equatable Implementations](substring/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](substring/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringInterpolation Implementations](substring/expressiblebystringinterpolation-implementations.md)
- [ExpressibleByStringLiteral Implementations](substring/expressiblebystringliteral-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](substring/expressiblebyunicodescalarliteral-implementations.md)
- [Hashable Implementations](substring/hashable-implementations.md)
- [LosslessStringConvertible Implementations](substring/losslessstringconvertible-implementations.md)
- [RangeReplaceableCollection Implementations](substring/rangereplaceablecollection-implementations.md)
- [Sequence Implementations](substring/sequence-implementations.md)
- [StringProtocol Implementations](substring/stringprotocol-implementations.md)
- [TextOutputStream Implementations](substring/textoutputstream-implementations.md)
- [TextOutputStreamable Implementations](substring/textoutputstreamable-implementations.md)

## See Also

### Related String Types

- [StringProtocol](stringprotocol.md) — A type that can represent a string as a collection of characters.
- [Index](string/index.md) — A position of a character or code unit in a string.
- [UnicodeScalarView](string/unicodescalarview.md) — A view of a string’s contents as a collection of Unicode scalar values.
- [UTF16View](string/utf16view.md) — A view of a string’s contents as a collection of UTF-16 code units.
- [UTF8View](string/utf8view.md) — A view of a string’s contents as a collection of UTF-8 code units.
- [Iterator](string/iterator.md) — A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [Encoding](string/encoding.md)
