---
title: 'makeIOCommandQueue(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makeiocommandqueue(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makeiocommandqueue(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makeiocommandqueue%28descriptor%3A%29.json'
content_hash: 'sha256:8d2d034785cf0ff9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeIOCommandQueue(descriptor:)

<sub>Instance Method</sub>

Creates an input/output command queue you use to submit commands that load assets from the file system into GPU resources or system memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeIOCommandQueue(descriptor: MTLIOCommandQueueDescriptor) throws -> any MTLIOCommandQueue
```

## Parameters

- `descriptor` — A descriptor instance that configures the command queue.

## Return Value

A new [MTLIOCommandQueue](../mtliocommandqueue.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

For information about using input/output command queues and file handles, see [Resource loading](../resource-loading.md).
