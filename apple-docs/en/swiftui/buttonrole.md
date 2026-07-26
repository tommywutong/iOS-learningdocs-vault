---
title: ButtonRole
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/buttonrole
source_url: 'https://developer.apple.com/documentation/swiftui/buttonrole'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/buttonrole.json'
content_hash: 'sha256:9b0965adb1cf8e88'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ButtonRole

<sub>Structure</sub>

A value that describes the purpose of a button.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ButtonRole
```

## Overview

A button role provides a description of a button’s purpose.  For example, the [destructive](buttonrole/destructive.md) role indicates that a button performs a destructive action, like delete user data:

```swift
Button("Delete", role: .destructive) { delete() }
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting button roles

- [cancel](buttonrole/cancel.md) — A role that indicates a button that cancels an operation.
- [destructive](buttonrole/destructive.md) — A role that indicates a destructive button.

### Type Properties

- [close](buttonrole/close.md) — A role that indicates a button that closes the current operation.
- [confirm](buttonrole/confirm.md) — A role that indicates a button that confirms an operation.

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
- [ButtonSizing](buttonsizing.md) — The sizing behavior of `Button`s and other button-like controls.
