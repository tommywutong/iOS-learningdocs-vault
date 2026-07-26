---
title: 'periodic(from:by:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/timelineschedule/periodic(from:by:)'
source_url: 'https://developer.apple.com/documentation/swiftui/timelineschedule/periodic(from:by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineschedule/periodic%28from%3Aby%3A%29.json'
content_hash: 'sha256:023c06b45de9b140'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TimelineSchedule](../timelineschedule.md)

# periodic(from:by:)

<sub>Type Method</sub>

A schedule for updating a timeline view at regular intervals.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func periodic(from startDate: Date, by interval: TimeInterval) -> PeriodicTimelineSchedule
```

## Parameters

- `startDate` — The date on which to start the sequence.

- `interval` — The time interval between successive sequence entries.

## Discussion

Initialize a [TimelineView](../timelineview.md) with a periodic timeline schedule when you want to schedule timeline view updates periodically with a custom interval:

```swift
TimelineView(.periodic(from: startDate, by: 3.0)) { context in
    Text(context.date.description)
}
```

The timeline view updates its content at the start date, and then again at dates separated in time by the interval amount, which is every three seconds in the example above. For a start date in the past, the view updates immediately, providing as context the date corresponding to the most recent interval boundary. The view then refreshes normally at subsequent interval boundaries. For a start date in the future, the view updates once with the current date, and then begins regular updates at the start date.

The schedule defines the [Entries](../periodictimelineschedule/entries.md) structure to return the sequence of dates when the timeline view calls the [entries(from:mode:)](<../periodictimelineschedule/entries(from_mode_).md>) method.

## See Also

### Getting built-in schedules

- [animation](animation.md) — A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [animation(minimumInterval:paused:)](<animation(minimuminterval_paused_).md>) — A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [everyMinute](everyminute.md) — A schedule for updating a timeline view at the start of every minute.
- [explicit(_:)](<explicit(__).md>) — A schedule for updating a timeline view at explicit points in time.
