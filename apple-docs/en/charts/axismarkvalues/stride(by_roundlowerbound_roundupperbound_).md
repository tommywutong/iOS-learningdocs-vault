---
title: 'stride(by:roundLowerBound:roundUpperBound:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/axismarkvalues/stride(by:roundlowerbound:roundupperbound:)'
source_url: 'https://developer.apple.com/documentation/charts/axismarkvalues/stride(by:roundlowerbound:roundupperbound:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axismarkvalues/stride%28by%3Aroundlowerbound%3Aroundupperbound%3A%29.json'
content_hash: 'sha256:9d9dcd500d8e10f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AxisMarkValues](../axismarkvalues.md)

# stride(by:roundLowerBound:roundUpperBound:)

<sub>Type Method</sub>

Creates values with the given number step.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func stride<P>(by stepSize: P, roundLowerBound: Bool? = nil, roundUpperBound: Bool? = nil) -> AxisMarkValues where P : BinaryFloatingPoint
```
