---
title: 'setDepthClipMode(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setdepthclipmode(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setdepthclipmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setdepthclipmode%28_%3A%29.json'
content_hash: 'sha256:076f51424ca1eab9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setDepthClipMode(_:)

<sub>Instance Method</sub>

Controls the behavior for fragments outside of the near or far planes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setDepthClipMode(_ depthClipMode: MTLDepthClipMode)
```

## Parameters

- `depthClipMode` — [MTLDepthClipMode](../mtldepthclipmode.md) to set.

## See Also

### Configuring depth and stencil behavior

- [- setDepthStencilState:](<setdepthstencilstate(__).md>) — Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [- setDepthBias:slopeScale:clamp:](<setdepthbias(__slopescale_clamp_).md>) — Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.
- [setDepthTestBounds(_:)](<setdepthtestbounds(__).md>) — Configures the range for depth bounds testing.
- [- setStencilReferenceValue:](<setstencilreferencevalue(__).md>) — Configures this encoder with a reference value for stencil testing.
- [- setStencilFrontReferenceValue:backReferenceValue:](<setstencilreferencevalue(front_back_).md>) — Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.
