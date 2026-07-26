---
title: 'applyFontTraits(_:range:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableattributedstring/applyfonttraits(_:range:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/applyfonttraits(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/applyfonttraits%28_%3Arange%3A%29.json'
content_hash: 'sha256:b444be10f10fbc59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# applyFontTraits(_:range:)

<sub>Instance Method</sub>

Applies the specified font-related attributes to characters in the string.

<sub>macOS</sub>

```swift
func applyFontTraits(_ traitMask: NSFontTraitMask, range: NSRange)
```

## Parameters

- `traitMask` — The font attributes to apply. For information about the font traits you can apply, see [NSFontManager](../../appkit/nsfontmanager.md).

- `range` — The range of characters.

## Discussion

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## See Also

### Changing Attributes

- [- setAttributes:range:](<setattributes(__range_).md>) — Sets the attributes for the characters in the specified range to the specified attributes.
- [- addAttribute:value:range:](<addattribute(__value_range_).md>) — Adds an attribute with the given name and value to the characters in the specified range.
- [- addAttributes:range:](<addattributes(__range_).md>) — Adds the given collection of attributes to the characters in the specified range.
- [- removeAttribute:range:](<removeattribute(__range_).md>) — Removes the named attribute from the characters in the specified range.
- [- setAlignment:range:](<setalignment(__range_).md>) — Sets the alignment characteristic of the paragraph style attribute for the specified range of text.
- [- setBaseWritingDirection:range:](<setbasewritingdirection(__range_).md>) — Sets the base writing direction for the characters to the specified direction.
- [- subscriptRange:](<subscriptrange(__).md>) — Decrements the value of the superscript attribute for characters in the specified range by one.
- [- superscriptRange:](<superscriptrange(__).md>) — Increments the value of the superscript attribute for characters in the specified range by one.
- [- unscriptRange:](<unscriptrange(__).md>) — Removes the superscript attribute from the characters in the specified range.
