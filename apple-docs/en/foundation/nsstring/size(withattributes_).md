---
title: 'size(withAttributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/size(withattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/size(withattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/size%28withattributes%3A%29.json'
content_hash: 'sha256:72df46987526b1b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# size(withAttributes:)

<sub>Instance Method</sub>

Returns the bounding box size the receiver occupies when drawn with the given attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func size(withAttributes attrs: [NSAttributedString.Key : Any]? = nil) -> CGSize
```

## Parameters

- `attrs` — A dictionary of text attributes to be applied to the string. These are the same attributes that can be applied to an `NSAttributedString` object, but in the case of `NSString` objects, the attributes apply to the entire string, rather than ranges within the string.

## Return Value

The bounding box size the receiver occupies when drawn with the specified attributes.

## Discussion

This method returns fractional sizes; to use a returned size to size views, you must raise its value to the nearest higher integer using the [ceil](../../kernel/1557272-ceil.md) function.

## See Also

### Sizing and Drawing Strings

- [- drawAtPoint:withAttributes:](<draw(at_withattributes_).md>) — Draws the receiver with the font and other display characteristics of the given attributes, at the specified point in the current graphics context.
- [- drawInRect:withAttributes:](<draw(in_withattributes_).md>) — Draws the attributed string inside the specified bounding rectangle.
- [- drawWithRect:options:attributes:context:](<draw(with_options_attributes_context_).md>) — Draws the attributed string in the specified bounding rectangle using the provided options.
- [- boundingRectWithSize:options:attributes:context:](<boundingrect(with_options_attributes_context_).md>) — Calculates and returns the bounding rect for the receiver drawn using the given options and display characteristics, within the specified rectangle in the current graphics context.
- [- variantFittingPresentationWidth:](<variantfittingpresentationwidth(__).md>) — Returns a string variation suitable for the specified presentation width.
- [NSStringDrawingOptions](../../uikit/nsstringdrawingoptions.md) — Constants that specify the rendering options for drawing a string.
