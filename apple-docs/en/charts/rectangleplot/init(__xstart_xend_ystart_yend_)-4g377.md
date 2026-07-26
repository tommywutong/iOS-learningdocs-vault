---
title: 'init(_:xStart:xEnd:yStart:yEnd:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/rectangleplot/init(_:xstart:xend:ystart:yend:)-4g377'
source_url: 'https://developer.apple.com/documentation/charts/rectangleplot/init(_:xstart:xend:ystart:yend:)-4g377'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/rectangleplot/init%28_%3Axstart%3Axend%3Aystart%3Ayend%3A%29-4g377.json'
content_hash: 'sha256:89f3e0ad4e90db83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [RectanglePlot](../rectangleplot.md)

# init(_:xStart:xEnd:yStart:yEnd:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<Data, X, Y>(_ data: Data, xStart: PlottableProjection<RectanglePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RectanglePlot<Content>.DataElement, X>, yStart: PlottableProjection<RectanglePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RectanglePlot<Content>.DataElement, Y>) where Content == VectorizedRectanglePlotContent<Data>, Data : RandomAccessCollection, X : Plottable, Y : Plottable
```

## See Also

### Plotting rectangles from a collection

- [init(_:x:y:width:height:)](<init(__x_y_width_height_).md>)
- [init(_:x:yStart:yEnd:width:)](<init(__x_ystart_yend_width_)-93op1.md>)
- [init(_:x:yStart:yEnd:width:)](<init(__x_ystart_yend_width_)-nnvk.md>)
- [init(_:x:yStart:yEnd:width:)](<init(__x_ystart_yend_width_)-12u1b.md>)
- [init(_:xStart:xEnd:y:height:)](<init(__xstart_xend_y_height_)-51nra.md>)
- [init(_:xStart:xEnd:y:height:)](<init(__xstart_xend_y_height_)-8s17v.md>)
- [init(_:xStart:xEnd:y:height:)](<init(__xstart_xend_y_height_)-15ish.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<init(__xstart_xend_ystart_yend_)-46wi0.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<init(__xstart_xend_ystart_yend_)-6d8yb.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<init(__xstart_xend_ystart_yend_)-6uuk4.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<init(__xstart_xend_ystart_yend_)-741lz.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<init(__xstart_xend_ystart_yend_)-ir9o.md>)
