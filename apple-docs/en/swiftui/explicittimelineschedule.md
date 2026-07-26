---
title: ExplicitTimelineSchedule
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/explicittimelineschedule
source_url: 'https://developer.apple.com/documentation/swiftui/explicittimelineschedule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/explicittimelineschedule.json'
content_hash: 'sha256:a2dfa81fa52143f1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ExplicitTimelineSchedule

<sub>Structure</sub>

A schedule for updating a timeline view at explicit points in time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ExplicitTimelineSchedule<Entries> where Entries : Sequence, Entries.Element == Date
```

## Overview

You can also use [explicit(_:)](<timelineschedule/explicit(__).md>) to construct this schedule.

## Relationships

- **Conforms To**: [TimelineSchedule](timelineschedule.md)

## Topics

### Creating a schedule

- [init(_:)](<explicittimelineschedule/init(__).md>) — Creates a schedule composed of an explicit sequence of dates.

### Getting the sequence of dates

- [entries(from:mode:)](<explicittimelineschedule/entries(from_mode_).md>) — Provides the sequence of dates with which you initialized the schedule.

## See Also

### Supporting types

- [AnimationTimelineSchedule](animationtimelineschedule.md) — A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [EveryMinuteTimelineSchedule](everyminutetimelineschedule.md) — A schedule for updating a timeline view at the start of every minute.
- [PeriodicTimelineSchedule](periodictimelineschedule.md) — A schedule for updating a timeline view at regular intervals.
