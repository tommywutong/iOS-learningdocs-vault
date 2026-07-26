---
title: buttonRepeatBehavior
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/buttonrepeatbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/buttonrepeatbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/buttonrepeatbehavior.json'
content_hash: 'sha256:39073a1c1f6f7b68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# buttonRepeatBehavior

<sub>Instance Property</sub>

Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var buttonRepeatBehavior: ButtonRepeatBehavior { get }
```

## Discussion

A value of `enabled` means that buttons will be able to repeatedly trigger their action, and `disabled` means they should not. A value of `automatic` means that buttons will defer to default behavior.

## See Also

### Creating buttons

- [Button](../button.md) — A control that initiates an action.
- [buttonStyle(_:)](<../view/buttonstyle(__).md>) — Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [buttonBorderShape(_:)](<../view/buttonbordershape(__).md>) — Sets the border shape for buttons in this view.
- [ButtonBorderShape](../buttonbordershape.md) — A shape used to draw a button’s border.
- [buttonRepeatBehavior(_:)](<../view/buttonrepeatbehavior(__).md>) — Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [ButtonRepeatBehavior](../buttonrepeatbehavior.md) — The options for controlling the repeatability of button actions.
- [buttonSizing(_:)](<../view/buttonsizing(__).md>) — The preferred sizing behavior of buttons in the view hierarchy.
- [ButtonSizing](../buttonsizing.md) — The sizing behavior of `Button`s and other button-like controls.
- [ButtonRole](../buttonrole.md) — A value that describes the purpose of a button.
