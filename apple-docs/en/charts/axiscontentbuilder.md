---
title: AxisContentBuilder
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/axiscontentbuilder
source_url: 'https://developer.apple.com/documentation/charts/axiscontentbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axiscontentbuilder.json'
content_hash: 'sha256:961bb9b0dfc1706d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# AxisContentBuilder

<sub>Structure</sub>

A result builder that constructs axis content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@resultBuilder struct AxisContentBuilder
```

## Topics

### Type Methods

- [buildBlock()](<axiscontentbuilder/buildblock().md>)
- [buildBlock(_:)](<axiscontentbuilder/buildblock(__)-27fku.md>) — Builds a result from a single component.
- [buildBlock(_:)](<axiscontentbuilder/buildblock(__)-6p3cy.md>) — Builds a result from multiple components.
- [buildEither(first:)](<axiscontentbuilder/buildeither(first_).md>) — Provides support for “if-else” statements in multi-statement closures, producing conditional content for the “then” branch.
- [buildEither(second:)](<axiscontentbuilder/buildeither(second_).md>) — Provides support for “if-else” statements in multi-statement closures, producing conditional content for the “else” branch.
- [buildExpression(_:)](<axiscontentbuilder/buildexpression(__).md>)
- [buildIf(_:)](<axiscontentbuilder/buildif(__).md>) — Provides support for “if” statements in multi-statement closures, producing an optional axis content that is visible only when the condition evaluates to `true`.
- [buildLimitedAvailability(_:)](<axiscontentbuilder/buildlimitedavailability(__).md>) — Provides support for “if” statements with `#available()` clauses in multi-statement closures, producing conditional content for the “then” branch, i.e. the conditionally-available branch.

## See Also

### Axes

- [Customizing axes in Swift Charts](customizing-axes-in-swift-charts.md) — Improve the clarity of your chart by configuring the appearance of its axes.
- [ChartAxisContent](chartaxiscontent.md) — A view that represents a chart’s axis.
- [AxisContent](axiscontent.md) — A type that represents the elements you use to build a chart’s axes.
- [AxisMarks](axismarks.md) — A group of visual marks that a chart draws to indicate the composition of a chart’s axes.
- [AnyAxisContent](anyaxiscontent.md) — A type-erased element of a chart’s axis.
