---
title: invertsAlpha
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/shadowoptions/invertsalpha
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/shadowoptions/invertsalpha'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/shadowoptions/invertsalpha.json'
content_hash: 'sha256:57983dc4e44f92af'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [ShadowOptions](../shadowoptions.md)

# invertsAlpha

<sub>Type Property</sub>

An option that causes the filter to invert the alpha of the shadow.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var invertsAlpha: GraphicsContext.ShadowOptions { get }
```

## Discussion

You can create an “inner shadow” effect by combining this option with [shadowAbove](shadowabove.md) and using the [sourceAtop](../blendmode-swift.struct/sourceatop.md) blend mode.

## See Also

### Getting shadow options

- [disablesGroup](disablesgroup.md) — An option that causes the filter to composite the object and its shadow separately in the current layer.
- [shadowAbove](shadowabove.md) — An option that causes the filter to draw the shadow above the object, rather than below it.
- [shadowOnly](shadowonly.md) — An option that causes the filter to draw only the shadow, and omit the source object.
