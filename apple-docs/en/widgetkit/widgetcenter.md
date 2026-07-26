---
title: WidgetCenter
framework: WidgetKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetcenter
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetcenter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetcenter.json'
content_hash: 'sha256:1c9b5825c57394ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# WidgetCenter

<sub>Class</sub>

An object that contains a list of user-configured widgets and is used for reloading widget timelines.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class WidgetCenter
```

## Overview

WidgetCenter provides information about user-configured widgets, such as their family. For widgets that use [IntentConfiguration](intentconfiguration.md), you can retrieve the user-edited values.

### Getting Configured Widget Information

To get a list of user-configured widgets, use [getCurrentConfigurations(_:)](<widgetcenter/getcurrentconfigurations(__).md>). This property provides an array of [WidgetInfo](widgetinfo.md) objects containing the following information:

```swift
struct WidgetInfo {
    public let configuration: INIntent?
    public let family: WidgetFamily
    public let kind: String
}
```

The `kind` string matches the parameter you use when creating the widget’s [StaticConfiguration](staticconfiguration.md) or [IntentConfiguration](intentconfiguration.md). The `family` property matches one of the options specified in the [supportedFamilies(_:)](<../swiftui/widgetconfiguration/supportedfamilies(__).md>) property of the widget’s configuration. If your widget is based on [IntentConfiguration](intentconfiguration.md), the `configuration` property provides the custom intent containing the user-customized values for each individual widget.

### Requesting a Reload of Your Widget’s Timeline

Changes in your app’s state may affect a widget’s timeline. When this happens, you can tell WidgetKit to reload the timeline for either a specific kind of widget or all widgets. For example, your app might register for push notifications based on the widgets the user has configured. When your app receives a push notification that changes the state for one or more of your widgets, requesting a reload of their timelines updates their display.

If you only need to reload a certain kind of widget, you can request a reload for only that kind. For example, in response to a push notification about a change in a game’s status, you could request a reload for only the game status widgets:

```swift
WidgetCenter.shared.reloadTimelines(ofKind: "com.mygame.gamestatus")
```

To request a reload for all of your widgets:

```swift
WidgetCenter.shared.reloadAllTimelines()
```

## Topics

### Getting Widget Information

- [shared](widgetcenter/shared.md) — The shared widget center.
- [getCurrentConfigurations(_:)](<widgetcenter/getcurrentconfigurations(__).md>) — Retrieves information about user-configured widgets.
- [UserInfoKey](widgetcenter/userinfokey.md) — An object that defines keys for accessing information in a user info dictionary.

### Reloading Widget Timelines

- [reloadTimelines(ofKind:)](<widgetcenter/reloadtimelines(ofkind_).md>) — Reloads the timelines for all widgets of a particular kind.
- [reloadAllTimelines()](<widgetcenter/reloadalltimelines().md>) — Reloads the timelines for all configured widgets belonging to the containing app.

### Reloading Recommended Preconfigured Widgets

- [invalidateConfigurationRecommendations()](<widgetcenter/invalidateconfigurationrecommendations().md>) — Invalidates and refreshes the preconfigured intent configurations for user-customizable widgets.

### Instance Properties

- [currentPushInfo](widgetcenter/currentpushinfo.md) — Provides the current push information for widget reloads and relevance refreshes.

### Instance Methods

- [currentConfigurations()](<widgetcenter/currentconfigurations().md>) — Retrieves information about user-configured widgets.
- [invalidateRelevance(ofKind:)](<widgetcenter/invalidaterelevance(ofkind_).md>) — Mark the relevance for a kind as invalid.

## See Also

### Timeline updates

- [Keeping a widget up to date](keeping-a-widget-up-to-date.md) — Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [TimelineProvider](timelineprovider.md) — A type that advises WidgetKit when to update a widget’s display.
- [AppIntentTimelineProvider](appintenttimelineprovider.md) — A type that advises WidgetKit when to update a user-configurable widget’s display.
- [IntentTimelineProvider](intenttimelineprovider.md) — A type that advises WidgetKit when to update a user-configurable widget’s display.
- [TimelineProviderContext](timelineprovidercontext.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [TimelineEntry](timelineentry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [Timeline](timeline.md) — An object that specifies a date for WidgetKit to update a widget’s view.
