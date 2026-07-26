---
title: 'setAttributes(_:range:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableattributedstring/setattributes(_:range:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/setattributes(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/setattributes%28_%3Arange%3A%29.json'
content_hash: 'sha256:0c8c2c8aeddc737a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# setAttributes(_:range:)

<sub>Instance Method</sub>

Sets the attributes for the characters in the specified range to the specified attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setAttributes(_ attrs: [NSAttributedString.Key : Any]?, range: NSRange)
```

## Parameters

- `attrs` — A dictionary containing the attributes to set. Attribute keys can be supplied by another framework or can be custom ones you define. For information about the system-supplied attribute keys, see the Constants section in [NSAttributedString](../nsattributedstring.md).

- `range` — The range of characters whose attributes are set.

## Discussion

These new attributes replace any attributes previously associated with the characters in `range`. Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

To set attributes for a zero-length `NSMutableAttributedString` displayed in a text view, use the `NSTextView` method [typingAttributes](../../appkit/nstextview/typingattributes.md).

## See Also

### Changing Attributes

- [- addAttribute:value:range:](<addattribute(__value_range_).md>) — Adds an attribute with the given name and value to the characters in the specified range.
- [- addAttributes:range:](<addattributes(__range_).md>) — Adds the given collection of attributes to the characters in the specified range.
- [- removeAttribute:range:](<removeattribute(__range_).md>) — Removes the named attribute from the characters in the specified range.
- [- applyFontTraits:range:](<applyfonttraits(__range_).md>) — Applies the specified font-related attributes to characters in the string.
- [- setAlignment:range:](<setalignment(__range_).md>) — Sets the alignment characteristic of the paragraph style attribute for the specified range of text.
- [- setBaseWritingDirection:range:](<setbasewritingdirection(__range_).md>) — Sets the base writing direction for the characters to the specified direction.
- [- subscriptRange:](<subscriptrange(__).md>) — Decrements the value of the superscript attribute for characters in the specified range by one.
- [- superscriptRange:](<superscriptrange(__).md>) — Increments the value of the superscript attribute for characters in the specified range by one.
- [- unscriptRange:](<unscriptrange(__).md>) — Removes the superscript attribute from the characters in the specified range.
