---
title: windowBackground
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shapestyle/windowbackground
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/windowbackground'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/windowbackground.json'
content_hash: 'sha256:f27050a2f1bc461f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# windowBackground

<sub>Type Property</sub>

A style appropriate for elements that should match the background of their containing window.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
@export(implementation) static var windowBackground: WindowBackgroundShapeStyle { get }
```

## Discussion

On macOS, this has a unique appearance compared to the default `ShapeStyle.background`. It matches the default background of a window: a wallpaper-tinted light gray in the light appearance and a wallpaper-tinted dark gray in the dark appearance.

On visionOS, the default glass window background can only be created using `glassBackgroundEffect`.

For information about how to use shape styles, see [ShapeStyle](../shapestyle.md).

## See Also

### Semantic styles

- [foreground](foreground.md) — The foreground style in the current context.
- [background](background.md) — The background style in the current context.
- [selection](selection.md) — A style used to visually indicate selection following platform conventional colors and behaviors.
- [separator](separator.md) — A style appropriate for foreground separator or border lines.
- [tint](tint.md) — A style that reflects the current tint color.
- [placeholder](placeholder.md) — A style appropriate for placeholder text.
- [link](link.md) — A style appropriate for links.
- [fill](fill.md) — An overlay fill style for filling shapes.
