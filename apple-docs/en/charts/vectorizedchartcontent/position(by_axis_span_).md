---
title: 'position(by:axis:span:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/vectorizedchartcontent/position(by:axis:span:)'
source_url: 'https://developer.apple.com/documentation/charts/vectorizedchartcontent/position(by:axis:span:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/vectorizedchartcontent/position%28by%3Aaxis%3Aspan%3A%29.json'
content_hash: 'sha256:2abd023c6d3c4075'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [VectorizedChartContent](../vectorizedchartcontent.md)

# position(by:axis:span:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func position(by value: PlottableProjection<Self.DataElement, some Plottable>, axis: Axis? = nil, span: MarkDimension = .automatic) -> some VectorizedChartContent<Self.DataElement>

```

## See Also

### Styling marks

- [foregroundStyle(_:)](<foregroundstyle(__).md>) — Represents data using a foreground style.
- [opacity(_:)](<opacity(__).md>)
- [lineStyle(_:)](<linestyle(__).md>) — Represents data using line styles.
