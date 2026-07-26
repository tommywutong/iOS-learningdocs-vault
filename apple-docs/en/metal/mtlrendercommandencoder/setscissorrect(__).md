---
title: 'setScissorRect(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setscissorrect(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setscissorrect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setscissorrect%28_%3A%29.json'
content_hash: 'sha256:c532b969b66a6b5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setScissorRect(_:)

<sub>Instance Method</sub>

Configures a rectangle for the fragment scissor test.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setScissorRect(_ rect: MTLScissorRect)
```

## Parameters

- `rect` — An [MTLScissorRect](../mtlscissorrect.md) instance that represents a rectangle that needs to lie completely within the current render attachment.

## Discussion

The rendering pipeline discards any fragments that lie outside the scissor rectangle.

The default scissor rectangle is the same size as the current render attachment, with its origin coordinates in the upper-left corner at `(0, 0)`.

> [!note] Note
> You can change the render pass’s scissor rectangle configuration by calling this method again or by calling the [setScissorRects(_:)](<setscissorrects(__).md>) method.

## See Also

### Configuring viewport and scissor behavior

- [- setViewport:](<setviewport(__).md>) — Configures the render pipeline with a viewport that applies a transformation and a clipping rectangle.
- [setViewports(_:)](<setviewports(__).md>) — Configures the render pipeline with multiple viewports that apply transformations and clipping rectangles.
- [setScissorRects(_:)](<setscissorrects(__).md>) — Configures multiple rectangles for the fragment scissor test.
