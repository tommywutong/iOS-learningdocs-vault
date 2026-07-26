---
title: 'draw(_:in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/draw(_:in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/draw(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/draw%28_%3Ain%3A%29.json'
content_hash: 'sha256:ba3e128d0e9b415f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# draw(_:in:)

<sub>Instance Method</sub>

Draws a resolved symbol into the context, using the specified rectangle as a layout frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func draw(_ symbol: GraphicsContext.ResolvedSymbol, in rect: CGRect)
```

## Parameters

- `symbol` — The [ResolvedSymbol](resolvedsymbol.md) to draw. Get a resolved symbol by calling [resolveSymbol(id:)](<resolvesymbol(id_).md>) with the identifier that you use to tag the corresponding child view during [Canvas](../canvas.md) initialization.

- `rect` — The rectangle in the current user space to draw the symbol in.

## Discussion

The current context state defines the full drawing operation. For example, the current transformation and clip shapes affect how SwiftUI draws the symbol.

## See Also

### Drawing images, text, and views

- [draw(_:in:style:)](<draw(__in_style_).md>) — Draws a resolved image into the context, using the specified rectangle as a layout frame.
- [draw(_:at:anchor:)](<draw(__at_anchor_).md>) — Draws a resolved image into the context, aligning an anchor within the image to a point in the context.
