---
title: makeCommandBufferWithUnretainedReferences()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandqueue/makecommandbufferwithunretainedreferences()
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandqueue/makecommandbufferwithunretainedreferences()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandqueue/makecommandbufferwithunretainedreferences%28%29.json'
content_hash: 'sha256:4293c36654b11197'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandQueue](../mtlcommandqueue.md)

# makeCommandBufferWithUnretainedReferences()

<sub>Instance Method</sub>

Returns a command buffer from the command queue that doesn’t maintain strong references to resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCommandBufferWithUnretainedReferences() -> (any MTLCommandBuffer)?
```

## Discussion

Use this method to create a command buffer that doesn’t retain or release any of the resources it needs to run its commands.

Apps typically create command buffers that don’t maintain references to resources for extremely performance-critical situations. Even though the runtime cost for retaining or releasing a single resource is trivial, the aggregate time savings may be worth it.

It’s your app’s responsibility to maintain strong references to all the resources the command buffer uses until it finishes running on the GPU.

> [!important] Important
> Releasing a resource before a command buffer’s commands complete may trigger a runtime error or erratic behavior.

This method sets the [retainedReferences](../mtlcommandbuffer/retainedreferences.md) property to [false](../../swift/false.md) for the command buffer it creates.

Each command queue has a fixed number of command buffers for its lifetime (see [- newCommandQueueWithMaxCommandBufferCount:](<../mtldevice/makecommandqueue(maxcommandbuffercount_).md>)). This method blocks the calling CPU thread when the queue doesn’t have any free command buffers, and returns after the GPU finishes executing one.

## See Also

### Creating command buffers

- [- commandBufferWithDescriptor:](<makecommandbuffer(descriptor_).md>) — Returns a command buffer from the command queue that you configure with a descriptor.
- [- commandBuffer](<makecommandbuffer().md>) — Returns a command buffer from the command queue that maintains strong references to resources.
