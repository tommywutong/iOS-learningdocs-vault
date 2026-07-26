---
title: AppIntentControlValueProvider
framework: WidgetKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/appintentcontrolvalueprovider
source_url: 'https://developer.apple.com/documentation/widgetkit/appintentcontrolvalueprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintentcontrolvalueprovider.json'
content_hash: 'sha256:eb69b53d6c9e0949'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# AppIntentControlValueProvider

<sub>Protocol</sub>

A type that uses a custom intent to provide a value to a control template.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
protocol AppIntentControlValueProvider
```

## Overview

The provider quickly and cheaply prepares a synchronous value to be shown while previewing the control in the add sheet. When the actual control needs to be rendered, the actual, current value will be fetched asynchronously.

The provider prepares these values using an intent containing user-editable parameters.

For instance, a control that opens and closes various doors in a user’s home may show a preview of the door being closed. When the actual control is rendered, the control may fetch the configured door’s status from the cloud:

```swift
struct DoorValueProvider: AppIntentControlValueProvider {
    func previewValue(configuration: SelectDoorIntent) -> Door {
        Door(id: configuration.doorId, isOpen: false)
    }

    func currentValue(configuration: SelectDoorIntent) async -> Door {
        let isOpen = await DoorManager.shared
            .status(doorId: configuration.doorId)
        return Door(id: configuration.doorId, isOpen: isOpen)
    }
}
```

## Topics

### Associated Types

- [Configuration](appintentcontrolvalueprovider/configuration.md) — The type of intent used to prepare the value.
- [Value](appintentcontrolvalueprovider/value.md) — The type of value provided to the template.

### Instance Methods

- [currentValue(configuration:)](<appintentcontrolvalueprovider/currentvalue(configuration_).md>) — The current value of the control.
- [previewValue(configuration:)](<appintentcontrolvalueprovider/previewvalue(configuration_).md>) — A value to be shown while previewing the control in the add sheet.

## See Also

### Previews

- [ControlValueProvider](controlvalueprovider.md) — A type that provides a value to a control template.
