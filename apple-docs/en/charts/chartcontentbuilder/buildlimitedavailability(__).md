---
title: 'buildLimitedAvailability(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontentbuilder/buildlimitedavailability(_:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontentbuilder/buildlimitedavailability(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontentbuilder/buildlimitedavailability%28_%3A%29.json'
content_hash: 'sha256:13b3c46b68b5c050'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContentBuilder](../chartcontentbuilder.md)

# buildLimitedAvailability(_:)

<sub>Type Method</sub>

Builds a partial result that propagates or erases type information outside a compiler-controlled availability check.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildLimitedAvailability(_ content: some ChartContent) -> AnyChartContent
```

## Discussion

This method provides support for `if` statements with `#available()` clauses in multi-statement closures, producing content for the conditionally-available branch.
