---
title: 'init(entries:policy:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/timeline/init(entries:policy:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/timeline/init(entries:policy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/timeline/init%28entries%3Apolicy%3A%29.json'
content_hash: 'sha256:67372048650cd2c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [Timeline](../timeline.md)

# init(entries:policy:)

<sub>Initializer</sub>

Creates a timeline for when you want WidgetKit to update a widget’s view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(entries: [EntryType], policy: TimelineReloadPolicy)
```

## Parameters

- `entries` — An array of timeline entries.

- `policy` — The policy that determines the earliest date and time WidgetKit requests a new timeline from a timeline provider.

## Discussion

Set the date and time of the first entry in a timeline to the current date and time. Add entries for future dates and times when you want WidgetKit to update the widget’s view. Note that the widget’s view might not be updated precisely at a timeline entry’s date and time; the update might occur later.
