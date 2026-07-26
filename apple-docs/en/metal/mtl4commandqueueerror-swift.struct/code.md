---
title: MTL4CommandQueueError.Code
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4commandqueueerror-swift.struct/code
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueueerror-swift.struct/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueueerror-swift.struct/code.json'
content_hash: 'sha256:4acd468091f9738c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueueError](../mtl4commandqueueerror-swift.struct.md)

# MTL4CommandQueueError.Code

<sub>Enumeration</sub>

Enumeration of kinds of errors that committing an array of command buffers instances can produce.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MTL4CommandQueueErrorAccessRevoked](code/accessrevoked.md) — Indicates that the system revokes GPU access because it’s responsible for too many timeouts or hangs.
- [MTL4CommandQueueErrorDeviceRemoved](code/deviceremoved.md) — Indicates the physical removal of the GPU before the command buffer completed. _(deprecated)_
- [MTL4CommandQueueErrorInternal](code/internal.md) — Indicates an internal problem in the Metal framework.
- [MTL4CommandQueueErrorNone](code/none.md) — Indicates the absence of any problems.
- [MTL4CommandQueueErrorNotPermitted](code/notpermitted.md) — Indicates a process doesn’t have access to a GPU device.
- [MTL4CommandQueueErrorOutOfMemory](code/outofmemory.md) — Indicates the GPU doesn’t have sufficient memory to execute a command buffer.
- [MTL4CommandQueueErrorTimeout](code/timeout.md) — Indicates the workload takes longer to execute than the system allows.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Submitting work to a GPU with Metal 4

- [MTL4CommandQueue](../mtl4commandqueue.md) — An abstraction representing a command queue that you use commit and synchronize command buffers and to perform other GPU operations.
- [MTL4CommandQueueDescriptor](../mtl4commandqueuedescriptor.md) — Groups together parameters for the creation of a new command queue.
- [MTL4CommandQueueError](../mtl4commandqueueerror-swift.struct.md)
- [MTL4CommandQueueErrorDomain](../mtl4commandqueueerrordomain.md)
- [MTL4CommandBuffer](../mtl4commandbuffer.md) — Records a sequence of GPU commands.
- [MTL4CommandBufferOptions](../mtl4commandbufferoptions.md) — Options to configure a command buffer before encoding work into it.
- [MTL4CommandEncoder](../mtl4commandencoder.md) — An encoder that writes GPU commands into a command buffer.
- [MTL4RenderEncoderOptions](../mtl4renderencoderoptions.md) — Custom render pass options you specify at encoder creation time.
- [MTL4ArgumentTable](../mtl4argumenttable.md) — Provides a mechanism to manage and provide resource bindings for buffers, textures, sampler states and other Metal resources.
- [MTL4ArgumentTableDescriptor](../mtl4argumenttabledescriptor.md) — Groups parameters for the creation of a Metal argument table.
- [MTL4CommandAllocator](../mtl4commandallocator.md) — Manages the memory backing the encoding of GPU commands into command buffers.
- [MTL4CommandAllocatorDescriptor](../mtl4commandallocatordescriptor.md) — Groups together parameters for creating a command allocator.
- [MTL4CommitOptions](../mtl4commitoptions.md) — Represents options to configure a commit operation on a command queue.
- [MTL4CommitFeedback](../mtl4commitfeedback.md) — Describes an object containing debug information from Metal to your app after completing a workload.
- [MTL4CommitFeedbackHandler](../mtl4commitfeedbackhandler.md) — Defines the block signature for a callback Metal invokes to provide your app feedback after completing a workload.
