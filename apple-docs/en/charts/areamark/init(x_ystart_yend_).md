---
title: 'init(x:yStart:yEnd:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/areamark/init(x:ystart:yend:)'
source_url: 'https://developer.apple.com/documentation/charts/areamark/init(x:ystart:yend:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/areamark/init%28x%3Aystart%3Ayend%3A%29.json'
content_hash: 'sha256:fc40742e65278638'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AreaMark](../areamark.md)

# init(x:yStart:yEnd:)

<sub>Initializer</sub>

Creates an area mark that plots values with a vertical interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>) where X : Plottable, Y : Plottable
```

## Parameters

- `x` — The horizontal position for the mark.

- `yStart` — The starting vertical position for the mark.

- `yEnd` — The ending vertical position for the mark.

## Discussion

Use this initializer to create a range area chart with vertical intervals. For example you can create a region that encompasses all the temperatures over the course of a day, across a number of days:

```swift
Chart(data) { day in
    AreaMark(
        x: .value("Date", day.date),
        yStart: .value("Minimum Temperature", minimumTemperature),
        yEnd: .value("Maximum Temperature", day.maximumTemperature)
    )
}
```

![](../../../../attachments/312b9822d288c8f1e400decc5e04ad9e/AreaMark-5-macOS@2x.png)

<sub>A chart that shows month names on the x-axis, ranging from January to October, and a number in the range 0 to 80 on the y-axis. A solid blue region spans the chart from left to right. The region is close to the middle of the y-axis on either end, and closer to the top of the chart in the middle. The region is thinner at the ends and thicker in the middle.</sub>

If you want to plot values that have a horiztonal interval, use [init(xStart:xEnd:y:)](<init(xstart_xend_y_).md>) instead.

## See Also

### Creating a range area chart

- [init(x:yStart:yEnd:series:)](<init(x_ystart_yend_series_).md>) — Creates an area mark that plots values with a vertical interval and associates it with the specified series.
- [init(xStart:xEnd:y:)](<init(xstart_xend_y_).md>) — Creates an area mark that plots values with a horizontal interval.
- [init(xStart:xEnd:y:series:)](<init(xstart_xend_y_series_).md>) — Creates an area mark that plots values with a horizontal interval and associates it with the specified series.
