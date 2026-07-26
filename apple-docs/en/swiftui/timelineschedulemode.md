---
title: TimelineScheduleMode
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/timelineschedulemode
source_url: 'https://developer.apple.com/documentation/swiftui/timelineschedulemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineschedulemode.json'
content_hash: 'sha256:54f0d6ebd3bcd7ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TimelineScheduleMode

<sub>Enumeration</sub>

A mode of operation for timeline schedule updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum TimelineScheduleMode
```

## Overview

A [TimelineView](timelineview.md) provides a mode when calling its schedule’s [entries(from:mode:)](<timelineschedule/entries(from_mode_).md>) method. The view chooses a mode based on the state of the system. For example, a watchOS view might request a lower frequency of updates, using the [TimelineScheduleMode.lowFrequency](timelineschedulemode/lowfrequency.md) mode, when the user lowers their wrist.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting timeline schedule modes

- [TimelineScheduleMode.normal](timelineschedulemode/normal.md) — A mode that produces schedule updates at the schedule’s natural cadence.
- [TimelineScheduleMode.lowFrequency](timelineschedulemode/lowfrequency.md) — A mode that produces schedule updates at a reduced rate.

## See Also

### Specifying a mode

- [Mode](timelineschedule/mode.md) — An alias for the timeline schedule update mode.
