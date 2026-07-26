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
doc_path: '/documentation/swiftui/everyminutetimelineschedule/entries(from:mode:)'
source_url: 'https://developer.apple.com/documentation/swiftui/everyminutetimelineschedule/entries(from:mode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/everyminutetimelineschedule/entries%28from%3Amode%3A%29.json'
content_hash: 'sha256:e35b59a2e3d4d447'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EveryMinuteTimelineSchedule](../everyminutetimelineschedule.md)

# entries(from:mode:)

<sub>Instance Method</sub>

Provides a sequence of per-minute dates starting from a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func entries(from startDate: Date, mode: TimelineScheduleMode) -> EveryMinuteTimelineSchedule.Entries
```

## Parameters

- `startDate` — The date from which the sequence begins.

- `mode` — The mode for the update schedule.

## Return Value

A sequence of per-minute dates in ascending order.

## Discussion

A [TimelineView](../timelineview.md) that you create with an every minute schedule calls this method to ask the schedule when to update its content. The method returns a sequence of per-minute dates in increasing order, from earliest to latest, that represents when the timeline view updates.

For a `startDate` that’s exactly minute-aligned, the schedule’s sequence of dates starts at that time. Otherwise, it starts at the beginning of the specified minute. For example, for start dates of both `10:09:32` and `10:09:00`, the first entry in the sequence is `10:09:00`.

## See Also

### Getting the sequence of dates

- [Entries](entries.md) — The sequence of dates in an every minute schedule.
