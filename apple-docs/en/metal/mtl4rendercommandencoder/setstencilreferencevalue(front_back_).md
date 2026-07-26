---
title: 'setStencilReferenceValue(front:back:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setstencilreferencevalue(front:back:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setstencilreferencevalue(front:back:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setstencilreferencevalue%28front%3Aback%3A%29.json'
content_hash: 'sha256:d153a7bb67f80d83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setStencilReferenceValue(front:back:)

<sub>Instance Method</sub>

Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setStencilReferenceValue(front frontReferenceValue: UInt32, back backReferenceValue: UInt32)
```

## Parameters

- `frontReferenceValue` — A stencil test comparison value the render pipeline applies to front-facing primitives.

- `backReferenceValue` — A stencil test comparison value the render pipeline applies to back-facing primitives.

## Discussion

The render pipeline applies `frontReferenceValue` to front-facing primitives and `backReferenceValue` to back-facing primitives.

## See Also

### Configuring depth and stencil behavior

- [- setDepthStencilState:](<setdepthstencilstate(__).md>) — Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [- setDepthBias:slopeScale:clamp:](<setdepthbias(__slopescale_clamp_).md>) — Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.
- [- setDepthClipMode:](<setdepthclipmode(__).md>) — Controls the behavior for fragments outside of the near or far planes.
- [setDepthTestBounds(_:)](<setdepthtestbounds(__).md>) — Configures the range for depth bounds testing.
- [- setStencilReferenceValue:](<setstencilreferencevalue(__).md>) — Configures this encoder with a reference value for stencil testing.
