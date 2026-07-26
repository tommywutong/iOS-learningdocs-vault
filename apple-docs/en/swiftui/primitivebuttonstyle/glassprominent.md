---
title: glassProminent
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/primitivebuttonstyle/glassprominent
source_url: 'https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/glassprominent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/primitivebuttonstyle/glassprominent.json'
content_hash: 'sha256:24de5f7fdcc44dd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PrimitiveButtonStyle](../primitivebuttonstyle.md)

# glassProminent

<sub>Type Property</sub>

A button style that applies a prominent Liquid Glass effect based on the button’s context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var glassProminent: GlassProminentButtonStyle { get }
```

## Discussion

In tvOS, this button style applies a Liquid Glass effect regardless of whether the button has focus. This style is similar to the [borderedProminent](borderedprominent.md) style.

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
- [glass](glass.md) — A button style that applies a Liquid Glass effect based on the button’s context.
- [glass(_:)](<glass(__).md>) — A button style that applies a configurable Liquid Glass effect based on the button’s context.
- [link](link.md) — A button style for buttons that emulate links.
- [plain](plain.md) — A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.
