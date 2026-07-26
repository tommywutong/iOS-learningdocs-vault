---
title: 'setBlendColor(red:green:blue:alpha:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setblendcolor(red:green:blue:alpha:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setblendcolor(red:green:blue:alpha:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setblendcolor%28red%3Agreen%3Ablue%3Aalpha%3A%29.json'
content_hash: 'sha256:51735709677d15e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setBlendColor(red:green:blue:alpha:)

<sub>Instance Method</sub>

Configures each pixel component value, including alpha, for the render pipeline’s constant blend color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBlendColor(red: Float, green: Float, blue: Float, alpha: Float)
```

## Parameters

- `red` — A value for the red component for the blend color constant.

- `green` — A value for the green component for the blend color constant.

- `blue` — A value for the blue component for the blend color constant.

- `alpha` — A value for the alpha component for the blend color constant.

## Discussion

The alpha and color values apply to all the render pass’s attachments. The `red`, `green`, and `blue` color parameters apply to the [MTLBlendFactorBlendColor](../mtlblendfactor/blendcolor.md) and [MTLBlendFactorOneMinusBlendColor](../mtlblendfactor/oneminusblendcolor.md) blend factors.

The `alpha` parameter applies to the [MTLBlendFactorBlendAlpha](../mtlblendfactor/blendalpha.md) and [MTLBlendFactorOneMinusBlendAlpha](../mtlblendfactor/oneminusblendalpha.md) blend factors.

The render pipeline’s default blend color value is `0.0` for each parameter, which is equivalent to [MTLBlendFactorZero](../mtlblendfactor/zero.md). For other blending factor values, see [MTLBlendFactor](../mtlblendfactor.md).

## See Also

### Configuring blend behavior

- [- setColorAttachmentMap:](<setcolorattachmentmap(__).md>) — Sets the mapping from logical shader color output to physical render pass color attachments.
