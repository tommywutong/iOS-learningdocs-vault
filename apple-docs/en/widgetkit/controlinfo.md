---
title: ControlInfo
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/controlinfo
source_url: 'https://developer.apple.com/documentation/widgetkit/controlinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlinfo.json'
content_hash: 'sha256:0545c5083a71962f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# ControlInfo

<sub>Structure</sub>

A structure that contains information about user-configured controls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
struct ControlInfo
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Identifiable](../swift/identifiable.md)

## Topics

### Instance Properties

- [kind](controlinfo/kind.md) — The string specified during creation of the control’s configuration.
- [pushInfo](controlinfo/pushinfo.md) — Push information about a control, if present.

### Instance Methods

- [configurationIntent(of:)](<controlinfo/configurationintent(of_).md>) — Gets the associated App Intent.

### Default Implementations

- [Identifiable Implementations](controlinfo/identifiable-implementations.md)

## See Also

### Setup and configuration

- [Creating controls to perform actions across the system](creating-controls-to-perform-actions-across-the-system.md) — Perform your app’s actions from Control Center, the Lock Screen, and the Action button.
- [Adding refinements and configuration to controls](adding-refinements-and-configuration-to-controls.md) — Customize the way controls display across the system and offer people the ability to configure them.
- [StaticControlConfiguration](staticcontrolconfiguration.md) — The description of a control that has no user-configurable options.
- [AppIntentControlConfiguration](appintentcontrolconfiguration.md) — The description of a control that uses a custom app intent to provide user-configurable options.
- [ControlCenter](controlcenter.md) — An object you use to access configuration information for controls and reload them.
- [ControlWidgetButton](controlwidgetbutton.md) — A control template representing a button.
- [ControlWidgetToggle](controlwidgettoggle.md) — A control template representing a toggle.
