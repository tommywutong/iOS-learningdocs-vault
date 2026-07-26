---
title: 'setTriangleFillMode(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/settrianglefillmode(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/settrianglefillmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/settrianglefillmode%28_%3A%29.json'
content_hash: 'sha256:b58bde00f38854a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setTriangleFillMode(_:)

<sub>Instance Method</sub>

Configures how subsequent draw commands rasterize triangle and triangle strip primitives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTriangleFillMode(_ fillMode: MTLTriangleFillMode)
```

## Parameters

- `fillMode` — [MTLTriangleFillMode](../mtltrianglefillmode.md) the render pass applies to draw commands that rasterize triangles or triangle strips.

## See Also

### Configuring rendering behavior

- [- setFrontFacingWinding:](<setfrontfacing(__).md>) — Configures the vertex winding order that determines which face of a geometric primitive is the front one.
- [- setCullMode:](<setcullmode(__).md>) — Controls whether Metal culls front facing primitives, back facing primitives, or culls no primitives at all.
