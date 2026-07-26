---
title: 'hueRotation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/filter/huerotation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/huerotation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/huerotation%28_%3A%29.json'
content_hash: 'sha256:ff1c7b456a5562fc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# hueRotation(_:)

<sub>Type Method</sub>

Returns a filter that applies a hue rotation adjustment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func hueRotation(_ angle: Angle) -> GraphicsContext.Filter
```

## Parameters

- `angle` — The amount by which to rotate the hue value of each pixel.

## Return Value

A filter that applies a hue rotation adjustment.

## Discussion

This filter is equivalent to the `hue-rotate` filter primitive defined by the Scalable Vector Graphics (SVG) specification.

## See Also

### Manipulating color

- [saturation(_:)](<saturation(__).md>) — Returns a filter that applies a saturation adjustment.
- [colorInvert(_:)](<colorinvert(__).md>) — Returns a filter that inverts the color of their results.
- [colorMultiply(_:)](<colormultiply(__).md>) — Returns a filter that multiplies each color component by the matching component of a given color.
- [grayscale(_:)](<grayscale(__).md>) — Returns a filter that applies a grayscale adjustment.
- [colorMatrix(_:)](<colormatrix(__).md>) — Returns a filter that multiplies by a given color matrix.
