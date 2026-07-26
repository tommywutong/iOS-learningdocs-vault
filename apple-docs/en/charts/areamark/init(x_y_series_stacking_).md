---
title: 'init(x:y:series:stacking:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/areamark/init(x:y:series:stacking:)'
source_url: 'https://developer.apple.com/documentation/charts/areamark/init(x:y:series:stacking:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/areamark/init%28x%3Ay%3Aseries%3Astacking%3A%29.json'
content_hash: 'sha256:cd348324dc9fe7a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AreaMark](../areamark.md)

# init(x:y:series:stacking:)

<sub>Initializer</sub>

Creates an area mark and associates it with the specified series.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<X, Y, S>(x: PlottableValue<X>, y: PlottableValue<Y>, series: PlottableValue<S>, stacking: MarkStackingMethod = .standard) where X : Plottable, Y : Plottable, S : Plottable
```

## Parameters

- `x` — The horizontal position for the mark.

- `y` — The vertical position for the mark.

- `series` — A series to associate the mark with.

- `stacking` — The way in which the chart stacks area regions. The default is [standard](../markstackingmethod/standard.md).

## Discussion

The initializer behaves like [init(x:y:stacking:)](<init(x_y_stacking_).md>), except that you can indicate which region each data point belongs to by providing a value for the `series` input. This enables you to plot more than one region on a single chart.

## See Also

### Creating an area mark

- [init(x:y:stacking:)](<init(x_y_stacking_).md>) — Creates an area mark using the specified horizontal and vertical positions.
