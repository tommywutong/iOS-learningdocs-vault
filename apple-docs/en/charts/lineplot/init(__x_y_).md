---
title: 'init(_:x:y:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/lineplot/init(_:x:y:)'
source_url: 'https://developer.apple.com/documentation/charts/lineplot/init(_:x:y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/lineplot/init%28_%3Ax%3Ay%3A%29.json'
content_hash: 'sha256:30e52387bd0dff1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [LinePlot](../lineplot.md)

# init(_:x:y:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<Data>(_ data: Data, x: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>, y: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>) where Content == VectorizedLinePlotContent<Data>, Data : RandomAccessCollection
```

## See Also

### Plotting lines from a collection

- [init(_:x:y:series:)](<init(__x_y_series_).md>)
