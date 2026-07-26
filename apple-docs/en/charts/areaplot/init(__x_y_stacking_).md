---
title: 'init(_:x:y:stacking:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/areaplot/init(_:x:y:stacking:)'
source_url: 'https://developer.apple.com/documentation/charts/areaplot/init(_:x:y:stacking:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/areaplot/init%28_%3Ax%3Ay%3Astacking%3A%29.json'
content_hash: 'sha256:3fe4e21f51d21732'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AreaPlot](../areaplot.md)

# init(_:x:y:stacking:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<Data>(_ data: Data, x: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, y: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, stacking: MarkStackingMethod = .standard) where Content == VectorizedAreaPlotContent<Data>, Data : RandomAccessCollection
```

## See Also

### Plotting areas from a collection

- [init(_:x:y:series:stacking:)](<init(__x_y_series_stacking_).md>)
- [init(_:xStart:xEnd:y:)](<init(__xstart_xend_y_).md>)
- [init(_:xStart:xEnd:y:series:)](<init(__xstart_xend_y_series_).md>)
- [init(_:x:yStart:yEnd:)](<init(__x_ystart_yend_).md>)
- [init(_:x:yStart:yEnd:series:)](<init(__x_ystart_yend_series_).md>)
