---
title: 'meshGradient(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/shading/meshgradient(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/shading/meshgradient(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/shading/meshgradient%28_%3A%29.json'
content_hash: 'sha256:6d93fc6ce4978adc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Shading](../shading.md)

# meshGradient(_:)

<sub>Type Method</sub>

Returns a shading instance that fills with a mesh gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func meshGradient(_ mesh: MeshGradient) -> GraphicsContext.Shading
```

## Parameters

- `mesh` — The mesh gradient defining the filled colors.

## Return Value

A shading that fills using the mesh gradient.
