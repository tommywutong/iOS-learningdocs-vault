---
title: 'fixAttributes(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableattributedstring/fixattributes(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/fixattributes(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/fixattributes%28in%3A%29.json'
content_hash: 'sha256:6f144bd9e3f64e8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# fixAttributes(in:)

<sub>Instance Method</sub>

Cleans up font, paragraph style, and attachment attributes within the given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fixAttributes(in range: NSRange)
```

## Parameters

- `range` — The character range within which to fix attributes. Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## Discussion

Removes attachment attributes assigned to characters other than [character](../../appkit/nstextattachment/character.md), assigns default fonts to characters with illegal fonts for their scripts and otherwise corrects font attribute assignments, and assigns the first paragraph style attribute value in each paragraph to all characters of the paragraph.

This method extends the range as needed to cover the last paragraph partially contained.

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of aRange lies beyond the end of the receiver’s characters.

`NSTextStorage` subclasses that return [true](../../swift/true.md) from the [fixesAttributesLazily](../../appkit/nstextstorage/fixesattributeslazily.md) method should avoid directly calling [- fixAttributesInRange:](<fixattributes(in_).md>) or else bracket such calls with [- beginEditing](<beginediting().md>) and [- endEditing](<endediting().md>) messages.

## See Also

### Fixing Attributes After Changes

- [- fixAttachmentAttributeInRange:](<fixattachmentattribute(in_).md>) — Cleans up attachment attributes in the specified range and removes all attachment attributes assigned to characters except the designated attachment character.
- [- fixFontAttributeInRange:](<fixfontattribute(in_).md>) — Fixes the font attribute in the specified range and assigns default fonts where appropriate.
- [- fixParagraphStyleAttributeInRange:](<fixparagraphstyleattribute(in_).md>) — Fixes the paragraph style attributes in the specified range and assigns a paragraph style to all characters in the paragraph.
