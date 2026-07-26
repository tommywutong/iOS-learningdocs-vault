---
title: 'setCullMode(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setcullmode(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setcullmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setcullmode%28_%3A%29.json'
content_hash: 'sha256:9aa60ba661cf8d13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setCullMode(_:)

<sub>Instance Method</sub>

Configures how the render pipeline determines which primitives to remove.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setCullMode(_ cullMode: MTLCullMode)
```

## Parameters

- `cullMode` — An [MTLCullMode](../mtlcullmode.md) value that configures how the render pipeline determines which primitives to remove from the pipeline.

## Discussion

This method configures which primitives the render pipeline removes, if any, based on the direction of each primitive’s face relative to the scene’s camera. For example, you can correctly cull hidden surfaces on some geometric models, such as a sphere made of filled triangles, if it uses orientable surfaces. A surface is _orientable_ if its primitives consistently use the same ordering for its vertices. Metal defines vertex ordering with the [MTLWinding](../mtlwinding.md) type, which includes [MTLWindingClockwise](../mtlwinding/clockwise.md) and [MTLWindingCounterClockwise](../mtlwinding/counterclockwise.md). You can tell the render pipeline which direction your primitives face by calling the [- setFrontFacingWinding:](<setfrontfacing(__).md>) method, which affects the primitives the culling mode removes.

The render pass’s default culling mode is [MTLCullModeNone](../mtlcullmode/none.md).

## See Also

### Configuring rendering behavior

- [- setTriangleFillMode:](<settrianglefillmode(__).md>) — Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [- setFrontFacingWinding:](<setfrontfacing(__).md>) — Configures which face of a primitive, such as a triangle, is the front.
