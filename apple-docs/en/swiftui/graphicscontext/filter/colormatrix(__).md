---
title: 'colorMatrix(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/filter/colormatrix(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/colormatrix(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/colormatrix%28_%3A%29.json'
content_hash: 'sha256:2d87b9f9c1038e3e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# colorMatrix(_:)

<sub>Type Method</sub>

Returns a filter that multiplies by a given color matrix.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func colorMatrix(_ matrix: ColorMatrix) -> GraphicsContext.Filter
```

## Parameters

- `matrix` — A [ColorMatrix](../../colormatrix.md) instance used by the filter.

## Return Value

A filter that transforms color using the given matrix.

## Discussion

This filter is equivalent to the `feColorMatrix` filter primitive defined by the Scalable Vector Graphics (SVG) specification.

The filter creates the output color `[R', G', B', A']` at each pixel from an input color `[R, G, B, A]` by multiplying the input color by the square matrix formed by the first four columns of the [ColorMatrix](../../colormatrix.md), then adding the fifth column to the result:

```swift
R' = r1 ✕ R + r2 ✕ G + r3 ✕ B + r4 ✕ A + r5
G' = g1 ✕ R + g2 ✕ G + g3 ✕ B + g4 ✕ A + g5
B' = b1 ✕ R + b2 ✕ G + b3 ✕ B + b4 ✕ A + b5
A' = a1 ✕ R + a2 ✕ G + a3 ✕ B + a4 ✕ A + a5
```

## See Also

### Manipulating color

- [saturation(_:)](<saturation(__).md>) — Returns a filter that applies a saturation adjustment.
- [colorInvert(_:)](<colorinvert(__).md>) — Returns a filter that inverts the color of their results.
- [colorMultiply(_:)](<colormultiply(__).md>) — Returns a filter that multiplies each color component by the matching component of a given color.
- [hueRotation(_:)](<huerotation(__).md>) — Returns a filter that applies a hue rotation adjustment.
- [grayscale(_:)](<grayscale(__).md>) — Returns a filter that applies a grayscale adjustment.
