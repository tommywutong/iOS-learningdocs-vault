---
title: 'dispatchThreads(indirectBuffer:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/dispatchthreads(indirectbuffer:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/dispatchthreads(indirectbuffer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/dispatchthreads%28indirectbuffer%3A%29.json'
content_hash: 'sha256:249db9016f39e311'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# dispatchThreads(indirectBuffer:)

<sub>Instance Method</sub>

Encodes a compute dispatch command with an arbitrarily sized grid, using an indirect buffer for arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func dispatchThreads(indirectBuffer: MTLGPUAddress)
```

## Parameters

- `indirectBuffer` — GPUAddress of a [MTLBuffer](../mtlbuffer.md) instance providing arguments. Lay out the data in this buffer as described in the [MTLDispatchThreadsIndirectArguments](../mtldispatchthreadsindirectarguments.md) structure. This address requires 4-byte alignment.

## See Also

### Running dispatch commands

- [- dispatchThreads:threadsPerThreadgroup:](<dispatchthreads(threadspergrid_threadsperthreadgroup_).md>) — Encodes a compute dispatch command using an arbitrarily-sized grid.
- [- dispatchThreadgroups:threadsPerThreadgroup:](<dispatchthreadgroups(threadgroupspergrid_threadsperthreadgroup_).md>) — Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries.
- [- dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:](<dispatchthreadgroups(indirectbuffer_threadsperthreadgroup_).md>) — Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries, using an indirect buffer for arguments.
