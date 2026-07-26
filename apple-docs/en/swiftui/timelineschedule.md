---
title: TimelineSchedule
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/timelineschedule
source_url: 'https://developer.apple.com/documentation/swiftui/timelineschedule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineschedule.json'
content_hash: 'sha256:2c4a1c69308fe7ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TimelineSchedule

<sub>Protocol</sub>

A type that provides a sequence of dates for use as a schedule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol TimelineSchedule
```

## Overview

Types that conform to this protocol implement a particular kind of schedule by defining an [entries(from:mode:)](<timelineschedule/entries(from_mode_).md>) method that returns a sequence of dates. Use a timeline schedule type when you initialize a [TimelineView](timelineview.md). For example, you can create a timeline view that updates every second, starting from some `startDate`, using a periodic schedule returned by [periodic(from:by:)](<timelineschedule/periodic(from_by_).md>):

```swift
TimelineView(.periodic(from: startDate, by: 1.0)) { context in
    // View content goes here.
}
```

You can also create custom timeline schedules. The timeline view updates its content according to the sequence of dates produced by the schedule.

## Relationships

- **Conforming Types**: [AnimationTimelineSchedule](animationtimelineschedule.md), [EveryMinuteTimelineSchedule](everyminutetimelineschedule.md), [ExplicitTimelineSchedule](explicittimelineschedule.md), [PeriodicTimelineSchedule](periodictimelineschedule.md)

## Topics

### Getting built-in schedules

- [animation](timelineschedule/animation.md) — A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [animation(minimumInterval:paused:)](<timelineschedule/animation(minimuminterval_paused_).md>) — A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [everyMinute](timelineschedule/everyminute.md) — A schedule for updating a timeline view at the start of every minute.
- [explicit(_:)](<timelineschedule/explicit(__).md>) — A schedule for updating a timeline view at explicit points in time.
- [periodic(from:by:)](<timelineschedule/periodic(from_by_).md>) — A schedule for updating a timeline view at regular intervals.

### Getting a sequence of dates

- [entries(from:mode:)](<timelineschedule/entries(from_mode_).md>) — Provides a sequence of dates starting around a given date.
- [Entries](timelineschedule/entries.md) — The sequence of dates within a schedule.

### Specifying a mode

- [Mode](timelineschedule/mode.md) — An alias for the timeline schedule update mode.
- [TimelineScheduleMode](timelineschedulemode.md) — A mode of operation for timeline schedule updates.

### Supporting types

- [AnimationTimelineSchedule](animationtimelineschedule.md) — A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [EveryMinuteTimelineSchedule](everyminutetimelineschedule.md) — A schedule for updating a timeline view at the start of every minute.
- [ExplicitTimelineSchedule](explicittimelineschedule.md) — A schedule for updating a timeline view at explicit points in time.
- [PeriodicTimelineSchedule](periodictimelineschedule.md) — A schedule for updating a timeline view at regular intervals.

## See Also

### Updating a view on a schedule

- [Updating watchOS apps with timelines](../watchos-apps/updating-watchos-apps-with-timelines.md) — Seamlessly schedule updates to your user interface, even while it’s inactive.
- [TimelineView](timelineview.md) — A view that updates according to a schedule that you provide.
- [TimelineViewDefaultContext](timelineviewdefaultcontext.md) — Information passed to a timeline view’s content callback.
