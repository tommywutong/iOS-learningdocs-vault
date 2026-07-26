---
title: plotAreaSize
framework: Swift Charts
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+（17.0 起废弃）, iPadOS 16.0+（17.0 起废弃）, Mac Catalyst 16.0+（17.0 起废弃）, macOS 13.0+（14.0 起废弃）, tvOS 16.0+（17.0 起废弃）, visionOS 1.0+, watchOS 9.0+（10.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/charts/chartproxy/plotareasize
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/plotareasize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/plotareasize.json'
content_hash: 'sha256:c4abeef9678f1c7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# plotAreaSize

<sub>Instance Property</sub>

The size of the plot in the chart.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var plotAreaSize: CGSize { get }
```

## Discussion

The plot is the area between the x and y axes, not including the axes themselves.

A chart must exist in the context of the chart proxy.
