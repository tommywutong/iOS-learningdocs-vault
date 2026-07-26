---
title: 'setDepthTestMinBound:maxBound:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setdepthtestminbound:maxbound:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setdepthtestminbound:maxbound:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setdepthtestminbound%3Amaxbound%3A.json'
content_hash: 'sha256:c0253d5627b8da92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setDepthTestMinBound:maxBound:

<sub>Instance Method</sub>

Configures the minimum and maximum bounds for depth bounds testing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setDepthTestMinBound:(float) minBound maxBound:(float) maxBound;
```

## Parameters

- `minBound` — A minimum bound for depth testing, which discards fragments with a stored depth that is less than `minBound`.

- `maxBound` — A maximum bound for depth testing, which discards fragments with a stored depth that is greater than `maxBound`.

## Discussion

The render command encoder disables depth bounds testing by default. The render command encoder also disables depth bounds testing when all of the following properties equal a specific value:

- The `minBound` property is equal to `0.0f`.
- The `maxBound` property is equal to `1.0f`. Both `minBound` and `maxBound` need to be within `[0.0f, 1.0f]`, and `minBound` needs to be less than or equal to `maxBound`.

## See Also

### Configuring depth and stencil behavior

- [- setDepthStencilState:](<setdepthstencilstate(__).md>) — Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [- setDepthBias:slopeScale:clamp:](<setdepthbias(__slopescale_clamp_).md>) — Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.
- [- setDepthClipMode:](<setdepthclipmode(__).md>) — Controls the behavior for fragments outside of the near or far planes.
- [- setStencilReferenceValue:](<setstencilreferencevalue(__).md>) — Configures this encoder with a reference value for stencil testing.
- [- setStencilFrontReferenceValue:backReferenceValue:](<setstencilreferencevalue(front_back_).md>) — Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.
