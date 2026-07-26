---
title: 'opacity(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/vectorizedchartcontent/opacity(_:)'
source_url: 'https://developer.apple.com/documentation/charts/vectorizedchartcontent/opacity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/vectorizedchartcontent/opacity%28_%3A%29.json'
content_hash: 'sha256:e7e25236f3eb159c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [VectorizedChartContent](../vectorizedchartcontent.md)

# opacity(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func opacity(_ keyPath: KeyPath<Self.DataElement, CGFloat>) -> some VectorizedChartContent<Self.DataElement>

```

## Parameters

- `keyPath` — Points to a value between 0 (fully transparent) and 1 (fully opaque).

## See Also

### Styling marks

- [foregroundStyle(_:)](<foregroundstyle(__).md>) — Represents data using a foreground style.
- [lineStyle(_:)](<linestyle(__).md>) — Represents data using line styles.
- [position(by:axis:span:)](<position(by_axis_span_).md>)
