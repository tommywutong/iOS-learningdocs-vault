---
title: 'buttonBorderShape(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/buttonbordershape(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/buttonbordershape(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/buttonbordershape%28_%3A%29.json'
content_hash: 'sha256:b6fecb2db544cc00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# buttonBorderShape(_:)

<sub>Instance Method</sub>

Sets the border shape for buttons in this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func buttonBorderShape(_ shape: ButtonBorderShape) -> some View

```

## Parameters

- `shape` — The shape to use.

## Discussion

The border shape is used to draw the platter for a bordered button.

The border shape affects buttons of the [bordered](../primitivebuttonstyle/bordered.md) and [borderedProminent](../primitivebuttonstyle/borderedprominent.md) styles.

> [!note] Note
> In macOS 15 and earlier, some border shapes are only applicable to bordered buttons in widgets.

## See Also

### Creating buttons

- [Button](../button.md) — A control that initiates an action.
- [buttonStyle(_:)](<buttonstyle(__).md>) — Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [ButtonBorderShape](../buttonbordershape.md) — A shape used to draw a button’s border.
- [buttonRepeatBehavior(_:)](<buttonrepeatbehavior(__).md>) — Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [ButtonRepeatBehavior](../buttonrepeatbehavior.md) — The options for controlling the repeatability of button actions.
- [buttonRepeatBehavior](../environmentvalues/buttonrepeatbehavior.md) — Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [buttonSizing(_:)](<buttonsizing(__).md>) — The preferred sizing behavior of buttons in the view hierarchy.
- [ButtonSizing](../buttonsizing.md) — The sizing behavior of `Button`s and other button-like controls.
- [ButtonRole](../buttonrole.md) — A value that describes the purpose of a button.
