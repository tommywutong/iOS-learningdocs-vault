---
title: AxisMark
framework: Swift Charts
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/axismark
source_url: 'https://developer.apple.com/documentation/charts/axismark'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axismark.json'
content_hash: 'sha256:f8a09b9f0839c243'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# AxisMark

<sub>Protocol</sub>

A type that serves as the basic building block for the elements of an axis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AxisMark
```

## Relationships

- **Conforming Types**: [AnyAxisMark](anyaxismark.md), [AxisGridLine](axisgridline.md), [AxisTick](axistick.md), [AxisValueLabel](axisvaluelabel.md), [BuilderConditional](builderconditional.md)

## Topics

### Instance Methods

- [font(_:)](<axismark/font(__).md>) — Sets the default font for text in this axis content.
- [foregroundStyle(_:)](<axismark/foregroundstyle(__).md>) — Sets the axis content’s foreground elements to use a given style.
- [offset(_:)](<axismark/offset(__).md>)
- [offset(x:y:)](<axismark/offset(x_y_).md>)

## See Also

### Axis marks

- [AxisTick](axistick.md) — A mark that a chart draws on an axis to indicate a reference point along that axis.
- [AxisGridLine](axisgridline.md) — A line that a chart draws across its plot area to indicate a reference point along a particular axis.
- [AxisValueLabel](axisvaluelabel.md) — A label that describes the value for an axis mark.
- [AxisValue](axisvalue.md) — A value for an axis mark.
- [AnyAxisMark](anyaxismark.md) — A type-erased axis mark.
- [AxisMarkBuilder](axismarkbuilder.md) — A result builder that constructs axis marks and overrides default marks.
