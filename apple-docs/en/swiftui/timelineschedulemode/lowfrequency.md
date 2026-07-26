---
title: TimelineScheduleMode.lowFrequency
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/timelineschedulemode/lowfrequency
source_url: 'https://developer.apple.com/documentation/swiftui/timelineschedulemode/lowfrequency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineschedulemode/lowfrequency.json'
content_hash: 'sha256:21139af4cfeb5994'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TimelineScheduleMode](../timelineschedulemode.md)

# TimelineScheduleMode.lowFrequency

<sub>Case</sub>

A mode that produces schedule updates at a reduced rate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case lowFrequency
```

## Discussion

In this mode, the schedule should generate only “major” updates, if possible. For example, a timeline providing updates to a timer might restrict updates to once a minute while in this mode.

## See Also

### Getting timeline schedule modes

- [TimelineScheduleMode.normal](normal.md) — A mode that produces schedule updates at the schedule’s natural cadence.
