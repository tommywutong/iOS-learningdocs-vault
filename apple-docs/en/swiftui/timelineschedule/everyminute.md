---
title: everyMinute
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/timelineschedule/everyminute
source_url: 'https://developer.apple.com/documentation/swiftui/timelineschedule/everyminute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineschedule/everyminute.json'
content_hash: 'sha256:80c56d256d94003a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TimelineSchedule](../timelineschedule.md)

# everyMinute

<sub>Type Property</sub>

A schedule for updating a timeline view at the start of every minute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var everyMinute: EveryMinuteTimelineSchedule { get }
```

## Discussion

Initialize a [TimelineView](../timelineview.md) with an every minute timeline schedule when you want to schedule timeline view updates at the start of every minute:

```swift
TimelineView(.everyMinute) { context in
    Text(context.date.description)
}
```

The schedule provides the first date as the beginning of the minute in which you use it to initialize the timeline view. For example, if you create the timeline view at `10:09:38`, the schedule’s first entry is `10:09:00`. In response, the timeline view performs its first update immediately, providing the beginning of the current minute, namely `10:09:00`, as context to its content. Subsequent updates happen at the beginning of each minute that follows.

The schedule defines the [Entries](../everyminutetimelineschedule/entries.md) structure to return the sequence of dates when the timeline view calls the [entries(from:mode:)](<../everyminutetimelineschedule/entries(from_mode_).md>) method.

## See Also

### Getting built-in schedules

- [animation](animation.md) — A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [animation(minimumInterval:paused:)](<animation(minimuminterval_paused_).md>) — A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [explicit(_:)](<explicit(__).md>) — A schedule for updating a timeline view at explicit points in time.
- [periodic(from:by:)](<periodic(from_by_).md>) — A schedule for updating a timeline view at regular intervals.
