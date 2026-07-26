---
title: 'projectionTransform(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/filter/projectiontransform(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/projectiontransform(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/projectiontransform%28_%3A%29.json'
content_hash: 'sha256:7d15850b1321f127'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# projectionTransform(_:)

<sub>Type Method</sub>

Returns a filter that transforms the rasterized form of subsequent graphics primitives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func projectionTransform(_ matrix: ProjectionTransform) -> GraphicsContext.Filter
```

## Parameters

- `matrix` — A projection transform to apply to the rasterized form of graphics primitives.

## Return Value

A filter that applies a transform.
