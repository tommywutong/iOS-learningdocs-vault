---
title: saturation
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/blendmode-swift.struct/saturation
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/saturation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/blendmode-swift.struct/saturation.json'
content_hash: 'sha256:5669f7a415be442f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [BlendMode](../blendmode-swift.struct.md)

# saturation

<sub>Type Property</sub>

A mode that uses the luminance and hue values of the background with the saturation of the source image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var saturation: GraphicsContext.BlendMode { get }
```

## Discussion

Areas of the background that have no saturation — namely, pure gray areas — don’t produce a change.

## See Also

### Mixing color components

- [hue](hue.md) — A mode that uses the luminance and saturation values of the background with the hue of the source image.
- [color](color.md) — A mode that uses the luminance values of the background with the hue and saturation values of the source image.
- [luminosity](luminosity.md) — A mode that uses the hue and saturation of the background with the luminance of the source image.
