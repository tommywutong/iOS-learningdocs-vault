---
title: 'nextWord(from:forward:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/nextword(from:forward:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/nextword(from:forward:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/nextword%28from%3Aforward%3A%29.json'
content_hash: 'sha256:9e935cc7fd23722e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# nextWord(from:forward:)

<sub>Instance Method</sub>

Returns the index of the first character of the word after or before the specified index.

<sub>macOS</sub>

```swift
func nextWord(from location: Int, forward isForward: Bool) -> Int
```

## Parameters

- `location` — The index in the attribute string.

- `isForward` — [true](../../swift/true.md) if the search should be forward, otherwise [false](../../swift/false.md).

## Return Value

[true](../../swift/true.md) if this is the first character after `index` that begins a word; if `flag` is [false](../../swift/false.md), it’s the first character before `index` that begins a word, whether `index` is located within a word or not.

## Discussion

If `index` lies at either end of the string and the search direction would progress past that end, it’s returned unchanged.

This method is intended for moving the insertion point during editing, not for linguistic analysis or parsing of text.

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if `index` lies beyond the end of the receiver’s characters.

## See Also

### Calculating linguistic units

- [- doubleClickAtIndex:](<doubleclick(at_).md>) — Returns the range of characters that form a word (or other linguistic unit) surrounding the specified index, taking language characteristics into account.
- [- lineBreakBeforeIndex:withinRange:](<linebreak(before_within_).md>) — Returns the appropriate line break when the character at the index doesn’t fit on the same line as the character at the beginning of the range.
- [- lineBreakByHyphenatingBeforeIndex:withinRange:](<linebreakbyhyphenating(before_within_).md>) — Returns the index of the closest character before the specified index, and within the specified range, that can fit on a new line by hyphenating.
