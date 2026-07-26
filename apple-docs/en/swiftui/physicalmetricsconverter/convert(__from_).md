---
title: 'convert(_:from:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/physicalmetricsconverter/convert(_:from:)'
source_url: 'https://developer.apple.com/documentation/swiftui/physicalmetricsconverter/convert(_:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/physicalmetricsconverter/convert%28_%3Afrom%3A%29.json'
content_hash: 'sha256:9046080d0f116a1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PhysicalMetricsConverter](../physicalmetricsconverter.md)

# convert(_:from:)

<sub>Instance Method</sub>

Converts a length in the specified unit to a length in points suitable for use in the environment this converter is associated with.

<sub>visionOS</sub>

```swift
@MainActor @preconcurrency func convert(_ lengthValue: CGFloat, from unit: UnitLength) -> CGFloat
```

## Return Value

A value in points. Use this value only in the scene this converter was associated with.

## See Also

### Converting a unit length

- [convert(_:to:)](<convert(__to_).md>) — Converts a point’s coordinates to physical length measurements in the specified unit.
