---
title: 'init(x:yStart:yEnd:width:stacking:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/barmark/init(x:ystart:yend:width:stacking:)'
source_url: 'https://developer.apple.com/documentation/charts/barmark/init(x:ystart:yend:width:stacking:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/barmark/init%28x%3Aystart%3Ayend%3Awidth%3Astacking%3A%29.json'
content_hash: 'sha256:5eee57592d65ed15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [BarMark](../barmark.md)

# init(x:yStart:yEnd:width:stacking:)

<sub>Initializer</sub>

Creates a bar mark that plots a value on x with fixed y interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<X>(x: PlottableValue<X>, yStart: CGFloat? = nil, yEnd: CGFloat? = nil, width: MarkDimension = .automatic, stacking: MarkStackingMethod = .standard) where X : Plottable
```

## Parameters

- `x` — The value plotted with x.

- `yStart` — The y start position. If `yStart` is `nil` then the rectangle will start at the leading edge of the plotting area.

- `yEnd` — The y end position. If `yEnd` is `nil` then the rectangle will end at the trailing edge of the plotting area.

- `width` — The bar width.  If `width` is `nil`, the default bar size will be applied.

- `stacking` — The stacking method for the bars with the same categorical/date values. If `stacking` is `nil`, the bars will not be stacked.

### Discussion

Use this initializer to create a chart with a single horizontal bar:

```swift
Chart(data) {
    BarMark(
        x: .value("Profit", $0.profit)
    )
    .foregroundStyle(by: .value("Product Category", $0.productCategory))
}
```

![](../../../../attachments/866989cb862990508465e796c804535b/BarMarkSwift.BarMarkHorizontalStacked1DBarChartWithForegroundColor@2x.png)

<sub>Horizontal bar chart with one bar on the x-axis showing profit ranging from 0 to 15000 with stacked categories Gizmos, Gadgets and Widgets. Legend showing the color mapped to a product category.</sub>

## See Also

### Creating a bar mark

- [init(x:yStart:yEnd:width:)](<init(x_ystart_yend_width_).md>) — Creates a bar mark that plots values with x and its y interval.
- [init(xStart:xEnd:y:height:)](<init(xstart_xend_y_height_).md>) — Creates a bar mark that plots values with its x interval and y.
- [init(x:y:width:height:stacking:)](<init(x_y_width_height_stacking_).md>) — Creates a bar mark that plots values with x and y.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-98wo9.md>) — Creates a bar mark that plots values with its x interval and fixed y position.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-7541n.md>) — Creates a bar mark with fixed x interval that plots values with its y interval.
- [init(x:y:width:height:stacking:)](<init(x_y_width_height_stacking_).md>) — Creates a bar mark that plots values with x and y.
- [init(xStart:xEnd:y:height:stacking:)](<init(xstart_xend_y_height_stacking_).md>) — Creates a bar mark that plots values on y with fixed x interval.
