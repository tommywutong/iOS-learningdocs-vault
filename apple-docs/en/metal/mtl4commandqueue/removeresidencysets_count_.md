---
title: 'removeResidencySets:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/removeresidencysets:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/removeresidencysets:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/removeresidencysets%3Acount%3A.json'
content_hash: 'sha256:90a7495283166c92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# removeResidencySets:count:

<sub>Instance Method</sub>

Removes multiple residency sets from a command queue’s list, which means Metal doesn’t apply them to the queue’s command buffers as you commit them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) removeResidencySets:(id<MTLResidencySet> const[]) residencySets count:(NSUInteger) count;
```

## Parameters

- `residencySets` — A C array of residency sets, each of which contains resource allocations, such as [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), and [MTLHeap](../mtlheap.md) instances.

- `count` — The number of elements in `residencySets`.

## Discussion

The method doesn’t remove the residency sets from command buffers the queue owns with an [status](../mtlcommandbuffer/status.md) property that’s equal to [MTLCommandBufferStatusCommitted](../mtlcommandbufferstatus/committed.md) or [MTLCommandBufferStatusScheduled](../mtlcommandbufferstatus/scheduled.md).

See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) and [MTLResidencySet](../mtlresidencyset.md) for more information.
