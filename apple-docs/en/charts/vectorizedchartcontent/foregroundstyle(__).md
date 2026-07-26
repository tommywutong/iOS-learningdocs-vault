---
title: 'foregroundStyle(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/vectorizedchartcontent/foregroundstyle(_:)'
source_url: 'https://developer.apple.com/documentation/charts/vectorizedchartcontent/foregroundstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/vectorizedchartcontent/foregroundstyle%28_%3A%29.json'
content_hash: 'sha256:29dd4f43f27aad58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [VectorizedChartContent](../vectorizedchartcontent.md)

# foregroundStyle(_:)

<sub>Instance Method</sub>

Represents data using a foreground style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func foregroundStyle(_ keyPath: KeyPath<Self.DataElement, some ShapeStyle>) -> some VectorizedChartContent<Self.DataElement>

```

## Parameters

- `keyPath` — The accessor for shape style.

## See Also

### Styling marks

- [opacity(_:)](<opacity(__).md>)
- [lineStyle(_:)](<linestyle(__).md>) — Represents data using line styles.
- [position(by:axis:span:)](<position(by_axis_span_).md>)
