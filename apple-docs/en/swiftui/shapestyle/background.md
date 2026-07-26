---
title: background
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shapestyle/background
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/background'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/background.json'
content_hash: 'sha256:bc971bd0eca6b63a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# background

<sub>Type Property</sub>

The background style in the current context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var background: BackgroundStyle { get }
```

## Discussion

Access this value to get the style SwiftUI uses for the background in the current context. The specific color that SwiftUI renders depends on factors like the platform and whether the user has turned on Dark Mode.

For information about how to use shape styles, see [ShapeStyle](../shapestyle.md).

## See Also

### Semantic styles

- [foreground](foreground.md) — The foreground style in the current context.
- [selection](selection.md) — A style used to visually indicate selection following platform conventional colors and behaviors.
- [separator](separator.md) — A style appropriate for foreground separator or border lines.
- [tint](tint.md) — A style that reflects the current tint color.
- [placeholder](placeholder.md) — A style appropriate for placeholder text.
- [link](link.md) — A style appropriate for links.
- [fill](fill.md) — An overlay fill style for filling shapes.
- [windowBackground](windowbackground.md) — A style appropriate for elements that should match the background of their containing window.
