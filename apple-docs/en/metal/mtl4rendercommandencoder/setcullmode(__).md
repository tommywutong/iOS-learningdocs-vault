---
title: 'setCullMode(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setcullmode(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setcullmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setcullmode%28_%3A%29.json'
content_hash: 'sha256:692be37d2f6d2238'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setCullMode(_:)

<sub>Instance Method</sub>

Controls whether Metal culls front facing primitives, back facing primitives, or culls no primitives at all.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setCullMode(_ cullMode: MTLCullMode)
```

## Parameters

- `cullMode` — [MTLCullMode](../mtlcullmode.md) to set.

## See Also

### Configuring rendering behavior

- [- setTriangleFillMode:](<settrianglefillmode(__).md>) — Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [- setFrontFacingWinding:](<setfrontfacing(__).md>) — Configures the vertex winding order that determines which face of a geometric primitive is the front one.
