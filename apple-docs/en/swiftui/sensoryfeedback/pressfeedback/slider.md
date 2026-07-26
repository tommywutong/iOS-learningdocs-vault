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
doc_path: /documentation/swiftui/sensoryfeedback/pressfeedback/slider
source_url: 'https://developer.apple.com/documentation/swiftui/sensoryfeedback/pressfeedback/slider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sensoryfeedback/pressfeedback/slider.json'
content_hash: 'sha256:772283de52a9e93e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SensoryFeedback](../../sensoryfeedback.md) · [PressFeedback](../pressfeedback.md)

# slider

<sub>Type Property</sub>

Indicates that a slider’s thumb has been pressed (touch down).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let slider: SensoryFeedback.PressFeedback
```

## Discussion

Slider controls should also play [release(_:)](<../release(__).md>) with [slider](../releasefeedback/slider.md).

Only plays feedback on visionOS.
