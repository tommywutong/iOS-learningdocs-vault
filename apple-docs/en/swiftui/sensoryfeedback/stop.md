---
title: stop
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sensoryfeedback/stop
source_url: 'https://developer.apple.com/documentation/swiftui/sensoryfeedback/stop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sensoryfeedback/stop.json'
content_hash: 'sha256:76fc59022b1ef551'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SensoryFeedback](../sensoryfeedback.md)

# stop

<sub>Type Property</sub>

Indicates that an activity stopped.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let stop: SensoryFeedback
```

## Discussion

Use this haptic when stopping a timer or other activity that was previously started.

Only plays feedback on watchOS.

## See Also

### Indicating start and stop

- [start](start.md) — Indicates that an activity started.
