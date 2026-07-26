---
title: 'setTessellationFactorScale(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settessellationfactorscale(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settessellationfactorscale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settessellationfactorscale%28_%3A%29.json'
content_hash: 'sha256:587e4b1a0c51f0e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTessellationFactorScale(_:)

<sub>Instance Method</sub>

Configures the scale factor for per-patch tessellation factors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTessellationFactorScale(_ scale: Float)
```

## Parameters

- `scale` — A positive, normal floating-point scale factor the render pass applies to the per-patch tessellation factors. The value of `scale` can’t be negative, infinite, equal to `NaN` (not a number), or a denormalized number.

## Discussion

The command converts `scale` to a half-precision floating-point value before it applies it to the per-patch tessellation factors (see [- setTessellationFactorBuffer:offset:instanceStride:](<settessellationfactorbuffer(__offset_instancestride_).md>)).

## See Also

### Configuring tessellation factors

- [- setTessellationFactorBuffer:offset:instanceStride:](<settessellationfactorbuffer(__offset_instancestride_).md>) — Configures the per-patch tessellation factors for any subsequent patch-drawing commands.
