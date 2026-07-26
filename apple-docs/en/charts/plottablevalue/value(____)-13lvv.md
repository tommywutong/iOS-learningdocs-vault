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
doc_path: '/documentation/charts/plottablevalue/value(_:_:)-13lvv'
source_url: 'https://developer.apple.com/documentation/charts/plottablevalue/value(_:_:)-13lvv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/plottablevalue/value%28_%3A_%3A%29-13lvv.json'
content_hash: 'sha256:f170911f962a1fb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [PlottableValue](../plottablevalue.md)

# value(_:_:)

<sub>Type Method</sub>

Creates a parameter value with label and value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func value<S>(_ label: S, _ value: Value) -> PlottableValue<Value> where S : StringProtocol
```

## Parameters

- `label` — The label.

- `value` — The parameter’s value.
