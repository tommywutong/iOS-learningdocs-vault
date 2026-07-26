---
title: ControlWidgetToggle
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/controlwidgettoggle
source_url: 'https://developer.apple.com/documentation/widgetkit/controlwidgettoggle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlwidgettoggle.json'
content_hash: 'sha256:6fea0bdacd2b9468'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# ControlWidgetToggle

<sub>Structure</sub>

A control template representing a toggle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct ControlWidgetToggle<Label, ValueLabel, Action> where Label : View, ValueLabel : View
```

## Overview

Toggles are controls that have two states, “off” and “on”.

## Relationships

- **Conforms To**: [ControlWidgetTemplate](../swiftui/controlwidgettemplate.md)

## Topics

### Initializers

- [init(isOn:action:label:)](<controlwidgettoggle/init(ison_action_label_).md>) — Creates a toggle template for a control.
- [init(isOn:action:label:valueLabel:)](<controlwidgettoggle/init(ison_action_label_valuelabel_).md>) — Creates a toggle template for a control.
- [init(_:isOn:action:valueLabel:)](<controlwidgettoggle/init(__ison_action_valuelabel_)-33wfq.md>) — Creates a toggle template for a control.
- [init(_:isOn:action:valueLabel:)](<controlwidgettoggle/init(__ison_action_valuelabel_)-5o6bn.md>) — Creates a toggle template for a control.
- [init(_:isOn:action:valueLabel:)](<controlwidgettoggle/init(__ison_action_valuelabel_)-4lk32.md>) — Creates a toggle template for a control.

### Default action label

- [ControlWidgetToggleDefaultLabel](controlwidgettoggledefaultlabel.md) — A view that represents the default label for a toggle control if you don’t provide a label.

## See Also

### Setup and configuration

- [Creating controls to perform actions across the system](creating-controls-to-perform-actions-across-the-system.md) — Perform your app’s actions from Control Center, the Lock Screen, and the Action button.
- [Adding refinements and configuration to controls](adding-refinements-and-configuration-to-controls.md) — Customize the way controls display across the system and offer people the ability to configure them.
- [StaticControlConfiguration](staticcontrolconfiguration.md) — The description of a control that has no user-configurable options.
- [AppIntentControlConfiguration](appintentcontrolconfiguration.md) — The description of a control that uses a custom app intent to provide user-configurable options.
- [ControlCenter](controlcenter.md) — An object you use to access configuration information for controls and reload them.
- [ControlInfo](controlinfo.md) — A structure that contains information about user-configured controls.
- [ControlWidgetButton](controlwidgetbutton.md) — A control template representing a button.
