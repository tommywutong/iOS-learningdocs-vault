---
title: 'placeholder(in:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/appintenttimelineprovider/placeholder(in:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/appintenttimelineprovider/placeholder(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintenttimelineprovider/placeholder%28in%3A%29.json'
content_hash: 'sha256:c225e399abaeacf7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AppIntentTimelineProvider](../appintenttimelineprovider.md)

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

When WidgetKit displays your widget for the first time, it renders the widget’s view as a placeholder. A placeholder view displays a generic representation of your widget, giving the user a general idea of what the widget shows. WidgetKit calls `placeholder(in:)` to request an entry representing the widget’s placeholder configuration. For example, the game status widget would implement this method as follows:

```swift
struct GameStatusProvider: TimelineProvider {
    func placeholder(in context: Context) -> SimpleEntry {
       GameStatusEntry(date: Date(), gameStatus: "—")
    }
}
```

In addition, WidgetKit may render your widget as a placeholder if user’s choose to hide sensitive information on Apple Watch or the iPhone Lock Screen. To learn more about redacting sensitive data, see [Creating a widget extension](../creating-a-widget-extension.md).

> [!important] Important
> `placeholder(in:)` is synchronous and returns a `TimelineEntry` immediately. Return from `placeholder(in:)` as quickly as possible.

## See Also

### Generating timelines

- [recommendations()](<recommendations().md>) — Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [relevance()](<relevance().md>) — Provides an object containing attributes that describe when a specific widget is relevant.
- [snapshot(for:in:)](<snapshot(for_in_).md>) — Provides a timeline entry representing the current time and state of a widget.
- [timeline(for:in:)](<timeline(for_in_).md>) — Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [Context](context.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [Entry](entry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [Intent](intent.md) — The intent that contains user-customized values.
