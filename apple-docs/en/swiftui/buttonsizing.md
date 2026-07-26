---
title: ButtonSizing
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/buttonsizing
source_url: 'https://developer.apple.com/documentation/swiftui/buttonsizing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/buttonsizing.json'
content_hash: 'sha256:a9ef2ba5ae99d24e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ButtonSizing

<sub>Structure</sub>

The sizing behavior of `Button`s and other button-like controls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ButtonSizing
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [automatic](buttonsizing/automatic.md) — The default button sizing behavior appropriate for the button’s contextual placement and platform.
- [fitted](buttonsizing/fitted.md) — Sizes a button along its primary axis to fit its inner content, compressing if necessary.
- [flexible](buttonsizing/flexible.md) — Sizes a button flexibly along its primary axis, filling its available space by expanding or compressing beyond its ideal size.

## See Also

### Creating buttons

- [Button](button.md) — A control that initiates an action.
- [buttonStyle(_:)](<view/buttonstyle(__).md>) — Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [buttonBorderShape(_:)](<view/buttonbordershape(__).md>) — Sets the border shape for buttons in this view.
- [ButtonBorderShape](buttonbordershape.md) — A shape used to draw a button’s border.
- [buttonRepeatBehavior(_:)](<view/buttonrepeatbehavior(__).md>) — Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [ButtonRepeatBehavior](buttonrepeatbehavior.md) — The options for controlling the repeatability of button actions.
- [buttonRepeatBehavior](environmentvalues/buttonrepeatbehavior.md) — Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [buttonSizing(_:)](<view/buttonsizing(__).md>) — The preferred sizing behavior of buttons in the view hierarchy.
- [ButtonRole](buttonrole.md) — A value that describes the purpose of a button.
