---
title: 'setFrontFacing(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setfrontfacing(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setfrontfacing(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setfrontfacing%28_%3A%29.json'
content_hash: 'sha256:a17da525ed94a9e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setFrontFacing(_:)

<sub>Instance Method</sub>

Configures the vertex winding order that determines which face of a geometric primitive is the front one.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFrontFacing(_ frontFacingWinding: MTLWinding)
```

## Parameters

- `frontFacingWinding` — A [MTLWinding](../mtlwinding.md) value that determines which side of a primitive the render pipeline interprets as front facing.

## See Also

### Configuring rendering behavior

- [- setTriangleFillMode:](<settrianglefillmode(__).md>) — Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [- setCullMode:](<setcullmode(__).md>) — Controls whether Metal culls front facing primitives, back facing primitives, or culls no primitives at all.
