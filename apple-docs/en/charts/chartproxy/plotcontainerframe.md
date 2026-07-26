---
title: plotContainerFrame
framework: Swift Charts
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/chartproxy/plotcontainerframe
source_url: 'https://developer.apple.com/documentation/charts/chartproxy/plotcontainerframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy/plotcontainerframe.json'
content_hash: 'sha256:19f9a2c88477863b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartProxy](../chartproxy.md)

# plotContainerFrame

<sub>Instance Property</sub>

An anchor to the frame of the chart’s plot container, or `nil` if there is no chart in the context of the chart proxy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var plotContainerFrame: Anchor<CGRect>? { get }
```

## Discussion

The plot is the area between the x and y axes, not including the axes themselves. If the chart is scrollable, the plot container frame only includes the visible portion of the plot. Otherwise, it is the same as [plotFrame](plotframe.md).

You can convert the anchor to a frame using a `GeometryProxy`. Below is an example adding a border to the plot container:

```swift
Chart { ... }
.chartOverlay { chartProxy in
    GeometryReader { geometryProxy in
        // Get the plot container's frame in the GeometryReader's coordinate space.
        // This frame stays the same when the chart scrolls.
        // In this example, we add a border to the plot container by stroking the frame.
        if let plotContainerFrame = chartProxy.plotContainerFrame {
            Path(geometryProxy[plotContainerFrame])
                .stroke(.black, lineWidth: 1)
                .allowsHitTesting(false)
        }
    }
}
```
