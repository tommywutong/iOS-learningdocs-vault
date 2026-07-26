---
title: overlay
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/blendmode-swift.struct/overlay
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/overlay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/blendmode-swift.struct/overlay.json'
content_hash: 'sha256:72bf33a6d5c7cf4c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [BlendMode](../blendmode-swift.struct.md)

# overlay

<sub>Type Property</sub>

A mode that either multiplies or screens the source image samples with the background image samples, depending on the background color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var overlay: GraphicsContext.BlendMode { get }
```

## Discussion

Drawing in this mode overlays the existing image samples while preserving the highlights and shadows of the background. The background color mixes with the source image to reflect the lightness or darkness of the background.

## See Also

### Adding contrast

- [softLight](softlight.md) — A mode that either darkens or lightens colors, depending on the source image sample color.
- [hardLight](hardlight.md) — A mode that either multiplies or screens colors, depending on the source image sample color.
