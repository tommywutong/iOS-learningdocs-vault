---
title: animation
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/timelineschedule/animation
source_url: 'https://developer.apple.com/documentation/swiftui/timelineschedule/animation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineschedule/animation.json'
content_hash: 'sha256:a549ff2b9d9473ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TimelineSchedule](../timelineschedule.md)

# animation

<sub>Type Property</sub>

A pausable schedule of dates updating at a frequency no more quickly than the provided interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var animation: AnimationTimelineSchedule { get }
```

## See Also

### Getting built-in schedules

- [animation(minimumInterval:paused:)](<animation(minimuminterval_paused_).md>) — A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [everyMinute](everyminute.md) — A schedule for updating a timeline view at the start of every minute.
- [explicit(_:)](<explicit(__).md>) — A schedule for updating a timeline view at explicit points in time.
- [periodic(from:by:)](<periodic(from_by_).md>) — A schedule for updating a timeline view at regular intervals.
