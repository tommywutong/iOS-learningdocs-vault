---
title: 'MTLCoordinate2DMake(_:_:)'
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcoordinate2dmake(_:_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcoordinate2dmake(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcoordinate2dmake%28_%3A_%3A%29.json'
content_hash: 'sha256:422e39d6e52221ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCoordinate2DMake(_:_:)

<sub>Function</sub>

Returns a new 2D point with the specified coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTLCoordinate2DMake(_ x: Float, _ y: Float) -> MTLCoordinate2D
```

## Parameters

- `x` — The x coordinate of the new point.

- `y` — The y coordinate of the new point.

## See Also

### Rasterization settings

- [Rendering at different rasterization rates](rendering-at-different-rasterization-rates.md) — Configure a rasterization rate map to vary rasterization rates depending on the amount of detail needed.
- [Creating a rasterization rate map](creating-a-rasterization-rate-map.md) — Define the rasterization rates for each part of your render target.
- [Rendering with a rasterization rate map](rendering-with-a-rasterization-rate-map.md) — Create offscreen textures to hold intermediate rasterized data.
- [Scaling variable rasterization rate content](scaling-variable-rasterization-rate-content.md) — Use the rate map data to scale the content to fill your destination texture.
- [MTLRasterizationRateMapDescriptor](mtlrasterizationratemapdescriptor.md) — An object that you use to configure new rasterization rate maps.
- [MTLRasterizationRateMap](mtlrasterizationratemap.md) — A compiled read-only instance that determines how to apply variable rasterization rates when rendering.
- [MTLCoordinate2D](mtlcoordinate2d.md) — A coordinate in the viewport.
