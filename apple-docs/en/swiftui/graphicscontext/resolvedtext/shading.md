---
title: shading
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/resolvedtext/shading
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/resolvedtext/shading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/resolvedtext/shading.json'
content_hash: 'sha256:b5c9825e902a951a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [ResolvedText](../resolvedtext.md)

# shading

<sub>Instance Property</sub>

The shading to fill uncolored text regions with.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var shading: GraphicsContext.Shading
```

## Discussion

This value defaults to the [foreground](../shading/foreground.md) shading.

## See Also

### Getting the text properties

- [firstBaseline(in:)](<firstbaseline(in_).md>) — Gets the distance from the first line’s ascender to its baseline.
- [lastBaseline(in:)](<lastbaseline(in_).md>) — Gets the distance from the first line’s ascender to the last line’s baseline.
- [measure(in:)](<measure(in_).md>) — Measures the size of the resolved text for a given area into which the text should be placed.
