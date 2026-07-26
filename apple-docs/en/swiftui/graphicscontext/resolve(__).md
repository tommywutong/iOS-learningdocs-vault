---
title: 'resolve(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/resolve(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/resolve(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/resolve%28_%3A%29.json'
content_hash: 'sha256:5a7e1dc7014d2a95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# resolve(_:)

<sub>Instance Method</sub>

Gets a version of an image that’s fixed with the current values of the graphics context’s environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resolve(_ image: Image) -> GraphicsContext.ResolvedImage
```

## Parameters

- `image` — The [Image](../image.md) to resolve.

## Return Value

An image that’s resolved into the current context’s environment, taking into account environment values like the display resolution and current color scheme.

## Discussion

You can measure the resolved image by looking at its [size](resolvedimage/size.md) and [baseline](resolvedimage/baseline.md) properties. You can draw the resolved image with the context’s [draw(_:in:style:)](<draw(__in_style_)-7rvee.md>) or [draw(_:at:anchor:)](<draw(__at_anchor_)-1z5wt.md>) method.

## See Also

### Resolving a drawn entity

- [resolveSymbol(id:)](<resolvesymbol(id_).md>) — Gets the identified child view as a resolved symbol, if the view exists.
- [ResolvedSymbol](resolvedsymbol.md) — A static sequence of drawing operations that may be drawn multiple times, preserving their resolution independence.
- [ResolvedImage](resolvedimage.md) — An image resolved to a particular environment.
- [ResolvedText](resolvedtext.md) — A text view resolved to a particular environment.
