---
title: 'init(xStart:xEnd:y:height:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/rectanglemark/init(xstart:xend:y:height:)-27222'
source_url: 'https://developer.apple.com/documentation/charts/rectanglemark/init(xstart:xend:y:height:)-27222'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/rectanglemark/init%28xstart%3Axend%3Ay%3Aheight%3A%29-27222.json'
content_hash: 'sha256:b3e4880c7c81f45c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [RectangleMark](../rectanglemark.md)

# init(xStart:xEnd:y:height:)

<sub>Initializer</sub>

Creates a rectangle mark with an x interval encoding and a y encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, height: MarkDimension = .automatic) where X : Plottable, Y : Plottable
```

## Parameters

- `xStart` — The value plotted with x start.

- `xEnd` — The value plotted with x end.

- `y` — The value plotted with y.

- `height` — The rectangle height. If `height` is not specified, then 70% of the step size will be used. If there is no step size a default height (in pts) will be used.

### Discussion

Use this initializer to map the x start, x end and y position to a rectangle for each data element. Optionally, specify the height of the rectangles.

The example below omits the optional `height` parameter and uses a number scale starting at (0,0) and ending at (6,6). The rectangle has the coordinates: (2,0), (2,4), (4,4), (4,0).

```swift
Chart(data) {
    RectangleMark(
        xStart: .value("Rect xStart", 2),
        xEnd: .value("Rect xEnd", 4),
        y: .value("Rect Y", 4)
    )
    .opacity(0.2)

    PointMark(
        x: .value("X", $0.x),
        y: .value("Y", $0.y)
    )
}
```

![](../../../../attachments/a6d00e8c07181e9cdc26a9fdcbd90265/RectangleMarkSwift.RectangleMarkScatterWithRectangleXIntervalY@2x.png)

<sub>Scatter plot chart with a rectangle mark annotation. 3 points on the chart at: (5, 5), (2.5, 2.5), (3, 3) the rectangle highlights a rectangular area with coordinates: (2,0), (2,4), (4,4), (4,0).</sub>

## See Also

### Creating a rectangle mark

- [init(x:yStart:yEnd:width:)](<init(x_ystart_yend_width_)-vh2x.md>) — Creates a rectangle mark with an y interval encoding and an x encoding.
- [init(x:yStart:yEnd:width:)](<init(x_ystart_yend_width_)-xhqp.md>) — Creates a rectangle mark that plots values on x and has a fixed y interval.
- [init(xStart:xEnd:y:height:)](<init(xstart_xend_y_height_)-4x46i.md>) — Creates a rectangle mark with a fixed x interval and y encoding.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-1qbzg.md>) — Creates a rectangle mark with x and y interval encodings.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-5682c.md>) — Creates a rectangle mark with fixed x and y intervals.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-5cbgh.md>) — Creates a rectangle mark with a y interval encoding and a fixed x interval.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-6jeka.md>) — Creates a rectangle mark with an x interval encoding and a fixed y interval.
- [init(x:y:width:height:)](<init(x_y_width_height_).md>) — Creates a rectangle that plots values with x and y.
- [init(x:y:z:)](<init(x_y_z_).md>) — Creates a rectangle mark for a 3D chart.
