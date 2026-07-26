---
title: TimelineProvider.Context
framework: WidgetKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/timelineprovider/context
source_url: 'https://developer.apple.com/documentation/widgetkit/timelineprovider/context'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/timelineprovider/context.json'
content_hash: 'sha256:05ac1be518e5e75c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [TimelineProvider](../timelineprovider.md)

# TimelineProvider.Context

<sub>Type Alias</sub>

An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
typealias Context = TimelineProviderContext
```

## Discussion

For more information, see [TimelineProviderContext](../timelineprovidercontext.md).

## See Also

### Generating Timelines

- [getSnapshot(in:completion:)](<getsnapshot(in_completion_).md>) — Provides a timeline entry that represents the current time and state of a widget.
- [getTimeline(in:completion:)](<gettimeline(in_completion_).md>) — Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [placeholder(in:)](<placeholder(in_).md>) — Provides a timeline entry representing a placeholder version of the widget.
- [Entry](entry.md) — A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
