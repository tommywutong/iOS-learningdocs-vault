---
title: CGColorEqualToColor
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorequaltocolor
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorequaltocolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorequaltocolor.json'
content_hash: 'sha256:8d2e8107337d9cc3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorEqualToColor

<sub>Function</sub>

Indicates whether two colors are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern bool CGColorEqualToColor(CGColorRef color1, CGColorRef color2);
```

## Parameters

- `color1` — The first color to compare.

- `color2` — The second color to compare.

## Return Value

A Boolean value that, if [true](../swift/true.md), indicates that the specified colors are equal. If the colors are not equal, the value is [false](../swift/false.md).

## Discussion

Two colors are equal if they share the same color space and numerically equal color components.

## See Also

### Examining a Color

- [CGColorGetAlpha](cgcolor/alpha.md) — Returns the value of the alpha component associated with a color.
- [CGColorGetColorSpace](cgcolor/colorspace.md) — Returns the color space associated with a color.
- [CGColorGetNumberOfComponents](cgcolor/numberofcomponents.md) — Returns the number of color components (including alpha) associated with a color.
- [CGColorGetPattern](cgcolor/pattern.md) — Returns the pattern associated with a color in a pattern color space.
- [CGColorGetComponents](cgcolorgetcomponents.md) — Returns the values of the color components (including alpha) associated with a color.
