---
title: multicolor
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolrenderingmode/multicolor
source_url: 'https://developer.apple.com/documentation/swiftui/symbolrenderingmode/multicolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolrenderingmode/multicolor.json'
content_hash: 'sha256:5c3a266618f2cb26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SymbolRenderingMode](../symbolrenderingmode.md)

# multicolor

<sub>Type Property</sub>

A mode that renders symbols as multiple layers with their inherit styles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let multicolor: SymbolRenderingMode
```

## Discussion

The layers may be filled with their own inherent styles, or the foreground style. For example, you can render a filled exclamation mark triangle in its inherent colors, with yellow for the triangle and white for the exclamation mark:

```swift
Image(systemName: "exclamationmark.triangle.fill")
    .symbolRenderingMode(.multicolor)
```

## See Also

### Getting symbol rendering modes

- [hierarchical](hierarchical.md) — A mode that renders symbols as multiple layers, with different opacities applied to the foreground style.
- [monochrome](monochrome.md) — A mode that renders symbols as a single layer filled with the foreground style.
- [palette](palette.md) — A mode that renders symbols as multiple layers, with different styles applied to the layers.
