---
title: ScaleType
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/scaletype
source_url: 'https://developer.apple.com/documentation/charts/scaletype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/scaletype.json'
content_hash: 'sha256:b11d0b18f8188929'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# ScaleType

<sub>Structure</sub>

The ways you can scale the domain or range of a plot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ScaleType
```

## Overview

Use this type with the `type:` parameter of `.chartXScale` view modifiers to customize scale types.

## Topics

### Type Properties

- [category](scaletype/category.md) — A scale that has discrete domain values as inputs.
- [date](scaletype/date.md) — A date scale where each range value y can be expressed as a function of the domain value x’s timestamp, with `y = a * x.timeIntervalSinceReferenceDate + b`.
- [linear](scaletype/linear.md) — A number scale where each range value y can be expressed as a linear function of the domain value x, with `y = a * x + b`.
- [log](scaletype/log.md) — A number scale where each range value y can be expressed as a logarithmic function of the domain value x, with `y = a * log(x) + b`.
- [squareRoot](scaletype/squareroot.md) — A number scale where each range value y can be expressed as a square root function of the domain value x, with `y = a * sqrt(x) + b`. This is equivalent to a power scale with exponent 0.5.
- [symmetricLog](scaletype/symmetriclog.md) — A number scale where each range value y can be expressed as a symmetric log function of the domain value x, with `y = a * sign(x) * log(1 + |x * slopeAtZero|) + b`. The constant `slopeAtZero` defaults to 1. You can configure it with `symmetricLog(slopeAtZero:)`.

### Type Methods

- [power(exponent:)](<scaletype/power(exponent_).md>) — A number scale where each range value y can be expressed as a power function of the domain value x, with `y = a * pow(x, exponent) + b`.
- [symmetricLog(slopeAtZero:)](<scaletype/symmetriclog(slopeatzero_).md>) — A number scale where each range value y can be expressed as a symmetric log function of the domain value x, with `y = a * sign(x) * log(1 + |x * slopeAtZero|) + b`.

## See Also

### Scales

- [ScaleRange](scalerange.md) — A type that you can use to configure the range of a chart.
- [PositionScaleRange](positionscalerange.md) — A type that configures the x-axis and y-axis values.
- [PlotDimensionScaleRange](plotdimensionscalerange.md) — A range that represents the plot area’s width or height.
- [ScaleDomain](scaledomain.md) — A type that you can use to configure the domain of a chart.
- [AutomaticScaleDomain](automaticscaledomain.md) — A domain that the chart infers from its data.
