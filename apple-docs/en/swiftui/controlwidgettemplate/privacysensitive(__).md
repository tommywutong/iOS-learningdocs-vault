---
title: 'privacySensitive(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/controlwidgettemplate/privacysensitive(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/controlwidgettemplate/privacysensitive(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlwidgettemplate/privacysensitive%28_%3A%29.json'
content_hash: 'sha256:9644c43c3553a452'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlWidgetTemplate](../controlwidgettemplate.md)

# privacySensitive(_:)

<sub>Instance Method</sub>

Marks the control template as containing sensitive, private user data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency func privacySensitive(_ sensitive: Bool = true) -> some ControlWidgetTemplate

```

## Parameters

- `sensitive` — A Boolean value that determines whether this control is sensitive.

## Discussion

The system redacts controls marked with this modifier when those controls are displayed on the Lock Screen and the device is locked.

Controls also respect the [privacySensitive(_:)](<../view/privacysensitive(__).md>) modifier applied to the control’s label. That modifier only redacts the control content, however. To redact the content _and_ the state of the control, apply this modifier to the control template:

```swift
struct GarageDoorOpener: ControlWidget {
    var body: some ControlWidgetConfiguration {
        StaticControlConfiguration(...) {
            ControlWidgetToggle(...) {
                Label(
                    $0 ? "Open" : "Closed",
                    systemImage: $0 ? "door.open" : "door.closed"
                )
            }
            .privacySensitive()
        }
    }
}
```
