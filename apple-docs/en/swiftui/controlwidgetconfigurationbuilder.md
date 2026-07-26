---
title: ControlWidgetConfigurationBuilder
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/controlwidgetconfigurationbuilder
source_url: 'https://developer.apple.com/documentation/swiftui/controlwidgetconfigurationbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlwidgetconfigurationbuilder.json'
content_hash: 'sha256:3a4ad1c568293ce6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ControlWidgetConfigurationBuilder

<sub>Structure</sub>

A custom attribute that constructs a control widget’s body.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@resultBuilder struct ControlWidgetConfigurationBuilder
```

## Overview

The `@ControlWidgetConfigurationBuilder` attribute allows your control widget’s body closure to produce a control widget configuration after zero or more other statements:

```swift
struct GarageDoorOpener: ControlWidget {
    var body: some ControlWidgetConfiguration {
        let kind = "com.yourcompany.GarageDoorOpener"

        StaticControlConfiguration(
            kind: kind
        ) {
            ...
        }
    }
}
```

## Topics

### Type Methods

- [buildBlock(_:)](<controlwidgetconfigurationbuilder/buildblock(__).md>) — Passes a single control widget configuration written as a child control through unmodified.
- [buildExpression(_:)](<controlwidgetconfigurationbuilder/buildexpression(__).md>) — Builds an expression within the builder.

## See Also

### Composing control widgets

- [ControlWidget](controlwidget.md) — The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.
- [ControlWidgetConfiguration](controlwidgetconfiguration.md) — A type that describes a control widget’s content.
- [EmptyControlWidgetConfiguration](emptycontrolwidgetconfiguration.md) — An empty control widget configuration.
- [ControlWidgetTemplate](controlwidgettemplate.md) — A type that describes a control widget’s content.
- [EmptyControlWidgetTemplate](emptycontrolwidgettemplate.md) — An empty control widget template.
- [ControlWidgetTemplateBuilder](controlwidgettemplatebuilder.md) — A custom attribute that constructs a control widget template’s body.
- [controlWidgetActionHint(_:)](<view/controlwidgetactionhint(__).md>) — The action hint of the control described by the modified label.
- [controlWidgetStatus(_:)](<view/controlwidgetstatus(__).md>) — The status of the control described by the modified label.
