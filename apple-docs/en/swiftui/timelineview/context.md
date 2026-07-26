---
title: TimelineView.Context
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/timelineview/context
source_url: 'https://developer.apple.com/documentation/swiftui/timelineview/context'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineview/context.json'
content_hash: 'sha256:c799157096d00d02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TimelineView](../timelineview.md)

# TimelineView.Context

<sub>Structure</sub>

Information passed to a timeline view’s content callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Context
```

## Overview

The context includes both the [date](context/date.md) from the schedule that triggered the callback, and a [cadence](context/cadence-swift.property.md) that you can use to customize the appearance of your view. For example, you might choose to display the second hand of an analog clock only when the cadence is [TimelineView.Context.Cadence.seconds](context/cadence-swift.enum/seconds.md) or faster.

## Topics

### Getting the date

- [date](context/date.md) — The date from the schedule that triggered the current view update.

### Getting the cadence

- [cadence](context/cadence-swift.property.md) — The rate at which the timeline updates the view.
- [Cadence](context/cadence-swift.enum.md) — A rate at which timeline views can receive updates.

### Invalidating the context

- [invalidateTimelineContent()](<context/invalidatetimelinecontent().md>) — Resets any pre-rendered views the system has from the timeline.

## See Also

### Creating a timeline

- [init(_:content:)](<init(__content_)-1mlmj.md>) — Creates a new timeline view that uses the given schedule.
