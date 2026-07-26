---
title: IntentTimelineProvider
framework: WidgetKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/intenttimelineprovider
source_url: 'https://developer.apple.com/documentation/widgetkit/intenttimelineprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/intenttimelineprovider.json'
content_hash: 'sha256:2eaf9a548b554cd2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# IntentTimelineProvider

<sub>Protocol</sub>

A type that advises WidgetKit when to update a user-configurable widget’s display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
protocol IntentTimelineProvider
```

## Overview

An Intent timeline provider performs the same function as [TimelineProvider](timelineprovider.md), but it also incorporates user-configured details into timeline entries.

For example, in a widget that displays the health status of a game character the user has chosen, the provider receives a custom intent specifying the character to display. In your Xcode project, you then define a custom SiriKit Intent Definition file. The intent definition can include the character’s details such as its name, avatar, strategic alliances, and so on.

![A screenshot showing a custom intent definition file configured with an](../../../attachments/cc1a99720381abca170a6ba17b6b24e6/IntentTimelineProvider-IntentDefinition@2x.png)

Xcode generates the following [INIntent](../intents/inintent.md) custom intent:

```swift
public class SelectCharacterIntent: INIntent {
    @NSManaged public var characterName: String?
    @NSManaged public var avatar: String?
    @NSManaged public var alliances: [String]?
    @NSManaged public var healthLevel: NSNumber?
}
```

Because users can add multiple instances of a particular widget, your provider needs a way to differentiate which instance WidgetKit is asking about. When WidgetKit calls [getSnapshot(for:in:completion:)](<intenttimelineprovider/getsnapshot(for_in_completion_).md>) or [getTimeline(for:in:completion:)](<intenttimelineprovider/gettimeline(for_in_completion_).md>), it passes an instance of your custom `INIntent`, configured with the user-selected details. The game widget provider accesses the properties of the intent and includes them in the [TimelineEntry](timelineentry.md). WidgetKit then invokes the widget configuration’s content closure, passing the timeline entry to allow the views to access the user-configured properties. For example, the provider might implement a `TimelineEntry` with properties corresponding to those in the custom intent:

```swift
struct CharacterDetailEntry: TimelineEntry {
    var date: Date
    var name: String?
    var avatar: String?
    var alliances: [String]?
    var healthLevel: Double?
}
```

To generate a snapshot, the game widget provider initializes the character detail entry using the properties from the intent.

```swift
struct CharacterDetailProvider: IntentTimelineProvider {
    func getSnapshot(for configuration: SelectCharacterIntent, in context: Context, completion: @escaping (CharacterDetailEntry) -> Void) {
        let entry = CharacterDetailEntry(
            date: Date(),
            name: configuration.characterName,
            avatar: configuration.avatar,
            alliances: configuration.alliances,
            healthLevel: configuration.healthLevel?.doubleValue
        )
        completion(entry)
    }
}
```

## Topics

### Generating Timelines

- [getSnapshot(for:in:completion:)](<intenttimelineprovider/getsnapshot(for_in_completion_).md>) — Provides a timeline entry representing the current time and state of a widget.
- [getTimeline(for:in:completion:)](<intenttimelineprovider/gettimeline(for_in_completion_).md>) — Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [placeholder(in:)](<intenttimelineprovider/placeholder(in_).md>) — Provides a timeline entry representing a placeholder version of the widget.
- [Entry](intenttimelineprovider/entry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [Intent](intenttimelineprovider/intent.md) — The intent that contains user-customized values.
- [recommendations()](<intenttimelineprovider/recommendations().md>) — Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [Context](intenttimelineprovider/context.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.

### Instance Methods

- [relevance()](<intenttimelineprovider/relevance().md>) — Provides an object containing attributes that describe when a specific widget is relevant.

## See Also

### Related Documentation

- [INIntent](../intents/inintent.md) — A request to fulfill in your app or Intents extension.

### Timeline updates

- [Keeping a widget up to date](keeping-a-widget-up-to-date.md) — Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [TimelineProvider](timelineprovider.md) — A type that advises WidgetKit when to update a widget’s display.
- [AppIntentTimelineProvider](appintenttimelineprovider.md) — A type that advises WidgetKit when to update a user-configurable widget’s display.
- [TimelineProviderContext](timelineprovidercontext.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [TimelineEntry](timelineentry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [Timeline](timeline.md) — An object that specifies a date for WidgetKit to update a widget’s view.
- [WidgetCenter](widgetcenter.md) — An object that contains a list of user-configured widgets and is used for reloading widget timelines.
