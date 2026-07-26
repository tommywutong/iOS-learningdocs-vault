---
title: ControlWidgetTemplateBuilder
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/controlwidgettemplatebuilder
source_url: 'https://developer.apple.com/documentation/swiftui/controlwidgettemplatebuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlwidgettemplatebuilder.json'
content_hash: 'sha256:063171298e5a1519'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ControlWidgetTemplateBuilder

<sub>Structure</sub>

A custom attribute that constructs a control widget template’s body.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@resultBuilder struct ControlWidgetTemplateBuilder
```

## Overview

The `@ControlWidgetTemplateBuilder` attribute allows your control template’s body closure to produce a control template after zero or more other statements:

```swift
struct GarageDoorOpener: ControlWidget {
    var body: some ControlWidgetConfiguration {
        let kind = "com.yourcompany.GarageDoorOpener"

        StaticControlConfiguration(
            kind: kind
        ) {
            let isOpen = ...

            ControlWidgetToggle(
                "Garage Door",
                isOn: isOpen,
                action: ToggleGarageDoor()
            ) {
                Label(
                    $0 ? "Open" : "Closed",
                    systemImage: $0 ?
                        "door.garage.open" : "door.garage.closed"
                )
            }
        }
    }
}
```

## Topics

### Type Methods

- [buildBlock(_:)](<controlwidgettemplatebuilder/buildblock(__).md>) — Passes a single control widget template written as a child view through unmodified.
- [buildExpression(_:)](<controlwidgettemplatebuilder/buildexpression(__).md>) — Builds an expression within the builder.

## See Also

### Composing control widgets

- [ControlWidget](controlwidget.md) — The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.
- [ControlWidgetConfiguration](controlwidgetconfiguration.md) — A type that describes a control widget’s content.
- [EmptyControlWidgetConfiguration](emptycontrolwidgetconfiguration.md) — An empty control widget configuration.
- [ControlWidgetConfigurationBuilder](controlwidgetconfigurationbuilder.md) — A custom attribute that constructs a control widget’s body.
- [ControlWidgetTemplate](controlwidgettemplate.md) — A type that describes a control widget’s content.
- [EmptyControlWidgetTemplate](emptycontrolwidgettemplate.md) — An empty control widget template.
- [controlWidgetActionHint(_:)](<view/controlwidgetactionhint(__).md>) — The action hint of the control described by the modified label.
- [controlWidgetStatus(_:)](<view/controlwidgetstatus(__).md>) — The status of the control described by the modified label.
