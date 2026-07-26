---
title: MarkDimension
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/markdimension
source_url: 'https://developer.apple.com/documentation/charts/markdimension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/markdimension.json'
content_hash: 'sha256:273be305d3631f04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# MarkDimension

<sub>Structure</sub>

An individual dimension representing a mark’s width or height.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct MarkDimension
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Escapable](../swift/escapable.md), [ExpressibleByFloatLiteral](../swift/expressiblebyfloatliteral.md), [ExpressibleByIntegerLiteral](../swift/expressiblebyintegerliteral.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Supporting types

- [MarkDimensions](markdimensions.md)

### Initializers

- [init(floatLiteral:)](<markdimension/init(floatliteral_).md>) — Creates a constant width or height from a floating point value.
- [init(integerLiteral:)](<markdimension/init(integerliteral_).md>) — Creates a constant width or height from an integer.

### Type Properties

- [automatic](markdimension/automatic.md) — A dimension that determines its value automatically.

### Type Methods

- [fixed(_:)](<markdimension/fixed(__).md>) — A constant dimension.
- [inset(_:)](<markdimension/inset(__).md>) — A dimension that’s the step size minus the specified inset value on each side.
- [ratio(_:)](<markdimension/ratio(__).md>) — A dimension that’s proportional to the scale step size, using the specified ratio.

## See Also

### Mark configuration

- [MarkStackingMethod](markstackingmethod.md) — The ways in which you can stack marks in a chart.
- [InterpolationMethod](interpolationmethod.md) — The ways in which line or area marks interpolate their data.
- [BasicChartSymbolShape](basicchartsymbolshape.md) — A basic chart symbol shape.
- [ChartSymbolShape](chartsymbolshape.md) — A type that can act as a shape for the marks that you add to a chart.
- [AnyChartSymbolShape](anychartsymbolshape.md) — A type-erased plotting shape.
