---
title: verticalSampleStorage
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratelayerdescriptor/verticalsamplestorage
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/verticalsamplestorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratelayerdescriptor/verticalsamplestorage.json'
content_hash: 'sha256:8e60e89b5a5e5e9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateLayerDescriptor](../mtlrasterizationratelayerdescriptor.md)

# verticalSampleStorage

<sub>Instance Property</sub>

A pointer to the storage for the layer map’s vertical rasterization rates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
@property (nonatomic, readonly) float * verticalSampleStorage;
```

## Discussion

Points to the first element in the array of vertical rasterization rates. The number of elements is equal to the [height](../mtlsize/height.md) value of [sampleCount](samplecount.md).

## See Also

### Inspecting the layer rate function parameters

- [sampleCount](samplecount.md) — The number of rows and columns in the layer map.
- [maxSampleCount](maxsamplecount.md) — The maximum number of rows and columns in the layer map.
- [horizontal](horizontal.md) — The horizontal rasterization rates for the layer map’s rows.
- [vertical](vertical.md) — The vertical rasterization rates for the layer map’s rows.
- [horizontalSampleStorage](horizontalsamplestorage.md) — A pointer to the storage for the layer map’s horizontal rasterization rates.
- [MTLRasterizationRateSampleArray](../mtlrasterizationratesamplearray.md) — An array instance that contains rasterization rates.
