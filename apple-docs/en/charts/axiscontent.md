---
title: AxisContent
framework: Swift Charts
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/axiscontent
source_url: 'https://developer.apple.com/documentation/charts/axiscontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axiscontent.json'
content_hash: 'sha256:2ef0faf07e20d865'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# AxisContent

<sub>Protocol</sub>

A type that represents the elements you use to build a chart’s axes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AxisContent
```

## Relationships

- **Conforming Types**: [AnyAxisContent](anyaxiscontent.md), [AxisMarks](axismarks.md), [BuilderConditional](builderconditional.md)

## Topics

### Instance Methods

- [compositingLayer()](<axiscontent/compositinglayer().md>) — Creates a compositing layer for the axis content.
- [compositingLayer(style:)](<axiscontent/compositinglayer(style_).md>) — Creates a compositing layer for the axis content, and apply view modifiers to the compositing layer.

## See Also

### Axes

- [Customizing axes in Swift Charts](customizing-axes-in-swift-charts.md) — Improve the clarity of your chart by configuring the appearance of its axes.
- [ChartAxisContent](chartaxiscontent.md) — A view that represents a chart’s axis.
- [AxisMarks](axismarks.md) — A group of visual marks that a chart draws to indicate the composition of a chart’s axes.
- [AnyAxisContent](anyaxiscontent.md) — A type-erased element of a chart’s axis.
- [AxisContentBuilder](axiscontentbuilder.md) — A result builder that constructs axis content.
