---
title: 'init(_:x:yStart:yEnd:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/areaplot/init(_:x:ystart:yend:)'
source_url: 'https://developer.apple.com/documentation/charts/areaplot/init(_:x:ystart:yend:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/areaplot/init%28_%3Ax%3Aystart%3Ayend%3A%29.json'
content_hash: 'sha256:5b12c688ae784ae7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AreaPlot](../areaplot.md)

# init(_:x:yStart:yEnd:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<Data, Y>(_ data: Data, x: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, yStart: PlottableProjection<AreaPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<AreaPlot<Content>.DataElement, Y>) where Content == VectorizedAreaPlotContent<Data>, Data : RandomAccessCollection, Y : Plottable
```

## See Also

### Plotting areas from a collection

- [init(_:x:y:stacking:)](<init(__x_y_stacking_).md>)
- [init(_:x:y:series:stacking:)](<init(__x_y_series_stacking_).md>)
- [init(_:xStart:xEnd:y:)](<init(__xstart_xend_y_).md>)
- [init(_:xStart:xEnd:y:series:)](<init(__xstart_xend_y_series_).md>)
- [init(_:x:yStart:yEnd:series:)](<init(__x_ystart_yend_series_).md>)
