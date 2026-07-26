---
title: MTL4CommandBuffer
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4commandbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandbuffer.json'
content_hash: 'sha256:7f1a20753e9720c1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4CommandBuffer

<sub>Protocol</sub>

Records a sequence of GPU commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTL4CommandBuffer : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [device](mtl4commandbuffer/device.md) — Returns the GPU device that this command buffer belongs to.
- [label](mtl4commandbuffer/label.md) — Assigns an optional label with this command buffer.

### Instance Methods

- [- beginCommandBufferWithAllocator:](<mtl4commandbuffer/begincommandbuffer(allocator_).md>) — Prepares a command buffer for encoding.
- [- beginCommandBufferWithAllocator:options:](<mtl4commandbuffer/begincommandbuffer(allocator_options_).md>) — Prepares a command buffer for encoding with additional options.
- [- endCommandBuffer](<mtl4commandbuffer/endcommandbuffer().md>) — Closes a command buffer to prepare it for submission to a command queue.
- [- computeCommandEncoder](<mtl4commandbuffer/makecomputecommandencoder().md>) — Creates a compute command encoder.
- [- machineLearningCommandEncoder](<mtl4commandbuffer/makemachinelearningcommandencoder().md>) — Creates a machine learning command encoder.
- [- renderCommandEncoderWithDescriptor:options:](<mtl4commandbuffer/makerendercommandencoder(descriptor_options_).md>) — Creates a render command encoder from a render pass descriptor with additional options.
- [- popDebugGroup](<mtl4commandbuffer/popdebuggroup().md>) — Pops the latest string from the stack of debug groups for this command buffer.
- [- pushDebugGroup:](<mtl4commandbuffer/pushdebuggroup(__).md>) — Pushes a string onto a stack of debug groups for this command buffer.
- [resolveCounterHeap(_:range:buffer:fenceToWait:fenceToUpdate:)](<mtl4commandbuffer/resolvecounterheap(__range_buffer_fencetowait_fencetoupdate_).md>) — Encodes a command that resolves an opaque counter heap into a buffer.
- [- useResidencySet:](<mtl4commandbuffer/useresidencyset(__).md>) — Applies a residency set to a command buffer.
- [useResidencySets(_:)](<mtl4commandbuffer/useresidencysets(__).md>) — Applies multiple residency sets to a command buffer.
- [- writeTimestampIntoHeap:atIndex:](<mtl4commandbuffer/writetimestamp(counterheap_index_).md>) — Writes a GPU timestamp into the given counter heap.

## See Also

### Submitting work to a GPU with Metal 4

- [MTL4CommandQueue](mtl4commandqueue.md) — An abstraction representing a command queue that you use commit and synchronize command buffers and to perform other GPU operations.
- [MTL4CommandQueueDescriptor](mtl4commandqueuedescriptor.md) — Groups together parameters for the creation of a new command queue.
- [MTL4CommandQueueError](mtl4commandqueueerror-swift.struct.md)
- [Code](mtl4commandqueueerror-swift.struct/code.md) — Enumeration of kinds of errors that committing an array of command buffers instances can produce.
- [MTL4CommandQueueErrorDomain](mtl4commandqueueerrordomain.md)
- [MTL4CommandBufferOptions](mtl4commandbufferoptions.md) — Options to configure a command buffer before encoding work into it.
- [MTL4CommandEncoder](mtl4commandencoder.md) — An encoder that writes GPU commands into a command buffer.
- [MTL4RenderEncoderOptions](mtl4renderencoderoptions.md) — Custom render pass options you specify at encoder creation time.
- [MTL4ArgumentTable](mtl4argumenttable.md) — Provides a mechanism to manage and provide resource bindings for buffers, textures, sampler states and other Metal resources.
- [MTL4ArgumentTableDescriptor](mtl4argumenttabledescriptor.md) — Groups parameters for the creation of a Metal argument table.
- [MTL4CommandAllocator](mtl4commandallocator.md) — Manages the memory backing the encoding of GPU commands into command buffers.
- [MTL4CommandAllocatorDescriptor](mtl4commandallocatordescriptor.md) — Groups together parameters for creating a command allocator.
- [MTL4CommitOptions](mtl4commitoptions.md) — Represents options to configure a commit operation on a command queue.
- [MTL4CommitFeedback](mtl4commitfeedback.md) — Describes an object containing debug information from Metal to your app after completing a workload.
- [MTL4CommitFeedbackHandler](mtl4commitfeedbackhandler.md) — Defines the block signature for a callback Metal invokes to provide your app feedback after completing a workload.
