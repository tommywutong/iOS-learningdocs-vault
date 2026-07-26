---
title: 'removeAllocations(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlresidencyset/removeallocations(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset/removeallocations(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset/removeallocations%28_%3A%29.json'
content_hash: 'sha256:5e6f266a62f001cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySet](../mtlresidencyset.md)

# removeAllocations(_:)

<sub>Instance Method</sub>

Stages multiple resources to leave the residency set’s list of allocations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeAllocations(_ allocations: [any MTLAllocation])
```

## Parameters

- `allocations` — An array of resource allocations, whose elements can be an arbitrarily mix of [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), and [MTLHeap](../mtlheap.md) instances.

## Discussion

Finalize the removal of these resource allocations, and all other changes you stage, by calling a residency set’s [- commit](<commit().md>) method.

## See Also

### Removing allocations

- [- removeAllAllocations](<removeallallocations().md>) — Stages all the resources in the residency set to leave its list of allocations.
- [- removeAllocation:](<removeallocation(__).md>) — Stages a single resource to leave the residency set’s list of allocations.
