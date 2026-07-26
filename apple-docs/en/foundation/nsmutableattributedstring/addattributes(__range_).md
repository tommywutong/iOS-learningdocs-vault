---
title: 'addAttributes(_:range:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableattributedstring/addattributes(_:range:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/addattributes(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/addattributes%28_%3Arange%3A%29.json'
content_hash: 'sha256:be9df73247c70634'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# addAttributes(_:range:)

<sub>Instance Method</sub>

Adds the given collection of attributes to the characters in the specified range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addAttributes(_ attrs: [NSAttributedString.Key : Any] = [:], range: NSRange)
```

## Parameters

- `attrs` — A dictionary containing the attributes to add. Attribute keys can be supplied by another framework or can be custom ones you define. For information about the system-supplied attribute keys, see the Constants section in [NSAttributedString](../nsattributedstring.md).

- `range` — The range of characters to which the specified attributes apply.

## Discussion

You may assign any name/value pair you wish to a range of characters. Raises an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md) if `attrs` is `nil` and an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## See Also

### Changing Attributes

- [- setAttributes:range:](<setattributes(__range_).md>) — Sets the attributes for the characters in the specified range to the specified attributes.
- [- addAttribute:value:range:](<addattribute(__value_range_).md>) — Adds an attribute with the given name and value to the characters in the specified range.
- [- removeAttribute:range:](<removeattribute(__range_).md>) — Removes the named attribute from the characters in the specified range.
- [- applyFontTraits:range:](<applyfonttraits(__range_).md>) — Applies the specified font-related attributes to characters in the string.
- [- setAlignment:range:](<setalignment(__range_).md>) — Sets the alignment characteristic of the paragraph style attribute for the specified range of text.
- [- setBaseWritingDirection:range:](<setbasewritingdirection(__range_).md>) — Sets the base writing direction for the characters to the specified direction.
- [- subscriptRange:](<subscriptrange(__).md>) — Decrements the value of the superscript attribute for characters in the specified range by one.
- [- superscriptRange:](<superscriptrange(__).md>) — Increments the value of the superscript attribute for characters in the specified range by one.
- [- unscriptRange:](<unscriptrange(__).md>) — Removes the superscript attribute from the characters in the specified range.
