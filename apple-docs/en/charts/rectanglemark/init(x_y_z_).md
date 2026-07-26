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
doc_path: '/documentation/charts/rectanglemark/init(x:y:z:)'
source_url: 'https://developer.apple.com/documentation/charts/rectanglemark/init(x:y:z:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/rectanglemark/init%28x%3Ay%3Az%3A%29.json'
content_hash: 'sha256:554a90cd245f5fe9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [RectangleMark](../rectanglemark.md)

# init(x:y:z:)

<sub>Initializer</sub>

Creates a rectangle mark for a 3D chart.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(x: PlottableValue<some Plottable>, y: PlottableValue<some Plottable>, z: PlottableValue<some Plottable>)
```

## Parameters

- `x` — The x value.

- `y` — The y value.

- `z` — The z value.

## Discussion

> [!important] Important
> A 3D RectangleMark requires one parameter to be a single numeric value and the other two parameters to be numeric ranges.

For example, the following `Chart3D` shows a rectangle mark that extends along the x-axis and y-axis.

```swift
Chart3D {
    RectangleMark(
        x: .value("x", -0.5..<0.5),
        y: .value("y", -0.5..<0.5),
        z: .value("z", 0)
    )
}
```

## See Also

### Creating a rectangle mark

- [init(x:yStart:yEnd:width:)](<init(x_ystart_yend_width_)-vh2x.md>) — Creates a rectangle mark with an y interval encoding and an x encoding.
- [init(x:yStart:yEnd:width:)](<init(x_ystart_yend_width_)-xhqp.md>) — Creates a rectangle mark that plots values on x and has a fixed y interval.
- [init(xStart:xEnd:y:height:)](<init(xstart_xend_y_height_)-27222.md>) — Creates a rectangle mark with an x interval encoding and a y encoding.
- [init(xStart:xEnd:y:height:)](<init(xstart_xend_y_height_)-4x46i.md>) — Creates a rectangle mark with a fixed x interval and y encoding.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-1qbzg.md>) — Creates a rectangle mark with x and y interval encodings.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-5682c.md>) — Creates a rectangle mark with fixed x and y intervals.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-5cbgh.md>) — Creates a rectangle mark with a y interval encoding and a fixed x interval.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-6jeka.md>) — Creates a rectangle mark with an x interval encoding and a fixed y interval.
- [init(x:y:width:height:)](<init(x_y_width_height_).md>) — Creates a rectangle that plots values with x and y.
