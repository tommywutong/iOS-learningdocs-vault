---
title: ButtonRepeatBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/buttonrepeatbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/buttonrepeatbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/buttonrepeatbehavior.json'
content_hash: 'sha256:57b7ce44537e6144'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ButtonRepeatBehavior

<sub>Structure</sub>

The options for controlling the repeatability of button actions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ButtonRepeatBehavior
```

## Overview

Use values of this type with the [buttonRepeatBehavior(_:)](<view/buttonrepeatbehavior(__).md>) modifier.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting repeat behaviors

- [automatic](buttonrepeatbehavior/automatic.md) — The automatic repeat behavior.
- [enabled](buttonrepeatbehavior/enabled.md) — Repeating button actions will be enabled.
- [disabled](buttonrepeatbehavior/disabled.md) — Repeating button actions will be disabled.

## See Also

### Creating buttons

- [Button](button.md) — A control that initiates an action.
- [buttonStyle(_:)](<view/buttonstyle(__).md>) — Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [buttonBorderShape(_:)](<view/buttonbordershape(__).md>) — Sets the border shape for buttons in this view.
- [ButtonBorderShape](buttonbordershape.md) — A shape used to draw a button’s border.
- [buttonRepeatBehavior(_:)](<view/buttonrepeatbehavior(__).md>) — Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [buttonRepeatBehavior](environmentvalues/buttonrepeatbehavior.md) — Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [buttonSizing(_:)](<view/buttonsizing(__).md>) — The preferred sizing behavior of buttons in the view hierarchy.
- [ButtonSizing](buttonsizing.md) — The sizing behavior of `Button`s and other button-like controls.
- [ButtonRole](buttonrole.md) — A value that describes the purpose of a button.
