---
title: AppIntentTimelineProvider.Context
framework: WidgetKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/appintenttimelineprovider/context
source_url: 'https://developer.apple.com/documentation/widgetkit/appintenttimelineprovider/context'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/appintenttimelineprovider/context.json'
content_hash: 'sha256:88515495b2c60db0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [AppIntentTimelineProvider](../appintenttimelineprovider.md)

# AppIntentTimelineProvider.Context

<sub>Type Alias</sub>

An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
typealias Context = TimelineProviderContext
```

## Discussion

For more information, see [TimelineProviderContext](../timelineprovidercontext.md).

## See Also

### Generating timelines

- [placeholder(in:)](<placeholder(in_).md>) — Provides a timeline entry representing a placeholder version of the widget.
- [recommendations()](<recommendations().md>) — Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [relevance()](<relevance().md>) — Provides an object containing attributes that describe when a specific widget is relevant.
- [snapshot(for:in:)](<snapshot(for_in_).md>) — Provides a timeline entry representing the current time and state of a widget.
- [timeline(for:in:)](<timeline(for_in_).md>) — Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [Entry](entry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [Intent](intent.md) — The intent that contains user-customized values.
