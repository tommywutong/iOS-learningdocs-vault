---
title: shading
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/resolvedimage/shading
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/resolvedimage/shading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/resolvedimage/shading.json'
content_hash: 'sha256:278ff9d62e4f0b98'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [ResolvedImage](../resolvedimage.md)

# shading

<sub>Instance Property</sub>

An optional shading to fill the image with.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var shading: GraphicsContext.Shading?
```

## Discussion

The value of this property defaults to [foreground](../shading/foreground.md) for template images, and to `nil` otherwise.

## See Also

### Getting the image properties

- [size](size.md) — The size of the image.
- [baseline](baseline.md) — The distance from the top of the image to its baseline.
