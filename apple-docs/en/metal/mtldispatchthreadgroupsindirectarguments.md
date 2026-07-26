---
title: MTLDispatchThreadgroupsIndirectArguments
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldispatchthreadgroupsindirectarguments
source_url: 'https://developer.apple.com/documentation/metal/mtldispatchthreadgroupsindirectarguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldispatchthreadgroupsindirectarguments.json'
content_hash: 'sha256:855fe0f8d2ec4f31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDispatchThreadgroupsIndirectArguments

<sub>Structure</sub>

The data layout required for arguments needed to specify the size of threadgroups.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLDispatchThreadgroupsIndirectArguments
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Specifying the size of the threadgroup

- [init()](<mtldispatchthreadgroupsindirectarguments/init().md>) — Returns a new data layout for dispatching threadgroups over indirect buffer calls.
- [init(threadgroupsPerGrid:)](<mtldispatchthreadgroupsindirectarguments/init(threadgroupspergrid_).md>) — Returns a new data layout for dispatching threadgroups over indirect buffer calls, with specified threadgroups per grid.
- [threadgroupsPerGrid](mtldispatchthreadgroupsindirectarguments/threadgroupspergrid.md) — The number of threadgroups for the grid, in each dimension.

## See Also

### Related Documentation

- [- dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:](<mtlcomputecommandencoder/dispatchthreadgroups(indirectbuffer_indirectbufferoffset_threadsperthreadgroup_).md>) — Encodes a dispatch call for a compute pass, using an indirect buffer that defines the size of a grid that aligns to threadgroup boundaries.

### Configuring a compute pass

- [MTLComputePassDescriptor](mtlcomputepassdescriptor.md) — A description of how to dispatch execution of pass commands and GPU performance sampling.
- [MTLDispatchType](mtldispatchtype.md) — The type of dispatch method to use when calling encoded functions.
- [MTLComputePassSampleBufferAttachmentDescriptor](mtlcomputepasssamplebufferattachmentdescriptor.md) — A configuration that instructs the GPU where to store counter data from the beginning and end of a compute pass.
- [MTLComputePassSampleBufferAttachmentDescriptorArray](mtlcomputepasssamplebufferattachmentdescriptorarray.md) — A container that stores an array of sample buffer attachments for a compute pass.
