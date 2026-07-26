---
title: MTL4ArgumentTableDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4argumenttabledescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4argumenttabledescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4argumenttabledescriptor.json'
content_hash: 'sha256:28efeeaefb260ba3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4ArgumentTableDescriptor

<sub>Class</sub>

Groups parameters for the creation of a Metal argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4ArgumentTableDescriptor
```

## Overview

Argument tables provide resource bindings to your Metal pipeline states.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [initializeBindings](mtl4argumenttabledescriptor/initializebindings.md) — Configures whether Metal initializes the bindings to nil values upon creation of argument table.
- [label](mtl4argumenttabledescriptor/label.md) — Assigns an optional label with the argument table for debug purposes.
- [maxBufferBindCount](mtl4argumenttabledescriptor/maxbufferbindcount.md) — Determines the number of buffer-binding slots for the argument table.
- [maxSamplerStateBindCount](mtl4argumenttabledescriptor/maxsamplerstatebindcount.md) — Determines the number of sampler state-binding slots for the argument table.
- [maxTextureBindCount](mtl4argumenttabledescriptor/maxtexturebindcount.md) — Determines the number of texture-binding slots for the argument table.
- [supportAttributeStrides](mtl4argumenttabledescriptor/supportattributestrides.md) — Controls whether Metal should reserve memory for attribute strides in the argument table.

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
- [MTL4CommandAllocator](mtl4commandallocator.md) — Manages the memory backing the encoding of GPU commands into command buffers.
- [MTL4CommandAllocatorDescriptor](mtl4commandallocatordescriptor.md) — Groups together parameters for creating a command allocator.
- [MTL4CommitOptions](mtl4commitoptions.md) — Represents options to configure a commit operation on a command queue.
- [MTL4CommitFeedback](mtl4commitfeedback.md) — Describes an object containing debug information from Metal to your app after completing a workload.
- [MTL4CommitFeedbackHandler](mtl4commitfeedbackhandler.md) — Defines the block signature for a callback Metal invokes to provide your app feedback after completing a workload.
