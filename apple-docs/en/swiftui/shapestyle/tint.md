---
title: tint
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shapestyle/tint
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/tint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/tint.json'
content_hash: 'sha256:4b5c19b6343e1dce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# tint

<sub>Type Property</sub>

A style that reflects the current tint color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var tint: TintShapeStyle { get }
```

## Discussion

You can set the tint color with the `tint(_:)` modifier. If no explicit tint is set, the tint is derived from the app’s accent color.

## See Also

### Semantic styles

- [foreground](foreground.md) — The foreground style in the current context.
- [background](background.md) — The background style in the current context.
- [selection](selection.md) — A style used to visually indicate selection following platform conventional colors and behaviors.
- [separator](separator.md) — A style appropriate for foreground separator or border lines.
- [placeholder](placeholder.md) — A style appropriate for placeholder text.
- [link](link.md) — A style appropriate for links.
- [fill](fill.md) — An overlay fill style for filling shapes.
- [windowBackground](windowbackground.md) — A style appropriate for elements that should match the background of their containing window.
