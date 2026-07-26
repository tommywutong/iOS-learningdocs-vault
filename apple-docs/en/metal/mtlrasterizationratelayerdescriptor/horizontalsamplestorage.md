---
title: horizontalSampleStorage
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratelayerdescriptor/horizontalsamplestorage
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/horizontalsamplestorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratelayerdescriptor/horizontalsamplestorage.json'
content_hash: 'sha256:e38bc5bd2a2474ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateLayerDescriptor](../mtlrasterizationratelayerdescriptor.md)

# horizontalSampleStorage

<sub>Instance Property</sub>

A pointer to the storage for the layer map’s horizontal rasterization rates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
@property (nonatomic, readonly) float * horizontalSampleStorage;
```

## Discussion

Points to the first element in the array of horizontal rasterization rates. The number of elements is equal to the [width](../mtlsize/width.md) value of [sampleCount](samplecount.md).

## See Also

### Inspecting the layer rate function parameters

- [sampleCount](samplecount.md) — The number of rows and columns in the layer map.
- [maxSampleCount](maxsamplecount.md) — The maximum number of rows and columns in the layer map.
- [horizontal](horizontal.md) — The horizontal rasterization rates for the layer map’s rows.
- [vertical](vertical.md) — The vertical rasterization rates for the layer map’s rows.
- [verticalSampleStorage](verticalsamplestorage.md) — A pointer to the storage for the layer map’s vertical rasterization rates.
- [MTLRasterizationRateSampleArray](../mtlrasterizationratesamplearray.md) — An array instance that contains rasterization rates.
