---
title: sampleCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratelayerdescriptor/samplecount
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/samplecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratelayerdescriptor/samplecount.json'
content_hash: 'sha256:9a94ce0d7e9ab448'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateLayerDescriptor](../mtlrasterizationratelayerdescriptor.md)

# sampleCount

<sub>Instance Property</sub>

The number of rows and columns in the layer map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sampleCount: MTLSize { get set }
```

## Discussion

The [sampleCount](samplecount.md) property splits the logical viewport coordinate space into a 2D grid of equal-sized cells. Its [depth](../mtlsize/depth.md) value is always `0`.

The default value is the same as [maxSampleCount](maxsamplecount.md).

## See Also

### Inspecting the layer rate function parameters

- [maxSampleCount](maxsamplecount.md) — The maximum number of rows and columns in the layer map.
- [horizontal](horizontal.md) — The horizontal rasterization rates for the layer map’s rows.
- [vertical](vertical.md) — The vertical rasterization rates for the layer map’s rows.
- [MTLRasterizationRateSampleArray](../mtlrasterizationratesamplearray.md) — An array instance that contains rasterization rates.
