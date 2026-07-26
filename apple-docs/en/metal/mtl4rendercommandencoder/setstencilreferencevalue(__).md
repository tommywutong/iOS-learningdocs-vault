---
title: 'setStencilReferenceValue(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setstencilreferencevalue(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setstencilreferencevalue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setstencilreferencevalue%28_%3A%29.json'
content_hash: 'sha256:60c1811ac8248ad3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setStencilReferenceValue(_:)

<sub>Instance Method</sub>

Configures this encoder with a reference value for stencil testing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setStencilReferenceValue(_ referenceValue: UInt32)
```

## Parameters

- `referenceValue` — A stencil test comparison value.

## Discussion

The render pipeline applies this reference value to both front-facing and back-facing primitives.

## See Also

### Configuring depth and stencil behavior

- [- setDepthStencilState:](<setdepthstencilstate(__).md>) — Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [- setDepthBias:slopeScale:clamp:](<setdepthbias(__slopescale_clamp_).md>) — Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.
- [- setDepthClipMode:](<setdepthclipmode(__).md>) — Controls the behavior for fragments outside of the near or far planes.
- [setDepthTestBounds(_:)](<setdepthtestbounds(__).md>) — Configures the range for depth bounds testing.
- [- setStencilFrontReferenceValue:backReferenceValue:](<setstencilreferencevalue(front_back_).md>) — Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.
