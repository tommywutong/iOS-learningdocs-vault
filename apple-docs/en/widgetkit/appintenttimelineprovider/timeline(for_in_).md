---
title: 'timeline(for:in:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/appintenttimelineprovider/timeline(for:in:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/appintenttimelineprovider/timeline(for:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintenttimelineprovider/timeline%28for%3Ain%3A%29.json'
content_hash: 'sha256:e3c853d6eb95679b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AppIntentTimelineProvider](../appintenttimelineprovider.md)

# timeline(for:in:)

<sub>Instance Method</sub>

Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func timeline(for configuration: Self.Intent, in context: Self.Context) async -> Timeline<Self.Entry>
```

## Parameters

- `configuration` — The intent containing user-customized values.

- `context` — An object describing the context to show the widget in.

## Return Value

An array of timeline entries for the current time and, optionally, any future times to update a widget.

## Discussion

The `configuration` parameter provides user-customized values, as defined in your custom intent.

## See Also

### Generating timelines

- [placeholder(in:)](<placeholder(in_).md>) — Provides a timeline entry representing a placeholder version of the widget.
- [recommendations()](<recommendations().md>) — Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [relevance()](<relevance().md>) — Provides an object containing attributes that describe when a specific widget is relevant.
- [snapshot(for:in:)](<snapshot(for_in_).md>) — Provides a timeline entry representing the current time and state of a widget.
- [Context](context.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [Entry](entry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [Intent](intent.md) — The intent that contains user-customized values.
