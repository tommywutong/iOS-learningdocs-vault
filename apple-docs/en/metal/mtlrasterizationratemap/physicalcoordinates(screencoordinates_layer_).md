---
title: 'physicalCoordinates(screenCoordinates:layer:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratemap/physicalcoordinates(screencoordinates:layer:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemap/physicalcoordinates(screencoordinates:layer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemap/physicalcoordinates%28screencoordinates%3Alayer%3A%29.json'
content_hash: 'sha256:129fec5e638cfc61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMap](../mtlrasterizationratemap.md)

# physicalCoordinates(screenCoordinates:layer:)

<sub>Instance Method</sub>

Converts a point in logical viewport coordinates to the corresponding physical coordinates in a render layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func physicalCoordinates(screenCoordinates: MTLCoordinate2D, layer layerIndex: Int) -> MTLCoordinate2D
```

## Parameters

- `screenCoordinates` — A point in viewport coordinates.

- `layerIndex` — The index of the rate map to use.

## Return Value

A point in the layer’s physical coordinate system corresponding to the source point.

## Discussion

The returned coordinates are always less than or equal to the input coordinates because the rasterization rate never exceeds 1:1 in any region.

## See Also

### Converting between viewport and physical coordinates

- [- mapPhysicalToScreenCoordinates:forLayer:](<screencoordinates(physicalcoordinates_layer_).md>) — Converts a point in physical coordinates inside a layer to its corresponding logical viewport coordinates.
