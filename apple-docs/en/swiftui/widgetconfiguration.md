---
title: WidgetConfiguration
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/widgetconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration.json'
content_hash: 'sha256:adcd9078bcd58596'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WidgetConfiguration

<sub>Protocol</sub>

A type that describes a widget’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol WidgetConfiguration
```

## Overview

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

## Relationships

- **Conforming Types**: [EmptyWidgetConfiguration](emptywidgetconfiguration.md), [LimitedAvailabilityConfiguration](limitedavailabilityconfiguration.md)

## Topics

### Implementing a widget

- [body](widgetconfiguration/body-swift.property.md) — The content and behavior of this widget.
- [Body](widgetconfiguration/body-swift.associatedtype.md) — The type of widget configuration representing the body of this configuration.

### Setting a name

- [configurationDisplayName(_:)](<widgetconfiguration/configurationdisplayname(__).md>) — Sets the localized name shown for a widget when a user adds or edits the widget.

### Setting a description

- [description(_:)](<widgetconfiguration/description(__).md>) — Sets the description shown for a widget when a user adds or edits it using the contents of a text view.

### Setting the appearance

- [supportedFamilies(_:)](<widgetconfiguration/supportedfamilies(__).md>) — Sets the sizes that a widget supports.
- [contentMarginsDisabled()](<widgetconfiguration/contentmarginsdisabled().md>) — Disable default content margins.
- [disfavoredLocations(_:for:)](<widgetconfiguration/disfavoredlocations(__for_).md>) — Sets the disfavored locations for a widget.
- [containerBackgroundRemovable(_:)](<widgetconfiguration/containerbackgroundremovable(__).md>) — A modifier that marks the background of a widget as removable.

### Managing background tasks

- [backgroundTask(_:action:)](<widgetconfiguration/backgroundtask(__action_).md>) — Runs the given action when the system provides a background task.
- [onBackgroundURLSessionEvents(matching:_:)](<widgetconfiguration/onbackgroundurlsessionevents(matching___).md>) — Adds an action to perform when events related to a URL session identified by a closure are waiting to be processed.

### Instance Methods

- [associatedKind(_:)](<widgetconfiguration/associatedkind(__).md>) — Tells the system that a relevance-based widget can replace a timeline-based widget.
- [promptsForUserConfiguration()](<widgetconfiguration/promptsforuserconfiguration().md>) — Specifies that a widget’s configuration UI should be automatically presented after the widget is added.
- [pushHandler(_:)](<widgetconfiguration/pushhandler(__).md>) — Register a type that can handle push tokens changing for widgets.
- [supplementalActivityFamilies(_:)](<widgetconfiguration/supplementalactivityfamilies(__).md>) — Sets the sizes that a Live Activity supports.
- [supportedMountingStyles(_:)](<widgetconfiguration/supportedmountingstyles(__).md>) — Specifies the mounting style for this widget.
- [widgetTexture(_:)](<widgetconfiguration/widgettexture(__).md>) — Specifies the widget texture for this widget.

## See Also

### Creating widgets

- [Building Widgets Using WidgetKit and SwiftUI](../widgetkit/building-widgets-using-widgetkit-and-swiftui.md) — Create widgets to show your app’s content on the Home screen, with custom intents for user-customizable settings.
- [Creating a widget extension](../widgetkit/creating-a-widget-extension.md) — Display your app’s content in a convenient, informative widget on various devices.
- [Keeping a widget up to date](../widgetkit/keeping-a-widget-up-to-date.md) — Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [Making a configurable widget](../widgetkit/making-a-configurable-widget.md) — Give people the option to customize their widgets by adding a custom app intent to your project.
- [Widget](widget.md) — The configuration and content of a widget to display on the Home screen or in Notification Center.
- [WidgetBundle](widgetbundle.md) — A container used to expose multiple widgets from a single widget extension.
- [LimitedAvailabilityConfiguration](limitedavailabilityconfiguration.md) — A type-erased widget configuration.
- [EmptyWidgetConfiguration](emptywidgetconfiguration.md) — An empty widget configuration.
