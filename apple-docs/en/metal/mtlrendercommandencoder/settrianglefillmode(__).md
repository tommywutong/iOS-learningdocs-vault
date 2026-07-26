---
title: 'setTriangleFillMode(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settrianglefillmode(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settrianglefillmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settrianglefillmode%28_%3A%29.json'
content_hash: 'sha256:a3473de339884655'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTriangleFillMode(_:)

<sub>Instance Method</sub>

Configures how subsequent draw commands rasterize triangle and triangle strip primitives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTriangleFillMode(_ fillMode: MTLTriangleFillMode)
```

## Parameters

- `fillMode` — A triangle filling mode the render pass applies to draw commands that rasterize triangles or triangle strips.

## Discussion

The render pass’s default mode is [MTLTriangleFillModeFill](../mtltrianglefillmode/fill.md).

## See Also

### Configuring rendering behavior

- [- setFrontFacingWinding:](<setfrontfacing(__).md>) — Configures which face of a primitive, such as a triangle, is the front.
- [- setCullMode:](<setcullmode(__).md>) — Configures how the render pipeline determines which primitives to remove.
