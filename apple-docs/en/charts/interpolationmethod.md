---
title: InterpolationMethod
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/interpolationmethod
source_url: 'https://developer.apple.com/documentation/charts/interpolationmethod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/interpolationmethod.json'
content_hash: 'sha256:d1ad43a18c244bbb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# InterpolationMethod

<sub>Structure</sub>

The ways in which line or area marks interpolate their data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct InterpolationMethod
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [cardinal](interpolationmethod/cardinal.md) — Interpolate data points with cardinal spline.
- [catmullRom](interpolationmethod/catmullrom.md) — Interpolate data points with Catmull-Rom spline.
- [linear](interpolationmethod/linear.md) — Interpolate data points linearly.
- [monotone](interpolationmethod/monotone.md) — Interpolate data points with a cubic spline that preserves monotonicity of the data.
- [stepCenter](interpolationmethod/stepcenter.md) — Interpolate data points with a step, or piece-wise constant function, where the data point is at the center of the step.
- [stepEnd](interpolationmethod/stepend.md) — Interpolate data points with a step, or piece-wise constant function, where the data point is at the end of the step.
- [stepStart](interpolationmethod/stepstart.md) — Interpolate data points with a step, or piece-wise constant function, where the data point is at the start of the step.

### Type Methods

- [cardinal(tension:)](<interpolationmethod/cardinal(tension_).md>) — Interpolate data points with cardinal spline, using the given tension parameter.
- [catmullRom(alpha:)](<interpolationmethod/catmullrom(alpha_).md>) — Interpolate data points with Catmull-Rom spline, using the given alpha parameter.

## See Also

### Mark configuration

- [MarkStackingMethod](markstackingmethod.md) — The ways in which you can stack marks in a chart.
- [MarkDimension](markdimension.md) — An individual dimension representing a mark’s width or height.
- [BasicChartSymbolShape](basicchartsymbolshape.md) — A basic chart symbol shape.
- [ChartSymbolShape](chartsymbolshape.md) — A type that can act as a shape for the marks that you add to a chart.
- [AnyChartSymbolShape](anychartsymbolshape.md) — A type-erased plotting shape.
