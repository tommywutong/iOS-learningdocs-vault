---
title: 'init(from:by:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/periodictimelineschedule/init(from:by:)'
source_url: 'https://developer.apple.com/documentation/swiftui/periodictimelineschedule/init(from:by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/periodictimelineschedule/init%28from%3Aby%3A%29.json'
content_hash: 'sha256:38b20a494c6a1f40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PeriodicTimelineSchedule](../periodictimelineschedule.md)

# init(from:by:)

<sub>Initializer</sub>

Creates a periodic update schedule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(from startDate: Date, by interval: TimeInterval)
```

## Parameters

- `startDate` — The date on which to start the sequence.

- `interval` — The time interval between successive sequence entries.

## Discussion

Use the [entries(from:mode:)](<entries(from_mode_).md>) method to get the sequence of dates.
