---
title: makeCommandQueue()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/makecommandqueue()
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makecommandqueue()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makecommandqueue%28%29.json'
content_hash: 'sha256:0879d544da557518'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeCommandQueue()

<sub>Instance Method</sub>

Creates a queue you use to submit rendering and computation commands to a GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCommandQueue() -> (any MTLCommandQueue)?
```

## Return Value

A new [MTLCommandQueue](../mtlcommandqueue.md) instance if the method completed successfully; otherwise `nil`.

## Discussion

A command queue can only submit commands to the GPU device instance that created it.

> [!important] Important
> The command queues you create with this method allow up to 64 uncompleted command buffers at time.

This method is the equivalent of passing `64` to the [- newCommandQueueWithMaxCommandBufferCount:](<makecommandqueue(maxcommandbuffercount_).md>) method.

**Swift**

```swift
let commandQueue = device.makeCommandQueue(maxCommandBufferCount: 64)
```

**Objective-C**

```objective-c
id<MTLCommandQueue> commandQueue;

NSUInteger capacity = 64;
commandQueue = [device newCommandQueueWithMaxCommandBufferCount:capacity];
```

## See Also

### Creating command queues

- [- newCommandQueueWithMaxCommandBufferCount:](<makecommandqueue(maxcommandbuffercount_).md>) — Creates a queue you use to submit rendering and computation commands to a GPU that has a fixed number of uncompleted command buffers.
