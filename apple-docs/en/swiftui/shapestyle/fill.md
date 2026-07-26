---
title: fill
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shapestyle/fill
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/fill'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/fill.json'
content_hash: 'sha256:216163deeeaaef5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# fill

<sub>Type Property</sub>

An overlay fill style for filling shapes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var fill: FillShapeStyle { get }
```

## Discussion

This shape style is appropriate for items situated on top of an existing background color. It incorporates transparency to allow the background color to show through.

Use the primary version of this style to fill thin or small shapes, such as the track of a slider on iOS. Use the secondary version of this style to fill medium-size shapes, such as the background of a switch on iOS. Use the tertiary version of this style to fill large shapes, such as input fields, search bars, or buttons on iOS. Use the quaternary version of this style to fill large areas that contain complex content, such as an expanded table cell on iOS.

## See Also

### Semantic styles

- [foreground](foreground.md) — The foreground style in the current context.
- [background](background.md) — The background style in the current context.
- [selection](selection.md) — A style used to visually indicate selection following platform conventional colors and behaviors.
- [separator](separator.md) — A style appropriate for foreground separator or border lines.
- [tint](tint.md) — A style that reflects the current tint color.
- [placeholder](placeholder.md) — A style appropriate for placeholder text.
- [link](link.md) — A style appropriate for links.
- [windowBackground](windowbackground.md) — A style appropriate for elements that should match the background of their containing window.
