---
title: accessoryBar
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/primitivebuttonstyle/accessorybar
source_url: 'https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/accessorybar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/primitivebuttonstyle/accessorybar.json'
content_hash: 'sha256:1b6eedca67640a56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PrimitiveButtonStyle](../primitivebuttonstyle.md)

# accessoryBar

<sub>Type Property</sub>

A button style that is typically used in the context of an accessory toolbar (sometimes refererred to as a “scope bar”), for buttons that narrow the focus of a search or other operation.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency static var accessoryBar: AccessoryBarButtonStyle { get }
```

## Discussion

This is the default button style for views in accessory toolbars, created with `ToolbarItemPlacement.init(id:_)`, and for searchable scopes.

This style will also affect button style `Toggle`s, as well as button style `Picker`s and `Menu`s.

```swift
HStack(alignment: .firstTextBaseline) {
    Button("Button") {}

    Toggle("Toggle", isOn: $isToggleOn)
        .toggleStyle(.button)

    Picker("Picker", selection: $selection) {
        Text("Option 1").tag(0)
        Text("Option 2").tag(1)
    }

    Picker("Inline Picker", selection: $selection) {
        Text("Option 1").tag(0)
        Text("Option 2").tag(1)
    }
    .pickerStyle(.inline)

    Menu("Menu") {
        Button("Item") {}
    }
}
.buttonStyle(.accessoryBar)
```

## See Also

### Getting built-in button styles

- [automatic](automatic.md) — The default button style, based on the button’s context.
- [accessoryBarAction](accessorybaraction.md) — A button style that you use for extra actions in an accessory toolbar.
- [bordered](bordered.md) — A button style that applies the standard border style based on the button’s context.
- [borderedProminent](borderedprominent.md) — A button style that applies the standard bordered prominent style based on the button’s context.
- [borderless](borderless.md) — A button style that doesn’t apply a border.
- [card](card.md) — A button style that doesn’t pad the content, and applies a Liquid Glass effect when the button has focus.
- [glass](glass.md) — A button style that applies a Liquid Glass effect based on the button’s context.
- [glassProminent](glassprominent.md) — A button style that applies a prominent Liquid Glass effect based on the button’s context.
- [glass(_:)](<glass(__).md>) — A button style that applies a configurable Liquid Glass effect based on the button’s context.
- [link](link.md) — A button style for buttons that emulate links.
- [plain](plain.md) — A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.
