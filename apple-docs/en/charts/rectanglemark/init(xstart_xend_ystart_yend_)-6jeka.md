---
title: 'init(xStart:xEnd:yStart:yEnd:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/rectanglemark/init(xstart:xend:ystart:yend:)-6jeka'
source_url: 'https://developer.apple.com/documentation/charts/rectanglemark/init(xstart:xend:ystart:yend:)-6jeka'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/rectanglemark/init%28xstart%3Axend%3Aystart%3Ayend%3A%29-6jeka.json'
content_hash: 'sha256:eaea5032979dce25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [RectangleMark](../rectanglemark.md)

# init(xStart:xEnd:yStart:yEnd:)

<sub>Initializer</sub>

Creates a rectangle mark with an x interval encoding and a fixed y interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<X>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, yStart: CGFloat? = nil, yEnd: CGFloat? = nil) where X : Plottable
```

## Discussion

- xStart: The value plotted with x start.
- xEnd: The value plotted with x end.
- yStart: The y end position. If `yStart` is `nil` then the rectangle will start at the leading edge of the plotting area.
- yEnd: The y end position. If `yEnd` is `nil` then the rectangle will end at the trailing edge of the plotting area.

### Discussion

Use this initializer to map the x start and x end to a rectangle for each data element. Optionally, specify the yStart or yEnd position of the rectangles.

The example below omits the optional `y` and `height` fields and uses a number scale starting at (0,0) and ending at (6,6). The rectangle has the coordinates: (2,0), (2,6), (4,6), (4,0).

```swift
Chart(data) {
    RectangleMark(
        xStart: .value("Rect xStart", 2),
        xEnd: .value("Rect xEnd", 4)
    )
    .opacity(0.2)

    PointMark(
        x: .value("X", $0.x),
        y: .value("Y", $0.y)
    )
}
```

![](../../../../attachments/7a1809238b03fd1d3bdc5d31f86f3633/RectangleMarkSwift.RectangleMarkScatterWithRectangleXInterval@2x.png)

<sub>Scatter plot chart with a rectangle mark annotation. 3 points on the chart at: (5, 5), (2.5, 2.5), (3, 3) the rectangle highlights a rectangular area with coordinates: (2,0), (2,6), (4,6), (4,0).</sub>

## See Also

### Creating a rectangle mark

- [init(x:yStart:yEnd:width:)](<init(x_ystart_yend_width_)-vh2x.md>) — Creates a rectangle mark with an y interval encoding and an x encoding.
- [init(x:yStart:yEnd:width:)](<init(x_ystart_yend_width_)-xhqp.md>) — Creates a rectangle mark that plots values on x and has a fixed y interval.
- [init(xStart:xEnd:y:height:)](<init(xstart_xend_y_height_)-27222.md>) — Creates a rectangle mark with an x interval encoding and a y encoding.
- [init(xStart:xEnd:y:height:)](<init(xstart_xend_y_height_)-4x46i.md>) — Creates a rectangle mark with a fixed x interval and y encoding.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-1qbzg.md>) — Creates a rectangle mark with x and y interval encodings.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-5682c.md>) — Creates a rectangle mark with fixed x and y intervals.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-5cbgh.md>) — Creates a rectangle mark with a y interval encoding and a fixed x interval.
- [init(x:y:width:height:)](<init(x_y_width_height_).md>) — Creates a rectangle that plots values with x and y.
- [init(x:y:z:)](<init(x_y_z_).md>) — Creates a rectangle mark for a 3D chart.
