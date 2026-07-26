---
title: ControlWidget
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/controlwidget
source_url: 'https://developer.apple.com/documentation/swiftui/controlwidget'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlwidget.json'
content_hash: 'sha256:24c20ba86eb0b2c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ControlWidget

<sub>Protocol</sub>

The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol ControlWidget
```

## Overview

Controls allow users to quickly read the state of your app or its accessories, and take quick actions, without having to open your app. Users can add, configure, and arrange controls to suit their individual needs. You can provide multiple types of controls, each representing a specific kind of action.

There are three key components to a control:

- A configuration that determines whether the control is configurable, identifies the control, and defines the SwiftUI template that provides the control’s content.
- A value provider that defines the value of the control when being previewed and when being actually rendered
- The template used by WidgetKit to display the control.

Controls are defined using templates in order to ensure that they control will work at all sizes and in all system spaces in which they might be displayed. These templates define images (specifically, symbol images) and text using simple SwiftUI views like [Label](label.md), [Text](text.md), and [Image](image.md); and tint colors using the [tint(_:)](<controlwidgettemplate/tint(__).md>) modifier.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Associated Types

- [Body](controlwidget/body-swift.associatedtype.md) — The type of configuration representing the content of this control.

### Initializers

- [init()](<controlwidget/init().md>) — Creates a control using `body` as its content.

### Instance Properties

- [body](controlwidget/body-swift.property.md) — The content and behavior of the control.

### Type Methods

- [main()](<controlwidget/main().md>)

## See Also

### Composing control widgets

- [ControlWidgetConfiguration](controlwidgetconfiguration.md) — A type that describes a control widget’s content.
- [EmptyControlWidgetConfiguration](emptycontrolwidgetconfiguration.md) — An empty control widget configuration.
- [ControlWidgetConfigurationBuilder](controlwidgetconfigurationbuilder.md) — A custom attribute that constructs a control widget’s body.
- [ControlWidgetTemplate](controlwidgettemplate.md) — A type that describes a control widget’s content.
- [EmptyControlWidgetTemplate](emptycontrolwidgettemplate.md) — An empty control widget template.
- [ControlWidgetTemplateBuilder](controlwidgettemplatebuilder.md) — A custom attribute that constructs a control widget template’s body.
- [controlWidgetActionHint(_:)](<view/controlwidgetactionhint(__).md>) — The action hint of the control described by the modified label.
- [controlWidgetStatus(_:)](<view/controlwidgetstatus(__).md>) — The status of the control described by the modified label.
