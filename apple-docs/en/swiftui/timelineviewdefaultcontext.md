---
title: TimelineViewDefaultContext
framework: SwiftUI
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/timelineviewdefaultcontext
source_url: 'https://developer.apple.com/documentation/swiftui/timelineviewdefaultcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineviewdefaultcontext.json'
content_hash: 'sha256:fea265be4a8e7e82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TimelineViewDefaultContext

<sub>Type Alias</sub>

Information passed to a timeline view’s content callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias TimelineViewDefaultContext = TimelineView<EveryMinuteTimelineSchedule, Never>.Context
```

## Discussion

The context includes both the date from the schedule that triggered the callback, and a cadence that you can use to customize the appearance of your view. For example, you might choose to display the second hand of an analog clock only when the cadence is [TimelineView.Context.Cadence.seconds](timelineview/context/cadence-swift.enum/seconds.md) or faster.

> [!note] Note
> This type alias uses a specific concrete instance of [Context](timelineview/context.md) that all timeline views can use. It does this to prevent introducing an unnecessary generic parameter dependency on the context type.

## See Also

### Updating a view on a schedule

- [Updating watchOS apps with timelines](../watchos-apps/updating-watchos-apps-with-timelines.md) — Seamlessly schedule updates to your user interface, even while it’s inactive.
- [TimelineView](timelineview.md) — A view that updates according to a schedule that you provide.
- [TimelineSchedule](timelineschedule.md) — A type that provides a sequence of dates for use as a schedule.
