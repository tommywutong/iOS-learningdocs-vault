---
title: inverse
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/clipoptions/inverse
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/clipoptions/inverse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/clipoptions/inverse.json'
content_hash: 'sha256:84176ffacedab2f6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [ClipOptions](../clipoptions.md)

# inverse

<sub>Type Property</sub>

An option to invert the shape or layer alpha as the clip mask.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var inverse: GraphicsContext.ClipOptions { get }
```

## Discussion

When you use this option, SwiftUI uses `1 - alpha` instead of `alpha` for the given clip shape.
