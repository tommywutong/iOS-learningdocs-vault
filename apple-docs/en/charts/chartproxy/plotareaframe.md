---
title: plotAreaFrame
framework: Swift Charts
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+（17.0 起废弃）, iPadOS 16.0+（17.0 起废弃）, Mac Catalyst 16.0+（17.0 起废弃）, macOS 13.0+（14.0 起废弃）, tvOS 16.0+（17.0 起废弃）, visionOS 1.0+, watchOS 9.0+（10.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/charts/chartproxy/plotareaframe
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/plotareaframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/plotareaframe.json'
content_hash: 'sha256:8f4f0515c737684b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# plotAreaFrame

<sub>Instance Property</sub>

An anchor to the frame of the chart’s plot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var plotAreaFrame: Anchor<CGRect> { get }
```

## Discussion

The plot is the area between the x and y axes, not including the axes themselves. If the chart is scrollable, the plot frame includes both visible and invisible portions of the plot.

A chart must exist in the context of the chart proxy. You can convert the anchor to a frame using a `GeometryProxy`.
