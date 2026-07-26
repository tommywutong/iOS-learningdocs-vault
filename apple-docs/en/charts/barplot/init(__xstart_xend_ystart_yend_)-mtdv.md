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
doc_path: '/documentation/charts/barplot/init(_:xstart:xend:ystart:yend:)-mtdv'
source_url: 'https://developer.apple.com/documentation/charts/barplot/init(_:xstart:xend:ystart:yend:)-mtdv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/barplot/init%28_%3Axstart%3Axend%3Aystart%3Ayend%3A%29-mtdv.json'
content_hash: 'sha256:4c2c2d816258e796'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [BarPlot](../barplot.md)

# init(_:xStart:xEnd:yStart:yEnd:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<Data, X>(_ data: Data, xStart: PlottableProjection<BarPlot<Content>.DataElement, X>, xEnd: PlottableProjection<BarPlot<Content>.DataElement, X>, yStart: KeyPath<BarPlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<BarPlot<Content>.DataElement, CGFloat>) where Content == VectorizedBarPlotContent<Data>, Data : RandomAccessCollection, X : Plottable
```

## See Also

### Plotting bars from a collection

- [init(_:x:y:width:height:stacking:)](<init(__x_y_width_height_stacking_).md>)
- [init(_:x:yStart:yEnd:width:)](<init(__x_ystart_yend_width_).md>)
- [init(_:x:yStart:yEnd:width:stacking:)](<init(__x_ystart_yend_width_stacking_)-2mtih.md>)
- [init(_:x:yStart:yEnd:width:stacking:)](<init(__x_ystart_yend_width_stacking_)-680hw.md>)
- [init(_:xStart:xEnd:y:height:stacking:)](<init(__xstart_xend_y_height_stacking_)-16tou.md>)
- [init(_:xStart:xEnd:y:height:stacking:)](<init(__xstart_xend_y_height_stacking_)-2x0yx.md>)
- [init(_:xStart:xEnd:y:height:)](<init(__xstart_xend_y_height_).md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<init(__xstart_xend_ystart_yend_)-48su5.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<init(__xstart_xend_ystart_yend_)-862wn.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<init(__xstart_xend_ystart_yend_)-raqh.md>)
