---
title: 'makeCommandQueue(maxCommandBufferCount:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makecommandqueue(maxcommandbuffercount:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makecommandqueue(maxcommandbuffercount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makecommandqueue%28maxcommandbuffercount%3A%29.json'
content_hash: 'sha256:e7f9b4ec1200dd59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeCommandQueue(maxCommandBufferCount:)

<sub>Instance Method</sub>

Creates a queue you use to submit rendering and computation commands to a GPU that has a fixed number of uncompleted command buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCommandQueue(maxCommandBufferCount: Int) -> (any MTLCommandQueue)?
```

## Parameters

- `maxCommandBufferCount` — An integer that sets the maximum number of uncompleted command buffers the queue can allow.

## Return Value

A new [MTLCommandQueue](../mtlcommandqueue.md) instance if the method completed successfully; otherwise `nil`.

## Discussion

A Command queue can only submit commands to the GPU device instance that created it.

## See Also

### Creating command queues

- [- newCommandQueue](<makecommandqueue().md>) — Creates a queue you use to submit rendering and computation commands to a GPU.
