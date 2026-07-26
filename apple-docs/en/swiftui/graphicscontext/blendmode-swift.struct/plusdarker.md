---
title: plusDarker
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/blendmode-swift.struct/plusdarker
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/plusdarker'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/blendmode-swift.struct/plusdarker.json'
content_hash: 'sha256:de6f1a5539c5e944'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [BlendMode](../blendmode-swift.struct.md)

# plusDarker

<sub>Type Property</sub>

A mode that adds the inverse of the color components of the source and background images, and then inverts the result, producing a darkened composite.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var plusDarker: GraphicsContext.BlendMode { get }
```

## Discussion

This mode implements the equation `R = MAX(0, 1 - ((1 - D) + (1 - S)))` where

- `R` is the composite image.
- `S` is the source image.
- `D` is the background.

## See Also

### Darkening

- [darken](darken.md) — A mode that creates composite image samples by choosing the darker samples from either the source image or the background.
- [multiply](multiply.md) — A mode that multiplies the source image samples with the background image samples.
- [colorBurn](colorburn.md) — A mode that darkens background image samples to reflect the source image samples.
