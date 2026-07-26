---
title: 'setDepthBias(_:slopeScale:clamp:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setdepthbias(_:slopescale:clamp:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthbias(_:slopescale:clamp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setdepthbias%28_%3Aslopescale%3Aclamp%3A%29.json'
content_hash: 'sha256:f2d57c90dfea313a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setDepthBias(_:slopeScale:clamp:)

<sub>Instance Method</sub>

Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setDepthBias(_ depthBias: Float, slopeScale: Float, clamp: Float)
```

## Parameters

- `depthBias` — A constant bias the render pipeline applies to all fragments.

- `slopeScale` — A bias coefficient that scales with the depth of the primitive relative to the camera.

- `clamp` — A value that limits the bias value the render pipeline can apply to a fragment. Pass a positive or negative value to limit the largest magnitude of a positive or negative bias, respectively. You can disable the bias clamping functionality by passing `0.0`.

## Discussion

Call this method to have the render pipeline apply a bias to the rasterized depth after the clipping stage. The bias affects both depth testing and the values the render pipeline writes to the depth render target. If you don’t explicitly call this method, the pipeline doesn’t apply a scale or a bias to a depth value.

Set a depth bias to improve the quality of techniques such as shadow mapping and avoid depth artifacts like shadow acne.

> [!note] Note
> A depth bias only influences triangle primitives, but doesn’t apply to points or lines.

## See Also

### Configuring depth and stencil behavior

- [- setDepthStencilState:](<setdepthstencilstate(__).md>) — Configures the combined depth and stencil state.
- [- setDepthClipMode:](<setdepthclipmode(__).md>) — Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [setDepthTestBounds(_:)](<setdepthtestbounds(__).md>) — Configures the range for depth bounds testing.
- [- setStencilReferenceValue:](<setstencilreferencevalue(__).md>) — Configures the same comparison value for front- and back-facing primitives.
- [- setStencilFrontReferenceValue:backReferenceValue:](<setstencilreferencevalues(front_back_).md>) — Configures different comparison values for front- and back-facing primitives.
