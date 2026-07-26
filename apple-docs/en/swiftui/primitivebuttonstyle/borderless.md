---
title: borderless
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 17.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/primitivebuttonstyle/borderless
source_url: 'https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/borderless'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/primitivebuttonstyle/borderless.json'
content_hash: 'sha256:7cd48a5abf42d7d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PrimitiveButtonStyle](../primitivebuttonstyle.md)

# borderless

<sub>Type Property</sub>

A button style that doesn’t apply a border.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated static var borderless: BorderlessButtonStyle { get }
```

## Discussion

In tvOS, when a person focuses on a borderless button, the button animates to a raised position with a Liquid Glass effect. This button style applies a Liquid Glass effect to the first image of the button’s content when the button gains focus. To apply the effect to a different subview of your button, apply the [hoverEffect(_:)](<../view/hovereffect(__).md>) modifier with a [highlight](../hovereffect/highlight.md) effect to that subview. For more information, see [Creating a tvOS media catalog app in SwiftUI](../creating-a-tvos-media-catalog-app-in-swiftui.md).

To apply this style to a button, or to a view that contains buttons, use the [buttonStyle(_:)](<../view/buttonstyle(__)-66fbx.md>) modifier.

## See Also

### Getting built-in button styles

- [automatic](automatic.md) — The default button style, based on the button’s context.
- [accessoryBar](accessorybar.md) — A button style that is typically used in the context of an accessory toolbar (sometimes refererred to as a “scope bar”), for buttons that narrow the focus of a search or other operation.
- [accessoryBarAction](accessorybaraction.md) — A button style that you use for extra actions in an accessory toolbar.
- [bordered](bordered.md) — A button style that applies the standard border style based on the button’s context.
- [borderedProminent](borderedprominent.md) — A button style that applies the standard bordered prominent style based on the button’s context.
- [card](card.md) — A button style that doesn’t pad the content, and applies a Liquid Glass effect when the button has focus.
- [glass](glass.md) — A button style that applies a Liquid Glass effect based on the button’s context.
- [glassProminent](glassprominent.md) — A button style that applies a prominent Liquid Glass effect based on the button’s context.
- [glass(_:)](<glass(__).md>) — A button style that applies a configurable Liquid Glass effect based on the button’s context.
- [link](link.md) — A button style for buttons that emulate links.
- [plain](plain.md) — A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.
