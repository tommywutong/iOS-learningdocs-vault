---
title: MTL4CommitFeedbackHandler
framework: Metal
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4commitfeedbackhandler
source_url: 'https://developer.apple.com/documentation/metal/mtl4commitfeedbackhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commitfeedbackhandler.json'
content_hash: 'sha256:a22c21f08213db80'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4CommitFeedbackHandler

<sub>Type Alias</sub>

Defines the block signature for a callback Metal invokes to provide your app feedback after completing a workload.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias MTL4CommitFeedbackHandler = @Sendable (any MTL4CommitFeedback) -> Void
```

## Parameters

- `commitFeedback` — A commit feedback instance containing information about the workload.

## Discussion

You register a commit feedback block with Metal by providing an instance of [MTL4CommitOptions](mtl4commitoptions.md) to the command queue’s commit method, [commit:count:options:](mtl4commandqueue/commit_count_options_.md). The commit options instance references your commit feedback handler after you add it via its [- addFeedbackHandler:](<mtl4commitoptions/addfeedbackhandler(__).md>) method.

## See Also

### Submitting work to a GPU with Metal 4

- [MTL4CommandQueue](mtl4commandqueue.md) — An abstraction representing a command queue that you use commit and synchronize command buffers and to perform other GPU operations.
- [MTL4CommandQueueDescriptor](mtl4commandqueuedescriptor.md) — Groups together parameters for the creation of a new command queue.
- [MTL4CommandQueueError](mtl4commandqueueerror-swift.struct.md)
- [Code](mtl4commandqueueerror-swift.struct/code.md) — Enumeration of kinds of errors that committing an array of command buffers instances can produce.
- [MTL4CommandQueueErrorDomain](mtl4commandqueueerrordomain.md)
- [MTL4CommandBuffer](mtl4commandbuffer.md) — Records a sequence of GPU commands.
- [MTL4CommandBufferOptions](mtl4commandbufferoptions.md) — Options to configure a command buffer before encoding work into it.
- [MTL4CommandEncoder](mtl4commandencoder.md) — An encoder that writes GPU commands into a command buffer.
- [MTL4RenderEncoderOptions](mtl4renderencoderoptions.md) — Custom render pass options you specify at encoder creation time.
- [MTL4ArgumentTable](mtl4argumenttable.md) — Provides a mechanism to manage and provide resource bindings for buffers, textures, sampler states and other Metal resources.
- [MTL4ArgumentTableDescriptor](mtl4argumenttabledescriptor.md) — Groups parameters for the creation of a Metal argument table.
- [MTL4CommandAllocator](mtl4commandallocator.md) — Manages the memory backing the encoding of GPU commands into command buffers.
- [MTL4CommandAllocatorDescriptor](mtl4commandallocatordescriptor.md) — Groups together parameters for creating a command allocator.
- [MTL4CommitOptions](mtl4commitoptions.md) — Represents options to configure a commit operation on a command queue.
- [MTL4CommitFeedback](mtl4commitfeedback.md) — Describes an object containing debug information from Metal to your app after completing a workload.
