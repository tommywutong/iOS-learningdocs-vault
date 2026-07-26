---
title: 'lineStyle(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/vectorizedchartcontent/linestyle(_:)'
source_url: 'https://developer.apple.com/documentation/charts/vectorizedchartcontent/linestyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/vectorizedchartcontent/linestyle%28_%3A%29.json'
content_hash: 'sha256:7883ae22b9aafa1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [VectorizedChartContent](../vectorizedchartcontent.md)

# lineStyle(_:)

<sub>Instance Method</sub>

Represents data using line styles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func lineStyle(_ style: KeyPath<Self.DataElement, StrokeStyle>) -> some VectorizedChartContent<Self.DataElement>

```

## Parameters

- `style` — The keyPath accessor for shape style.

## See Also

### Styling marks

- [foregroundStyle(_:)](<foregroundstyle(__).md>) — Represents data using a foreground style.
- [opacity(_:)](<opacity(__).md>)
- [position(by:axis:span:)](<position(by_axis_span_).md>)
