---
title: monochrome
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolrenderingmode/monochrome
source_url: 'https://developer.apple.com/documentation/swiftui/symbolrenderingmode/monochrome'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolrenderingmode/monochrome.json'
content_hash: 'sha256:997c0d12620976b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SymbolRenderingMode](../symbolrenderingmode.md)

# monochrome

<sub>Type Property</sub>

A mode that renders symbols as a single layer filled with the foreground style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let monochrome: SymbolRenderingMode
```

## Discussion

For example, you can render a filled exclamation mark triangle in purple:

```swift
Image(systemName: "exclamationmark.triangle.fill")
    .symbolRenderingMode(.monochrome)
    .foregroundStyle(Color.purple)
```

## See Also

### Getting symbol rendering modes

- [hierarchical](hierarchical.md) — A mode that renders symbols as multiple layers, with different opacities applied to the foreground style.
- [multicolor](multicolor.md) — A mode that renders symbols as multiple layers with their inherit styles.
- [palette](palette.md) — A mode that renders symbols as multiple layers, with different styles applied to the layers.
