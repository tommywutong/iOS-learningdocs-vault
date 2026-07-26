---
title: screen
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/blendmode-swift.struct/screen
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/screen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/blendmode-swift.struct/screen.json'
content_hash: 'sha256:7a6326e9f81a7415'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [BlendMode](../blendmode-swift.struct.md)

# screen

<sub>Type Property</sub>

A mode that multiplies the inverse of the source image samples with the inverse of the background image samples.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var screen: GraphicsContext.BlendMode { get }
```

## Discussion

Drawing in this mode results in colors that are at least as light as either of the two contributing sample colors.

## See Also

### Lightening

- [lighten](lighten.md) — A mode that creates composite image samples by choosing the lighter samples from either the source image or the background.
- [colorDodge](colordodge.md) — A mode that brightens the background image samples to reflect the source image samples.
- [plusLighter](pluslighter.md) — A mode that adds the components of the source and background images, resulting in a lightened composite.
