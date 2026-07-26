---
title: 'makeMTL4CommandQueue(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makemtl4commandqueue(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makemtl4commandqueue(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makemtl4commandqueue%28descriptor%3A%29.json'
content_hash: 'sha256:008fa50414976eb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeMTL4CommandQueue(descriptor:)

<sub>Instance Method</sub>

Creates a new command queue from a queue descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeMTL4CommandQueue(descriptor: MTL4CommandQueueDescriptor) throws -> any MTL4CommandQueue
```

## Parameters

- `descriptor` — A [MTL4CommandQueueDescriptor](../mtl4commandqueuedescriptor.md) instance that configures the [MTL4CommandQueue](../mtl4commandqueue.md) instance.

## Return Value

A [MTL4CommandQueue](../mtl4commandqueue.md) instance, or `nil` if the function failed.
