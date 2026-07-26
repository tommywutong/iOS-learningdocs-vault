---
title: ButtonBorderShape
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/buttonbordershape
source_url: 'https://developer.apple.com/documentation/swiftui/buttonbordershape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/buttonbordershape.json'
content_hash: 'sha256:290567da2823e8c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ButtonBorderShape

<sub>Structure</sub>

A shape used to draw a button’s border.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ButtonBorderShape
```

## Overview

Use the [buttonBorderShape(_:)](<view/buttonbordershape(__).md>) view modifier to apply the shape to bordered buttons within a view hierarchy.

## Relationships

- **Conforms To**: [Animatable](animatable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [InsettableShape](insettableshape.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Shape](shape.md), [View](view.md)

## Topics

### Getting border shapes

- [automatic](buttonbordershape/automatic.md) — A shape that defers to the system to determine an appropriate shape for the given context and platform.
- [capsule](buttonbordershape/capsule.md) — A capsule shape.
- [circle](buttonbordershape/circle.md) — A circular shape.
- [roundedRectangle](buttonbordershape/roundedrectangle.md) — A rounded rectangle shape.
- [roundedRectangle(radius:)](<buttonbordershape/roundedrectangle(radius_).md>) — A rounded rectangle shape.

## See Also

### Creating buttons

- [Button](button.md) — A control that initiates an action.
- [buttonStyle(_:)](<view/buttonstyle(__).md>) — Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [buttonBorderShape(_:)](<view/buttonbordershape(__).md>) — Sets the border shape for buttons in this view.
- [buttonRepeatBehavior(_:)](<view/buttonrepeatbehavior(__).md>) — Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [ButtonRepeatBehavior](buttonrepeatbehavior.md) — The options for controlling the repeatability of button actions.
- [buttonRepeatBehavior](environmentvalues/buttonrepeatbehavior.md) — Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [buttonSizing(_:)](<view/buttonsizing(__).md>) — The preferred sizing behavior of buttons in the view hierarchy.
- [ButtonSizing](buttonsizing.md) — The sizing behavior of `Button`s and other button-like controls.
- [ButtonRole](buttonrole.md) — A value that describes the purpose of a button.
