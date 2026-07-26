---
title: 'tint(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/controlwidgettemplate/tint(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/controlwidgettemplate/tint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlwidgettemplate/tint%28_%3A%29.json'
content_hash: 'sha256:d51e275f5ff1d4d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlWidgetTemplate](../controlwidgettemplate.md)

# tint(_:)

<sub>Instance Method</sub>

Sets the tint color within this control template.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency func tint(_ tint: Color?) -> some ControlWidgetTemplate

```

## Parameters

- `tint` — The tint [Color](../color.md) to apply.

## Discussion

Controls don’t respect the [tint(_:)](<../view/tint(__).md>) modifier when applied to control labels, nor do controls support arbitrary tint shape styles. Instead, define a tint color for your control by applying this modifier to its template:

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
            .tint(.orange)
        }
    }
}
```
