---
title: 'buildIf(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/axiscontentbuilder/buildif(_:)'
source_url: 'https://developer.apple.com/documentation/charts/axiscontentbuilder/buildif(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axiscontentbuilder/buildif%28_%3A%29.json'
content_hash: 'sha256:f4d60408656c1f36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AxisContentBuilder](../axiscontentbuilder.md)

# buildIf(_:)

<sub>Type Method</sub>

Provides support for “if” statements in multi-statement closures, producing an optional axis content that is visible only when the condition evaluates to `true`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildIf<T>(_ content: T?) -> T? where T : AxisContent
```
