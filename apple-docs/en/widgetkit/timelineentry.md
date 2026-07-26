---
title: TimelineEntry
framework: WidgetKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/timelineentry
source_url: 'https://developer.apple.com/documentation/widgetkit/timelineentry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/timelineentry.json'
content_hash: 'sha256:376332f54ce28fbf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# TimelineEntry

<sub>Protocol</sub>

A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
protocol TimelineEntry
```

## Overview

A [TimelineProvider](timelineprovider.md) creates one or more timeline entries with dates that tell WidgetKit when to display a widget. To render a widget, WidgetKit executes the `content` block of the widget’s configuration, passing the corresponding timeline entry.

When you declare a structure conforming to `TimelineEntry`, include any additional information that the configuration’s content block requires to render the widget. The following code shows a timeline entry structure for a widget that displays a game character’s health level.

```swift
struct CharacterDetailEntry: TimelineEntry {
    var date: Date
    var healthLevel: Double
}
```

The content block of the widget’s configuration receives the entry as a parameter and then passes the relevant information to the view that renders your widget.

```swift
struct CharacterDetailWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(
            kind: "com.mygame.character-detail",
            provider: CharacterDetailProvider()) { entry in
            CharacterDetailView(entry: entry)
        }
        .configurationDisplayName("Character Details")
        .description("Displays a character's health and other details")
        .supportedFamilies([.systemSmall, .systemMedium, .systemLarge])
    }
}
```

## Topics

### Configuring Timeline Entry Properties

- [date](timelineentry/date.md) — The date for WidgetKit to render a widget.
- [relevance](timelineentry/relevance.md) — The relevance of a widget’s content to the user.

## See Also

### Timeline updates

- [Keeping a widget up to date](keeping-a-widget-up-to-date.md) — Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [TimelineProvider](timelineprovider.md) — A type that advises WidgetKit when to update a widget’s display.
- [AppIntentTimelineProvider](appintenttimelineprovider.md) — A type that advises WidgetKit when to update a user-configurable widget’s display.
- [IntentTimelineProvider](intenttimelineprovider.md) — A type that advises WidgetKit when to update a user-configurable widget’s display.
- [TimelineProviderContext](timelineprovidercontext.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [Timeline](timeline.md) — An object that specifies a date for WidgetKit to update a widget’s view.
- [WidgetCenter](widgetcenter.md) — An object that contains a list of user-configured widgets and is used for reloading widget timelines.
