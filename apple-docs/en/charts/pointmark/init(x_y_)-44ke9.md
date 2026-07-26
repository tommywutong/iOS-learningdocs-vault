---
title: 'init(x:y:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/pointmark/init(x:y:)-44ke9'
source_url: 'https://developer.apple.com/documentation/charts/pointmark/init(x:y:)-44ke9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/pointmark/init%28x%3Ay%3A%29-44ke9.json'
content_hash: 'sha256:b4ae4c63b80de027'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [PointMark](../pointmark.md)

# init(x:y:)

<sub>Initializer</sub>

Creates a point mark that plots values to x and y.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>) where X : Plottable, Y : Plottable
```

## Parameters

- `x` — The value plotted with x.

- `y` — The value plotted with y.

### Discussion

Use this initializer to plot one property with x and another property with y:

```swift
Chart(data) {
    PointMark(
        x: .value("Wing Length", $0.wingLength),
        y: .value("Wing Length", $0.wingWidth)
    )
}
```

![](../../../../attachments/fca032573a6787a1f164ba898618e71a/PointMarkSwift.PointMarkScatterChart@2x.png)

<sub>A scatter plot with wing width plotted on the x-axis and wing height plotted on the y-axis. There are 12 points on the chart that demonstrate a roughly linear relationship between wing width and height.</sub>

For more background, see the first example used in [PointMark](../pointmark.md) which shows the structure that contains the `wingLength` and `wingHeight` properties.

## See Also

### Creating a point mark

- [init(x:y:)](<init(x_y_)-9dswq.md>) — Creates a point mark with fixed x position and plots values with y.
- [init(x:y:)](<init(x_y_)-9hppd.md>) — Creates a point mark that plots a value on x with fixed y position.
- [init(x:y:z:)](<init(x_y_z_).md>) — Creates a 3D point mark that plots values to x, y and z.
