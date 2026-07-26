---
title: Intent
framework: WidgetKit
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/intenttimelineprovider/intent
source_url: 'https://developer.apple.com/documentation/widgetkit/intenttimelineprovider/intent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/intenttimelineprovider/intent.json'
content_hash: 'sha256:3c0e0002a43c8b53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [IntentTimelineProvider](../intenttimelineprovider.md)

# Intent

<sub>Associated Type</sub>

The intent that contains user-customized values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
associatedtype Intent : INIntent
```

## See Also

### Generating Timelines

- [getSnapshot(for:in:completion:)](<getsnapshot(for_in_completion_).md>) — Provides a timeline entry representing the current time and state of a widget.
- [getTimeline(for:in:completion:)](<gettimeline(for_in_completion_).md>) — Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [placeholder(in:)](<placeholder(in_).md>) — Provides a timeline entry representing a placeholder version of the widget.
- [Entry](entry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [recommendations()](<recommendations().md>) — Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [Context](context.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
