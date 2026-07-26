---
title: difference
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/blendmode-swift.struct/difference
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/difference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/blendmode-swift.struct/difference.json'
content_hash: 'sha256:6a805d125e2060f3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [BlendMode](../blendmode-swift.struct.md)

# difference

<sub>Type Property</sub>

A mode that subtracts the brighter of the source image sample color or the background image sample color from the other.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var difference: GraphicsContext.BlendMode { get }
```

## Discussion

Source image sample values that are black produce no change; white inverts the background color values.

## See Also

### Inverting

- [exclusion](exclusion.md) — A mode that produces an effect similar to that produced by the difference blend mode, but with lower contrast.
