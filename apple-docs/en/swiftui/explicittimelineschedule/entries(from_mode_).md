---
title: 'entries(from:mode:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/explicittimelineschedule/entries(from:mode:)'
source_url: 'https://developer.apple.com/documentation/swiftui/explicittimelineschedule/entries(from:mode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/explicittimelineschedule/entries%28from%3Amode%3A%29.json'
content_hash: 'sha256:9c7315a002ae9ffa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ExplicitTimelineSchedule](../explicittimelineschedule.md)

# entries(from:mode:)

<sub>Instance Method</sub>

Provides the sequence of dates with which you initialized the schedule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func entries(from startDate: Date, mode: TimelineScheduleMode) -> Entries
```

## Parameters

- `startDate` — The date from which the sequence begins. This particular implementation of the protocol method ignores the start date.

- `mode` — The mode for the update schedule. This particular implementation of the protocol method ignores the mode.

## Return Value

The sequence of dates that you provided at initialization.

## Discussion

A [TimelineView](../timelineview.md) that you create with a schedule calls this [TimelineSchedule](../timelineschedule.md) method to ask the schedule when to update its content. The explicit timeline schedule implementation of this method returns the unmodified sequence of dates that you provided when you created the schedule with [explicit(_:)](<../timelineschedule/explicit(__).md>). As a result, this particular implementation ignores the `startDate` and `mode` parameters.
