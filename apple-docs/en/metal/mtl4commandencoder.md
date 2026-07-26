---
title: MTL4CommandEncoder
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4commandencoder
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandencoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandencoder.json'
content_hash: 'sha256:160b2bed05d96543'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4CommandEncoder

<sub>Protocol</sub>

An encoder that writes GPU commands into a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTL4CommandEncoder : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [MTL4ComputeCommandEncoder](mtl4computecommandencoder.md), [MTL4MachineLearningCommandEncoder](mtl4machinelearningcommandencoder.md), [MTL4RenderCommandEncoder](mtl4rendercommandencoder.md)

## Topics

### Instance Properties

- [commandBuffer](mtl4commandencoder/commandbuffer.md) — Returns the command buffer that is currently encoding commands.
- [label](mtl4commandencoder/label.md) — Provides an optional label to assign to the command encoder for debug purposes.

### Instance Methods

- [barrier(afterEncoderStages:beforeEncoderStages:visibilityOptions:)](<mtl4commandencoder/barrier(afterencoderstages_beforeencoderstages_visibilityoptions_).md>) — Encodes an intra-pass barrier.
- [barrier(afterQueueStages:beforeStages:visibilityOptions:)](<mtl4commandencoder/barrier(afterqueuestages_beforestages_visibilityoptions_).md>) — Encodes a consumer barrier on work you commit to the same command queue.
- [barrier(afterStages:beforeQueueStages:visibilityOptions:)](<mtl4commandencoder/barrier(afterstages_beforequeuestages_visibilityoptions_).md>) — Encodes a producer barrier on work committed to the same command queue.
- [- endEncoding](<mtl4commandencoder/endencoding().md>) — Declares that all command generation from this encoder is complete.
- [- insertDebugSignpost:](<mtl4commandencoder/insertdebugsignpost(__).md>) — Inserts a debug string into the frame data to aid debugging.
- [- popDebugGroup](<mtl4commandencoder/popdebuggroup().md>) — Pops the latest debug group string from this encoder’s stack of debug groups.
- [- pushDebugGroup:](<mtl4commandencoder/pushdebuggroup(__).md>) — Pushes a string onto this encoder’s stack of debug groups.
- [- updateFence:afterEncoderStages:](<mtl4commandencoder/updatefence(__afterencoderstages_).md>) — Encodes a command that instructs the GPU to update a fence after one or more stages, which can unblock other passes waiting for the fence.
- [- waitForFence:beforeEncoderStages:](<mtl4commandencoder/waitforfence(__beforeencoderstages_).md>) — Encodes a command that instructs the GPU to pause before starting one or more stages of the pass until a pass updates a fence.

## See Also

### Submitting work to a GPU with Metal 4

- [MTL4CommandQueue](mtl4commandqueue.md) — An abstraction representing a command queue that you use commit and synchronize command buffers and to perform other GPU operations.
- [MTL4CommandQueueDescriptor](mtl4commandqueuedescriptor.md) — Groups together parameters for the creation of a new command queue.
- [MTL4CommandQueueError](mtl4commandqueueerror-swift.struct.md)
- [Code](mtl4commandqueueerror-swift.struct/code.md) — Enumeration of kinds of errors that committing an array of command buffers instances can produce.
- [MTL4CommandQueueErrorDomain](mtl4commandqueueerrordomain.md)
- [MTL4CommandBuffer](mtl4commandbuffer.md) — Records a sequence of GPU commands.
- [MTL4CommandBufferOptions](mtl4commandbufferoptions.md) — Options to configure a command buffer before encoding work into it.
- [MTL4RenderEncoderOptions](mtl4renderencoderoptions.md) — Custom render pass options you specify at encoder creation time.
- [MTL4ArgumentTable](mtl4argumenttable.md) — Provides a mechanism to manage and provide resource bindings for buffers, textures, sampler states and other Metal resources.
- [MTL4ArgumentTableDescriptor](mtl4argumenttabledescriptor.md) — Groups parameters for the creation of a Metal argument table.
- [MTL4CommandAllocator](mtl4commandallocator.md) — Manages the memory backing the encoding of GPU commands into command buffers.
- [MTL4CommandAllocatorDescriptor](mtl4commandallocatordescriptor.md) — Groups together parameters for creating a command allocator.
- [MTL4CommitOptions](mtl4commitoptions.md) — Represents options to configure a commit operation on a command queue.
- [MTL4CommitFeedback](mtl4commitfeedback.md) — Describes an object containing debug information from Metal to your app after completing a workload.
- [MTL4CommitFeedbackHandler](mtl4commitfeedbackhandler.md) — Defines the block signature for a callback Metal invokes to provide your app feedback after completing a workload.
