---
title: 'removeAllocations:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlresidencyset/removeallocations:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset/removeallocations:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset/removeallocations%3Acount%3A.json'
content_hash: 'sha256:d689c494fc1c29ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySet](../mtlresidencyset.md)

# removeAllocations:count:

<sub>Instance Method</sub>

Stages multiple resources to leave the residency set’s list of allocations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) removeAllocations:(id<MTLAllocation> const[]) allocations count:(NSUInteger) count;
```

## Parameters

- `allocations` — A C array of resource allocations, whose elements can be an arbitrarily mix of [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), and [MTLHeap](../mtlheap.md) instances.

- `count` — The number of elements in `allocations`.

## Discussion

Finalize the removal of these resource allocations, and all other changes you stage, by calling a residency set’s [- commit](<commit().md>) method.

## See Also

### Removing allocations

- [- removeAllAllocations](<removeallallocations().md>) — Stages all the resources in the residency set to leave its list of allocations.
- [- removeAllocation:](<removeallocation(__).md>) — Stages a single resource to leave the residency set’s list of allocations.
