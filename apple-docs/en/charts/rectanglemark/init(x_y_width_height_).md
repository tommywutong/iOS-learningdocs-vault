---
title: 'init(x:y:width:height:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/rectanglemark/init(x:y:width:height:)'
source_url: 'https://developer.apple.com/documentation/charts/rectanglemark/init(x:y:width:height:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/rectanglemark/init%28x%3Ay%3Awidth%3Aheight%3A%29.json'
content_hash: 'sha256:e9a319b6a8fd10e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [RectangleMark](../rectanglemark.md)

# init(x:y:width:height:)

<sub>Initializer</sub>

Creates a rectangle that plots values with x and y.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension = .automatic, height: MarkDimension = .automatic) where X : Plottable, Y : Plottable
```

## Parameters

- `x` — The value plotted with x.

- `y` — The value plotted with y.

- `width` — The rectangle width.  If `width` is not specified, then 70% of the step size will be used. If there is no step size a default width (in pts) will be used.

- `height` — The rectangle height.  If `height` is not specified, then 70% of the step size will be used. If there is no step size a default height (in pts) will be used.

### Discussion

Use this initializer to map an x and y position to a rectangle for each data element. Optionally, specify the width or height of the rectangles.

The example below omits the optional `width` and `height` parameters and uses a number scale starting at (0,0). The rectangle has the coordinates: (0,0), (0,3), (3,0), (3,3).

```swift
Chart(data) {
    RectangleMark(
        x: .value("Rect X", 3),
        y: .value("Rect Y", 3)
    )
    .opacity(0.2)

    PointMark(
        x: .value("X", $0.x),
        y: .value("Y", $0.y)
    )
}
```

![](../../../../attachments/b486caaff77bf328cb2280043d9b512a/RectangleMarkSwift.RectangleMarkScatterWithRectangleXY@2x.png)

<sub>Scatter plot chart with a rectangle mark annotation. 3 points on the chart at: (5, 5), (2.5, 2.5), (3, 3) the rectangle highlights a rectangular area with coordinates: (0,0), (0,3), (3,0), (3,3).</sub>

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
- [init(x:y:z:)](<init(x_y_z_).md>) — Creates a rectangle mark for a 3D chart.
