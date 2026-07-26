---
title: maxSampleCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratelayerdescriptor/maxsamplecount
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/maxsamplecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratelayerdescriptor/maxsamplecount.json'
content_hash: 'sha256:46f9c6b29bf83f4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateLayerDescriptor](../mtlrasterizationratelayerdescriptor.md)

# maxSampleCount

<sub>Instance Property</sub>

The maximum number of rows and columns in the layer map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxSampleCount: MTLSize { get }
```

## Discussion

Its [depth](../mtlsize/depth.md) value is always `0`.

## See Also

### Inspecting the layer rate function parameters

- [sampleCount](samplecount.md) — The number of rows and columns in the layer map.
- [horizontal](horizontal.md) — The horizontal rasterization rates for the layer map’s rows.
- [vertical](vertical.md) — The vertical rasterization rates for the layer map’s rows.
- [MTLRasterizationRateSampleArray](../mtlrasterizationratesamplearray.md) — An array instance that contains rasterization rates.
