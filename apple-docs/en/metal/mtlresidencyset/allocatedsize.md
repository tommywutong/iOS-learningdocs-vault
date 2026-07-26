---
title: allocatedSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresidencyset/allocatedsize
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset/allocatedsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset/allocatedsize.json'
content_hash: 'sha256:d316a20b6929bf93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySet](../mtlresidencyset.md)

# allocatedSize

<sub>Instance Property</sub>

The amount of resident memory, in bytes, the residency set’s resource allocations consume.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var allocatedSize: UInt64 { get }
```

## Discussion

The residency set updates the property’s value when you call the [- commit](<commit().md>) method.

## See Also

### Inspecting a residency set

- [label](label.md) — An optional name that can help you identify the residency set.
- [device](device.md) — The Metal device that owns the residency set.
- [- containsAllocation:](<containsallocation(__).md>) — Returns a Boolean value that indicates whether the residency set contains a specific resource allocation.
- [allAllocations](allallocations.md) — The residency set’s current list of resource allocations.
- [allocationCount](allocationcount.md) — The number of resource allocations in the residency set.
