---
title: SensoryFeedback.Weight
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sensoryfeedback/weight
source_url: 'https://developer.apple.com/documentation/swiftui/sensoryfeedback/weight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sensoryfeedback/weight.json'
content_hash: 'sha256:a2b2e9c37dec25d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SensoryFeedback](../sensoryfeedback.md)

# SensoryFeedback.Weight

<sub>Structure</sub>

The weight to be represented by a type of feedback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Weight
```

## Overview

`Weight` values can be passed to `SensoryFeedback.impact(weight:intensity:)`.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting flexibility values

- [light](weight/light.md) — Indicates a collision between small or lightweight UI objects.
- [medium](weight/medium.md) — Indicates a collision between medium-sized or medium-weight UI objects.
- [heavy](weight/heavy.md) — Indicates a collision between large or heavyweight UI objects.

## See Also

### Producing a physical impact

- [impact](impact.md) — Provides a physical metaphor you can use to complement a visual experience.
- [impact(weight:intensity:)](<impact(weight_intensity_).md>) — Provides a physical metaphor you can use to complement a visual experience.
- [impact(flexibility:intensity:)](<impact(flexibility_intensity_).md>) — Provides a physical metaphor you can use to complement a visual experience.
- [Flexibility](flexibility.md) — The flexibility to be represented by a type of feedback.
