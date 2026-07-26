---
title: 'dispatchThreads(threadsPerGrid:threadsPerThreadgroup:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/dispatchthreads(threadspergrid:threadsperthreadgroup:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/dispatchthreads(threadspergrid:threadsperthreadgroup:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/dispatchthreads%28threadspergrid%3Athreadsperthreadgroup%3A%29.json'
content_hash: 'sha256:c5a77d0af55580f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# dispatchThreads(threadsPerGrid:threadsPerThreadgroup:)

<sub>Instance Method</sub>

Encodes a compute dispatch command using an arbitrarily-sized grid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func dispatchThreads(threadsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)
```

## Parameters

- `threadsPerGrid` — An [MTLSize](../mtlsize.md) instance that represents the number of threads in the grid, in each dimension.

- `threadsPerThreadgroup` — An [MTLSize](../mtlsize.md) instance that represents the number of threads in one threadgroup, in each dimension.

## See Also

### Running dispatch commands

- [- dispatchThreadsWithIndirectBuffer:](<dispatchthreads(indirectbuffer_).md>) — Encodes a compute dispatch command with an arbitrarily sized grid, using an indirect buffer for arguments.
- [- dispatchThreadgroups:threadsPerThreadgroup:](<dispatchthreadgroups(threadgroupspergrid_threadsperthreadgroup_).md>) — Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries.
- [- dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:](<dispatchthreadgroups(indirectbuffer_threadsperthreadgroup_).md>) — Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries, using an indirect buffer for arguments.
