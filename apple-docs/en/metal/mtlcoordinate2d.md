---
title: MTLCoordinate2D
framework: Metal
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcoordinate2d
source_url: 'https://developer.apple.com/documentation/metal/mtlcoordinate2d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcoordinate2d.json'
content_hash: 'sha256:cfeefad6c308632e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCoordinate2D

<sub>Type Alias</sub>

A coordinate in the viewport.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias MTLCoordinate2D = MTLSamplePosition
```

## See Also

### Rasterization settings

- [Rendering at different rasterization rates](rendering-at-different-rasterization-rates.md) — Configure a rasterization rate map to vary rasterization rates depending on the amount of detail needed.
- [Creating a rasterization rate map](creating-a-rasterization-rate-map.md) — Define the rasterization rates for each part of your render target.
- [Rendering with a rasterization rate map](rendering-with-a-rasterization-rate-map.md) — Create offscreen textures to hold intermediate rasterized data.
- [Scaling variable rasterization rate content](scaling-variable-rasterization-rate-content.md) — Use the rate map data to scale the content to fill your destination texture.
- [MTLRasterizationRateMapDescriptor](mtlrasterizationratemapdescriptor.md) — An object that you use to configure new rasterization rate maps.
- [MTLRasterizationRateMap](mtlrasterizationratemap.md) — A compiled read-only instance that determines how to apply variable rasterization rates when rendering.
- [MTLCoordinate2DMake](<mtlcoordinate2dmake(____).md>) — Returns a new 2D point with the specified coordinates.
