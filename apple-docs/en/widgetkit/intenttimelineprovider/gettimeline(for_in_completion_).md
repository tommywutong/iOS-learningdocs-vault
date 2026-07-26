---
title: 'getTimeline(for:in:completion:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/intenttimelineprovider/gettimeline(for:in:completion:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/intenttimelineprovider/gettimeline(for:in:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/intenttimelineprovider/gettimeline%28for%3Ain%3Acompletion%3A%29.json'
content_hash: 'sha256:ece4571c4574b5d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [IntentTimelineProvider](../intenttimelineprovider.md)

# getTimeline(for:in:completion:)

<sub>Instance Method</sub>

Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@preconcurrency func getTimeline(for configuration: Self.Intent, in context: Self.Context, completion: @escaping @Sendable (Timeline<Self.Entry>) -> Void)
```

## Parameters

- `configuration` — The intent containing user-customized values.

- `context` — An object describing the context to show the widget in.

- `completion` — The completion handler to call after you create the timeline.

## Discussion

The `configuration` parameter provides user-customized values, as defined in your custom intent definition.

## See Also

### Generating Timelines

- [getSnapshot(for:in:completion:)](<getsnapshot(for_in_completion_).md>) — Provides a timeline entry representing the current time and state of a widget.
- [placeholder(in:)](<placeholder(in_).md>) — Provides a timeline entry representing a placeholder version of the widget.
- [Entry](entry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [Intent](intent.md) — The intent that contains user-customized values.
- [recommendations()](<recommendations().md>) — Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [Context](context.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
