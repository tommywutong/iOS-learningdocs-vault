---
title: 'fixParagraphStyleAttribute(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableattributedstring/fixparagraphstyleattribute(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/fixparagraphstyleattribute(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/fixparagraphstyleattribute%28in%3A%29.json'
content_hash: 'sha256:91f4cd31301f09ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# fixParagraphStyleAttribute(in:)

<sub>Instance Method</sub>

Fixes the paragraph style attributes in the specified range and assigns a paragraph style to all characters in the paragraph.

<sub>macOS</sub>

```swift
func fixParagraphStyleAttribute(in range: NSRange)
```

## Parameters

- `range` — The range of characters.

## Discussion

This method assigns the first paragraph style attribute value in each paragraph to all characters of the paragraph. This method extends the range as needed to cover the last paragraph partially contained. A paragraph is delimited by any of these characters, the longest possible sequence being preferred to any shorter:

- U+000D (`\r` or CR)
- U+000A (`\n` or LF)
- U+2029 (Unicode paragraph separator)  `\r\n`, in that order (also known as CRLF)

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## See Also

### Fixing Attributes After Changes

- [- fixAttributesInRange:](<fixattributes(in_).md>) — Cleans up font, paragraph style, and attachment attributes within the given range.
- [- fixAttachmentAttributeInRange:](<fixattachmentattribute(in_).md>) — Cleans up attachment attributes in the specified range and removes all attachment attributes assigned to characters except the designated attachment character.
- [- fixFontAttributeInRange:](<fixfontattribute(in_).md>) — Fixes the font attribute in the specified range and assigns default fonts where appropriate.
