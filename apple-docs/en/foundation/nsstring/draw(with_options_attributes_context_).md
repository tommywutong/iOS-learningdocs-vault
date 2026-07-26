---
title: 'draw(with:options:attributes:context:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/draw(with:options:attributes:context:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/draw(with:options:attributes:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/draw%28with%3Aoptions%3Aattributes%3Acontext%3A%29.json'
content_hash: 'sha256:2b35c58c32f226f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# draw(with:options:attributes:context:)

<sub>Instance Method</sub>

Draws the attributed string in the specified bounding rectangle using the provided options.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func draw(with rect: CGRect, options: NSStringDrawingOptions = [], attributes: [NSAttributedString.Key : Any]? = nil, context: NSStringDrawingContext?)
```

<sub>macOS</sub>

```swift
func draw(with rect: CGRect, options: NSString.DrawingOptions = [], attributes: [NSAttributedString.Key : Any]? = nil, context: NSStringDrawingContext?)
```

## Parameters

- `rect` — The bounding rectangle in which to draw the string.

- `options` — Additional drawing options to apply to the string during rendering. For a list of possible values, see [NSStringDrawingOptions](../../uikit/nsstringdrawingoptions.md).

- `attributes` — The text attributes with which to draw the string. These are the same attributes that can be applied to an `NSAttributedString` object, but in the case of `NSString` objects, the attributes apply to the entire string, rather than ranges within the string.

- `context` — A context object with information about how to adjust the font tracking and scaling information. On return, the specified object contains information about the actual values used to render the string. This parameter may be `nil`.

## Discussion

This method draws as much of the string as it can inside the specified rectangle, wrapping the string text as needed to make it fit. If the string is too big to fit completely inside the rectangle, the method scales the font or adjusts the letter spacing to make the string fit within the given bounds.

If newline characters are present in the string, those characters are honored and cause subsequent text to be placed on the next line underneath the starting point. To correctly draw and size multi-line text, pass [usesLineFragmentOrigin](../../uikit/nsstringdrawingoptions/useslinefragmentorigin.md) in the options parameter.

### Special Considerations

This method uses the baseline origin by default.

If [usesLineFragmentOrigin](../../uikit/nsstringdrawingoptions/useslinefragmentorigin.md) is not specified, the rectangle’s height will be ignored and the operation considered to be single-line rendering.

## See Also

### Sizing and Drawing Strings

- [- drawAtPoint:withAttributes:](<draw(at_withattributes_).md>) — Draws the receiver with the font and other display characteristics of the given attributes, at the specified point in the current graphics context.
- [- drawInRect:withAttributes:](<draw(in_withattributes_).md>) — Draws the attributed string inside the specified bounding rectangle.
- [- boundingRectWithSize:options:attributes:context:](<boundingrect(with_options_attributes_context_).md>) — Calculates and returns the bounding rect for the receiver drawn using the given options and display characteristics, within the specified rectangle in the current graphics context.
- [- sizeWithAttributes:](<size(withattributes_).md>) — Returns the bounding box size the receiver occupies when drawn with the given attributes.
- [- variantFittingPresentationWidth:](<variantfittingpresentationwidth(__).md>) — Returns a string variation suitable for the specified presentation width.
- [NSStringDrawingOptions](../../uikit/nsstringdrawingoptions.md) — Constants that specify the rendering options for drawing a string.
