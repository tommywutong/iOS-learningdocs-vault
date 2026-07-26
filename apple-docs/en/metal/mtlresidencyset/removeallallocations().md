---
title: removeAllAllocations()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresidencyset/removeallallocations()
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset/removeallallocations()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset/removeallallocations%28%29.json'
content_hash: 'sha256:2207eaef1031a6fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySet](../mtlresidencyset.md)

# removeAllAllocations()

<sub>Instance Method</sub>

Stages all the resources in the residency set to leave its list of allocations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeAllAllocations()
```

## Discussion

Finalize the removal of these resource allocations, and all others changes you stage, by calling a residency set’s [- commit](<commit().md>) method.

## See Also

### Removing allocations

- [- removeAllocation:](<removeallocation(__).md>) — Stages a single resource to leave the residency set’s list of allocations.
- [removeAllocations(_:)](<removeallocations(__).md>) — Stages multiple resources to leave the residency set’s list of allocations.
