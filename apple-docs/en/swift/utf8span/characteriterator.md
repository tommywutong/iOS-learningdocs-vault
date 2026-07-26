---
title: UTF8Span.CharacterIterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/characteriterator
source_url: 'https://developer.apple.com/documentation/swift/utf8span/characteriterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/characteriterator.json'
content_hash: 'sha256:26ed0ac4e712f9e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# UTF8Span.CharacterIterator

<sub>Structure</sub>

Iterate the `Character` contents of a `UTF8Span`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CharacterIterator
```

## Overview

```swift
func countCharacters(_ string: borrowing String) {
    var iterator = string.utf8Span.makeCharacterIterator()
    var count = 0
    while let character = iterator.next() {
        count += 1
        print("Character \(count): \(character)")
    }
    print("Total: \(count) characters")
}

let string = "لاهور"
countCharacters(string)
// Prints "Character 1: ل"
// Prints "Character 2: ا"
// Prints "Character 3: ه"
// Prints "Character 4: و"
// Prints "Character 5: ر"
// Prints "Total: 5 characters"
```

## Topics

### Initializers

- [init(_:)](<characteriterator/init(__).md>)

### Instance Properties

- [codeUnits](characteriterator/codeunits.md)
- [currentCodeUnitOffset](characteriterator/currentcodeunitoffset.md) — The byte offset of the start of the next `Character`. This is always scalar-aligned. It is always `Character`-aligned relative to the last call to `reset` (or the start of the span if not called).

### Instance Methods

- [next()](<characteriterator/next().md>) — Return the `Character` starting at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the end of the `Character`, which is also the start of the next `Character`.
- [prefix()](<characteriterator/prefix().md>) — Returns the UTF8Span containing all the content up to the iterator’s current position.
- [previous()](<characteriterator/previous().md>) — Return the `Character` ending at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the start of the returned `Character`, which is also the end of the previous `Character`.
- [reset(roundingBackwardsFrom:)](<characteriterator/reset(roundingbackwardsfrom_).md>) — Reset to the nearest character-aligned position `<= i`.
- [reset(roundingForwardsFrom:)](<characteriterator/reset(roundingforwardsfrom_).md>) — Reset to the nearest character-aligned position `>= i`.
- [reset(toUnchecked:)](<characteriterator/reset(tounchecked_).md>) — Reset this iterator to `codeUnitOffset`, skipping _all_ safety checks.
- [skipBack()](<characteriterator/skipback().md>) — Move `currentCodeUnitOffset` to the start of the previous `Character`, without constructing it.
- [skipBack(by:)](<characteriterator/skipback(by_).md>) — Move `currentCodeUnitOffset` to the start of the previous `n` `Character`s, without constructing them.
- [skipForward()](<characteriterator/skipforward().md>) — Advance `currentCodeUnitOffset` to the end of the current `Character`, without constructing it.
- [skipForward(by:)](<characteriterator/skipforward(by_).md>) — Advance `currentCodeUnitOffset` to the end of `n` `Characters`, without constructing them.
- [suffix()](<characteriterator/suffix().md>) — Returns the UTF8Span containing all the content after the iterator’s current position.
