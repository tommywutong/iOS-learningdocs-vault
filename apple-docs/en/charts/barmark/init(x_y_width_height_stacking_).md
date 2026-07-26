---
title: 'init(x:y:width:height:stacking:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/barmark/init(x:y:width:height:stacking:)'
source_url: 'https://developer.apple.com/documentation/charts/barmark/init(x:y:width:height:stacking:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/barmark/init%28x%3Ay%3Awidth%3Aheight%3Astacking%3A%29.json'
content_hash: 'sha256:08929bf5b4a901e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [BarMark](../barmark.md)

# init(x:y:width:height:stacking:)

<sub>Initializer</sub>

Creates a bar mark that plots values with x and y.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension = .automatic, height: MarkDimension = .automatic, stacking: MarkStackingMethod = .standard) where X : Plottable, Y : Plottable
```

## Parameters

- `x` — The value plotted with x.

- `y` — The value plotted with y.

- `width` — The bar width. If `width` is `nil`, the default bar size will be applied.

- `height` — The bar height. If `height` is `nil`, the default bar size will be applied.

- `stacking` — The stacking method for the bars with the same categorical/date values. If `stacking` is `nil`, the bars will not be stacked.

### Discussion

Use this initializer to create a chart with one or more bars.  For horizontal bars, plot categories or dates with y and numbers with x. For vertical bars, plot categories or dates with x and numbers with y:

```swift
Chart(data) {
    BarMark(
        x: .value("Department", $0.department),
        y: .value("Profit", $0.profit)
    )
}
```

![](../../../../attachments/a69f46e0c2563656f66919f67861d18e/BarMarkSwift.BarMarkBarChart@2x.png)

<sub>Vertical bar chart with x-axis showing department categories Production, Marketing, Finance and with y-axis ranging from 0 to 15000. There are 3 bars: Production 15000, Marketing 8000, Finance 10000.</sub>

## See Also

### Creating a bar mark

- [init(x:yStart:yEnd:width:)](<init(x_ystart_yend_width_).md>) — Creates a bar mark that plots values with x and its y interval.
- [init(xStart:xEnd:y:height:)](<init(xstart_xend_y_height_).md>) — Creates a bar mark that plots values with its x interval and y.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-98wo9.md>) — Creates a bar mark that plots values with its x interval and fixed y position.
- [init(xStart:xEnd:yStart:yEnd:)](<init(xstart_xend_ystart_yend_)-7541n.md>) — Creates a bar mark with fixed x interval that plots values with its y interval.
- [init(x:yStart:yEnd:width:stacking:)](<init(x_ystart_yend_width_stacking_).md>) — Creates a bar mark that plots a value on x with fixed y interval.
- [init(xStart:xEnd:y:height:stacking:)](<init(xstart_xend_y_height_stacking_).md>) — Creates a bar mark that plots values on y with fixed x interval.
