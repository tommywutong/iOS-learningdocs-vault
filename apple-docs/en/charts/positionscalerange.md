---
title: PositionScaleRange
framework: Swift Charts
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/positionscalerange
source_url: 'https://developer.apple.com/documentation/charts/positionscalerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/positionscalerange.json'
content_hash: 'sha256:67127d989f2f8e74'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# PositionScaleRange

<sub>Protocol</sub>

A type that configures the x-axis and y-axis values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol PositionScaleRange : ScaleRange where Self.VisualValue == CGFloat
```

## Relationships

- **Inherits From**: [ScaleRange](scalerange.md)

- **Conforming Types**: [PlotDimensionScaleRange](plotdimensionscalerange.md)

## Topics

### Type Properties

- [plotDimension](positionscalerange/plotdimension.md) — A scale range that fills the plot area.

### Type Methods

- [plotDimension(padding:)](<positionscalerange/plotdimension(padding_).md>) — A scale range that fills the plot area with the given padding value at start and end.
- [plotDimension(startPadding:endPadding:)](<positionscalerange/plotdimension(startpadding_endpadding_).md>) — A scale range that fills the plot area with the given padding values at start and end, respectively.

## See Also

### Scales

- [ScaleRange](scalerange.md) — A type that you can use to configure the range of a chart.
- [PlotDimensionScaleRange](plotdimensionscalerange.md) — A range that represents the plot area’s width or height.
- [ScaleDomain](scaledomain.md) — A type that you can use to configure the domain of a chart.
- [AutomaticScaleDomain](automaticscaledomain.md) — A domain that the chart infers from its data.
- [ScaleType](scaletype.md) — The ways you can scale the domain or range of a plot.
