---
title: ChartContentBuilder
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/chartcontentbuilder
source_url: 'https://developer.apple.com/documentation/charts/chartcontentbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontentbuilder.json'
content_hash: 'sha256:cc257f6e72458bd8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# ChartContentBuilder

<sub>Structure</sub>

A result builder that you use to compose the contents of a chart.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@resultBuilder struct ChartContentBuilder
```

## Overview

This [Result Builder](https://docs.swift.org/swift-book/LanguageGuide/AdvancedOperators.html#ID630) combines any number of [ChartContent](chartcontent.md) instances into a single composite instance, including support for conditionals.

You don’t call the methods of the result builder directly. Instead, Swift uses them to combine the elements that you declare in any closure that has the `@ChartContentBuilder` attribute. In particular, you rely on this behavior when you declare the `content` inside a [Chart](chart.md) initializer like [init(content:)](<chart/init(content_).md>).

## Topics

### Building chart content

- [buildBlock()](<chartcontentbuilder/buildblock().md>) — Produces empty chart content.

### Building conditionally

- [buildIf(_:)](<chartcontentbuilder/buildif(__).md>) — Builds a partial result that’s conditionally present.
- [buildEither(first:)](<chartcontentbuilder/buildeither(first_).md>) — Builds a partial result from a condition that’s true.
- [buildEither(second:)](<chartcontentbuilder/buildeither(second_).md>) — Builds a partial result from a condition that’s false.

### Building with conditional availability

- [buildLimitedAvailability(_:)](<chartcontentbuilder/buildlimitedavailability(__).md>) — Builds a partial result that propagates or erases type information outside a compiler-controlled availability check.

### Supporting types

- [BuilderConditional](builderconditional.md) — A conditional result from a result builder.

### Type Methods

- [buildBlock(_:)](<chartcontentbuilder/buildblock(__)-51ukk.md>) — Builds a result from multiple components.
- [buildBlock(_:)](<chartcontentbuilder/buildblock(__)-797vj.md>) — Builds a result from a single component.
- [buildExpression(_:)](<chartcontentbuilder/buildexpression(__).md>)

## See Also

### Charts

- [Creating a chart using Swift Charts](creating-a-chart-using-swift-charts.md) — Make a chart by combining chart building blocks in SwiftUI.
- [Visualizing your app’s data](visualizing-your-app-s-data.md) — Build complex and interactive charts using Swift Charts.
- [Chart](chart.md) — A SwiftUI view that displays a chart.
- [ChartContent](chartcontent.md) — A type that represents the content that you draw on a chart.
- [Plot](plot.md) — A mechanism for grouping chart contents into a single entity.
