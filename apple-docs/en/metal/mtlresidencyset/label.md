---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresidencyset/label
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset/label.json'
content_hash: 'sha256:f8a72ef9ad7550e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySet](../mtlresidencyset.md)

# label

<sub>Instance Property</sub>

An optional name that can help you identify the residency set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get }
```

## Discussion

The value of this property comes from the [label](../mtlresidencysetdescriptor/label.md) property of the [MTLResidencySetDescriptor](../mtlresidencysetdescriptor.md) instance you use to create the residency set with [- newResidencySetWithDescriptor:error:](<../mtldevice/makeresidencyset(descriptor_).md>).

## See Also

### Inspecting a residency set

- [device](device.md) — The Metal device that owns the residency set.
- [- containsAllocation:](<containsallocation(__).md>) — Returns a Boolean value that indicates whether the residency set contains a specific resource allocation.
- [allAllocations](allallocations.md) — The residency set’s current list of resource allocations.
- [allocationCount](allocationcount.md) — The number of resource allocations in the residency set.
- [allocatedSize](allocatedsize.md) — The amount of resident memory, in bytes, the residency set’s resource allocations consume.
