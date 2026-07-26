---
title: ControlWidgetButton
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/controlwidgetbutton
source_url: 'https://developer.apple.com/documentation/widgetkit/controlwidgetbutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlwidgetbutton.json'
content_hash: 'sha256:ebdc769685f3d1e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# ControlWidgetButton

<sub>Structure</sub>

A control template representing a button.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct ControlWidgetButton<Label, ActionLabel, Action> where Label : View, ActionLabel : View
```

## Overview

Buttons don’t have state; use them for fire-and-forget actions such as playing a sound or launching an app.

## Relationships

- **Conforms To**: [ControlWidgetTemplate](../swiftui/controlwidgettemplate.md)

## Topics

### Initializers

- [init(action:label:)](<controlwidgetbutton/init(action_label_)-77p8j.md>) — Creates a button template for a control.
- [init(action:label:)](<controlwidgetbutton/init(action_label_)-8oxxp.md>) — Creates a button template for a control that launches an app.
- [init(action:label:actionLabel:)](<controlwidgetbutton/init(action_label_actionlabel_).md>) — Creates a button template for a control.
- [init(action:label:actionLabel:)](<controlwidgetbutton/init(action_label_actionlabel_).md>) — Creates a button template for a control.
- [init(_:action:actionLabel:)](<controlwidgetbutton/init(__action_actionlabel_)-4sgji.md>) — Creates a button template for a control.
- [init(_:action:actionLabel:)](<controlwidgetbutton/init(__action_actionlabel_)-67uvw.md>) — Creates a button template for a control.
- [init(_:action:actionLabel:)](<controlwidgetbutton/init(__action_actionlabel_)-1kxch.md>) — Creates a button template for a control.

### Default action label

- [ControlWidgetButtonDefaultActionLabel](controlwidgetbuttondefaultactionlabel.md) — A view representing the default action label for a `ControlWidgetButton` if none is specified.

## See Also

### Setup and configuration

- [Creating controls to perform actions across the system](creating-controls-to-perform-actions-across-the-system.md) — Perform your app’s actions from Control Center, the Lock Screen, and the Action button.
- [Adding refinements and configuration to controls](adding-refinements-and-configuration-to-controls.md) — Customize the way controls display across the system and offer people the ability to configure them.
- [StaticControlConfiguration](staticcontrolconfiguration.md) — The description of a control that has no user-configurable options.
- [AppIntentControlConfiguration](appintentcontrolconfiguration.md) — The description of a control that uses a custom app intent to provide user-configurable options.
- [ControlCenter](controlcenter.md) — An object you use to access configuration information for controls and reload them.
- [ControlInfo](controlinfo.md) — A structure that contains information about user-configured controls.
- [ControlWidgetToggle](controlwidgettoggle.md) — A control template representing a toggle.
