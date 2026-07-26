---
title: opacity
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/opacity
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/opacity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/opacity.json'
content_hash: 'sha256:be4fd1cb56e33f80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# opacity

<sub>Instance Property</sub>

The opacity of drawing operations in the context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var opacity: Double { get set }
```

## Discussion

Set this value to affect the opacity of content that you subsequently draw into the context. Changing this value has no impact on the content you previously drew into the context.

## See Also

### Setting opacity and the blend mode

- [blendMode](blendmode-swift.property.md) — The blend mode used by drawing operations in the context.
- [BlendMode](blendmode-swift.struct.md) — The ways that a graphics context combines new content with background content.
