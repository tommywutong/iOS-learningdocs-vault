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
doc_path: /documentation/metal/mtlresidencysetdescriptor/label
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencysetdescriptor/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencysetdescriptor/label.json'
content_hash: 'sha256:642b0063a1a5b220'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySetDescriptor](../mtlresidencysetdescriptor.md)

# label

<sub>Instance Property</sub>

An optional name that can help you identify a residency set you create with the descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## Discussion

Metal applies the value of this property to the [label](../mtlresidencyset/label.md) property of an [MTLResidencySet](../mtlresidencyset.md) that you create by passing the descriptor to [- newResidencySetWithDescriptor:error:](<../mtldevice/makeresidencyset(descriptor_).md>).

## See Also

### Configuring the residency set

- [initialCapacity](initialcapacity.md) — The number of allocations a new residency set can store without reallocating memory.
