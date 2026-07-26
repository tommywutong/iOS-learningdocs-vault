---
title: 'dispatchThreadgroups(indirectBuffer:threadsPerThreadgroup:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/dispatchthreadgroups(indirectbuffer:threadsperthreadgroup:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/dispatchthreadgroups(indirectbuffer:threadsperthreadgroup:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/dispatchthreadgroups%28indirectbuffer%3Athreadsperthreadgroup%3A%29.json'
content_hash: 'sha256:6801ed59e4a099c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# dispatchThreadgroups(indirectBuffer:threadsPerThreadgroup:)

<sub>Instance Method</sub>

Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries, using an indirect buffer for arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func dispatchThreadgroups(indirectBuffer: MTLGPUAddress, threadsPerThreadgroup: MTLSize)
```

## Parameters

- `indirectBuffer` — GPUAddress of a [MTLBuffer](../mtlbuffer.md) instance providing compute parameters. Lay out the data in this buffer as described in the [MTLDispatchThreadgroupsIndirectArguments](../mtldispatchthreadgroupsindirectarguments.md) structure. This address requires 4-byte alignment.

- `threadsPerThreadgroup` — A [MTLSize](../mtlsize.md) instance that represents the number of threads in one threadgroup, in each dimension.

## Discussion

This method allows you to supply the threadgroups-per-grid counts indirectly via an [MTLBuffer](../mtlbuffer.md) index. This enables you to calculate this value in the GPU timeline from a shader function, enabling GPU-driven workflows.

Metal assumes that the buffer contents correspond to the layout of struct [MTLDispatchThreadgroupsIndirectArguments](../mtldispatchthreadgroupsindirectarguments.md). You are responsible for ensuring this address aligns to 4-bytes.

Use an instance of [MTLResidencySet](../mtlresidencyset.md) to mark residency of the indirect buffer that the `indirectBuffer` parameter references.

## See Also

### Running dispatch commands

- [- dispatchThreads:threadsPerThreadgroup:](<dispatchthreads(threadspergrid_threadsperthreadgroup_).md>) — Encodes a compute dispatch command using an arbitrarily-sized grid.
- [- dispatchThreadsWithIndirectBuffer:](<dispatchthreads(indirectbuffer_).md>) — Encodes a compute dispatch command with an arbitrarily sized grid, using an indirect buffer for arguments.
- [- dispatchThreadgroups:threadsPerThreadgroup:](<dispatchthreadgroups(threadgroupspergrid_threadsperthreadgroup_).md>) — Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries.
