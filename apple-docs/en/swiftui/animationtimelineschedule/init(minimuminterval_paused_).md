---
title: 'init(minimumInterval:paused:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animationtimelineschedule/init(minimuminterval:paused:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animationtimelineschedule/init(minimuminterval:paused:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animationtimelineschedule/init%28minimuminterval%3Apaused%3A%29.json'
content_hash: 'sha256:287cf30290a0e92e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnimationTimelineSchedule](../animationtimelineschedule.md)

# init(minimumInterval:paused:)

<sub>Initializer</sub>

Create a pausable schedule of dates updating at a frequency no more quickly than the provided interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(minimumInterval: Double? = nil, paused: Bool = false)
```

## Parameters

- `minimumInterval` — The minimum interval to update the schedule at. Pass nil to let the system pick an appropriate update interval.

- `paused` — If the schedule should stop generating updates.
