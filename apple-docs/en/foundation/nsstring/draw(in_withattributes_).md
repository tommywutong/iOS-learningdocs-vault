---
title: 'draw(in:withAttributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/draw(in:withattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/draw(in:withattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/draw%28in%3Awithattributes%3A%29.json'
content_hash: 'sha256:0aa604af5418c04e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# draw(in:withAttributes:)

<sub>Instance Method</sub>

Draws the attributed string inside the specified bounding rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func draw(in rect: CGRect, withAttributes attrs: [NSAttributedString.Key : Any]? = nil)
```

## Parameters

- `rect` — The bounding rectangle in which to draw the string. In AppKit, the origin of the bounding box is normally in the lower-left corner, but the origin is in the upper-left corner if the focused view is flipped.

- `attrs` — The text attributes with which to draw the string. These are the same attributes that can be applied to an `NSAttributedString` object, but in the case of `NSString` objects, the attributes apply to the entire string, rather than ranges within the string.

## Discussion

This method draws as much of the string as it can inside the specified rectangle, wrapping the string text as needed to make it fit. If the string is too long to fit inside the rectangle, the method renders as much as possible and clips the rest.

If newline characters are present in the string, those characters are honored and cause subsequent text to be placed on the next line underneath the starting point.

There must be either a focused view or an active graphics context when you call this method.

## See Also

### Sizing and Drawing Strings

- [- drawAtPoint:withAttributes:](<draw(at_withattributes_).md>) — Draws the receiver with the font and other display characteristics of the given attributes, at the specified point in the current graphics context.
- [- drawWithRect:options:attributes:context:](<draw(with_options_attributes_context_).md>) — Draws the attributed string in the specified bounding rectangle using the provided options.
- [- boundingRectWithSize:options:attributes:context:](<boundingrect(with_options_attributes_context_).md>) — Calculates and returns the bounding rect for the receiver drawn using the given options and display characteristics, within the specified rectangle in the current graphics context.
- [- sizeWithAttributes:](<size(withattributes_).md>) — Returns the bounding box size the receiver occupies when drawn with the given attributes.
- [- variantFittingPresentationWidth:](<variantfittingpresentationwidth(__).md>) — Returns a string variation suitable for the specified presentation width.
- [NSStringDrawingOptions](../../uikit/nsstringdrawingoptions.md) — Constants that specify the rendering options for drawing a string.
