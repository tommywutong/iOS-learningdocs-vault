---
title: StaticConfiguration
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/staticconfiguration
source_url: 'https://developer.apple.com/documentation/widgetkit/staticconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/staticconfiguration.json'
content_hash: 'sha256:8235e19b35c5d3b8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# StaticConfiguration

<sub>Structure</sub>

An object describing the content of a widget that has no user-configurable options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct StaticConfiguration<Content> where Content : View
```

## Overview

The following example shows the configuration for the leaderboard widget of the [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) sample code project.

```swift
struct LeaderboardWidget: Widget {

    public var body: some WidgetConfiguration {
        StaticConfiguration(kind: EmojiRanger.LeaderboardWidgetKind, provider: LeaderboardProvider()) { entry in
            LeaderboardWidgetEntryView(entry: entry)
        }
        .configurationDisplayName("Ranger Leaderboard")
        .description("See all the rangers.")
        .supportedFamilies(LeaderboardWidget.supportedFamilies)
    }
}
```

Every widget has a unique `kind`, a string that you choose. You use this string to identify your widget when reloading its timeline with [WidgetCenter](widgetcenter.md).

The timeline provider is an object that determines the timeline for refreshing your widget. Providing future dates for updating your widget allows the system to optimize the refresh process.

The content closure contains the SwiftUI views that WidgetKit needs to render the widget. When WidgetKit invokes the content closure, it passes a timeline entry created by the widget provider’s [getSnapshot(in:completion:)](<timelineprovider/getsnapshot(in_completion_).md>) or [getTimeline(in:completion:)](<timelineprovider/gettimeline(in_completion_).md>) method.

Modifiers let you specify the families your widget supports, and the details shown when users add or edit their widgets.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [WidgetConfiguration](../swiftui/widgetconfiguration.md)

## Topics

### Creating a widget configuration

- [init(kind:provider:content:)](<staticconfiguration/init(kind_provider_content_).md>) — Creates a configuration for a widget, with no user-configurable options.
- [body](../swiftui/widgetconfiguration/body-swift.property.md) — The content and behavior of this widget.

### Setting the display name

- [configurationDisplayName(_:)](<../swiftui/widgetconfiguration/configurationdisplayname(__)-2c3zv.md>) — Sets the name shown for a widget when a user adds or edits it using the specified string.
- [configurationDisplayName(_:)](<../swiftui/widgetconfiguration/configurationdisplayname(__)-3sbn4.md>) — Sets the name shown for a widget when a user adds or edits it using the contents of a text view.
- [configurationDisplayName(_:)](<../swiftui/widgetconfiguration/configurationdisplayname(__)-4v9q.md>) — Sets the localized name shown for a widget when a user adds or edits the widget.

### Setting the description

- [description(_:)](<../swiftui/widgetconfiguration/description(__)-1bvuj.md>) — Sets the description shown for a widget when a user adds or edits it using the contents of a text view.
- [description(_:)](<../swiftui/widgetconfiguration/description(__)-2bfr.md>) — Sets the description shown for a widget when a user adds or edits it using the specified string.
- [description(_:)](<../swiftui/widgetconfiguration/description(__)-4q9pa.md>) — Sets the localized description shown for a widget when a user adds or edits the widget.

### Setting the supported families

- [supportedFamilies(_:)](<../swiftui/widgetconfiguration/supportedfamilies(__).md>) — Sets the sizes that a widget supports.
- [supplementalActivityFamilies(_:)](<../swiftui/widgetconfiguration/supplementalactivityfamilies(__).md>) — Sets the sizes that a Live Activity supports.

### Handling background network requests

- [backgroundTask(_:action:)](<../swiftui/widgetconfiguration/backgroundtask(__action_).md>) — Runs the given action when the system provides a background task.
- [onBackgroundURLSessionEvents(matching:_:)](<../swiftui/widgetconfiguration/onbackgroundurlsessionevents(matching___)-2e152.md>) — Adds an action to perform when events related to a URL session identified by a closure are waiting to be processed.
- [onBackgroundURLSessionEvents(matching:_:)](<../swiftui/widgetconfiguration/onbackgroundurlsessionevents(matching___)-fw6x.md>) — Adds an action to perform when events related to a URL session with a matching identifier are waiting to be processed.

## See Also

### Widget creation

- [Creating a widget extension](creating-a-widget-extension.md) — Display your app’s content in a convenient, informative widget on various devices.
- [Developing a WidgetKit strategy](developing-a-widgetkit-strategy.md) — Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) — Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [Preparing widgets for additional platforms, contexts, and appearances](preparing-widgets-for-additional-contexts-and-appearances.md) — Create widgets that support additional platforms and adapt to their context.
- [Widget](../swiftui/widget.md) — The configuration and content of a widget to display on the Home screen or in Notification Center.
- [WidgetFamily](widgetfamily.md) — Values that define the widget’s size and shape.
