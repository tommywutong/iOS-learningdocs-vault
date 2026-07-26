---
title: palette
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolrenderingmode/palette
source_url: 'https://developer.apple.com/documentation/swiftui/symbolrenderingmode/palette'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolrenderingmode/palette.json'
content_hash: 'sha256:ef7bc76631cd910b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SymbolRenderingMode](../symbolrenderingmode.md)

# palette

<sub>Type Property</sub>

A mode that renders symbols as multiple layers, with different styles applied to the layers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let palette: SymbolRenderingMode
```

## Discussion

In this mode SwiftUI maps each successively defined layer in the image to the next of the primary, secondary, and tertiary variants of the foreground style. You can specify these styles explicitly using the [foregroundStyle(_:_:)](<../view/foregroundstyle(____).md>) and [foregroundStyle(_:_:_:)](<../view/foregroundstyle(______).md>) modifiers. If you only specify a primary foreground style, SwiftUI automatically derives the others from that style. For example, you can render a filled exclamation mark triangle with yellow as the tint color for the exclamation mark, and fill the triangle with cyan:

```swift
Image(systemName: "exclamationmark.triangle.fill")
    .symbolRenderingMode(.palette)
    .foregroundStyle(Color.yellow, Color.cyan)
```

You can also omit the symbol rendering mode, as specifying multiple foreground styles implies switching to palette rendering mode:

```swift
Image(systemName: "exclamationmark.triangle.fill")
    .foregroundStyle(Color.yellow, Color.cyan)
```

## See Also

### Getting symbol rendering modes

- [hierarchical](hierarchical.md) — A mode that renders symbols as multiple layers, with different opacities applied to the foreground style.
- [monochrome](monochrome.md) — A mode that renders symbols as a single layer filled with the foreground style.
- [multicolor](multicolor.md) — A mode that renders symbols as multiple layers with their inherit styles.
