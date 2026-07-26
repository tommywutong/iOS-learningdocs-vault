---
title: 'placeholder(in:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/intenttimelineprovider/placeholder(in:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/intenttimelineprovider/placeholder(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/intenttimelineprovider/placeholder%28in%3A%29.json'
content_hash: 'sha256:8adaa6f519e078b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [IntentTimelineProvider](../intenttimelineprovider.md)

# placeholder(in:)

<sub>Instance Method</sub>

Provides a timeline entry representing a placeholder version of the widget.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func placeholder(in context: Self.Context) -> Self.Entry
```

## Parameters

- `context` — An object that describes the context in which to show the widget.

## Return Value

A timeline entry that represents a placeholder version of the widget.

## Discussion

When WidgetKit displays your widget for the first time, it renders the widget’s view as a placeholder. A placeholder view displays a generic representation of your widget, giving the user a general idea of what the widget shows. WidgetKit calls `placeholder(in:)` to request an entry representing the widget’s placeholder configuration. For example, the  [Emoji Rangers: Supporting Live Activities, interactivity, and animations](../emoji-rangers-supporting-live-activities-interactivity-and-animations.md) sample code project implements this method for its leaderboard widget as follows:

```swift
struct LeaderboardProvider: TimelineProvider {

    public typealias Entry = LeaderboardEntry

    func placeholder(in context: Context) -> LeaderboardEntry {
        return LeaderboardEntry(date: Date(), heros: EmojiRanger.availableHeros)
    }
}
```

In addition, WidgetKit may render your widget as a placeholder if user’s choose to hide sensitive information on Apple Watch or the iPhone Lock Screen. To learn more about redacting sensitive data, see [Creating a widget extension](../creating-a-widget-extension.md).

> [!important] Important
> `placeholder(in:)` is synchronous and returns a `TimelineEntry` immediately. Return from `placeholder(in:)` as quickly as possible.

## See Also

### Generating Timelines

- [getSnapshot(for:in:completion:)](<getsnapshot(for_in_completion_).md>) — Provides a timeline entry representing the current time and state of a widget.
- [getTimeline(for:in:completion:)](<gettimeline(for_in_completion_).md>) — Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [Entry](entry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [Intent](intent.md) — The intent that contains user-customized values.
- [recommendations()](<recommendations().md>) — Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [Context](context.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
