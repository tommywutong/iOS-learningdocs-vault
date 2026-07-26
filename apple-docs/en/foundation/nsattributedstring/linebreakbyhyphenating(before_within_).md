---
title: 'lineBreakByHyphenating(before:within:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/linebreakbyhyphenating(before:within:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/linebreakbyhyphenating(before:within:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/linebreakbyhyphenating%28before%3Awithin%3A%29.json'
content_hash: 'sha256:b96988ddfd80cd0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# lineBreakByHyphenating(before:within:)

<sub>Instance Method</sub>

Returns the index of the closest character before the specified index, and within the specified range, that can fit on a new line by hyphenating.

<sub>macOS</sub>

```swift
func lineBreakByHyphenating(before location: Int, within aRange: NSRange) -> Int
```

## Parameters

- `location` — The location in the attributed string.

- `aRange` — The range.

## Return Value

Returns the index of the closest character before  `index` within `aRange`, that can be placed on a new line by hyphenating. Returns `NSNotFound` if no line break by hyphenation is possible before `index`.

## Discussion

In other words, during text layout, finds the appropriate line break by hyphenation (the character index at which the hyphen glyph should be inserted) when the character at `index` won’t fit on the same line as the character at the beginning of `aRange`.

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if `index` or any part of `aRange` lies beyond the end of the receiver’s characters.

## See Also

### Calculating linguistic units

- [- doubleClickAtIndex:](<doubleclick(at_).md>) — Returns the range of characters that form a word (or other linguistic unit) surrounding the specified index, taking language characteristics into account.
- [- lineBreakBeforeIndex:withinRange:](<linebreak(before_within_).md>) — Returns the appropriate line break when the character at the index doesn’t fit on the same line as the character at the beginning of the range.
- [- nextWordFromIndex:forward:](<nextword(from_forward_).md>) — Returns the index of the first character of the word after or before the specified index.
