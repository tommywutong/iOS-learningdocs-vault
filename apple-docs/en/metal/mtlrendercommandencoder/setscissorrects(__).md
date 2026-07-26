---
title: 'setScissorRects(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.13+, tvOS 14.5+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setscissorrects(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setscissorrects(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setscissorrects%28_%3A%29.json'
content_hash: 'sha256:5150e54dc15bcf8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setScissorRects(_:)

<sub>Instance Method</sub>

Configures multiple rectangles for the fragment scissor test.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setScissorRects(_ scissorRects: [MTLScissorRect])
```

## Parameters

- `scissorRects` — An array of [MTLScissorRect](../mtlscissorrect.md) instances the command applies to the render pipeline for clipping.

## Discussion

The rendering pipeline discards any fragments that lie outside the scissor rectangle. The default scissor rectangle is the same size as the current render attachment, with its origin coordinates in the upper-left corner at `(0, 0)`.

Use this method to configure a different scissor rectangle for multiple viewports you configure with the [setViewports(_:)](<setviewports(__).md>) method. Multiple viewports give your app the ability to draw into separate areas of an image with a single draw call. You can either set a single scissor rectangle for all viewports with the [- setScissorRect:](<setscissorrect(__).md>) method, or set each viewport’s rectangle with this method.

> [!important] Important
> The number of scissor rectangles you pass to this method needs to match the number of viewports you configure with the [setViewports(_:)](<setviewports(__).md>) method.

The maximum number of viewports and scissor rectangles a GPU supports varies by device family. For more information, see [MTLGPUFamily](../mtlgpufamily.md) and [Detecting GPU features and Metal software versions](../detecting-gpu-features-and-metal-software-versions.md).

The rendering pipeline sends each primitive to a single viewport and its associated scissor rectangle. You can select which viewport each primitive uses in your vertex shader by adding the `[[viewport_array_index]]` attribute to an output value.

> [!note] Note
> You can change the render pass’s scissor rectangle configuration by calling this method again or by calling the [- setScissorRect:](<setscissorrect(__).md>) method.

The [- setScissorRect:](<setscissorrect(__).md>) method is equivalent to calling this method with a single element in the `scissorRects` array.

## See Also

### Configuring viewport and scissor behavior

- [- setViewport:](<setviewport(__).md>) — Configures the render pipeline with a viewport that applies a transformation and a clipping rectangle.
- [setViewports(_:)](<setviewports(__).md>) — Configures the render pipeline with multiple viewports that apply transformations and clipping rectangles.
- [- setScissorRect:](<setscissorrect(__).md>) — Configures a rectangle for the fragment scissor test.
