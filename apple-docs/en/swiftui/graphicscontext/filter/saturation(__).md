---
title: 'saturation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/filter/saturation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/saturation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/saturation%28_%3A%29.json'
content_hash: 'sha256:f51e33571fdb9995'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# saturation(_:)

<sub>Type Method</sub>

Returns a filter that applies a saturation adjustment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func saturation(_ amount: Double) -> GraphicsContext.Filter
```

## Parameters

- `amount` — The amount of the saturation adjustment. A value of zero to completely desaturates each pixel, while a value of one makes no change. You can use values greater than one.

## Return Value

A filter that applies a saturation adjustment.

## Discussion

This filter is equivalent to the `saturate` filter primitive defined by the Scalable Vector Graphics (SVG) specification.

## See Also

### Manipulating color

- [colorInvert(_:)](<colorinvert(__).md>) — Returns a filter that inverts the color of their results.
- [colorMultiply(_:)](<colormultiply(__).md>) — Returns a filter that multiplies each color component by the matching component of a given color.
- [hueRotation(_:)](<huerotation(__).md>) — Returns a filter that applies a hue rotation adjustment.
- [grayscale(_:)](<grayscale(__).md>) — Returns a filter that applies a grayscale adjustment.
- [colorMatrix(_:)](<colormatrix(__).md>) — Returns a filter that multiplies by a given color matrix.
