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
doc_path: '/documentation/charts/axismarkbuilder/buildblock(_:)-97cxo'
source_url: 'https://developer.apple.com/documentation/charts/axismarkbuilder/buildblock(_:)-97cxo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axismarkbuilder/buildblock%28_%3A%29-97cxo.json'
content_hash: 'sha256:0174606aad8e1814'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AxisMarkBuilder](../axismarkbuilder.md)

# buildBlock(_:)

<sub>Type Method</sub>

Builds a result from multiple components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildBlock<each T>(_ content: repeat each T) -> some AxisMark where repeat each T : AxisMark

```

## Parameters

- `content` — The components.
