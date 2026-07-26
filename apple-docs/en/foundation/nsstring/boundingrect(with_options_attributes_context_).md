---
title: 'boundingRect(with:options:attributes:context:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/boundingrect(with:options:attributes:context:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/boundingrect(with:options:attributes:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/boundingrect%28with%3Aoptions%3Aattributes%3Acontext%3A%29.json'
content_hash: 'sha256:b90a8ca9a9085249'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# boundingRect(with:options:attributes:context:)

<sub>Instance Method</sub>

Calculates and returns the bounding rect for the receiver drawn using the given options and display characteristics, within the specified rectangle in the current graphics context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func boundingRect(with size: CGSize, options: NSStringDrawingOptions = [], attributes: [NSAttributedString.Key : Any]? = nil, context: NSStringDrawingContext?) -> CGRect
```

<sub>macOS</sub>

```swift
func boundingRect(with size: CGSize, options: NSString.DrawingOptions = [], attributes: [NSAttributedString.Key : Any]? = nil, context: NSStringDrawingContext?) -> CGRect
```

## Parameters

- `size` — The size of the rectangle to draw in.

- `options` — String drawing options.

- `attributes` — A dictionary of text attributes to be applied to the string. These are the same attributes that can be applied to an `NSAttributedString` object, but in the case of `NSString` objects, the attributes apply to the entire string, rather than ranges within the string.

- `context` — The string drawing context to use for the receiver, specifying minimum scale factor and tracking adjustments.

## Return Value

The bounding rect for the receiver drawn using the given options and display characteristics. The rect origin returned from this method is the first glyph origin.

## Discussion

To correctly draw and size multi-line text, pass [usesLineFragmentOrigin](../../uikit/nsstringdrawingoptions/useslinefragmentorigin.md) in the options parameter.

This method returns fractional sizes (in the `size` component of the returned [CGRect](../../corefoundation/cgrect.md)); to use a returned size to size views, you must raise its value to the nearest higher integer using the [ceil](../../kernel/1557272-ceil.md) function.

This method returns the actual bounds of the glyphs in the string. Some of the glyphs (spaces, for example) are allowed to overlap the layout constraints specified by the size passed in, so in some cases the width value of the size component of the returned [CGRect](../../corefoundation/cgrect.md) can exceed the width value of the `size` parameter.

## See Also

### Sizing and Drawing Strings

- [- drawAtPoint:withAttributes:](<draw(at_withattributes_).md>) — Draws the receiver with the font and other display characteristics of the given attributes, at the specified point in the current graphics context.
- [- drawInRect:withAttributes:](<draw(in_withattributes_).md>) — Draws the attributed string inside the specified bounding rectangle.
- [- drawWithRect:options:attributes:context:](<draw(with_options_attributes_context_).md>) — Draws the attributed string in the specified bounding rectangle using the provided options.
- [- sizeWithAttributes:](<size(withattributes_).md>) — Returns the bounding box size the receiver occupies when drawn with the given attributes.
- [- variantFittingPresentationWidth:](<variantfittingpresentationwidth(__).md>) — Returns a string variation suitable for the specified presentation width.
- [NSStringDrawingOptions](../../uikit/nsstringdrawingoptions.md) — Constants that specify the rendering options for drawing a string.
