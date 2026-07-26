---
title: 'setViewport(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setviewport(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setviewport(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setviewport%28_%3A%29.json'
content_hash: 'sha256:931cf85722464154'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setViewport(_:)

<sub>Instance Method</sub>

Configures the render pipeline with a viewport that applies a transformation and a clipping rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setViewport(_ viewport: MTLViewport)
```

## Parameters

- `viewport` — An [MTLViewport](../mtlviewport.md) instance the command applies to the render pipeline for transformations and clipping.

## Discussion

The render pipeline linearly maps vertex positions from normalized device coordinates to viewport coordinates by applying a viewport during the rasterization stage. It applies the transform first and then rasterizes the primitive while clipping any fragments outside the scissor rectangle (see [- setScissorRect:](<setscissorrect(__).md>)) or the render target’s extents.

The viewport’s [originX](../mtlviewport/originx.md) and [originY](../mtlviewport/originy.md) properties, which default to `0.0`, represent the number of pixels from the top-left corner of the render target. Positive [originX](../mtlviewport/originx.md) values go to the right and positive [originY](../mtlviewport/originy.md) values go downward. The default values for its [width](../mtlviewport/width.md) and [height](../mtlviewport/height.md) properties are the render target’s width and height, respectively. The default values for its [znear](../mtlviewport/znear.md) and [zfar](../mtlviewport/zfar.md) properties are `0.0` and `1.0`, respectively, which you can flip.

> [!note] Note
> You can change the render pass’s viewport configuration by calling this method again, or by calling the [setViewports(_:)](<setviewports(__).md>) method.

## See Also

### Configuring viewport and scissor behavior

- [setViewports(_:)](<setviewports(__).md>) — Configures the render pipeline with multiple viewports that apply transformations and clipping rectangles.
- [- setScissorRect:](<setscissorrect(__).md>) — Configures a rectangle for the fragment scissor test.
- [setScissorRects(_:)](<setscissorrects(__).md>) — Configures multiple rectangles for the fragment scissor test.
