---
title: 'convert(_:to:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/physicalmetricsconverter/convert(_:to:)'
source_url: 'https://developer.apple.com/documentation/swiftui/physicalmetricsconverter/convert(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/physicalmetricsconverter/convert%28_%3Ato%3A%29.json'
content_hash: 'sha256:eec25d6c7b81c921'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PhysicalMetricsConverter](../physicalmetricsconverter.md)

# convert(_:to:)

<sub>Instance Method</sub>

Converts a point’s coordinates to physical length measurements in the specified unit.

<sub>visionOS</sub>

```swift
@MainActor @preconcurrency func convert(_ point: CGPoint, to unit: UnitLength) -> CGPoint
```

## Return Value

A point value with physical length measurements, in the given unit

## Discussion

The point is assumed to be in the coordinate system of the scene that this converter is associated with. If the scene is scaled, the physical measurement will take this scale into account.

## See Also

### Converting a unit length

- [convert(_:from:)](<convert(__from_).md>) — Converts a length in the specified unit to a length in points suitable for use in the environment this converter is associated with.
