---
title: 'greedy(priority:minimumSpacing:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/axisvaluelabelcollisionresolution/greedy(priority:minimumspacing:)'
source_url: 'https://developer.apple.com/documentation/charts/axisvaluelabelcollisionresolution/greedy(priority:minimumspacing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axisvaluelabelcollisionresolution/greedy%28priority%3Aminimumspacing%3A%29.json'
content_hash: 'sha256:f7411cc7aee15dc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AxisValueLabelCollisionResolution](../axisvaluelabelcollisionresolution.md)

# greedy(priority:minimumSpacing:)

<sub>Type Method</sub>

Use a greedy algorithm. Display a label if it’s not overlapping with other labels.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func greedy(priority: Double = 0, minimumSpacing: CGFloat? = nil) -> AxisValueLabelCollisionResolution
```

## Parameters

- `priority` — The priority of the label. A label with higher priority will get placed first by the greedy algorithm.

- `minimumSpacing` — The minimum spacing between the label and its adjacent labels.
