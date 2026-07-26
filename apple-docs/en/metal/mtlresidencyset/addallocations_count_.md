---
title: 'addAllocations:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlresidencyset/addallocations:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset/addallocations:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset/addallocations%3Acount%3A.json'
content_hash: 'sha256:49c7d5a5328b90da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySet](../mtlresidencyset.md)

# addAllocations:count:

<sub>Instance Method</sub>

Stages multiple resources to join the residency set’s list of allocations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) addAllocations:(id<MTLAllocation> const[]) allocations count:(NSUInteger) count;
```

## Parameters

- `allocations` — A C array of resource allocations, whose elements can be an arbitrarily mix of [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), and [MTLHeap](../mtlheap.md) instances.

- `count` — The number of elements in `allocations`.

## Discussion

Finalize the inclusion of these resource allocations, and all other changes you stage, by calling a residency set’s [- commit](<commit().md>) method.

## See Also

### Adding allocations

- [- addAllocation:](<addallocation(__).md>) — Stages a single resource to join the residency set’s list of allocations.
