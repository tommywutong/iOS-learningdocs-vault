---
title: 'imageblockMemoryLength(forDimensions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpipelinestate/imageblockmemorylength(fordimensions:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/imageblockmemorylength(fordimensions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/imageblockmemorylength%28fordimensions%3A%29.json'
content_hash: 'sha256:934ab3b20494c434'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# imageblockMemoryLength(forDimensions:)

<sub>Instance Method</sub>

Returns the length of an imageblock’s memory for the specified imageblock dimensions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func imageblockMemoryLength(forDimensions imageblockDimensions: MTLSize) -> Int
```

## Parameters

- `imageblockDimensions` — An [MTLSize](../mtlsize.md) instance that represent the dimensions of an imageblock.

## Discussion

The imageblock dimensions need to match a valid tile size, such as one of the following:

- 32 x 32
- 32 x 16
- 16 x 16

The GPU partitions tile memory between imageblocks and threadgroup memory,

> [!important] Important
> The total memory allocations for imageblocks and threadgroup memory can’t exceed the tile memory limit for the GPU device.

For information about identifying tile memory limits for GPU devices, see either of the following:

- [Metal Feature Set Tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf)
- [Metal Feature Set Tables (Numbers)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.zip)

## See Also

### Checking tile shader memory requirements

- [maxTotalThreadsPerThreadgroup](maxtotalthreadsperthreadgroup.md) — The largest number of threads the pipeline state can have in a single tile shader threadgroup.
- [threadgroupSizeMatchesTileSize](threadgroupsizematchestilesize.md) — A Boolean value that indicates whether the pipeline state needs a threadgroup’s size to equal a tile’s size.
- [imageblockSampleLength](imageblocksamplelength.md) — The memory size, in byes, of the render pipeline’s imageblock for a single sample.
