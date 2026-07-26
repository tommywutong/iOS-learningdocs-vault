---
title: relevance()
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 26.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/appintenttimelineprovider/relevance()
source_url: 'https://developer.apple.com/documentation/widgetkit/appintenttimelineprovider/relevance()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintenttimelineprovider/relevance%28%29.json'
content_hash: 'sha256:96d3262a0f2b7575'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AppIntentTimelineProvider](../appintenttimelineprovider.md)

# relevance()

<sub>Instance Method</sub>

Provides an object containing attributes that describe when a specific widget is relevant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func relevance() async -> WidgetRelevance<Self.Intent>
```

## Return Value

The object that contains attributes that describe when a specific widget is relevant.

## Discussion

The system can use the relevance to show this widget in the Smart Stack when the provided relevance matches a person’s context. For example, if you indicate relevance at a specific location, the system could show the widget when a person is at or close to the location.

By default, this method returns no relevances. Implement this requirement to tell the system that your widget is relevant.

> [!note] Note
> Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit API is only available in watchOS. Calling its API on other platforms doesn’t have any effect. For more information, refer to [Increasing the visibility of widgets in Smart Stacks](../widget-suggestions-in-smart-stacks.md).

## Default Implementations

### AppIntentTimelineProvider Implementations

- [relevance()](<relevance()-9vl5j.md>) — Provides an object containing attributes that describe when a specific widget is relevant.

## See Also

### Generating timelines

- [placeholder(in:)](<placeholder(in_).md>) — Provides a timeline entry representing a placeholder version of the widget.
- [recommendations()](<recommendations().md>) — Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [snapshot(for:in:)](<snapshot(for_in_).md>) — Provides a timeline entry representing the current time and state of a widget.
- [timeline(for:in:)](<timeline(for_in_).md>) — Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [Context](context.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [Entry](entry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [Intent](intent.md) — The intent that contains user-customized values.
