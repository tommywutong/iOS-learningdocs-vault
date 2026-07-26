---
title: ControlValueProvider
framework: WidgetKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/controlvalueprovider
source_url: 'https://developer.apple.com/documentation/widgetkit/controlvalueprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlvalueprovider.json'
content_hash: 'sha256:24784f061f5d0817'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# ControlValueProvider

<sub>Protocol</sub>

A type that provides a value to a control template.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
protocol ControlValueProvider
```

## Overview

The provider quickly and cheaply prepares a synchronous value to be shown while previewing the control in the add sheet. When the actual control needs to be rendered, the actual, current value will be fetched asynchronously.

For instance, a control that opens and closes a garage door may show a preview of the door being closed. When the actual control is rendered, the control may fetch the door’s status from the cloud:

```swift
struct GarageDoorValueProvider: ControlValueProvider {
    var previewValue: Bool { false }

    func currentValue() async -> Bool {
        await GarageDoorManager.shared.doorStatus()
    }
}
```

## Topics

### Associated Types

- [Value](controlvalueprovider/value.md) — The type of value provided to the template.

### Instance Properties

- [previewValue](controlvalueprovider/previewvalue.md) — A value to be shown while previewing the control in the add sheet.

### Instance Methods

- [currentValue()](<controlvalueprovider/currentvalue().md>) — The current value of the control.

## See Also

### Previews

- [AppIntentControlValueProvider](appintentcontrolvalueprovider.md) — A type that uses a custom intent to provide a value to a control template.
