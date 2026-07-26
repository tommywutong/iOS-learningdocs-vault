---
title: 'explicit(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/timelineschedule/explicit(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/timelineschedule/explicit(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineschedule/explicit%28_%3A%29.json'
content_hash: 'sha256:535ba81610502fd5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TimelineSchedule](../timelineschedule.md)

# explicit(_:)

<sub>Type Method</sub>

A schedule for updating a timeline view at explicit points in time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func explicit<S>(_ dates: S) -> ExplicitTimelineSchedule<S> where Self == ExplicitTimelineSchedule<S>, S : Sequence, S.Element == Date
```

## Parameters

- `dates` — The sequence of dates at which a timeline view updates. Use a monotonically increasing sequence of dates, and ensure that at least one is in the future.

## Discussion

Initialize a [TimelineView](../timelineview.md) with an explicit timeline schedule when you want to schedule view updates at particular points in time:

```swift
let dates = [
    Date(timeIntervalSinceNow: 10), // Update ten seconds from now,
    Date(timeIntervalSinceNow: 12) // and a few seconds later.
]

struct MyView: View {
    var body: some View {
        TimelineView(.explicit(dates)) { context in
            Text(context.date.description)
        }
    }
}
```

The timeline view updates its content on exactly the dates that you specify, until it runs out of dates, after which it stops changing. If the dates you provide are in the past, the timeline view updates exactly once with the last entry. If you only provide dates in the future, the timeline view renders with the current date until the first date arrives. If you provide one or more dates in the past and one or more in the future, the view renders the most recent past date, refreshing normally on all subsequent dates.

## See Also

### Getting built-in schedules

- [animation](animation.md) — A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [animation(minimumInterval:paused:)](<animation(minimuminterval_paused_).md>) — A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [everyMinute](everyminute.md) — A schedule for updating a timeline view at the start of every minute.
- [periodic(from:by:)](<periodic(from_by_).md>) — A schedule for updating a timeline view at regular intervals.
