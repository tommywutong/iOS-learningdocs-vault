---
title: layerCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratemap/layercount
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemap/layercount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemap/layercount.json'
content_hash: 'sha256:e09db5f28557ba28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMap](../mtlrasterizationratemap.md)

# layerCount

<sub>Instance Property</sub>

The number of layers in the rate map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var layerCount: Int { get }
```

## See Also

### Inspecting geometric and rendering properties

- [screenSize](screensize.md) — The logical size, in pixels, of the viewport coordinate system.
- [- physicalSizeForLayer:](<physicalsize(layer_).md>) — Returns the dimensions, in pixels, of the area in the render target affected by the rasterization rate map.
- [physicalGranularity](physicalgranularity.md) — The granularity, in physical pixels, at which the rasterization rate varies.
