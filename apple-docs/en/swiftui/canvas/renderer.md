---
title: renderer
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/canvas/renderer
source_url: 'https://developer.apple.com/documentation/swiftui/canvas/renderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/canvas/renderer.json'
content_hash: 'sha256:c4cf9f7e6e07956a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Canvas](../canvas.md)

# renderer

<sub>Instance Property</sub>

The drawing callback that you use to draw into the canvas.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var renderer: (inout GraphicsContext, CGSize) -> Void
```

## Parameters

- `context` — The graphics context to draw into.

- `size` — The current size of the view.

## See Also

### Rendering

- [rendersAsynchronously](rendersasynchronously.md) — A Boolean that indicates whether the canvas can present its contents to its parent view asynchronously.
