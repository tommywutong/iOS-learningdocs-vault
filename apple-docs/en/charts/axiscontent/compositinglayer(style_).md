---
title: 'compositingLayer(style:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/axiscontent/compositinglayer(style:)'
source_url: 'https://developer.apple.com/documentation/charts/axiscontent/compositinglayer(style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axiscontent/compositinglayer%28style%3A%29.json'
content_hash: 'sha256:4e57899b06d7b66c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AxisContent](../axiscontent.md)

# compositingLayer(style:)

<sub>Instance Method</sub>

Creates a compositing layer for the axis content, and apply view modifiers to the compositing layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compositingLayer<V>(@ViewBuilder style: (PlaceholderContentView<Self>) -> V) -> some AxisContent where V : View

```

## Parameters

- `style` — A closure that applies view modifiers to the compositing layer.
