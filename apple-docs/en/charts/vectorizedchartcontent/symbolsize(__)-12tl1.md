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
doc_path: '/documentation/charts/vectorizedchartcontent/symbolsize(_:)-12tl1'
source_url: 'https://developer.apple.com/documentation/charts/vectorizedchartcontent/symbolsize(_:)-12tl1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/vectorizedchartcontent/symbolsize%28_%3A%29-12tl1.json'
content_hash: 'sha256:dafc15bba3b45046'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [VectorizedChartContent](../vectorizedchartcontent.md)

# symbolSize(_:)

<sub>Instance Method</sub>

Sets the plotting symbol size for the chart content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func symbolSize(_ size: KeyPath<Self.DataElement, CGSize>) -> some VectorizedChartContent<Self.DataElement>

```

## Parameters

- `size` — The symbol’s bounding box’s dimensions.

## See Also

### Setting symbol appearance

- [symbol(by:)](<symbol(by_).md>) — Represents data using different kinds of symbols.
- [symbolSize(_:)](<symbolsize(__)-3nwop.md>) — Sets the plotting symbol size for the chart content according to a perceived area.
