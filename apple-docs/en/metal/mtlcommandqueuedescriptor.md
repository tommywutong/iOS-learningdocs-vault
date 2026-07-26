---
title: MTLCommandQueueDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandqueuedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandqueuedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandqueuedescriptor.json'
content_hash: 'sha256:df9aab5efde68c91'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCommandQueueDescriptor

<sub>Class</sub>

A configuration that customizes the behavior for a new command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLCommandQueueDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [logState](mtlcommandqueuedescriptor/logstate.md) — The shader logging configuration that the command queue uses.
- [maxCommandBufferCount](mtlcommandqueuedescriptor/maxcommandbuffercount.md) — An integer that sets the maximum number of uncompleted command buffers the queue can allow.

## See Also

### Submitting work to a GPU with Metal

- [Setting up a command structure](setting-up-a-command-structure.md) — Discover how Metal executes commands on a GPU.
- [MTLCommandQueue](mtlcommandqueue.md) — An instance you use to create, submit, and schedule command buffers to a specific GPU device to run the commands within those buffers.
- [MTLCommandBuffer](mtlcommandbuffer.md) — A container that stores a sequence of GPU commands that you encode into it.
- [MTLCommandBufferDescriptor](mtlcommandbufferdescriptor.md) — A configuration that customizes the behavior for a new command buffer.
- [MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md) — The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [MTLCommandEncoder](mtlcommandencoder.md) — An encoder that writes GPU commands into a command buffer.
