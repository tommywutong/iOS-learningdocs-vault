---
title: UTF8Span.UnicodeScalarIterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/unicodescalariterator
source_url: 'https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/unicodescalariterator.json'
content_hash: 'sha256:c98511080d29f093'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# UTF8Span.UnicodeScalarIterator

<sub>Structure</sub>

Iterate the `Unicode.Scalar`s contents of a `UTF8Span`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UnicodeScalarIterator
```

## Overview

```swift
func printScalarValues(_ string: borrowing String) {
    var iterator = string.utf8Span.makeUnicodeScalarIterator()
    while let scalar = iterator.next() {
        print(scalar.escaped(asASCII: true))
    }
}

let string = "A🎉"
printScalarValues(string)
// Prints "A"
// Prints "\u{0001F389}"
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../bitwisecopyable.md), [Copyable](../copyable.md)

## Topics

### Initializers

- [init(_:)](<unicodescalariterator/init(__).md>)

### Instance Properties

- [codeUnits](unicodescalariterator/codeunits.md)
- [currentCodeUnitOffset](unicodescalariterator/currentcodeunitoffset.md) — The byte offset of the start of the next scalar. This is always scalar-aligned.

### Instance Methods

- [next()](<unicodescalariterator/next().md>) — Decode and return the scalar starting at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the end of the returned scalar, which is also the start of the next scalar.
- [prefix()](<unicodescalariterator/prefix().md>) — Returns the UTF8Span containing all the content up to the iterator’s current position.
- [previous()](<unicodescalariterator/previous().md>) — Decode and return the scalar ending at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the start of the returned scalar, which is also the end of the previous scalar.
- [reset(roundingBackwardsFrom:)](<unicodescalariterator/reset(roundingbackwardsfrom_).md>) — Reset to the nearest scalar-aligned code unit offset `<= i`.
- [reset(roundingForwardsFrom:)](<unicodescalariterator/reset(roundingforwardsfrom_).md>) — Reset to the nearest scalar-aligned code unit offset `>= i`.
- [reset(toUnchecked:)](<unicodescalariterator/reset(tounchecked_).md>) — Reset this iterator to `codeUnitOffset`, skipping _all_ safety checks (including bounds checks).
- [skipBack()](<unicodescalariterator/skipback().md>) — Move `currentCodeUnitOffset` to the start of the previous scalar, without decoding it.
- [skipBack(by:)](<unicodescalariterator/skipback(by_).md>) — Move `currentCodeUnitOffset` to the start of the previous `n` scalars, without decoding them.
- [skipForward()](<unicodescalariterator/skipforward().md>) — Advance `currentCodeUnitOffset` to the end of the current scalar, without decoding it.
- [skipForward(by:)](<unicodescalariterator/skipforward(by_).md>) — Advance `currentCodeUnitOffset` to the end of `n` scalars, without decoding them.
- [suffix()](<unicodescalariterator/suffix().md>) — Returns the UTF8Span containing all the content after the iterator’s current position.
