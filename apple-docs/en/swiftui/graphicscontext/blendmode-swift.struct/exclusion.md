---
title: exclusion
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/blendmode-swift.struct/exclusion
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/exclusion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/blendmode-swift.struct/exclusion.json'
content_hash: 'sha256:51043027983e4526'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [BlendMode](../blendmode-swift.struct.md)

# exclusion

<sub>Type Property</sub>

A mode that produces an effect similar to that produced by the difference blend mode, but with lower contrast.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var exclusion: GraphicsContext.BlendMode { get }
```

## Discussion

Source image sample values that are black don’t produce a change; white inverts the background color values.

## See Also

### Inverting

- [difference](difference.md) — A mode that subtracts the brighter of the source image sample color or the background image sample color from the other.
