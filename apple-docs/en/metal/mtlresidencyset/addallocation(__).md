---
title: 'addAllocation(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlresidencyset/addallocation(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset/addallocation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset/addallocation%28_%3A%29.json'
content_hash: 'sha256:8fc8c249329e3eb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySet](../mtlresidencyset.md)

# addAllocation(_:)

<sub>Instance Method</sub>

Stages a single resource to join the residency set’s list of allocations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addAllocation(_ allocation: any MTLAllocation)
```

## Parameters

- `allocation` — A resource allocation, such as an [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), or [MTLHeap](../mtlheap.md).

## Discussion

Finalize the inclusion of these resource allocations, and all other changes you stage, by calling a residency set’s [- commit](<commit().md>) method.

## See Also

### Adding allocations

- [addAllocations(_:)](<addallocations(__).md>) — Stages multiple resources to join the residency set’s list of allocations.
