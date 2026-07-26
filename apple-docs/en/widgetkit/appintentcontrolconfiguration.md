---
title: AppIntentControlConfiguration
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/appintentcontrolconfiguration
source_url: 'https://developer.apple.com/documentation/widgetkit/appintentcontrolconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintentcontrolconfiguration.json'
content_hash: 'sha256:cc255f6cec3edaa6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# AppIntentControlConfiguration

<sub>Structure</sub>

The description of a control that uses a custom app intent to provide user-configurable options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct AppIntentControlConfiguration<Configuration, Content> where Configuration : ControlConfigurationIntent, Content : ControlWidgetTemplate
```

## Overview

The following example shows the configuration for a door opener control able to open a door specified by the user.

```swift
struct DoorOpener: ControlWidget {
    var body: some ControlWidgetConfiguration {
        AppIntentControlConfiguration(
            kind: "com.yourcompany.GarageDoorOpener",
            provider: DoorValueProvider()
        ) { door in
            ControlWidgetToggle(
                door.name,
                isOn: door.isOpen,
                action: ToggleDoor(door)
            ) {
                Label(
                    $0 ? "Open" : "Closed",
                    systemImage: $0 ? "door.open" : "door.closed"
                )
            }
        }
    }
}
```

Every control has a unique `kind`, a string that you choose. You use this string to identify your control when reloading its template with [ControlCenter](controlcenter.md).

The value provider is an object that determines a value to use to render your template. This provider receives an intent containing user-editable parameters.

The content closure defines the template that WidgetKit needs to render the control. If you create the configuration using a value provider, when WidgetKit invokes the content closure, it passes a value created by the provider’s `AppIntentControlValueProvider/previewValue` property or `AppIntentControlValueProvider/currentValue()` function.

## Relationships

- **Conforms To**: [ControlWidgetConfiguration](../swiftui/controlwidgetconfiguration.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(kind:intent:content:)](<appintentcontrolconfiguration/init(kind_intent_content_).md>) — Creates a configuration for a control that uses a custom app intent to provide user-configurable options.
- [init(kind:provider:content:)](<appintentcontrolconfiguration/init(kind_provider_content_).md>) — Creates a configuration for a control that uses a custom app intent to provide user-configurable options.

## See Also

### Setup and configuration

- [Creating controls to perform actions across the system](creating-controls-to-perform-actions-across-the-system.md) — Perform your app’s actions from Control Center, the Lock Screen, and the Action button.
- [Adding refinements and configuration to controls](adding-refinements-and-configuration-to-controls.md) — Customize the way controls display across the system and offer people the ability to configure them.
- [StaticControlConfiguration](staticcontrolconfiguration.md) — The description of a control that has no user-configurable options.
- [ControlCenter](controlcenter.md) — An object you use to access configuration information for controls and reload them.
- [ControlInfo](controlinfo.md) — A structure that contains information about user-configured controls.
- [ControlWidgetButton](controlwidgetbutton.md) — A control template representing a button.
- [ControlWidgetToggle](controlwidgettoggle.md) — A control template representing a toggle.
