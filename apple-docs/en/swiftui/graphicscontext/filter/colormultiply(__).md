---
title: 'colorMultiply(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/filter/colormultiply(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/colormultiply(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/colormultiply%28_%3A%29.json'
content_hash: 'sha256:862dbac12f7be911'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# colorMultiply(_:)

<sub>Type Method</sub>

Returns a filter that multiplies each color component by the matching component of a given color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func colorMultiply(_ color: Color) -> GraphicsContext.Filter
```

## Parameters

- `color` — The color that the filter uses for the multiplication operation.

## Return Value

A filter that multiplies color components.

## See Also

### Manipulating color

- [saturation(_:)](<saturation(__).md>) — Returns a filter that applies a saturation adjustment.
- [colorInvert(_:)](<colorinvert(__).md>) — Returns a filter that inverts the color of their results.
- [hueRotation(_:)](<huerotation(__).md>) — Returns a filter that applies a hue rotation adjustment.
- [grayscale(_:)](<grayscale(__).md>) — Returns a filter that applies a grayscale adjustment.
- [colorMatrix(_:)](<colormatrix(__).md>) — Returns a filter that multiplies by a given color matrix.
