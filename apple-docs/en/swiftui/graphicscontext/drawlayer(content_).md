---
title: 'drawLayer(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/drawlayer(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/drawlayer(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/drawlayer%28content%3A%29.json'
content_hash: 'sha256:1b0873ecbc30539a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# drawLayer(content:)

<sub>Instance Method</sub>

Draws a new layer, created by drawing code that you provide, into the context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func drawLayer(content: (inout GraphicsContext) throws -> Void) rethrows
```

## Parameters

- `content` — A closure that receives a new [GraphicsContext](../graphicscontext.md) as input. This context represents a new transparency layer that you can draw into. When the closure returns, SwiftUI draws the new layer into the current context.
