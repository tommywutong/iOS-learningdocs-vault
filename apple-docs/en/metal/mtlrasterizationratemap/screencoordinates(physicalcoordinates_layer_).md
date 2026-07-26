---
title: 'screenCoordinates(physicalCoordinates:layer:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratemap/screencoordinates(physicalcoordinates:layer:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemap/screencoordinates(physicalcoordinates:layer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemap/screencoordinates%28physicalcoordinates%3Alayer%3A%29.json'
content_hash: 'sha256:9f2053b98aca86ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMap](../mtlrasterizationratemap.md)

# screenCoordinates(physicalCoordinates:layer:)

<sub>Instance Method</sub>

Converts a point in physical coordinates inside a layer to its corresponding logical viewport coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func screenCoordinates(physicalCoordinates: MTLCoordinate2D, layer layerIndex: Int) -> MTLCoordinate2D
```

## Parameters

- `physicalCoordinates` — A point in layer coordinates.

- `layerIndex` — The index of the rate map to use.

## Return Value

A point in the view coordinates corresponding to the source point.

## Discussion

The returned coordinates are always greater than or equal to the input coordinates because the rasterization rate never exceeds 1:1 in any region.

## See Also

### Converting between viewport and physical coordinates

- [- mapScreenToPhysicalCoordinates:forLayer:](<physicalcoordinates(screencoordinates_layer_).md>) — Converts a point in logical viewport coordinates to the corresponding physical coordinates in a render layer.
