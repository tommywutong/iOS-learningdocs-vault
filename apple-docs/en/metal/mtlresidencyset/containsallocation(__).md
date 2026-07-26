---
title: 'containsAllocation(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlresidencyset/containsallocation(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset/containsallocation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset/containsallocation%28_%3A%29.json'
content_hash: 'sha256:a0bd5e84a1715941'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySet](../mtlresidencyset.md)

# containsAllocation(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the residency set contains a specific resource allocation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func containsAllocation(_ anAllocation: any MTLAllocation) -> Bool
```

## Parameters

- `anAllocation` — A resource allocation, such as an [MTLBuffer](../mtlbuffer.md), [MTLTexture](../mtltexture.md), or [MTLHeap](../mtlheap.md).

## See Also

### Inspecting a residency set

- [label](label.md) — An optional name that can help you identify the residency set.
- [device](device.md) — The Metal device that owns the residency set.
- [allAllocations](allallocations.md) — The residency set’s current list of resource allocations.
- [allocationCount](allocationcount.md) — The number of resource allocations in the residency set.
- [allocatedSize](allocatedsize.md) — The amount of resident memory, in bytes, the residency set’s resource allocations consume.
