---
title: 'setStageInRegion(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setstageinregion(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setstageinregion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setstageinregion%28_%3A%29.json'
content_hash: 'sha256:795bac5a3fae6ae9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setStageInRegion(_:)

<sub>Instance Method</sub>

Sets the dimensions over the thread grid of how your compute kernel receives stage-in arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setStageInRegion(_ region: MTLRegion)
```

## Parameters

- `region` — The [MTLRegion](../mtlregion.md) defining how to interpret a thread’s location as a coordinate for stage-in data.

## Discussion

The region’s origin point, starting from `(0,0,0)` in the upper left of the bound data, determines the final index of `[[stage_in]]` data. Note that the total number of threads Metal launches may be larger than your stage-in data.

To determine the index used to fetch `[[stage_in]]` data for a given thread, the GPU adds the values specified by the region’s origin to the thread position in the grid. Threads in the grid outside of the maximum stage-in data size have undefined behavior when accessing the stage-in memory region.

## See Also

### Configuring stage-in data

- [- setStageInRegionWithIndirectBuffer:indirectBufferOffset:](<setstageinregionwithindirectbuffer(__indirectbufferoffset_).md>) — Sets the region of the stage-in attributes to apply to a compute kernel using an indirect buffer.
