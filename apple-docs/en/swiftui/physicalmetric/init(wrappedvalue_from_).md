---
title: 'init(wrappedValue:from:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/physicalmetric/init(wrappedvalue:from:)'
source_url: 'https://developer.apple.com/documentation/swiftui/physicalmetric/init(wrappedvalue:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/physicalmetric/init%28wrappedvalue%3Afrom%3A%29.json'
content_hash: 'sha256:72ee6e7ebab5eacf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PhysicalMetric](../physicalmetric.md)

# init(wrappedValue:from:)

<sub>Initializer</sub>

Creates a value that maps the specified point, whose dimensions are specified in physical length measurements in the given unit, to the corresponding value in points in the associated scene.

<sub>visionOS</sub>

```swift
init(wrappedValue point: CGPoint, from unit: UnitLength) where Value == CGPoint
```
