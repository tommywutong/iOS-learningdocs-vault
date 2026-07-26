---
title: 'alphaMultiply(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/filter/alphamultiply(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/alphamultiply(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/alphamultiply%28_%3A%29.json'
content_hash: 'sha256:b42d693b108fbc7d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# alphaMultiply(_:)

<sub>Type Method</sub>

Returns a filter that multiplies the alpha component by a given color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func alphaMultiply(_ color: Color) -> GraphicsContext.Filter
```

## Parameters

- `color` — The color that the filter uses for the multiplication operation.

## Return Value

A filter that multiplies the alpha component.
