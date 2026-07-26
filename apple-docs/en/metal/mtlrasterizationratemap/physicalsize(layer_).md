---
title: 'physicalSize(layer:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratemap/physicalsize(layer:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemap/physicalsize(layer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemap/physicalsize%28layer%3A%29.json'
content_hash: 'sha256:222acb16c2f4bd9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMap](../mtlrasterizationratemap.md)

# physicalSize(layer:)

<sub>Instance Method</sub>

Returns the dimensions, in pixels, of the area in the render target affected by the rasterization rate map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func physicalSize(layer layerIndex: Int) -> MTLSize
```

## Parameters

- `layerIndex` — The index of the layer.

## Return Value

The dimensions, in pixels, of the area in the render target affected by the rasterization rate map.

## Discussion

Your render targets should be at least as large as the physical size returned by this method. Each layer may have different rasterization rates and therefore different physical size requirements.

## See Also

### Inspecting geometric and rendering properties

- [layerCount](layercount.md) — The number of layers in the rate map.
- [screenSize](screensize.md) — The logical size, in pixels, of the viewport coordinate system.
- [physicalGranularity](physicalgranularity.md) — The granularity, in physical pixels, at which the rasterization rate varies.
