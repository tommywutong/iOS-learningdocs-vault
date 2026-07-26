---
title: foreground
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shapestyle/foreground
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/foreground'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/foreground.json'
content_hash: 'sha256:93893fbd9a4b13b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# foreground

<sub>Type Property</sub>

The foreground style in the current context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var foreground: ForegroundStyle { get }
```

## Discussion

Access this value to get the style SwiftUI uses for foreground elements, like text, symbols, and shapes, in the current context. Use the [foregroundStyle(_:)](<../view/foregroundstyle(__).md>) modifier to set a new foreground style for a given view and its child views.

For information about how to use shape styles, see [ShapeStyle](../shapestyle.md).

## See Also

### Semantic styles

- [background](background.md) — The background style in the current context.
- [selection](selection.md) — A style used to visually indicate selection following platform conventional colors and behaviors.
- [separator](separator.md) — A style appropriate for foreground separator or border lines.
- [tint](tint.md) — A style that reflects the current tint color.
- [placeholder](placeholder.md) — A style appropriate for placeholder text.
- [link](link.md) — A style appropriate for links.
- [fill](fill.md) — An overlay fill style for filling shapes.
- [windowBackground](windowbackground.md) — A style appropriate for elements that should match the background of their containing window.
