---
title: device
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresidencyset/device
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset/device.json'
content_hash: 'sha256:ae0dc7d3c2e93617'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySet](../mtlresidencyset.md)

# device

<sub>Instance Property</sub>

The Metal device that owns the residency set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

The device assigns itself to this property when you create a residency set with its [- newResidencySetWithDescriptor:error:](<../mtldevice/makeresidencyset(descriptor_).md>) method.

## See Also

### Inspecting a residency set

- [label](label.md) — An optional name that can help you identify the residency set.
- [- containsAllocation:](<containsallocation(__).md>) — Returns a Boolean value that indicates whether the residency set contains a specific resource allocation.
- [allAllocations](allallocations.md) — The residency set’s current list of resource allocations.
- [allocationCount](allocationcount.md) — The number of resource allocations in the residency set.
- [allocatedSize](allocatedsize.md) — The amount of resident memory, in bytes, the residency set’s resource allocations consume.
