---
title: 'setDepthBias(_:slopeScale:clamp:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setdepthbias(_:slopescale:clamp:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setdepthbias(_:slopescale:clamp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setdepthbias%28_%3Aslopescale%3Aclamp%3A%29.json'
content_hash: 'sha256:a99a5738c2311326'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setDepthBias(_:slopeScale:clamp:)

<sub>Instance Method</sub>

Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setDepthBias(_ depthBias: Float, slopeScale: Float, clamp: Float)
```

## Parameters

- `depthBias` — A constant bias the render pipeline applies to all fragments.

- `slopeScale` — A bias coefficient that scales with the depth of the primitive relative to the camera.

- `clamp` — A value that limits the bias value the render pipeline can apply to a fragment. Pass a positive or negative value to limit the largest magnitude of a positive or negative bias, respectively. Set this value to `0` to disable bias clamping.

## See Also

### Configuring depth and stencil behavior

- [- setDepthStencilState:](<setdepthstencilstate(__).md>) — Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [- setDepthClipMode:](<setdepthclipmode(__).md>) — Controls the behavior for fragments outside of the near or far planes.
- [setDepthTestBounds(_:)](<setdepthtestbounds(__).md>) — Configures the range for depth bounds testing.
- [- setStencilReferenceValue:](<setstencilreferencevalue(__).md>) — Configures this encoder with a reference value for stencil testing.
- [- setStencilFrontReferenceValue:backReferenceValue:](<setstencilreferencevalue(front_back_).md>) — Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.
