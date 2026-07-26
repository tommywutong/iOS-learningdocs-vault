---
title: 'removeResidencySet(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandqueue/removeresidencyset(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandqueue/removeresidencyset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandqueue/removeresidencyset%28_%3A%29.json'
content_hash: 'sha256:72814d2755887559'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandQueue](../mtlcommandqueue.md)

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

The method doesn’t remove the residency set from command buffers the queue owns with a [status](../mtlcommandbuffer/status.md) property that’s equal to [MTLCommandBufferStatusCommitted](../mtlcommandbufferstatus/committed.md) or [MTLCommandBufferStatusScheduled](../mtlcommandbufferstatus/scheduled.md).

See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) and [MTLResidencySet](../mtlresidencyset.md) for more information.

## See Also

### Detaching residency sets

- [removeResidencySets(_:)](<removeresidencysets(__).md>) — Removes multiple residency sets from a command queue’s list, which means Metal doesn’t apply them to the queue’s command buffers as you commit them.
