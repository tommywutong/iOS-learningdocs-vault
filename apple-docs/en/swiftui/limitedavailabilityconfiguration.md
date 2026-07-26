---
title: LimitedAvailabilityConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+, Mac Catalyst 16.1+, macOS 13.0+, visionOS 1.0+, watchOS 9.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/limitedavailabilityconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/limitedavailabilityconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/limitedavailabilityconfiguration.json'
content_hash: 'sha256:d9a136472430bc41'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# LimitedAvailabilityConfiguration

<sub>Structure</sub>

A type-erased widget configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @frozen @preconcurrency struct LimitedAvailabilityConfiguration
```

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your behalf.

## Relationships

- **Conforms To**: [WidgetConfiguration](widgetconfiguration.md)

## See Also

### Creating widgets

- [Building Widgets Using WidgetKit and SwiftUI](../widgetkit/building-widgets-using-widgetkit-and-swiftui.md) — Create widgets to show your app’s content on the Home screen, with custom intents for user-customizable settings.
- [Creating a widget extension](../widgetkit/creating-a-widget-extension.md) — Display your app’s content in a convenient, informative widget on various devices.
- [Keeping a widget up to date](../widgetkit/keeping-a-widget-up-to-date.md) — Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [Making a configurable widget](../widgetkit/making-a-configurable-widget.md) — Give people the option to customize their widgets by adding a custom app intent to your project.
- [Widget](widget.md) — The configuration and content of a widget to display on the Home screen or in Notification Center.
- [WidgetBundle](widgetbundle.md) — A container used to expose multiple widgets from a single widget extension.
- [WidgetConfiguration](widgetconfiguration.md) — A type that describes a widget’s content.
- [EmptyWidgetConfiguration](emptywidgetconfiguration.md) — An empty widget configuration.
