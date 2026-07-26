---
title: AppIntentTimelineProvider
framework: WidgetKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/appintenttimelineprovider
source_url: 'https://developer.apple.com/documentation/widgetkit/appintenttimelineprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintenttimelineprovider.json'
content_hash: 'sha256:7c79c7f10691ece5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# AppIntentTimelineProvider

<sub>Protocol</sub>

A type that advises WidgetKit when to update a user-configurable widget’s display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
protocol AppIntentTimelineProvider
```

## Overview

An App Intent timeline provider performs the same function as [TimelineProvider](timelineprovider.md), but it also incorporates user-configured details into timeline entries.

For example, in a widget that displays the health status of a game character the user has chosen, the provider receives a custom intent specifying the character to display. In your app code, you then define a custom App Intent. The intent can include the character’s details such as its name, avatar, strategic alliances, and so on.

```swift
struct CharacterConfiguration: WidgetConfigurationIntent {
    static var title: LocalizedStringResource = "Character"

    @Parameter(title: "Name")
    var name: String

    @Parameter(title: "Avatar", default: "Player 1")
    var avatar: String

    @Parameter(title: "Alliances", default: [])
    var alliances: [String]

    @Parameter(title: "Health", default: 100.0)
    var healthLevel: Double
}
```

Because users can add multiple instances of a particular widget, your provider needs a way to differentiate which instance WidgetKit is asking about. When WidgetKit calls [snapshot(for:in:)](<appintenttimelineprovider/snapshot(for_in_).md>) or [timeline(for:in:)](<appintenttimelineprovider/timeline(for_in_).md>), it passes an instance of your configuration intent, configured with the user-selected details. The game widget provider accesses the properties of the intent and includes them in the [TimelineEntry](timelineentry.md). WidgetKit then invokes the widget configuration’s content closure, passing the timeline entry to allow the views to access the user-configured properties. For example, the provider might implement a `TimelineEntry` with properties corresponding to those in the custom intent:

```swift
struct CharacterDetailEntry: TimelineEntry {
    var date: Date
    var name: String
    var avatar: String
    var alliances: [String]
    var healthLevel: Double
}
```

To generate a snapshot, the game widget provider initializes the character detail entry using the properties from the intent.

```swift
struct CharacterDetailProvider: AppIntentTimelineProvider {
    func snapshot(for configuration: CharacterConfiguration, in context: Context) async -> CharacterDetailEntry {
        return CharacterDetailEntry(
            date: Date(),
            name: configuration.characterName,
            avatar: configuration.avatar,
            alliances: configuration.alliances,
            healthLevel: configuration.healthLevel?.doubleValue
        )
    }
}
```

## Topics

### Generating timelines

- [placeholder(in:)](<appintenttimelineprovider/placeholder(in_).md>) — Provides a timeline entry representing a placeholder version of the widget.
- [recommendations()](<appintenttimelineprovider/recommendations().md>) — Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [relevance()](<appintenttimelineprovider/relevance().md>) — Provides an object containing attributes that describe when a specific widget is relevant.
- [snapshot(for:in:)](<appintenttimelineprovider/snapshot(for_in_).md>) — Provides a timeline entry representing the current time and state of a widget.
- [timeline(for:in:)](<appintenttimelineprovider/timeline(for_in_).md>) — Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [Context](appintenttimelineprovider/context.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [Entry](appintenttimelineprovider/entry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [Intent](appintenttimelineprovider/intent.md) — The intent that contains user-customized values.

## See Also

### Timeline updates

- [Keeping a widget up to date](keeping-a-widget-up-to-date.md) — Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [TimelineProvider](timelineprovider.md) — A type that advises WidgetKit when to update a widget’s display.
- [IntentTimelineProvider](intenttimelineprovider.md) — A type that advises WidgetKit when to update a user-configurable widget’s display.
- [TimelineProviderContext](timelineprovidercontext.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [TimelineEntry](timelineentry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [Timeline](timeline.md) — An object that specifies a date for WidgetKit to update a widget’s view.
- [WidgetCenter](widgetcenter.md) — An object that contains a list of user-configured widgets and is used for reloading widget timelines.
