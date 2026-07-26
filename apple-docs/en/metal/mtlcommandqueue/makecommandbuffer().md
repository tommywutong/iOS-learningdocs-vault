---
title: makeCommandBuffer()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandqueue/makecommandbuffer()
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandqueue/makecommandbuffer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandqueue/makecommandbuffer%28%29.json'
content_hash: 'sha256:c19b9334b81dbeae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandQueue](../mtlcommandqueue.md)

# makeCommandBuffer()

<sub>Instance Method</sub>

Returns a command buffer from the command queue that maintains strong references to resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCommandBuffer() -> (any MTLCommandBuffer)?
```

## Discussion

The command buffers you create with this method maintain strong references to the resources you encode into it, including buffers, textures, samplers, and pipeline states. The command buffer releases these references after it finishes running on the GPU.

This method sets the [retainedReferences](../mtlcommandbuffer/retainedreferences.md) property to [true](../../swift/true.md) for the command buffer it creates.

Each command queue has a fixed number of command buffers for its lifetime (see [- newCommandQueueWithMaxCommandBufferCount:](<../mtldevice/makecommandqueue(maxcommandbuffercount_).md>)). This method blocks the calling CPU thread when the queue doesn’t have any free command buffers, and returns after the GPU finishes executing one.

## See Also

### Creating command buffers

- [- commandBufferWithDescriptor:](<makecommandbuffer(descriptor_).md>) — Returns a command buffer from the command queue that you configure with a descriptor.
- [- commandBufferWithUnretainedReferences](<makecommandbufferwithunretainedreferences().md>) — Returns a command buffer from the command queue that doesn’t maintain strong references to resources.
