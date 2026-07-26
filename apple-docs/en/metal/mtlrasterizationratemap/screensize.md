---
title: screenSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratemap/screensize
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemap/screensize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemap/screensize.json'
content_hash: 'sha256:3c78ec5312874fc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMap](../mtlrasterizationratemap.md)

# screenSize

<sub>Instance Property</sub>

The logical size, in pixels, of the viewport coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var screenSize: MTLSize { get }
```

## See Also

### Inspecting geometric and rendering properties

- [layerCount](layercount.md) — The number of layers in the rate map.
- [- physicalSizeForLayer:](<physicalsize(layer_).md>) — Returns the dimensions, in pixels, of the area in the render target affected by the rasterization rate map.
- [physicalGranularity](physicalgranularity.md) — The granularity, in physical pixels, at which the rasterization rate varies.
