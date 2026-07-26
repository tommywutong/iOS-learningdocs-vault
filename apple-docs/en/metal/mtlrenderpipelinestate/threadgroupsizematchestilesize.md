---
title: threadgroupSizeMatchesTileSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinestate/threadgroupsizematchestilesize
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/threadgroupsizematchestilesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/threadgroupsizematchestilesize.json'
content_hash: 'sha256:eef489766b7c478b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# threadgroupSizeMatchesTileSize

<sub>Instance Property</sub>

A Boolean value that indicates whether the pipeline state needs a threadgroup’s size to equal a tile’s size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var threadgroupSizeMatchesTileSize: Bool { get }
```

## See Also

### Checking tile shader memory requirements

- [maxTotalThreadsPerThreadgroup](maxtotalthreadsperthreadgroup.md) — The largest number of threads the pipeline state can have in a single tile shader threadgroup.
- [imageblockSampleLength](imageblocksamplelength.md) — The memory size, in byes, of the render pipeline’s imageblock for a single sample.
- [- imageblockMemoryLengthForDimensions:](<imageblockmemorylength(fordimensions_).md>) — Returns the length of an imageblock’s memory for the specified imageblock dimensions.
