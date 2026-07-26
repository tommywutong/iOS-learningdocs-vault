---
title: 'colorInvert(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/filter/colorinvert(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/colorinvert(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/colorinvert%28_%3A%29.json'
content_hash: 'sha256:8b1f601679feb426'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# colorInvert(_:)

<sub>Type Method</sub>

Returns a filter that inverts the color of their results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func colorInvert(_ amount: Double = 1) -> GraphicsContext.Filter
```

## Parameters

- `amount` — The inversion amount. A value of one results in total inversion, while a value of zero leaves the result unchanged. Other values apply a linear multiplier effect.

## Return Value

A filter that applies a color inversion.

## Discussion

This filter is equivalent to the `invert` filter primitive defined by the Scalable Vector Graphics (SVG) specification.

## See Also

### Manipulating color

- [saturation(_:)](<saturation(__).md>) — Returns a filter that applies a saturation adjustment.
- [colorMultiply(_:)](<colormultiply(__).md>) — Returns a filter that multiplies each color component by the matching component of a given color.
- [hueRotation(_:)](<huerotation(__).md>) — Returns a filter that applies a hue rotation adjustment.
- [grayscale(_:)](<grayscale(__).md>) — Returns a filter that applies a grayscale adjustment.
- [colorMatrix(_:)](<colormatrix(__).md>) — Returns a filter that multiplies by a given color matrix.
