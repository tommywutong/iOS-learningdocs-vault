---
title: 'disabled(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/controlwidgettemplate/disabled(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/controlwidgettemplate/disabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlwidgettemplate/disabled%28_%3A%29.json'
content_hash: 'sha256:6455b3241ae1be6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlWidgetTemplate](../controlwidgettemplate.md)

# disabled(_:)

<sub>Instance Method</sub>

Determines whether people can interact with this control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency func disabled(_ disabled: Bool) -> some ControlWidgetTemplate

```

## Parameters

- `disabled` — A Boolean value that determines whether users can interact with this control.

## Discussion

Controls also respect the [disabled(_:)](<../view/disabled(__).md>) modifier applied to the control’s label. That modifier only disables the label, however. To disable the control overall, apply this modifier to the control template:

```swift
struct GarageDoorOpener: ControlWidget {
    var body: some ControlWidgetConfiguration {
        StaticControlConfiguration(
            kind: "com.myapp.garagedooropener",
            provider: DoorValueProvider()
        ) { door in
            ControlWidgetToggle(...) {
                Label(
                    $0 ? "Open" : "Closed",
                    systemImage: $0 ? "door.open" : "door.closed"
                )
            }
            .disabled(door.isSafetyLockEngaged)
        }
    }
}
```
