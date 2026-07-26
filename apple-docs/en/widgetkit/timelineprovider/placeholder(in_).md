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
doc_path: '/documentation/widgetkit/timelineprovider/placeholder(in:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/timelineprovider/placeholder(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/timelineprovider/placeholder%28in%3A%29.json'
content_hash: 'sha256:5ea2d579289a5597'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [TimelineProvider](../timelineprovider.md)

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

In addition, WidgetKit may render your widget as a placeholder if users choose to hide sensitive information on Apple Watch or the iPhone Lock Screen. To learn more about redacting sensitive data, see [Creating a widget extension](../creating-a-widget-extension.md).

> [!important] Important
> `placeholder(in:)` is synchronous and returns a `TimelineEntry` immediately. Return from `placeholder(in:)` as quickly as possible.

## See Also

### Generating Timelines

- [getSnapshot(in:completion:)](<getsnapshot(in_completion_).md>) — Provides a timeline entry that represents the current time and state of a widget.
- [getTimeline(in:completion:)](<gettimeline(in_completion_).md>) — Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [Entry](entry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [Context](context.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
