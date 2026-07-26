---
title: 'removeResidencySets(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandqueue/removeresidencysets(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandqueue/removeresidencysets(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandqueue/removeresidencysets%28_%3A%29.json'
content_hash: 'sha256:fcd4ca2a6beef928'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandQueue](../mtlcommandqueue.md)

# removeResidencySets(_:)

<sub>Instance Method</sub>

Removes multiple residency sets from a command queue’s list, which means Metal doesn’t apply them to the queue’s command buffers as you commit them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeResidencySets(_ residencySets: [any MTLResidencySet])
```

## Parameters

- `residencySets` — An array of residency sets, each of which contains resource allocations, such as [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), and [MTLHeap](../mtlheap.md) instances.

## Discussion

The method doesn’t remove the residency sets from command buffers the queue owns with a [status](../mtlcommandbuffer/status.md) property that’s equal to [MTLCommandBufferStatusCommitted](../mtlcommandbufferstatus/committed.md) or [MTLCommandBufferStatusScheduled](../mtlcommandbufferstatus/scheduled.md).

See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) and [MTLResidencySet](../mtlresidencyset.md) for more information.

## See Also

### Detaching residency sets

- [- removeResidencySet:](<removeresidencyset(__).md>) — Removes a residency set from a command queue’s list, which means Metal doesn’t apply it to the queue’s command buffers as you commit them.
