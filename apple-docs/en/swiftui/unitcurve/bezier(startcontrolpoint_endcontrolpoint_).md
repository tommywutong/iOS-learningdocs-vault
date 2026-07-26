---
title: 'bezier(startControlPoint:endControlPoint:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/unitcurve/bezier(startcontrolpoint:endcontrolpoint:)'
source_url: 'https://developer.apple.com/documentation/swiftui/unitcurve/bezier(startcontrolpoint:endcontrolpoint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitcurve/bezier%28startcontrolpoint%3Aendcontrolpoint%3A%29.json'
content_hash: 'sha256:148f88c849f26ca3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UnitCurve](../unitcurve.md)

# bezier(startControlPoint:endControlPoint:)

<sub>Type Method</sub>

Creates a new curve using bezier control points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func bezier(startControlPoint: UnitPoint, endControlPoint: UnitPoint) -> UnitCurve
```

## Parameters

- `startControlPoint` — The cubic Bézier control point associated with the curve’s start point at (0, 0). The tangent vector from the start point to its control point defines the initial velocity of the timing function.

- `endControlPoint` — The cubic Bézier control point associated with the curve’s end point at (1, 1). The tangent vector from the end point to its control point defines the final velocity of the timing function.

## Discussion

The x components of the control points are clamped to the range [0,1] when the curve is evaluated.
