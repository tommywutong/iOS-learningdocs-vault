---
title: 'addResidencySets:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandqueue/addresidencysets:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandqueue/addresidencysets:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandqueue/addresidencysets%3Acount%3A.json'
content_hash: 'sha256:1e107870cacf60cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandQueue](../mtlcommandqueue.md)

# addResidencySets:count:

<sub>Instance Method</sub>

Applies multiple residency sets to a queue, which Metal applies to the queue’s command buffers as you commit them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) addResidencySets:(id<MTLResidencySet> const[]) residencySets count:(NSUInteger) count;
```

## Parameters

- `residencySets` — A C array of residency sets, each of which contains resource allocations, such as [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), and [MTLHeap](../mtlheap.md) instances.

- `count` — The number of elements in `residencySets`.

## Discussion

Each command queue can maintain a list of up to 32 different residency sets. See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) and [MTLResidencySet](../mtlresidencyset.md) for more information.

## See Also

### Attaching residency sets

- [- addResidencySet:](<addresidencyset(__).md>) — Applies a residency set to a queue, which Metal applies to the queue’s command buffers as you commit them.
