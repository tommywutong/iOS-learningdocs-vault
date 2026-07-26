---
title: physicalGranularity
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratemap/physicalgranularity
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemap/physicalgranularity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemap/physicalgranularity.json'
content_hash: 'sha256:844d7d68e36f1fc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMap](../mtlrasterizationratemap.md)

# physicalGranularity

<sub>Instance Property</sub>

The granularity, in physical pixels, at which the rasterization rate varies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var physicalGranularity: MTLSize { get }
```

## Discussion

If you’re using a rendering algorithm that uses binning or tiling to partition the rendered image, you may want to use the value of this property to determine your bin sizes.

The depth component of the returned [MTLSize](../mtlsize.md) structure is always `0`.

## See Also

### Inspecting geometric and rendering properties

- [layerCount](layercount.md) — The number of layers in the rate map.
- [screenSize](screensize.md) — The logical size, in pixels, of the viewport coordinate system.
- [- physicalSizeForLayer:](<physicalsize(layer_).md>) — Returns the dimensions, in pixels, of the area in the render target affected by the rasterization rate map.
