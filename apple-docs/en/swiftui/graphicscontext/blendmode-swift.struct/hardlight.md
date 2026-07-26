---
title: hardLight
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/blendmode-swift.struct/hardlight
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/hardlight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/blendmode-swift.struct/hardlight.json'
content_hash: 'sha256:81052c71c4b6fd2a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [BlendMode](../blendmode-swift.struct.md)

# hardLight

<sub>Type Property</sub>

A mode that either multiplies or screens colors, depending on the source image sample color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var hardLight: GraphicsContext.BlendMode { get }
```

## Discussion

If the source image sample color is lighter than 50% gray, the background is lightened, similar to screening. If the source image sample color is darker than 50% gray, the background is darkened, similar to multiplying. If the source image sample color is equal to 50% gray, the source image is not changed. Image samples that are equal to pure black or pure white result in pure black or white. The overall effect is similar to what you’d achieve by shining a harsh spotlight on the source image. Use this to add highlights to a scene.

## See Also

### Adding contrast

- [overlay](overlay.md) — A mode that either multiplies or screens the source image samples with the background image samples, depending on the background color.
- [softLight](softlight.md) — A mode that either darkens or lightens colors, depending on the source image sample color.
