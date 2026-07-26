---
title: darken
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/blendmode-swift.struct/darken
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/darken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/blendmode-swift.struct/darken.json'
content_hash: 'sha256:8fb4530fe91815f1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [BlendMode](../blendmode-swift.struct.md)

# darken

<sub>Type Property</sub>

A mode that creates composite image samples by choosing the darker samples from either the source image or the background.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var darken: GraphicsContext.BlendMode { get }
```

## Discussion

When you draw in this mode, source image samples that are darker than the background replace the background. Otherwise, the background image samples remain unchanged.

## See Also

### Darkening

- [multiply](multiply.md) — A mode that multiplies the source image samples with the background image samples.
- [colorBurn](colorburn.md) — A mode that darkens background image samples to reflect the source image samples.
- [plusDarker](plusdarker.md) — A mode that adds the inverse of the color components of the source and background images, and then inverts the result, producing a darkened composite.
