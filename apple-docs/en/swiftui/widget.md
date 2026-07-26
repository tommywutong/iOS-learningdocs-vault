---
title: Widget
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/widget
source_url: 'https://developer.apple.com/documentation/swiftui/widget'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widget.json'
content_hash: 'sha256:07d2abc5b1cc99c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Widget

<sub>Protocol</sub>

The configuration and content of a widget to display on the Home screen or in Notification Center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol Widget
```

## Overview

Widgets show glanceable and relevant content from your app right on the iOS Home screen or in Notification Center on macOS. Users can add, configure, and arrange widgets to suit their individual needs. You can provide multiple types of widgets, each presenting a specific kind of information. When users want more information, like to read the full article for a headline or to see the details of a package delivery, the widget lets them get to the information in your app quickly.

There are three key components to a widget:

- A configuration that determines whether the widget is configurable, identifies the widget, and defines the SwiftUI views that show the widget’s content.
- A timeline provider that drives the process of updating the widget’s view over time.
- SwiftUI views used by WidgetKit to display the widget.

For information about adding a widget extension to your app, and keeping your widget up to date, see [Creating a widget extension](../widgetkit/creating-a-widget-extension.md) and [Keeping a widget up to date](../widgetkit/keeping-a-widget-up-to-date.md), respectively.

By adding a custom SiriKit intent definition, you can let users customize their widgets to show the information that’s most relevant to them. If you’ve already added support for Siri or Shortcuts, you’re well on your way to supporting customizable widgets. For more information, see [Making a configurable widget](../widgetkit/making-a-configurable-widget.md).

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

### Implementing a widget

- [body](widget/body-swift.property.md) — The content and behavior of the widget.
- [Body](widget/body-swift.associatedtype.md) — The type of configuration representing the content of the widget.

### Running a widget

- [init()](<widget/init().md>) — Creates a widget using `body` as its content.
- [main()](<widget/main().md>) — Initializes and runs the widget.

## See Also

### Creating widgets

- [Building Widgets Using WidgetKit and SwiftUI](../widgetkit/building-widgets-using-widgetkit-and-swiftui.md) — Create widgets to show your app’s content on the Home screen, with custom intents for user-customizable settings.
- [Creating a widget extension](../widgetkit/creating-a-widget-extension.md) — Display your app’s content in a convenient, informative widget on various devices.
- [Keeping a widget up to date](../widgetkit/keeping-a-widget-up-to-date.md) — Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [Making a configurable widget](../widgetkit/making-a-configurable-widget.md) — Give people the option to customize their widgets by adding a custom app intent to your project.
- [WidgetBundle](widgetbundle.md) — A container used to expose multiple widgets from a single widget extension.
- [LimitedAvailabilityConfiguration](limitedavailabilityconfiguration.md) — A type-erased widget configuration.
- [WidgetConfiguration](widgetconfiguration.md) — A type that describes a widget’s content.
- [EmptyWidgetConfiguration](emptywidgetconfiguration.md) — An empty widget configuration.
