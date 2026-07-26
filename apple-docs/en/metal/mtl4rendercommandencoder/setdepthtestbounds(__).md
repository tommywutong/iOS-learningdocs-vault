---
title: 'setDepthTestBounds(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setdepthtestbounds(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setdepthtestbounds(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setdepthtestbounds%28_%3A%29.json'
content_hash: 'sha256:09a20d197a485387'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setDepthTestBounds(_:)

<sub>Instance Method</sub>

Configures the range for depth bounds testing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setDepthTestBounds(_ bounds: ClosedRange<Float>)
```

## Parameters

- `bounds` — A closed range the renderer applies to depth bounds testing. The renderer discards fragments with a stored depth that is outside `bounds`.

## Discussion

The render command encoder disables depth bounds testing by default. The render command encoder also disables depth bounds testing when the `bounds` property equals `0.0...1.0`. `bounds.lowerBound` needs to be greater than or equal to `0.0`. `bounds.upperBound` needs to be less than or equal to `1.0`.

## See Also

### Configuring depth and stencil behavior

- [- setDepthStencilState:](<setdepthstencilstate(__).md>) — Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [- setDepthBias:slopeScale:clamp:](<setdepthbias(__slopescale_clamp_).md>) — Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.
- [- setDepthClipMode:](<setdepthclipmode(__).md>) — Controls the behavior for fragments outside of the near or far planes.
- [- setStencilReferenceValue:](<setstencilreferencevalue(__).md>) — Configures this encoder with a reference value for stencil testing.
- [- setStencilFrontReferenceValue:backReferenceValue:](<setstencilreferencevalue(front_back_).md>) — Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.
