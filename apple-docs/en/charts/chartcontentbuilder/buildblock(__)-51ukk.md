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
doc_path: '/documentation/charts/chartcontentbuilder/buildblock(_:)-51ukk'
source_url: 'https://developer.apple.com/documentation/charts/chartcontentbuilder/buildblock(_:)-51ukk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontentbuilder/buildblock%28_%3A%29-51ukk.json'
content_hash: 'sha256:422c47c58e6e327a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContentBuilder](../chartcontentbuilder.md)

# buildBlock(_:)

<sub>Type Method</sub>

Builds a result from multiple components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildBlock<each C>(_ content: repeat each C) -> some ChartContent where repeat each C : ChartContent

```

## Parameters

- `content` — The components.
