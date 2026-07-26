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
doc_path: '/documentation/charts/axiscontentbuilder/buildlimitedavailability(_:)'
source_url: 'https://developer.apple.com/documentation/charts/axiscontentbuilder/buildlimitedavailability(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axiscontentbuilder/buildlimitedavailability%28_%3A%29.json'
content_hash: 'sha256:aff3097f8127ad20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AxisContentBuilder](../axiscontentbuilder.md)

# buildLimitedAvailability(_:)

<sub>Type Method</sub>

Provides support for “if” statements with `#available()` clauses in multi-statement closures, producing conditional content for the “then” branch, i.e. the conditionally-available branch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildLimitedAvailability<Content>(_ content: Content) -> AnyAxisContent where Content : AxisContent
```
