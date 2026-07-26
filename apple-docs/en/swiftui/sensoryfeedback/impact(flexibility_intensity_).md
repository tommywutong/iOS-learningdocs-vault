---
title: 'impact(flexibility:intensity:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/sensoryfeedback/impact(flexibility:intensity:)'
source_url: 'https://developer.apple.com/documentation/swiftui/sensoryfeedback/impact(flexibility:intensity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sensoryfeedback/impact%28flexibility%3Aintensity%3A%29.json'
content_hash: 'sha256:a3601bc3be2403e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SensoryFeedback](../sensoryfeedback.md)

# impact(flexibility:intensity:)

<sub>Type Method</sub>

Provides a physical metaphor you can use to complement a visual experience.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func impact(flexibility: SensoryFeedback.Flexibility, intensity: Double = 1.0) -> SensoryFeedback
```

## Discussion

Use this to provide feedback for UI elements colliding. It should supplement the user experience, since only some platforms will play feedback in response to it.

Not all platforms will play different feedback for different flexibilities and intensities of impact.

Only plays feedback on iOS and watchOS.

## See Also

### Producing a physical impact

- [impact](impact.md) — Provides a physical metaphor you can use to complement a visual experience.
- [impact(weight:intensity:)](<impact(weight_intensity_).md>) — Provides a physical metaphor you can use to complement a visual experience.
- [Flexibility](flexibility.md) — The flexibility to be represented by a type of feedback.
- [Weight](weight.md) — The weight to be represented by a type of feedback.
