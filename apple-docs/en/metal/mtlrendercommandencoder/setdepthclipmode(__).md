---
title: 'setDepthClipMode(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setdepthclipmode(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthclipmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setdepthclipmode%28_%3A%29.json'
content_hash: 'sha256:1e7abb918ad25af0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setDepthClipMode(_:)

<sub>Instance Method</sub>

Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setDepthClipMode(_ depthClipMode: MTLDepthClipMode)
```

## Parameters

- `depthClipMode` — The mode that determines how to handle fragments outside the near and far planes.

## Discussion

You can use depth clipping to ignore fragments outside the z-axis boundaries of a viewing volume.

The render pass’s default clip mode is [MTLDepthClipModeClip](../mtldepthclipmode/clip.md).

## See Also

### Configuring depth and stencil behavior

- [- setDepthStencilState:](<setdepthstencilstate(__).md>) — Configures the combined depth and stencil state.
- [- setDepthBias:slopeScale:clamp:](<setdepthbias(__slopescale_clamp_).md>) — Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [setDepthTestBounds(_:)](<setdepthtestbounds(__).md>) — Configures the range for depth bounds testing.
- [- setStencilReferenceValue:](<setstencilreferencevalue(__).md>) — Configures the same comparison value for front- and back-facing primitives.
- [- setStencilFrontReferenceValue:backReferenceValue:](<setstencilreferencevalues(front_back_).md>) — Configures different comparison values for front- and back-facing primitives.
