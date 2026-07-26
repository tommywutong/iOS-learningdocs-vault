---
title: 'character(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/character(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/character(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/character%28at%3A%29.json'
content_hash: 'sha256:72922794f935812d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# character(at:)

<sub>Instance Method</sub>

Returns the character at a given UTF-16 code unit index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func character(at index: Int) -> unichar
```

## Parameters

- `index` — The index of the character to retrieve. > [!important] Important > Raises an `NSRangeException` if `index` lies beyond the end of the receiver.

## Return Value

The character at the array position given by `index`.

## Discussion

You should always use the [- rangeOfComposedCharacterSequenceAtIndex:](<rangeofcomposedcharactersequence(at_).md>) or [- rangeOfComposedCharacterSequencesForRange:](<rangeofcomposedcharactersequences(for_).md>) method to determine character boundaries, so that any surrogate pairs or character clusters are handled correctly.

## See Also

### Getting Characters and Bytes

- [- getCharacters:range:](<getcharacters(__range_).md>) — Copies characters from a given range in the receiver into a given buffer.
- [- getBytes:maxLength:usedLength:encoding:options:range:remainingRange:](<getbytes(__maxlength_usedlength_encoding_options_range_remaining_).md>) — Gets a given range of characters as bytes in a specified encoding.
