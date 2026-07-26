---
title: 'init(x:yStart:yEnd:series:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/areamark/init(x:ystart:yend:series:)'
source_url: 'https://developer.apple.com/documentation/charts/areamark/init(x:ystart:yend:series:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/areamark/init%28x%3Aystart%3Ayend%3Aseries%3A%29.json'
content_hash: 'sha256:7137149ce391b558'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AreaMark](../areamark.md)

# init(x:yStart:yEnd:series:)

<sub>Initializer</sub>

Creates an area mark that plots values with a vertical interval and associates it with the specified series.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<X, Y, S>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, series: PlottableValue<S>) where X : Plottable, Y : Plottable, S : Plottable
```

## Parameters

- `x` — The horizontal position for the mark.

- `yStart` — The starting vertical position for the mark.

- `yEnd` — The ending vertical position for the mark.

- `series` — A series to associate the mark with.

## Discussion

The initializer behaves like [init(x:yStart:yEnd:)](<init(x_ystart_yend_).md>), except that you can indicate which region each interval belongs to by providing a value for the `series` input. This enables you to plot more than one region on a single chart.

To plot a series of values that have a horizontal interval, use [init(xStart:xEnd:y:series:)](<init(xstart_xend_y_series_).md>) instead.

## See Also

### Creating a range area chart

- [init(x:yStart:yEnd:)](<init(x_ystart_yend_).md>) — Creates an area mark that plots values with a vertical interval.
- [init(xStart:xEnd:y:)](<init(xstart_xend_y_).md>) — Creates an area mark that plots values with a horizontal interval.
- [init(xStart:xEnd:y:series:)](<init(xstart_xend_y_series_).md>) — Creates an area mark that plots values with a horizontal interval and associates it with the specified series.
