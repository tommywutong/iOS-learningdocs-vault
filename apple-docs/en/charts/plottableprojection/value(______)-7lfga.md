---
title: 'value(_:_:_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/plottableprojection/value(_:_:_:)-7lfga'
source_url: 'https://developer.apple.com/documentation/charts/plottableprojection/value(_:_:_:)-7lfga'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/plottableprojection/value%28_%3A_%3A_%3A%29-7lfga.json'
content_hash: 'sha256:d29099db808eac2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [PlottableProjection](../plottableprojection.md)

# value(_:_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func value(_ label: some StringProtocol, _ start: KeyPath<DataElement, DataValue>, _ end: KeyPath<DataElement, DataValue>) -> PlottableProjection<DataElement, DataValue> where DataValue : Comparable
```
