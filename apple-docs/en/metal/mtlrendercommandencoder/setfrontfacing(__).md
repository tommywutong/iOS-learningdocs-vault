---
title: 'setFrontFacing(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setfrontfacing(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfrontfacing(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setfrontfacing%28_%3A%29.json'
content_hash: 'sha256:f88ae2e0472cb8e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setFrontFacing(_:)

<sub>Instance Method</sub>

Configures which face of a primitive, such as a triangle, is the front.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFrontFacing(_ frontFacingWinding: MTLWinding)
```

## Parameters

- `frontFacingWinding` — An [MTLWinding](../mtlwinding.md) value that configures how the render pipeline defines which side of a primitive is its front.

## Discussion

The render pass’s default front-facing mode is [MTLWindingClockwise](../mtlwinding/clockwise.md).

The winding direction of a primitive determines whether the render pass culls it (see [- setCullMode:](<setcullmode(__).md>)).

## See Also

### Configuring rendering behavior

- [- setTriangleFillMode:](<settrianglefillmode(__).md>) — Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [- setCullMode:](<setcullmode(__).md>) — Configures how the render pipeline determines which primitives to remove.
