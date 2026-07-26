---
title: SensoryFeedback.Flexibility
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sensoryfeedback/flexibility
source_url: 'https://developer.apple.com/documentation/swiftui/sensoryfeedback/flexibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sensoryfeedback/flexibility.json'
content_hash: 'sha256:e2e78df6e1fa4479'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SensoryFeedback](../sensoryfeedback.md)

# SensoryFeedback.Flexibility

<sub>Structure</sub>

The flexibility to be represented by a type of feedback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Flexibility
```

## Overview

`Flexibility` values can be passed to `SensoryFeedback.impact(flexibility:intensity:)`.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting flexibility values

- [rigid](flexibility/rigid.md) — Indicates a collision between hard or inflexible UI objects.
- [soft](flexibility/soft.md) — Indicates a collision between soft or flexible UI objects.
- [solid](flexibility/solid.md) — Indicates a collision between solid UI objects of medium flexibility.

## See Also

### Producing a physical impact

- [impact](impact.md) — Provides a physical metaphor you can use to complement a visual experience.
- [impact(weight:intensity:)](<impact(weight_intensity_).md>) — Provides a physical metaphor you can use to complement a visual experience.
- [impact(flexibility:intensity:)](<impact(flexibility_intensity_).md>) — Provides a physical metaphor you can use to complement a visual experience.
- [Weight](weight.md) — The weight to be represented by a type of feedback.
