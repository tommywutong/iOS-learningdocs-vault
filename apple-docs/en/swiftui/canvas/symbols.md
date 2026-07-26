---
title: symbols
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/canvas/symbols
source_url: 'https://developer.apple.com/documentation/swiftui/canvas/symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/canvas/symbols.json'
content_hash: 'sha256:8a9a658dd4510125'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Canvas](../canvas.md)

# symbols

<sub>Instance Property</sub>

A view that provides child views that you can use in the drawing callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var symbols: Symbols
```

## Discussion

Uniquely tag each child view using the `View/tag(_:)` modifier, so that you can find them from within your renderer using the [resolveSymbol(id:)](<../graphicscontext/resolvesymbol(id_).md>) method.
