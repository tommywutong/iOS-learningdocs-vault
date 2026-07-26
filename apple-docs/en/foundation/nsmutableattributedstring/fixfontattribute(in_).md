---
title: 'fixFontAttribute(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableattributedstring/fixfontattribute(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/fixfontattribute(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/fixfontattribute%28in%3A%29.json'
content_hash: 'sha256:924b3c927b99cde0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# fixFontAttribute(in:)

<sub>Instance Method</sub>

Fixes the font attribute in the specified range and assigns default fonts where appropriate.

<sub>macOS</sub>

```swift
func fixFontAttribute(in range: NSRange)
```

## Parameters

- `range` — The range of characters.

## Discussion

This method assigns default fonts to characters with illegal fonts for their scripts and corrects other font attribute assignments. For example, Kanji characters assigned a Latin font are reassigned an appropriate Kanji font. Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## See Also

### Fixing Attributes After Changes

- [- fixAttributesInRange:](<fixattributes(in_).md>) — Cleans up font, paragraph style, and attachment attributes within the given range.
- [- fixAttachmentAttributeInRange:](<fixattachmentattribute(in_).md>) — Cleans up attachment attributes in the specified range and removes all attachment attributes assigned to characters except the designated attachment character.
- [- fixParagraphStyleAttributeInRange:](<fixparagraphstyleattribute(in_).md>) — Fixes the paragraph style attributes in the specified range and assigns a paragraph style to all characters in the paragraph.
