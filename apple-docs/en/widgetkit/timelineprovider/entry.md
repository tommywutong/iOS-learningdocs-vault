---
title: Entry
framework: WidgetKit
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/timelineprovider/entry
source_url: 'https://developer.apple.com/documentation/widgetkit/timelineprovider/entry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/timelineprovider/entry.json'
content_hash: 'sha256:6642141849781b6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [TimelineProvider](../timelineprovider.md)

# Entry

<sub>Associated Type</sub>

A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
associatedtype Entry : TimelineEntry
```

## See Also

### Generating Timelines

- [getSnapshot(in:completion:)](<getsnapshot(in_completion_).md>) — Provides a timeline entry that represents the current time and state of a widget.
- [getTimeline(in:completion:)](<gettimeline(in_completion_).md>) — Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [placeholder(in:)](<placeholder(in_).md>) — Provides a timeline entry representing a placeholder version of the widget.
- [Context](context.md) — An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
