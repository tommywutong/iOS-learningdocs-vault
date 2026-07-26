---
title: 'entries(from:mode:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animationtimelineschedule/entries(from:mode:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animationtimelineschedule/entries(from:mode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animationtimelineschedule/entries%28from%3Amode%3A%29.json'
content_hash: 'sha256:b0112a8b44363cb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnimationTimelineSchedule](../animationtimelineschedule.md)

# entries(from:mode:)

<sub>Instance Method</sub>

Returns entries at the frequency of the animation schedule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func entries(from start: Date, mode: TimelineScheduleMode) -> AnimationTimelineSchedule.Entries
```

## Discussion

When in `.lowFrequency` mode, return no entries, effectively pausing the animation.
