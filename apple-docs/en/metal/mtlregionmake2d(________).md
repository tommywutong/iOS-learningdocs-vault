---
title: 'MTLRegionMake2D(_:_:_:_:)'
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlregionmake2d(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlregionmake2d(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlregionmake2d%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:9f0e734d1ea3fc86'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRegionMake2D(_:_:_:_:)

<sub>Function</sub>

Creates a 3D representation of a 2D region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTLRegionMake2D(_ x: Int, _ y: Int, _ width: Int, _ height: Int) -> MTLRegion
```

## Parameters

- `x` — The x coordinate of the origin.

- `y` — The y coordinate of the origin.

- `width` — The width of the volume.

- `height` — The height of the volume.

## Return Value

A region whose x, y, width, and height values are as specified. The z coordinate of the region’s origin is set to `0`, and the region’s depth is set to `1`.

## See Also

### Creating regions

- [init()](<mtlregion/init().md>) — Initializes a new region.
- [init(origin:size:)](<mtlregion/init(origin_size_).md>) — Initializes a new region with the specified origin and size.
- [MTLRegionMake1D](<mtlregionmake1d(____).md>) — Creates a 3D representation of a 1D region.
- [MTLRegionMake3D](<mtlregionmake3d(____________).md>) — Creates a 3D region.
