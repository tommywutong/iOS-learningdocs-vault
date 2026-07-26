---
title: 'symbolSize(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/vectorizedchartcontent/symbolsize(_:)-3nwop'
source_url: 'https://developer.apple.com/documentation/charts/vectorizedchartcontent/symbolsize(_:)-3nwop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/vectorizedchartcontent/symbolsize%28_%3A%29-3nwop.json'
content_hash: 'sha256:64418487b796329c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [VectorizedChartContent](../vectorizedchartcontent.md)

# symbolSize(_:)

<sub>Instance Method</sub>

Sets the plotting symbol size for the chart content according to a perceived area.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func symbolSize(_ area: KeyPath<Self.DataElement, CGFloat>) -> some VectorizedChartContent<Self.DataElement>

```

## Parameters

- `area` — The perceived area in square points. For example, a square with 10 points on each side has an area of 100 square points.

## See Also

### Setting symbol appearance

- [symbol(by:)](<symbol(by_).md>) — Represents data using different kinds of symbols.
- [symbolSize(_:)](<symbolsize(__)-12tl1.md>) — Sets the plotting symbol size for the chart content.
