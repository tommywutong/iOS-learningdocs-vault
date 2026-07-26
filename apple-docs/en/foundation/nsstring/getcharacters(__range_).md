---
title: 'getCharacters(_:range:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/getcharacters(_:range:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/getcharacters(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/getcharacters%28_%3Arange%3A%29.json'
content_hash: 'sha256:51b787fb516c6923'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# getCharacters(_:range:)

<sub>Instance Method</sub>

Copies characters from a given range in the receiver into a given buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getCharacters(_ buffer: UnsafeMutablePointer<unichar>, range: NSRange)
```

## Parameters

- `buffer` — Upon return, contains the characters from the receiver. `buffer` must be large enough to contain the characters in the range `aRange` (`aRange.length*sizeof(unichar)`).

- `range` — The range of characters to retrieve. The range must not exceed the bounds of the receiver. > [!important] Important > Raises an `NSRangeException` if any part of `aRange` lies beyond the bounds of the receiver.

## Discussion

This method does not add a `NULL` character.

The abstract implementation of this method uses [- characterAtIndex:](<character(at_).md>) repeatedly, correctly extracting the characters, though very inefficiently. Subclasses should override it to provide a fast implementation.

You should always use the [- rangeOfComposedCharacterSequenceAtIndex:](<rangeofcomposedcharactersequence(at_).md>) or [- rangeOfComposedCharacterSequencesForRange:](<rangeofcomposedcharactersequences(for_).md>) method to determine character boundaries, so that any surrogate pairs or character clusters are handled correctly.

## See Also

### Getting Characters and Bytes

- [- characterAtIndex:](<character(at_).md>) — Returns the character at a given UTF-16 code unit index.
- [- getBytes:maxLength:usedLength:encoding:options:range:remainingRange:](<getbytes(__maxlength_usedlength_encoding_options_range_remaining_).md>) — Gets a given range of characters as bytes in a specified encoding.
