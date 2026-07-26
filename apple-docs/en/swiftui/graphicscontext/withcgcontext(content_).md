---
title: 'withCGContext(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/withcgcontext(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/withcgcontext(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/withcgcontext%28content%3A%29.json'
content_hash: 'sha256:b3bb5574e27a043c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# withCGContext(content:)

<sub>Instance Method</sub>

Provides a Core Graphics context that you can use as a proxy to draw into this context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withCGContext(content: (CGContext) throws -> Void) rethrows
```

## Parameters

- `content` — A closure that receives a [CGContext](../../coregraphics/cgcontext.md) that you use to perform drawing operations, just like you draw into a [GraphicsContext](../graphicscontext.md) instance. Any filters, blend mode settings, clip masks, and other state set before calling `withCGContext(content:)` apply to drawing operations in the Core Graphics context as well. Any state you set on the Core Graphics context is lost when the closure returns. Accessing the Core Graphics context after the closure returns produces undefined behavior.

## Discussion

Use this method to use existing drawing code that relies on Core Graphics primitives.
