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
doc_path: '/documentation/charts/axiscontentbuilder/buildblock(_:)-6p3cy'
source_url: 'https://developer.apple.com/documentation/charts/axiscontentbuilder/buildblock(_:)-6p3cy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axiscontentbuilder/buildblock%28_%3A%29-6p3cy.json'
content_hash: 'sha256:0edc1a7c56ebf768'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AxisContentBuilder](../axiscontentbuilder.md)

# buildBlock(_:)

<sub>Type Method</sub>

Builds a result from multiple components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildBlock<each T>(_ content: repeat each T) -> some AxisContent where repeat each T : AxisContent

```

## Parameters

- `content` — The components.
