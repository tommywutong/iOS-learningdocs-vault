---
title: slider
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sensoryfeedback/releasefeedback/slider
source_url: 'https://developer.apple.com/documentation/swiftui/sensoryfeedback/releasefeedback/slider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sensoryfeedback/releasefeedback/slider.json'
content_hash: 'sha256:37d6e40fa71c772e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SensoryFeedback](../../sensoryfeedback.md) · [ReleaseFeedback](../releasefeedback.md)

# slider

<sub>Type Property</sub>

Indicates that a slider’s thumb has been released (touch up).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let slider: SensoryFeedback.ReleaseFeedback
```

## Discussion

Slider controls should also play [press(_:)](<../press(__).md>) with [slider](../pressfeedback/slider.md).

Only plays feedback on visionOS.
