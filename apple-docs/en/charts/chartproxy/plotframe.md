---
title: plotFrame
framework: Swift Charts
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/chartproxy/plotframe
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/plotframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/plotframe.json'
content_hash: 'sha256:4592a7ae71ce9422'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# plotFrame

<sub>Instance Property</sub>

An anchor to the frame of the chart’s plot, or `nil` if there is no chart in the context of the chart proxy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var plotFrame: Anchor<CGRect>? { get }
```

## Discussion

The plot is the area between the x and y axes, not including the axes themselves. If the chart is scrollable, the plot frame includes both visible and invisible portions of the plot.

You can convert the anchor to a frame using a `GeometryProxy`.
