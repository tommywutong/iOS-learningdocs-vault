---
title: AnnotationOverflowResolution.Strategy
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/annotationoverflowresolution/strategy
source_url: 'https://developer.apple.com/documentation/charts/annotationoverflowresolution/strategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/annotationoverflowresolution/strategy.json'
content_hash: 'sha256:ed41f1a8288ebde7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AnnotationOverflowResolution](../annotationoverflowresolution.md)

# AnnotationOverflowResolution.Strategy

<sub>Structure</sub>

Strategies for annotation overflow resolution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Strategy
```

## Topics

### Type Properties

- [automatic](strategy/automatic.md) — Automatically chooses a overflow resolution.
- [disabled](strategy/disabled.md) — Places the annotation “as-is”.
- [fit](strategy/fit.md) — Fits the annotation automatically, adjusting its position to ensure it doesn’t overflow.
- [padScale](strategy/padscale.md) — Pads the scale of the chart to make space for the annotation.

### Type Methods

- [fit(to:)](<strategy/fit(to_).md>) — Fits the annotation to the given boundary, adjusting its position to ensure it doesn’t overflow.
