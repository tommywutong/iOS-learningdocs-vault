---
title: 'init(_:x:yStart:yEnd:series:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/areaplot/init(_:x:ystart:yend:series:)'
source_url: 'https://developer.apple.com/documentation/charts/areaplot/init(_:x:ystart:yend:series:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/areaplot/init%28_%3Ax%3Aystart%3Ayend%3Aseries%3A%29.json'
content_hash: 'sha256:bc9e854ec8d5813f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AreaPlot](../areaplot.md)

# init(_:x:yStart:yEnd:series:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<Data, Y>(_ data: Data, x: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, yStart: PlottableProjection<AreaPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<AreaPlot<Content>.DataElement, Y>, series: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>) where Content == VectorizedAreaPlotContent<Data>, Data : RandomAccessCollection, Y : Plottable
```

## See Also

### Plotting areas from a collection

- [init(_:x:y:stacking:)](<init(__x_y_stacking_).md>)
- [init(_:x:y:series:stacking:)](<init(__x_y_series_stacking_).md>)
- [init(_:xStart:xEnd:y:)](<init(__xstart_xend_y_).md>)
- [init(_:xStart:xEnd:y:series:)](<init(__xstart_xend_y_series_).md>)
- [init(_:x:yStart:yEnd:)](<init(__x_ystart_yend_).md>)
