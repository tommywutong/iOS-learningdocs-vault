---
title: blendMode
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/blendmode-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/blendmode-swift.property.json'
content_hash: 'sha256:1fa459cbb6d31f25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# blendMode

<sub>Instance Property</sub>

The blend mode used by drawing operations in the context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var blendMode: GraphicsContext.BlendMode { get set }
```

## Discussion

Set this value to affect how any content that you subsequently draw into the context blends with content that’s already in the context. Use one of the [BlendMode](blendmode-swift.struct.md) values.

## See Also

### Setting opacity and the blend mode

- [opacity](opacity.md) — The opacity of drawing operations in the context.
- [BlendMode](blendmode-swift.struct.md) — The ways that a graphics context combines new content with background content.
