---
title: date
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/timelineview/context/date
source_url: 'https://developer.apple.com/documentation/swiftui/timelineview/context/date'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineview/context/date.json'
content_hash: 'sha256:53ec20987f552bf5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [TimelineView](../../timelineview.md) · [Context](../context.md)

# date

<sub>Instance Property</sub>

The date from the schedule that triggered the current view update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let date: Date
```

## Discussion

The first time a [TimelineView](../../timelineview.md) closure receives this date, it might be in the past. For example, if you create an [everyMinute](../../timelineschedule/everyminute.md) schedule at `10:09:55`, the schedule creates entries `10:09:00`, `10:10:00`, `10:11:00`, and so on. In response, the timeline view performs an initial update immediately, at `10:09:55`, but the context contains the `10:09:00` date entry. Subsequent entries arrive at their corresponding times.
