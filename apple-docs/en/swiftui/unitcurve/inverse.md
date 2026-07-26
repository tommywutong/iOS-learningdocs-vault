---
title: inverse
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/unitcurve/inverse
source_url: 'https://developer.apple.com/documentation/swiftui/unitcurve/inverse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitcurve/inverse.json'
content_hash: 'sha256:f23d64d7ba52727a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UnitCurve](../unitcurve.md)

# inverse

<sub>Instance Property</sub>

Returns a copy of the curve with its x and y components swapped.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var inverse: UnitCurve { get }
```

## Discussion

The inverse can be used to solve a curve in reverse: given a known output (y) value, the corresponding input (x) value can be found by using `inverse`:

```swift
let curve = UnitCurve.easeInOut

/// The input time for which an easeInOut curve returns 0.6.
let inputTime = curve.inverse.evaluate(at: 0.6)
```
