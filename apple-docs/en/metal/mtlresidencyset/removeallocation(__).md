---
title: 'removeAllocation(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlresidencyset/removeallocation(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset/removeallocation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset/removeallocation%28_%3A%29.json'
content_hash: 'sha256:dc557c3e07e5bf0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySet](../mtlresidencyset.md)

# removeAllocation(_:)

<sub>Instance Method</sub>

Stages a single resource to leave the residency set’s list of allocations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeAllocation(_ allocation: any MTLAllocation)
```

## Parameters

- `allocation` — A resource allocation, such as an [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), or [MTLHeap](../mtlheap.md).

## Discussion

Finalize the removal of these resource allocations, and all others changes you stage, by calling a residency set’s [- commit](<commit().md>) method.

## See Also

### Removing allocations

- [- removeAllAllocations](<removeallallocations().md>) — Stages all the resources in the residency set to leave its list of allocations.
- [removeAllocations(_:)](<removeallocations(__).md>) — Stages multiple resources to leave the residency set’s list of allocations.
