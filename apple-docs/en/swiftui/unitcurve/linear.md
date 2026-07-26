---
title: linear
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/unitcurve/linear
source_url: 'https://developer.apple.com/documentation/swiftui/unitcurve/linear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitcurve/linear.json'
content_hash: 'sha256:28329954c0e60a3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UnitCurve](../unitcurve.md)

# linear

<sub>Type Property</sub>

A linear curve.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let linear: UnitCurve
```

## Discussion

As the linear curve is a straight line from (0, 0) to (1, 1), the output progress is always equal to the input progress, and the velocity is always equal to 1.0.
