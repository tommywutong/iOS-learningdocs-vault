---
title: opaque
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/bluroptions/opaque
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/bluroptions/opaque'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/bluroptions/opaque.json'
content_hash: 'sha256:befc19dd5828c1a1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [BlurOptions](../bluroptions.md)

# opaque

<sub>Type Property</sub>

An option that causes the filter to ensure the result is completely opaque.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var opaque: GraphicsContext.BlurOptions { get }
```

## Discussion

The filter ensure opacity by dividing each pixel by its alpha value. The result may be undefined if the input to the filter isn’t also completely opaque.

## See Also

### Getting blur options

- [dithersResult](dithersresult.md) — An option that causes the filter to dither the result, to reduce banding.
