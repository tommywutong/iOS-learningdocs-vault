---
title: MTLCommandBufferDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbufferdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbufferdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbufferdescriptor.json'
content_hash: 'sha256:51b1bb9d5c4166cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCommandBufferDescriptor

<sub>Class</sub>

A configuration that customizes the behavior for a new command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLCommandBufferDescriptor
```

## Overview

Create a command buffer with a custom configuration by creating an [MTLCommandBufferDescriptor](mtlcommandbufferdescriptor.md) instance and passing it to an [MTLCommandQueue](mtlcommandqueue.md) instance’s [- commandBufferWithDescriptor:](<mtlcommandqueue/makecommandbuffer(descriptor_).md>) method. You can configure whether the command buffer retains references to resources that its commands refer to with the [retainedReferences](mtlcommandbufferdescriptor/retainedreferences.md) property. The command buffer can save extra error information, which is useful during development, by setting its [errorOptions](mtlcommandbufferdescriptor/erroroptions.md) property to [MTLCommandBufferErrorOptionEncoderExecutionStatus](mtlcommandbuffererroroption/encoderexecutionstatus.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the command buffer

- [logState](mtlcommandbufferdescriptor/logstate.md) — The shader logging configuration that the command buffer uses.
- [retainedReferences](mtlcommandbufferdescriptor/retainedreferences.md) — A Boolean value that indicates whether the command buffer the descriptor creates maintains strong references to the resources it uses.
- [errorOptions](mtlcommandbufferdescriptor/erroroptions.md) — The reporting configuration that indicates which information the GPU driver stores in a command buffer’s error property.
- [MTLCommandBufferErrorOption](mtlcommandbuffererroroption.md) — Options for reporting errors from a command buffer.

## See Also

### Submitting work to a GPU with Metal

- [Setting up a command structure](setting-up-a-command-structure.md) — Discover how Metal executes commands on a GPU.
- [MTLCommandQueue](mtlcommandqueue.md) — An instance you use to create, submit, and schedule command buffers to a specific GPU device to run the commands within those buffers.
- [MTLCommandQueueDescriptor](mtlcommandqueuedescriptor.md) — A configuration that customizes the behavior for a new command queue.
- [MTLCommandBuffer](mtlcommandbuffer.md) — A container that stores a sequence of GPU commands that you encode into it.
- [MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md) — The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [MTLCommandEncoder](mtlcommandencoder.md) — An encoder that writes GPU commands into a command buffer.
