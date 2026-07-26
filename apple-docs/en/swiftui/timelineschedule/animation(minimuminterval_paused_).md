---
title: 'animation(minimumInterval:paused:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/timelineschedule/animation(minimuminterval:paused:)'
source_url: 'https://developer.apple.com/documentation/swiftui/timelineschedule/animation(minimuminterval:paused:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineschedule/animation%28minimuminterval%3Apaused%3A%29.json'
content_hash: 'sha256:40a503f18f3d61d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TimelineSchedule](../timelineschedule.md)

# animation(minimumInterval:paused:)

<sub>Type Method</sub>

A pausable schedule of dates updating at a frequency no more quickly than the provided interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func animation(minimumInterval: Double? = nil, paused: Bool = false) -> AnimationTimelineSchedule
```

## Parameters

- `minimumInterval` — The minimum interval to update the schedule at. Pass nil to let the system pick an appropriate update interval.

- `paused` — If the schedule should stop generating updates.

## See Also

### Getting built-in schedules

- [animation](animation.md) — A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [everyMinute](everyminute.md) — A schedule for updating a timeline view at the start of every minute.
- [explicit(_:)](<explicit(__).md>) — A schedule for updating a timeline view at explicit points in time.
- [periodic(from:by:)](<periodic(from_by_).md>) — A schedule for updating a timeline view at regular intervals.
