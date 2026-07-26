---
title: allAllocations
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresidencyset/allallocations
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset/allallocations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset/allallocations.json'
content_hash: 'sha256:e2db7971101fa887'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySet](../mtlresidencyset.md)

# allAllocations

<sub>Instance Property</sub>

The residency set’s current list of resource allocations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var allAllocations: [any MTLAllocation] { get }
```

## Discussion

This property is an array of resource allocations, and its elements can be an arbitrary mix of [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), and [MTLHeap](../mtlheap.md) instances.

The residency set updates the property’s value when you call the [- commit](<commit().md>) method.

## See Also

### Inspecting a residency set

- [label](label.md) — An optional name that can help you identify the residency set.
- [device](device.md) — The Metal device that owns the residency set.
- [- containsAllocation:](<containsallocation(__).md>) — Returns a Boolean value that indicates whether the residency set contains a specific resource allocation.
- [allocationCount](allocationcount.md) — The number of resource allocations in the residency set.
- [allocatedSize](allocatedsize.md) — The amount of resident memory, in bytes, the residency set’s resource allocations consume.
