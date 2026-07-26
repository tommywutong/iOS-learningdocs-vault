---
title: AxisMarkBuilder
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/axismarkbuilder
source_url: 'https://developer.apple.com/documentation/charts/axismarkbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axismarkbuilder.json'
content_hash: 'sha256:b707277ba4b75767'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# AxisMarkBuilder

<sub>Structure</sub>

A result builder that constructs axis marks and overrides default marks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@resultBuilder struct AxisMarkBuilder
```

## Topics

### Type Methods

- [buildBlock()](<axismarkbuilder/buildblock().md>)
- [buildBlock(_:)](<axismarkbuilder/buildblock(__)-5kk19.md>) — Builds a result from a single component.
- [buildBlock(_:)](<axismarkbuilder/buildblock(__)-97cxo.md>) — Builds a result from multiple components.
- [buildEither(first:)](<axismarkbuilder/buildeither(first_).md>) — Provides support for “if-else” statements in multi-statement closures, producing conditional content for the “then” branch.
- [buildEither(second:)](<axismarkbuilder/buildeither(second_).md>) — Provides support for “if-else” statements in multi-statement closures, producing conditional content for the “else” branch.
- [buildExpression(_:)](<axismarkbuilder/buildexpression(__).md>)
- [buildIf(_:)](<axismarkbuilder/buildif(__).md>) — Provides support for “if” statements in multi-statement closures, producing an optional axis content that is visible only when the condition evaluates to `true`.
- [buildLimitedAvailability(_:)](<axismarkbuilder/buildlimitedavailability(__).md>) — Provides support for “if” statements with `#available()` clauses in multi-statement closures, producing conditional content for the “then” branch, i.e. the conditionally-available branch.

## See Also

### Axis marks

- [AxisMark](axismark.md) — A type that serves as the basic building block for the elements of an axis.
- [AxisTick](axistick.md) — A mark that a chart draws on an axis to indicate a reference point along that axis.
- [AxisGridLine](axisgridline.md) — A line that a chart draws across its plot area to indicate a reference point along a particular axis.
- [AxisValueLabel](axisvaluelabel.md) — A label that describes the value for an axis mark.
- [AxisValue](axisvalue.md) — A value for an axis mark.
- [AnyAxisMark](anyaxismark.md) — A type-erased axis mark.
