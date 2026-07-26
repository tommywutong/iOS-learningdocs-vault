---
title: 'init(_:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/timelineview/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/timelineview/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineview/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:a75868995b6624ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TimelineView](../timelineview.md)

# init(_:content:)

<sub>Initializer</sub>

Creates a new timeline view that uses the given schedule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ schedule: Schedule, @ContentBuilder content: @escaping (TimelineViewDefaultContext) -> Content)
```

## Parameters

- `schedule` — A schedule that produces a sequence of dates that indicate the instances when the view should update. Use a type that conforms to [TimelineSchedule](../timelineschedule.md), like [everyMinute](../timelineschedule/everyminute.md), or a custom timeline schedule that you define.

- `content` — A closure that generates view content at the moments indicated by the schedule. The closure takes an input of type [TimelineViewDefaultContext](../timelineviewdefaultcontext.md) that includes the date from the schedule that prompted the update, as well as a [Cadence](context/cadence-swift.enum.md) value that the view can use to customize its appearance.
