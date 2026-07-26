---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/explicittimelineschedule/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/explicittimelineschedule/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/explicittimelineschedule/init%28_%3A%29.json'
content_hash: 'sha256:89960dd8e62f04a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ExplicitTimelineSchedule](../explicittimelineschedule.md)

# init(_:)

<sub>Initializer</sub>

Creates a schedule composed of an explicit sequence of dates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ dates: Entries)
```

## Parameters

- `dates` — The sequence of dates at which a timeline view updates. Use a monotonically increasing sequence of dates, and ensure that at least one is in the future.

## Discussion

Use the [entries(from:mode:)](<entries(from_mode_).md>) method to get the sequence of dates.
