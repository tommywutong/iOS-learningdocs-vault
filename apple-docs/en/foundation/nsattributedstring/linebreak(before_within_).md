---
title: 'lineBreak(before:within:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/linebreak(before:within:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/linebreak(before:within:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/linebreak%28before%3Awithin%3A%29.json'
content_hash: 'sha256:e8030dd2d1676eb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# lineBreak(before:within:)

<sub>Instance Method</sub>

Returns the appropriate line break when the character at the index doesn’t fit on the same line as the character at the beginning of the range.

<sub>macOS</sub>

```swift
func lineBreak(before location: Int, within aRange: NSRange) -> Int
```

## Parameters

- `location` — The index in the attributed string.

- `aRange` — The range.

## Return Value

Returns the index of the closest character before `index` within `aRange`, that can be placed on a new line when laying out text. Returns `NSNotFound` if no line break is possible before `index`.

## Discussion

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if `index` or any part of `aRange` lies beyond the end of the receiver’s characters.

## See Also

### Calculating linguistic units

- [- doubleClickAtIndex:](<doubleclick(at_).md>) — Returns the range of characters that form a word (or other linguistic unit) surrounding the specified index, taking language characteristics into account.
- [- lineBreakByHyphenatingBeforeIndex:withinRange:](<linebreakbyhyphenating(before_within_).md>) — Returns the index of the closest character before the specified index, and within the specified range, that can fit on a new line by hyphenating.
- [- nextWordFromIndex:forward:](<nextword(from_forward_).md>) — Returns the index of the first character of the word after or before the specified index.
