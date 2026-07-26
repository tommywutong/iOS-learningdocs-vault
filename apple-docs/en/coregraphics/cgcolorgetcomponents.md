---
title: CGColorGetComponents
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorgetcomponents
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorgetcomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorgetcomponents.json'
content_hash: 'sha256:b05caefcef07651f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorGetComponents

<sub>Function</sub>

Returns the values of the color components (including alpha) associated with a color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern const CGFloat *CGColorGetComponents(CGColorRef color);
```

## Parameters

- `color` — A color.

## Return Value

An array of intensity values for the color components (including alpha) associated with the specified color. The size of the array is one more than the number of components of the color space for the color.

## See Also

### Examining a Color

- [CGColorEqualToColor](cgcolorequaltocolor.md) — Indicates whether two colors are equal.
- [CGColorGetAlpha](cgcolor/alpha.md) — Returns the value of the alpha component associated with a color.
- [CGColorGetColorSpace](cgcolor/colorspace.md) — Returns the color space associated with a color.
- [CGColorGetNumberOfComponents](cgcolor/numberofcomponents.md) — Returns the number of color components (including alpha) associated with a color.
- [CGColorGetPattern](cgcolor/pattern.md) — Returns the pattern associated with a color in a pattern color space.
