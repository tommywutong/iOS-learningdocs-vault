---
title: components
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolor/components
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolor/components'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolor/components.json'
content_hash: 'sha256:64a190cff021beb0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColor](../cgcolor.md)

# components

<sub>Instance Property</sub>

Returns the values of the color components (including alpha) associated with a color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var components: [CGFloat]? { get }
```

## Discussion

An array of intensity values for the color components (including alpha) associated with the specified color. The size of the array is equal to the color’s [CGColorGetNumberOfComponents](numberofcomponents.md) value.

## See Also

### Examining a Color

- [CGColorGetAlpha](alpha.md) — Returns the value of the alpha component associated with a color.
- [CGColorGetColorSpace](colorspace.md) — Returns the color space associated with a color.
- [CGColorGetNumberOfComponents](numberofcomponents.md) — Returns the number of color components (including alpha) associated with a color.
- [CGColorGetPattern](pattern.md) — Returns the pattern associated with a color in a pattern color space.
