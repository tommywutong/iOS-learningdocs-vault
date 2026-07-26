---
title: invalidateTimelineContent()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/timelineview/context/invalidatetimelinecontent()
source_url: 'https://developer.apple.com/documentation/swiftui/timelineview/context/invalidatetimelinecontent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timelineview/context/invalidatetimelinecontent%28%29.json'
content_hash: 'sha256:39ebb6dda418fdcb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [TimelineView](../../timelineview.md) · [Context](../context.md)

# invalidateTimelineContent()

<sub>Instance Method</sub>

Resets any pre-rendered views the system has from the timeline.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
func invalidateTimelineContent()
```

## Discussion

When entering Always On Display, the system might pre-render frames. If the content of these frames must change in a way that isn’t reflected by the schedule or the timeline view’s current bindings — for example, because the user changes the title of a future calendar event — call this method to request that the frames be regenerated.
