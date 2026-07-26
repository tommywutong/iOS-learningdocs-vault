---
title: 'buttonRepeatBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/buttonrepeatbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/buttonrepeatbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/buttonrepeatbehavior%28_%3A%29.json'
content_hash: 'sha256:4a5a9297f73a6265'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# buttonRepeatBehavior(_:)

<sub>Instance Method</sub>

Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func buttonRepeatBehavior(_ behavior: ButtonRepeatBehavior) -> some View

```

## Parameters

- `behavior` — A value of `enabled` means that buttons should enable repeating behavior and a value of `disabled` means that buttons should disallow repeating behavior.

## Discussion

Apply this to buttons that increment or decrement a value or perform some other inherently iterative operation. Interactions such as pressing-and-holding on the button, holding the button’s keyboard shortcut, or holding down the space key while the button is focused will trigger this repeat behavior.

```swift
Button {
    playbackSpeed.advance(by: 1)
} label: {
    Label("Speed up", systemImage: "hare")
}
.buttonRepeatBehavior(.enabled)
```

This affects all system button styles, as well as automatically affects custom `ButtonStyle` conforming types. This does not automatically apply to custom `PrimitiveButtonStyle` conforming types, and the `EnvironmentValues.buttonRepeatBehavior` value should be used to adjust their custom gestures as appropriate.

## See Also

### Creating buttons

- [Button](../button.md) — A control that initiates an action.
- [buttonStyle(_:)](<buttonstyle(__).md>) — Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [buttonBorderShape(_:)](<buttonbordershape(__).md>) — Sets the border shape for buttons in this view.
- [ButtonBorderShape](../buttonbordershape.md) — A shape used to draw a button’s border.
- [ButtonRepeatBehavior](../buttonrepeatbehavior.md) — The options for controlling the repeatability of button actions.
- [buttonRepeatBehavior](../environmentvalues/buttonrepeatbehavior.md) — Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [buttonSizing(_:)](<buttonsizing(__).md>) — The preferred sizing behavior of buttons in the view hierarchy.
- [ButtonSizing](../buttonsizing.md) — The sizing behavior of `Button`s and other button-like controls.
- [ButtonRole](../buttonrole.md) — A value that describes the purpose of a button.
