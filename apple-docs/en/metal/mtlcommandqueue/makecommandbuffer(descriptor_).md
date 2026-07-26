---
title: 'makeCommandBuffer(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandqueue/makecommandbuffer(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandqueue/makecommandbuffer(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandqueue/makecommandbuffer%28descriptor%3A%29.json'
content_hash: 'sha256:4ff49e5fd0d208a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandQueue](../mtlcommandqueue.md)

# makeCommandBuffer(descriptor:)

<sub>Instance Method</sub>

Returns a command buffer from the command queue that you configure with a descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCommandBuffer(descriptor: MTLCommandBufferDescriptor) -> (any MTLCommandBuffer)?
```

## Parameters

- `descriptor` — An [MTLCommandBufferDescriptor](../mtlcommandbufferdescriptor.md) instance that configures the [MTLCommandBuffer](../mtlcommandbuffer.md) the method returns.

## Discussion

Use this method to create a command buffer that you configure with a descriptor. You can configure whether the command buffer retains references to resources that its commands refer to by setting the `descriptor` parameter’s [retainedReferences](../mtlcommandbufferdescriptor/retainedreferences.md) property. You can also configure whether the command buffer saves extra error information, which is useful during development, by setting the descriptor’s [errorOptions](../mtlcommandbufferdescriptor/erroroptions.md) property.

Each command queue has a fixed number of command buffers for its lifetime (see [- newCommandQueueWithMaxCommandBufferCount:](<../mtldevice/makecommandqueue(maxcommandbuffercount_).md>)). This method blocks the calling CPU thread when the queue doesn’t have any free command buffers, and returns after the GPU finishes executing one.

## See Also

### Creating command buffers

- [- commandBuffer](<makecommandbuffer().md>) — Returns a command buffer from the command queue that maintains strong references to resources.
- [- commandBufferWithUnretainedReferences](<makecommandbufferwithunretainedreferences().md>) — Returns a command buffer from the command queue that doesn’t maintain strong references to resources.
