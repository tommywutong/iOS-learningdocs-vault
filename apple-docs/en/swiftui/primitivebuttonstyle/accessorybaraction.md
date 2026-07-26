---
title: accessoryBarAction
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/primitivebuttonstyle/accessorybaraction
source_url: 'https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/accessorybaraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/primitivebuttonstyle/accessorybaraction.json'
content_hash: 'sha256:3a5fe82067eb02d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PrimitiveButtonStyle](../primitivebuttonstyle.md)

# accessoryBarAction

<sub>Type Property</sub>

A button style that you use for extra actions in an accessory toolbar.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency static var accessoryBarAction: AccessoryBarActionButtonStyle { get }
```

## Discussion

Use this style for buttons that perform extra actions relative to the accessory toolbar’s main functions, like adding or editing filters. This style also affects other view types that you apply a button style to, like [Toggle](../toggle.md), [Picker](../picker.md), and [Menu](../menu.md) instances.

## See Also

### Getting built-in button styles

- [automatic](automatic.md) — The default button style, based on the button’s context.
- [accessoryBar](accessorybar.md) — A button style that is typically used in the context of an accessory toolbar (sometimes refererred to as a “scope bar”), for buttons that narrow the focus of a search or other operation.
- [bordered](bordered.md) — A button style that applies the standard border style based on the button’s context.
- [borderedProminent](borderedprominent.md) — A button style that applies the standard bordered prominent style based on the button’s context.
- [borderless](borderless.md) — A button style that doesn’t apply a border.
- [card](card.md) — A button style that doesn’t pad the content, and applies a Liquid Glass effect when the button has focus.
- [glass](glass.md) — A button style that applies a Liquid Glass effect based on the button’s context.
- [glassProminent](glassprominent.md) — A button style that applies a prominent Liquid Glass effect based on the button’s context.
- [glass(_:)](<glass(__).md>) — A button style that applies a configurable Liquid Glass effect based on the button’s context.
- [link](link.md) — A button style for buttons that emulate links.
- [plain](plain.md) — A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.
