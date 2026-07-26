---
title: link
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/primitivebuttonstyle/link
source_url: 'https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/link'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/primitivebuttonstyle/link.json'
content_hash: 'sha256:663a40540b912c29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PrimitiveButtonStyle](../primitivebuttonstyle.md)

# link

<sub>Type Property</sub>

A button style for buttons that emulate links.

<sub>macOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var link: LinkButtonStyle { get }
```

## Discussion

To apply this style to a button, or to a view that contains buttons, use the [buttonStyle(_:)](<../view/buttonstyle(__).md>) modifier.

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
- [glassProminent](glassprominent.md) — A button style that applies a prominent Liquid Glass effect based on the button’s context.
- [glass(_:)](<glass(__).md>) — A button style that applies a configurable Liquid Glass effect based on the button’s context.
- [plain](plain.md) — A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.
