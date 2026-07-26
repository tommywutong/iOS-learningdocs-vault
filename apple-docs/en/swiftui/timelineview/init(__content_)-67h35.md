---
title: 'init(_:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/timelineview/init(_:content:)-67h35'
source_url: 'https://developer.apple.com/documentation/swiftui/timelineview/init(_:content:)-67h35'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineview/init%28_%3Acontent%3A%29-67h35.json'
content_hash: 'sha256:6a28e812198b994e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TimelineView](../timelineview.md)

# init(_:content:)

<sub>Initializer</sub>

Creates a new timeline view that uses the given schedule.

> [!warning] Deprecated
> Use [init(_:content:)](<init(__content_)-1mlmj.md>) instead. The replacement initializer’s `context` closure takes a [TimelineViewDefaultContext](../timelineviewdefaultcontext.md) as its input rather than a [Context](context.md) to prevent introducing an unnecessary generic parameter dependency on the context type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ schedule: Schedule, @ContentBuilder content: @escaping (TimelineView<Schedule, Content>.Context) -> Content)
```

## Parameters

- `schedule` — A schedule that produces a sequence of dates that indicate the instances when the view should update. Use a type that conforms to [TimelineSchedule](../timelineschedule.md), like [everyMinute](../timelineschedule/everyminute.md), or a custom timeline schedule that you define.

- `content` — A closure that generates view content at the moments indicated by the schedule. The closure takes an input of type [Context](context.md) that includes the date from the schedule that prompted the update, as well as a [Cadence](context/cadence-swift.enum.md) value that the view can use to customize its appearance.
