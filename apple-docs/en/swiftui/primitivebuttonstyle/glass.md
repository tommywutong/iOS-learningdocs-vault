---
title: glass
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/primitivebuttonstyle/glass
source_url: 'https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/glass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/primitivebuttonstyle/glass.json'
content_hash: 'sha256:5e0e68d8a63213ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PrimitiveButtonStyle](../primitivebuttonstyle.md)

# glass

<sub>Type Property</sub>

A button style that applies a Liquid Glass effect based on the button’s context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
@export(implementation) nonisolated static var glass: GlassButtonStyle { get }
```

## Discussion

In tvOS, this button style applies a Liquid Glass effect regardless of whether the button has focus.

To apply this style to a button, or to a view that contains buttons, use the [buttonStyle(_:)](<../view/buttonstyle(__)-66fbx.md>) modifier.

## See Also

### Getting built-in button styles

- [automatic](automatic.md) — The default button style, based on the button’s context.
- [accessoryBar](accessorybar.md) — A button style that is typically used in the context of an accessory toolbar (sometimes refererred to as a “scope bar”), for buttons that narrow the focus of a search or other operation.
- [accessoryBarAction](accessorybaraction.md) — A button style that you use for extra actions in an accessory toolbar.
- [bordered](bordered.md) — A button style that applies the standard border style based on the button’s context.
- [borderedProminent](borderedprominent.md) — A button style that applies the standard bordered prominent style based on the button’s context.
- [borderless](borderless.md) — A button style that doesn’t apply a border.
- [card](card.md) — A button style that doesn’t pad the content, and applies a Liquid Glass effect when the button has focus.
- [glassProminent](glassprominent.md) — A button style that applies a prominent Liquid Glass effect based on the button’s context.
- [glass(_:)](<glass(__).md>) — A button style that applies a configurable Liquid Glass effect based on the button’s context.
- [link](link.md) — A button style for buttons that emulate links.
- [plain](plain.md) — A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.
