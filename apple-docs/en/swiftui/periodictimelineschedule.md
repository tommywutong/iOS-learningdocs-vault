---
title: PeriodicTimelineSchedule
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/periodictimelineschedule
source_url: 'https://developer.apple.com/documentation/swiftui/periodictimelineschedule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/periodictimelineschedule.json'
content_hash: 'sha256:b9cd62f1f9cb0dc5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PeriodicTimelineSchedule

<sub>Structure</sub>

A schedule for updating a timeline view at regular intervals.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PeriodicTimelineSchedule
```

## Overview

You can also use [periodic(from:by:)](<timelineschedule/periodic(from_by_).md>) to construct this schedule.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [TimelineSchedule](timelineschedule.md)

## Topics

### Creating a schedule

- [init(from:by:)](<periodictimelineschedule/init(from_by_).md>) — Creates a periodic update schedule.

### Getting the sequence of dates

- [entries(from:mode:)](<periodictimelineschedule/entries(from_mode_).md>) — Provides a sequence of periodic dates starting from around a given date.
- [Entries](periodictimelineschedule/entries.md) — The sequence of dates in periodic schedule.

## See Also

### Supporting types

- [AnimationTimelineSchedule](animationtimelineschedule.md) — A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [EveryMinuteTimelineSchedule](everyminutetimelineschedule.md) — A schedule for updating a timeline view at the start of every minute.
- [ExplicitTimelineSchedule](explicittimelineschedule.md) — A schedule for updating a timeline view at explicit points in time.
