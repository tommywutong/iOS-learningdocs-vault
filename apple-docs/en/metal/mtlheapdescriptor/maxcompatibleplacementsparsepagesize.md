---
title: maxCompatiblePlacementSparsePageSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheapdescriptor/maxcompatibleplacementsparsepagesize
source_url: 'https://developer.apple.com/documentation/metal/mtlheapdescriptor/maxcompatibleplacementsparsepagesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheapdescriptor/maxcompatibleplacementsparsepagesize.json'
content_hash: 'sha256:6511eb36ef531083'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeapDescriptor](../mtlheapdescriptor.md)

# maxCompatiblePlacementSparsePageSize

<sub>Instance Property</sub>

Specifies the largest sparse page size that the Metal heap supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxCompatiblePlacementSparsePageSize: MTLSparsePageSize { get set }
```

## Discussion

This parameter only affects the heap if you set the [type](type.md) property of this descriptor to [MTLHeapTypePlacement](../mtlheaptype/placement.md).

The value you assign to this property determines the compatibility of the Metal heap with with placement sparse resources, because placement sparse resources require that their sparse page size be less than or equal to the placement sparse page of the Metal heap that this property controls.
