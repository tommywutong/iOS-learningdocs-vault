---
title: 'setViewports:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 14.5+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setviewports:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setviewports:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setviewports%3Acount%3A.json'
content_hash: 'sha256:0273ad10495256f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setViewports:count:

<sub>Instance Method</sub>

Configures the render pipeline with multiple viewports that apply transformations and clipping rectangles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setViewports:(const MTLViewport[]) viewports count:(NSUInteger) count;
```

## Parameters

- `viewports` — An array of [MTLViewport](../mtlviewport.md) instances the command applies to the render pipeline for transformations and clipping.

- `count` — The number of elements in the `viewports` array.

## Discussion

Use this method to configure multiple active viewports and corresponding scissor rectangles. Multiple viewports give your app the ability to draw into separate areas of an image with a single draw call. You can either set a single scissor rectangle for all viewports with the [- setScissorRect:](<setscissorrect(__).md>) method, or set each viewport’s rectangle with the [setScissorRects(_:)](<setscissorrects(__).md>) method.

> [!important] Important
> The number of scissor rectangles you pass to [setScissorRects(_:)](<setscissorrects(__).md>) needs to match the number of viewports you configure with this method.

The maximum number of viewports and scissor rectangles a GPU supports varies by device family. For more information, see [MTLGPUFamily](../mtlgpufamily.md) and [Detecting GPU features and Metal software versions](../detecting-gpu-features-and-metal-software-versions.md).

The rendering pipeline sends each primitive to a single viewport and its associated scissor rectangle. You can select which viewport each primitive uses in your vertex shader by adding the `[[viewport_array_index]]` attribute to an output value.

The render pipeline linearly maps vertex positions from normalized device coordinates to viewport coordinates by applying a viewport during the rasterization stage. It applies the transform first and then rasterizes the primitive while clipping any fragments outside the scissor rectangle (see [- setScissorRect:](<setscissorrect(__).md>)) or the render target’s extents.

The viewport’s [originX](../mtlviewport/originx.md) and [originY](../mtlviewport/originy.md) properties, which default to `0.0`, represent the number of pixels from the top-left corner of the render target. Positive [originX](../mtlviewport/originx.md) values go to the right and positive [originY](../mtlviewport/originy.md) values go downward. The default values for its [width](../mtlviewport/width.md) and [height](../mtlviewport/height.md) properties are the render target’s width and height, respectively. The default values for its [znear](../mtlviewport/znear.md) and [zfar](../mtlviewport/zfar.md) properties are `0.0` and `1.0`, respectively, which you can flip.

> [!note] Note
> You can change the render pass’s viewport configuration by calling this method again or by calling the [- setViewport:](<setviewport(__).md>) method.

The [- setViewport:](<setviewport(__).md>) method is equivalent to calling this method with a single viewport element in the `viewports` array.

## See Also

### Configuring viewport and scissor behavior

- [- setViewport:](<setviewport(__).md>) — Configures the render pipeline with a viewport that applies a transformation and a clipping rectangle.
- [- setScissorRect:](<setscissorrect(__).md>) — Configures a rectangle for the fragment scissor test.
- [setScissorRects:count:](setscissorrects_count_.md) — Configures multiple rectangles for the fragment scissor test.
