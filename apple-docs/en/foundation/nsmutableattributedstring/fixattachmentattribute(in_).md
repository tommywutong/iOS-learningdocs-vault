---
title: 'fixAttachmentAttribute(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableattributedstring/fixattachmentattribute(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/fixattachmentattribute(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/fixattachmentattribute%28in%3A%29.json'
content_hash: 'sha256:ebbd90f2f6618a14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# fixAttachmentAttribute(in:)

<sub>Instance Method</sub>

Cleans up attachment attributes in the specified range and removes all attachment attributes assigned to characters except the designated attachment character.

<sub>macOS</sub>

```swift
func fixAttachmentAttribute(in range: NSRange)
```

## Parameters

- `range` — The range of characters.

## Discussion

The method preserves the attachment attribute on the [character](../../appkit/nstextattachment/character.md) special character. The method raises a [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the string’s characters.

## See Also

### Fixing Attributes After Changes

- [- fixAttributesInRange:](<fixattributes(in_).md>) — Cleans up font, paragraph style, and attachment attributes within the given range.
- [- fixFontAttributeInRange:](<fixfontattribute(in_).md>) — Fixes the font attribute in the specified range and assigns default fonts where appropriate.
- [- fixParagraphStyleAttributeInRange:](<fixparagraphstyleattribute(in_).md>) — Fixes the paragraph style attributes in the specified range and assigns a paragraph style to all characters in the paragraph.
