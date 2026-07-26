---
title: 'removeResidencySet(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/removeresidencyset(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/removeresidencyset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/removeresidencyset%28_%3A%29.json'
content_hash: 'sha256:eb9413d6a13b2426'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# removeResidencySet(_:)

<sub>Instance Method</sub>

Removes a residency set from a command queue’s list, which means Metal doesn’t apply it to the queue’s command buffers as you commit them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeResidencySet(_ residencySet: any MTLResidencySet)
```

## Parameters

- `residencySet` — A residency set that contains resource allocations, such as [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), and [MTLHeap](../mtlheap.md) instances.

## Discussion

The method doesn’t remove the residency set from command buffers the queue owns with an [status](../mtlcommandbuffer/status.md) property that’s equal to [MTLCommandBufferStatusCommitted](../mtlcommandbufferstatus/committed.md) or [MTLCommandBufferStatusScheduled](../mtlcommandbufferstatus/scheduled.md).

See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) and [MTLResidencySet](../mtlresidencyset.md) for more information.
