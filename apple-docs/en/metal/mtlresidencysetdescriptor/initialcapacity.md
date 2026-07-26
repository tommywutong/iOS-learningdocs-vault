---
title: initialCapacity
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresidencysetdescriptor/initialcapacity
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencysetdescriptor/initialcapacity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencysetdescriptor/initialcapacity.json'
content_hash: 'sha256:1f1b41ebc719556a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySetDescriptor](../mtlresidencysetdescriptor.md)

# initialCapacity

<sub>Instance Property</sub>

The number of allocations a new residency set can store without reallocating memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var initialCapacity: Int { get set }
```

## Discussion

Reduce the memory reallocations the set needs to make by setting the property to a value large enough to hold the allocations you expect. You can leave the property at its default value of `0`, which tells Metal to give the residency set the standard starting capacity.

> [!note] Note
> The residency set can hold more allocations than its initial capacity.

## See Also

### Configuring the residency set

- [label](label.md) — An optional name that can help you identify a residency set you create with the descriptor.
