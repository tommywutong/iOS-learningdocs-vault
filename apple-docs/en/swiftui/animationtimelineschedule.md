---
title: AnimationTimelineSchedule
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animationtimelineschedule
source_url: 'https://developer.apple.com/documentation/swiftui/animationtimelineschedule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animationtimelineschedule.json'
content_hash: 'sha256:f85c0a32e2e5930e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnimationTimelineSchedule

<sub>Structure</sub>

A pausable schedule of dates updating at a frequency no more quickly than the provided interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AnimationTimelineSchedule
```

## Overview

You can also use [animation(minimumInterval:paused:)](<timelineschedule/animation(minimuminterval_paused_).md>) to construct this schedule.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [TimelineSchedule](timelineschedule.md)

## Topics

### Creating a schedule

- [init(minimumInterval:paused:)](<animationtimelineschedule/init(minimuminterval_paused_).md>) — Create a pausable schedule of dates updating at a frequency no more quickly than the provided interval.

### Getting the sequence of dates

- [entries(from:mode:)](<animationtimelineschedule/entries(from_mode_).md>) — Returns entries at the frequency of the animation schedule.

## See Also

### Supporting types

- [EveryMinuteTimelineSchedule](everyminutetimelineschedule.md) — A schedule for updating a timeline view at the start of every minute.
- [ExplicitTimelineSchedule](explicittimelineschedule.md) — A schedule for updating a timeline view at explicit points in time.
- [PeriodicTimelineSchedule](periodictimelineschedule.md) — A schedule for updating a timeline view at regular intervals.
