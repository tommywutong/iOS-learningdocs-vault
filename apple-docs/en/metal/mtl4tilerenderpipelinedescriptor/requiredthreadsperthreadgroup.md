---
title: requiredThreadsPerThreadgroup
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4tilerenderpipelinedescriptor/requiredthreadsperthreadgroup
source_url: 'https://developer.apple.com/documentation/metal/mtl4tilerenderpipelinedescriptor/requiredthreadsperthreadgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4tilerenderpipelinedescriptor/requiredthreadsperthreadgroup.json'
content_hash: 'sha256:ad2a0d6ac8b978b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4TileRenderPipelineDescriptor](../mtl4tilerenderpipelinedescriptor.md)

# requiredThreadsPerThreadgroup

<sub>Instance Property</sub>

Sets the required number of threads per threadgroup for tile dispatches.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requiredThreadsPerThreadgroup: MTLSize { get set }
```

## Discussion

This value is typically optional, except in the cases where the tile function that [tileFunctionDescriptor](tilefunctiondescriptor.md) references uses `CooperativeTensors`. In this case, you need to provide a non-zero value to this property.

Additionally, when you set this value, the `threadsPerTile` argument of any tile dispatch needs to match it.

Setting this value to a size of 0 in every dimension disables this property.
