---
title: 'initWithSampleCount:horizontal:vertical:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratelayerdescriptor/initwithsamplecount:horizontal:vertical:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/initwithsamplecount:horizontal:vertical:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratelayerdescriptor/initwithsamplecount%3Ahorizontal%3Avertical%3A.json'
content_hash: 'sha256:da877b582d0142ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateLayerDescriptor](../mtlrasterizationratelayerdescriptor.md)

# initWithSampleCount:horizontal:vertical:

<sub>Instance Method</sub>

Initializes the layer map with the provided grid size and rasterization rates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (instancetype) initWithSampleCount:(MTLSize) sampleCount horizontal:(const float *) horizontal vertical:(const float *) vertical;
```

## Parameters

- `sampleCount` — The size of the grid. Specify the width and height to determine the number of columns and rows in the layer map. The initializer ignores the depth component.

- `horizontal` — The rasterization rates for the layer map’s columns. There needs to be at least as many samples as the width you specified in `sampleCount`.

- `vertical` — The rasterization rates for the layer map’s columns. There needs to be at least as many samples as the height you specified in `sampleCount`.

## Return Value

A layer descriptor with a grid of the specified size. The layer descriptor copies the  rasterization rates.

## See Also

### Creating a layer rasterization rate descriptor

- [- initWithSampleCount:](<init(samplecount_).md>) — Initializes the layer map with an empty grid.
