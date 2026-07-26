---
title: start
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sensoryfeedback/start
source_url: 'https://developer.apple.com/documentation/swiftui/sensoryfeedback/start'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sensoryfeedback/start.json'
content_hash: 'sha256:76e26086c2ad22d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SensoryFeedback](../sensoryfeedback.md)

# start

<sub>Type Property</sub>

Indicates that an activity started.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let start: SensoryFeedback
```

## Discussion

Use this haptic when starting a timer or any other activity that can be explicitly started and stopped.

Only plays feedback on watchOS.

## See Also

### Indicating start and stop

- [stop](stop.md) — Indicates that an activity stopped.
