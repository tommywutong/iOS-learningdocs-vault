---
title: 'init(x:y:z:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/pointmark/init(x:y:z:)'
source_url: 'https://developer.apple.com/documentation/charts/pointmark/init(x:y:z:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/pointmark/init%28x%3Ay%3Az%3A%29.json'
content_hash: 'sha256:098aa90ae4d106d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [PointMark](../pointmark.md)

# init(x:y:z:)

<sub>Initializer</sub>

Creates a 3D point mark that plots values to x, y and z.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(x: PlottableValue<some Plottable>, y: PlottableValue<some Plottable>, z: PlottableValue<some Plottable>)
```

## Parameters

- `x` — The x position.

- `y` — The y position.

- `z` — The z position.

## Discussion

> [!important] Important
> A 3D PointMark requires exactly three numeric points.

Use this initializer to plot one property with each of the x, y and z axes:

```swift
Chart3D(data) {
    PointMark(
        x: .value("Wing Length", $0.wingLength),
        y: .value("Wing Width", $0.wingWidth),
        z: .value("Weight", $0.weight)
    )
}
```

## See Also

### Creating a point mark

- [init(x:y:)](<init(x_y_)-44ke9.md>) — Creates a point mark that plots values to x and y.
- [init(x:y:)](<init(x_y_)-9dswq.md>) — Creates a point mark with fixed x position and plots values with y.
- [init(x:y:)](<init(x_y_)-9hppd.md>) — Creates a point mark that plots a value on x with fixed y position.
