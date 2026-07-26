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
doc_path: '/documentation/charts/pointmark/init(x:y:)-9dswq'
source_url: 'https://developer.apple.com/documentation/charts/pointmark/init(x:y:)-9dswq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/pointmark/init%28x%3Ay%3A%29-9dswq.json'
content_hash: 'sha256:68e90a9850e9e74f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [PointMark](../pointmark.md)

# init(x:y:)

<sub>Initializer</sub>

Creates a point mark with fixed x position and plots values with y.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<Y>(x: CGFloat? = nil, y: PlottableValue<Y>) where Y : Plottable
```

## Parameters

- `x` — The x position.  If `x` is `nil`, the bar will be centered horizontally by default.

- `y` — The value plotted with y.

### Discussion

Use this initializer to plot a property to y:

```swift
Chart(data) {
    PointMark(
        y: .value("Weight", $0.weight)
    )
}
```

![Vertical point chart with weight plotted to the y-axis. There are 9 points at: 22, 24, 18, 22, 30, 27, 20, 14, 29.](../../../../attachments/50181f48d9c044281492be817a26addc/PointMarkSwift.PointMarkVerticalPointChart@2x.png)

For more background, see the first example used in [PointMark](../pointmark.md) which shows the structure that contains the `weight` property.

## See Also

### Creating a point mark

- [init(x:y:)](<init(x_y_)-44ke9.md>) — Creates a point mark that plots values to x and y.
- [init(x:y:)](<init(x_y_)-9hppd.md>) — Creates a point mark that plots a value on x with fixed y position.
- [init(x:y:z:)](<init(x_y_z_).md>) — Creates a 3D point mark that plots values to x, y and z.
