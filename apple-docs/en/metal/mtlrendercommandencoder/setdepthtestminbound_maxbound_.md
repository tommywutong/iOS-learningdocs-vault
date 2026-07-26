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
doc_path: '/documentation/metal/mtlrendercommandencoder/setdepthtestminbound:maxbound:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthtestminbound:maxbound:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setdepthtestminbound%3Amaxbound%3A.json'
content_hash: 'sha256:e08bb3b5dba0802f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

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

- [- setDepthStencilState:](<setdepthstencilstate(__).md>) — Configures the combined depth and stencil state.
- [- setDepthBias:slopeScale:clamp:](<setdepthbias(__slopescale_clamp_).md>) — Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [- setDepthClipMode:](<setdepthclipmode(__).md>) — Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [- setStencilReferenceValue:](<setstencilreferencevalue(__).md>) — Configures the same comparison value for front- and back-facing primitives.
- [- setStencilFrontReferenceValue:backReferenceValue:](<setstencilreferencevalues(front_back_).md>) — Configures different comparison values for front- and back-facing primitives.
