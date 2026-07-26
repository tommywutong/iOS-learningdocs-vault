---
title: ChartSymbolShape
framework: Swift Charts
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/chartsymbolshape
source_url: 'https://developer.apple.com/documentation/charts/chartsymbolshape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartsymbolshape.json'
content_hash: 'sha256:a48298897751c767'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# ChartSymbolShape

<sub>Protocol</sub>

A type that can act as a shape for the marks that you add to a chart.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ChartSymbolShape : Shape
```

## Relationships

- **Inherits From**: [Animatable](../swiftui/animatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Shape](../swiftui/shape.md), [View](../swiftui/view.md)

- **Conforming Types**: [AnyChartSymbolShape](anychartsymbolshape.md), [BasicChartSymbolShape](basicchartsymbolshape.md)

## Topics

### Instance Properties

- [perceptualUnitRect](chartsymbolshape/perceptualunitrect.md) — Returns a rectangle that bounds the shape in such a way that viewers perceive it as having the same size and position as a unit rectangle.

### Instance Methods

- [strokeBorder(lineWidth:)](<chartsymbolshape/strokeborder(linewidth_).md>)
- [strokeBorder(style:)](<chartsymbolshape/strokeborder(style_).md>)

### Type Properties

- [asterisk](chartsymbolshape/asterisk.md) — Asterisk symbol.
- [circle](chartsymbolshape/circle.md) — Circle symbol.
- [cross](chartsymbolshape/cross.md) — Cross symbol.
- [diamond](chartsymbolshape/diamond.md) — Diamond symbol.
- [pentagon](chartsymbolshape/pentagon.md) — Pentagon symbol.
- [plus](chartsymbolshape/plus.md) — Plus symbol.
- [square](chartsymbolshape/square.md) — Square symbol.
- [triangle](chartsymbolshape/triangle.md) — Triangle symbol.

## See Also

### Mark configuration

- [MarkStackingMethod](markstackingmethod.md) — The ways in which you can stack marks in a chart.
- [MarkDimension](markdimension.md) — An individual dimension representing a mark’s width or height.
- [InterpolationMethod](interpolationmethod.md) — The ways in which line or area marks interpolate their data.
- [BasicChartSymbolShape](basicchartsymbolshape.md) — A basic chart symbol shape.
- [AnyChartSymbolShape](anychartsymbolshape.md) — A type-erased plotting shape.
