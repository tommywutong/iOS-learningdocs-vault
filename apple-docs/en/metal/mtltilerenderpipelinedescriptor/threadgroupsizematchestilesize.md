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
doc_path: /documentation/metal/mtltilerenderpipelinedescriptor/threadgroupsizematchestilesize
source_url: 'https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor/threadgroupsizematchestilesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltilerenderpipelinedescriptor/threadgroupsizematchestilesize.json'
content_hash: 'sha256:1e2ff4506e4e7b1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTileRenderPipelineDescriptor](../mtltilerenderpipelinedescriptor.md)

# threadgroupSizeMatchesTileSize

<sub>Instance Property</sub>

A Boolean value that indicates whether all threadgroups for this pipeline completely cover tiles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var threadgroupSizeMatchesTileSize: Bool { get set }
```

## Discussion

Metal can optimize code generation when the threadgroup and tile sizes match.

## See Also

### Specifying rasterization and visibility state

- [rasterSampleCount](rastersamplecount.md) — The number of samples in each fragment.
