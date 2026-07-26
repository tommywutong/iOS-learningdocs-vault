---
title: 'value(_:_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/plottablevalue/value(_:_:)-f1kk'
source_url: 'https://developer.apple.com/documentation/charts/plottablevalue/value(_:_:)-f1kk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/plottablevalue/value%28_%3A_%3A%29-f1kk.json'
content_hash: 'sha256:58e507945d74b7b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [PlottableValue](../plottablevalue.md)

# value(_:_:)

<sub>Type Method</sub>

Creates a parameter value with label and value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func value<S>(_ label: S, _ range: Range<Value>) -> PlottableValue<Value> where Value : Comparable, S : StringProtocol
```

## Parameters

- `label` — The label.
