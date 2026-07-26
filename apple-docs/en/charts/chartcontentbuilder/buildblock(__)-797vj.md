---
title: 'buildBlock(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontentbuilder/buildblock(_:)-797vj'
source_url: 'https://developer.apple.com/documentation/charts/chartcontentbuilder/buildblock(_:)-797vj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontentbuilder/buildblock%28_%3A%29-797vj.json'
content_hash: 'sha256:c7b284dc4a795b10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContentBuilder](../chartcontentbuilder.md)

# buildBlock(_:)

<sub>Type Method</sub>

Builds a result from a single component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildBlock<C>(_ content: C) -> C where C : ChartContent
```

## Parameters

- `content` — The component.
