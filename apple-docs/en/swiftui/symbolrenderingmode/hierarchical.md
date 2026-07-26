---
title: hierarchical
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolrenderingmode/hierarchical
source_url: 'https://developer.apple.com/documentation/swiftui/symbolrenderingmode/hierarchical'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolrenderingmode/hierarchical.json'
content_hash: 'sha256:a8b593dbcaa700a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SymbolRenderingMode](../symbolrenderingmode.md)

# hierarchical

<sub>Type Property</sub>

A mode that renders symbols as multiple layers, with different opacities applied to the foreground style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let hierarchical: SymbolRenderingMode
```

## Discussion

SwiftUI fills the first layer with the foreground style, and the others the secondary, and tertiary variants of the foreground style. You can specify these styles explicitly using the [foregroundStyle(_:_:)](<../view/foregroundstyle(____).md>) and [foregroundStyle(_:_:_:)](<../view/foregroundstyle(______).md>) modifiers. If you only specify a primary foreground style, SwiftUI automatically derives the others from that style. For example, you can render a filled exclamation mark triangle with purple as the tint color for the exclamation mark, and lower opacity purple for the triangle:

```swift
Image(systemName: "exclamationmark.triangle.fill")
    .symbolRenderingMode(.hierarchical)
    .foregroundStyle(Color.purple)
```

## See Also

### Getting symbol rendering modes

- [monochrome](monochrome.md) — A mode that renders symbols as a single layer filled with the foreground style.
- [multicolor](multicolor.md) — A mode that renders symbols as multiple layers with their inherit styles.
- [palette](palette.md) — A mode that renders symbols as multiple layers, with different styles applied to the layers.
