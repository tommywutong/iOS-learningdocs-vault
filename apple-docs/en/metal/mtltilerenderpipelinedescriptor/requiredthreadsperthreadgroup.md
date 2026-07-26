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
doc_path: /documentation/metal/mtltilerenderpipelinedescriptor/requiredthreadsperthreadgroup
source_url: 'https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor/requiredthreadsperthreadgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltilerenderpipelinedescriptor/requiredthreadsperthreadgroup.json'
content_hash: 'sha256:c38520b894d278e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTileRenderPipelineDescriptor](../mtltilerenderpipelinedescriptor.md)

# requiredThreadsPerThreadgroup

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requiredThreadsPerThreadgroup: MTLSize { get set }
```

## Discussion

Sets the required threads-per-threadgroup during tile dispatches. The `threadsPerTile` argument of any tile dispatch must match to this value if it is set. Setting this to a size of 0 in every dimension disables this property
