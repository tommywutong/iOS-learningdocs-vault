---
title: lighten
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/blendmode-swift.struct/lighten
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/lighten'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/blendmode-swift.struct/lighten.json'
content_hash: 'sha256:eb365a81c19ff035'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [BlendMode](../blendmode-swift.struct.md)

# lighten

<sub>Type Property</sub>

A mode that creates composite image samples by choosing the lighter samples from either the source image or the background.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var lighten: GraphicsContext.BlendMode { get }
```

## Discussion

When you draw in this mode, source image samples that are lighter than the background replace the background. Otherwise, the background image samples remain unchanged.

## See Also

### Lightening

- [screen](screen.md) — A mode that multiplies the inverse of the source image samples with the inverse of the background image samples.
- [colorDodge](colordodge.md) — A mode that brightens the background image samples to reflect the source image samples.
- [plusLighter](pluslighter.md) — A mode that adds the components of the source and background images, resulting in a lightened composite.
