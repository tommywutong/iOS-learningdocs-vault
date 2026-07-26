---
title: 'MTLRegionMake1D(_:_:)'
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlregionmake1d(_:_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlregionmake1d(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlregionmake1d%28_%3A_%3A%29.json'
content_hash: 'sha256:16377692e02d5d4d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRegionMake1D(_:_:)

<sub>Function</sub>

Creates a 3D representation of a 1D region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTLRegionMake1D(_ x: Int, _ width: Int) -> MTLRegion
```

## Parameters

- `x` — The x coordinate of the origin.

- `width` — The width of the volume.

## Return Value

A region whose x and width values are as specified.  The y and z coordinates of the region’s origin are set to `0`, and the region’s height and depth are set to `1.`

## See Also

### Creating regions

- [init()](<mtlregion/init().md>) — Initializes a new region.
- [init(origin:size:)](<mtlregion/init(origin_size_).md>) — Initializes a new region with the specified origin and size.
- [MTLRegionMake2D](<mtlregionmake2d(________).md>) — Creates a 3D representation of a 2D region.
- [MTLRegionMake3D](<mtlregionmake3d(____________).md>) — Creates a 3D region.
