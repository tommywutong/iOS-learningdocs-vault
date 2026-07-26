---
title: 'doubleClick(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/doubleclick(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/doubleclick(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/doubleclick%28at%3A%29.json'
content_hash: 'sha256:b9818dc64d4b96dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# doubleClick(at:)

<sub>Instance Method</sub>

Returns the range of characters that form a word (or other linguistic unit) surrounding the specified index, taking language characteristics into account.

<sub>macOS</sub>

```swift
func doubleClick(at location: Int) -> NSRange
```

## Parameters

- `location` — The index in the attributed string.

## Return Value

Returns the range of characters that form a word (or other linguistic unit) surrounding the given index, taking language characteristics into account.

## Discussion

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if `index` lies beyond the end of the receiver’s characters.

## See Also

### Calculating linguistic units

- [- lineBreakBeforeIndex:withinRange:](<linebreak(before_within_).md>) — Returns the appropriate line break when the character at the index doesn’t fit on the same line as the character at the beginning of the range.
- [- lineBreakByHyphenatingBeforeIndex:withinRange:](<linebreakbyhyphenating(before_within_).md>) — Returns the index of the closest character before the specified index, and within the specified range, that can fit on a new line by hyphenating.
- [- nextWordFromIndex:forward:](<nextword(from_forward_).md>) — Returns the index of the first character of the word after or before the specified index.
