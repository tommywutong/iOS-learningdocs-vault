---
title: EveryMinuteTimelineSchedule
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/everyminutetimelineschedule
source_url: 'https://developer.apple.com/documentation/swiftui/everyminutetimelineschedule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/everyminutetimelineschedule.json'
content_hash: 'sha256:16885d83d2ca4803'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EveryMinuteTimelineSchedule

<sub>Structure</sub>

A schedule for updating a timeline view at the start of every minute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct EveryMinuteTimelineSchedule
```

## Overview

You can also use [everyMinute](timelineschedule/everyminute.md) to construct this schedule.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [TimelineSchedule](timelineschedule.md)

## Topics

### Creating a schedule

- [init()](<everyminutetimelineschedule/init().md>) — Creates a per-minute update schedule.

### Getting the sequence of dates

- [entries(from:mode:)](<everyminutetimelineschedule/entries(from_mode_).md>) — Provides a sequence of per-minute dates starting from a given date.
- [Entries](everyminutetimelineschedule/entries.md) — The sequence of dates in an every minute schedule.

## See Also

### Supporting types

- [AnimationTimelineSchedule](animationtimelineschedule.md) — A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [ExplicitTimelineSchedule](explicittimelineschedule.md) — A schedule for updating a timeline view at explicit points in time.
- [PeriodicTimelineSchedule](periodictimelineschedule.md) — A schedule for updating a timeline view at regular intervals.
