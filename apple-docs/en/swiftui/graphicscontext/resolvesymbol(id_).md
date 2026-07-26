---
title: 'resolveSymbol(id:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/resolvesymbol(id:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/resolvesymbol(id:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/resolvesymbol%28id%3A%29.json'
content_hash: 'sha256:3c2e79d1860d2565'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# resolveSymbol(id:)

<sub>Instance Method</sub>

Gets the identified child view as a resolved symbol, if the view exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resolveSymbol<ID>(id: ID) -> GraphicsContext.ResolvedSymbol? where ID : Hashable
```

## Parameters

- `id` — The value that you used to tag the view when you define it in the `symbols` parameter of the [Canvas](../canvas.md) initializer [init(opaque:colorMode:rendersAsynchronously:renderer:symbols:)](<../canvas/init(opaque_colormode_rendersasynchronously_renderer_symbols_).md>).

## Return Value

The resolved symbol, or `nil` if SwiftUI can’t find a child view with the given `id`.

## See Also

### Resolving a drawn entity

- [resolve(_:)](<resolve(__).md>) — Gets a version of an image that’s fixed with the current values of the graphics context’s environment.
- [ResolvedSymbol](resolvedsymbol.md) — A static sequence of drawing operations that may be drawn multiple times, preserving their resolution independence.
- [ResolvedImage](resolvedimage.md) — An image resolved to a particular environment.
- [ResolvedText](resolvedtext.md) — A text view resolved to a particular environment.
