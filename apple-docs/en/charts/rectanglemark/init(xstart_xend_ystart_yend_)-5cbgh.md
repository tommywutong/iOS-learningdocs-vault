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
doc_path: '/documentation/charts/rectanglemark/init(xstart:xend:ystart:yend:)-5cbgh'
source_url: 'https://developer.apple.com/documentation/charts/rectanglemark/init(xstart:xend:ystart:yend:)-5cbgh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/rectanglemark/init%28xstart%3Axend%3Aystart%3Ayend%3A%29-5cbgh.json'
content_hash: 'sha256:b3681d6053f1e50c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [RectangleMark](../rectanglemark.md)

# init(xStart:xEnd:yStart:yEnd:)

<sub>Initializer</sub>

Creates a rectangle mark with a y interval encoding and a fixed x interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<Y>(xStart: CGFloat? = nil, xEnd: CGFloat? = nil, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>) where Y : Plottable
```

## Discussion

- yStart: The value plotted with y end.
- yEnd: The value plotted with y end.
- xStart: The x start position. If `xStart` is `nil` then the rectangle will start at the leading edge of the plotting area.
- xEnd: The x end position. If `xEnd` is `nil` then the rectangle will end at the trailing edge of the plotting area.

### Discussion

Use this initializer to map the y start and y end position to a rectangle for each data element. Optionally, specify the xStart or xEnd position of the rectangles.

The example below omits the optional `x` and `width` fields and uses a number scale starting at (0,0) and ending at (6,6). The rectangle has the coordinates: (0,2), (0,4), (6,4), (6,2).

```swift
Chart(data) {
    RectangleMark(
        yStart: .value("Rect yStart", 2),
        yEnd: .value("Rect yEnd", 4)
    )
    .opacity(0.2)

    PointMark(
        x: .value("X", $0.x),
        y: .value("Y", $0.y)
    )
}
```

![](../../../../attachments/cd82c66494023d9087b825e3843c8322/RectangleMarkSwift.RectangleMarkScatterWithRectangleYInterval@2x.png)

<sub>Scatter plot chart with a rectangle mark annotation. 3 points on the chart at: (5, 5), (2.5, 2.5), (3, 3) the rectangle highlights a rectangular area with coordinates: (0,2), (0,4), (6,4), (6,2).</sub>

## See Also

### Creating a rectangle mark

- [init(x:yStart:yEnd:width:)](<init(x_ystart_yend_width_)-vh2x.md>) — Creates a rectangle mark with an y interval encoding and an x encoding.
- [init(x:yStart:yEnd:width:)](<init(x_ystart_yend_width_)-xhqp.md>) — Creates a rectangle mark that plots values on x and has a fixed y interval.
- [init(xStart:xEnd:y:height:)](<init(xstart_xend_y_height_)-27222.md>) — Creates a rectangle mark with an x interval encoding and a y encoding.
- [init(xStart:xEnd:y:height:)](<init(xstart_xend_y_height_)-4x46i.md>) — Creates a rectangle mark with a fixed x interval and y encoding.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-1qbzg.md>) — Creates a rectangle mark with x and y interval encodings.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-5682c.md>) — Creates a rectangle mark with fixed x and y intervals.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-6jeka.md>) — Creates a rectangle mark with an x interval encoding and a fixed y interval.
- [init(x:y:width:height:)](<init(x_y_width_height_).md>) — Creates a rectangle that plots values with x and y.
- [init(x:y:z:)](<init(x_y_z_).md>) — Creates a rectangle mark for a 3D chart.
