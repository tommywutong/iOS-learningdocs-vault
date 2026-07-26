---
title: ActivityConfiguration
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/activityconfiguration
source_url: 'https://developer.apple.com/documentation/widgetkit/activityconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/activityconfiguration.json'
content_hash: 'sha256:5fd6cbbfdf0bb7ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# ActivityConfiguration

<sub>Structure</sub>

An object that describes the content of a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency struct ActivityConfiguration<Attributes> where Attributes : ActivityAttributes
```

## Overview

To learn more about offering Live Activities for your app, see [ActivityKit](../activitykit.md).

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [WidgetConfiguration](../swiftui/widgetconfiguration.md)

## Topics

### Creating a Live Activity configuration

- [ActivityViewContext](activityviewcontext.md) — A structure that describes the view context for creating the views of a Live Activity.
- [init(for:content:dynamicIsland:)](<activityconfiguration/init(for_content_dynamicisland_).md>) — Creates a configuration object for a Live Activity.

## See Also

### Live Activity setup

- [Displaying live data with Live Activities](../activitykit/displaying-live-data-with-live-activities.md) — Display up-to-date data and offer quick interactions in the Dynamic Island, on the Lock Screen, in CarPlay, and on a paired Mac or Apple Watch.
- [ActivityKit](../activitykit.md) — Share live updates from your app as Live Activities on iPhone, iPad, Apple Watch, and the Mac.
- [Creating a widget extension](creating-a-widget-extension.md) — Display your app’s content in a convenient, informative widget on various devices.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) — Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [DynamicIsland](dynamicisland.md) — The layout and configuration for a Live Activity that appears in the Dynamic Island.
- [NSUserActivityTypeLiveActivity](nsuseractivitytypeliveactivity.md) — A string that the system passes to the app on launch from a Live Activity that doesn’t provide a URL.
- [ActivityPreviewViewKind](activitypreviewviewkind.md) — Values that represent Live Activity presentations for use in Xcode previews.
- [ActivityFamily](activityfamily.md) — A family that defines the Live Activity’s size.
