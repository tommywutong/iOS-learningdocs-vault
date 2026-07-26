---
title: placementSparsePageSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexturedescriptor/placementsparsepagesize
source_url: 'https://developer.apple.com/documentation/metal/mtltexturedescriptor/placementsparsepagesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexturedescriptor/placementsparsepagesize.json'
content_hash: 'sha256:e5aeec778f34b997'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureDescriptor](../mtltexturedescriptor.md)

# placementSparsePageSize

<sub>Instance Property</sub>

Determines the page size for a placement sparse texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var placementSparsePageSize: MTLSparsePageSize { get set }
```

## Discussion

Set this property to a non-zero value to create a _placement sparse texture_.

Placement sparse textures are instances of [MTLTexture](../mtltexture.md) that you assign memory to using a [MTLHeap](../mtlheap.md) instance of type [MTLHeapTypePlacement](../mtlheaptype/placement.md) and a [maxCompatiblePlacementSparsePageSize](../mtlheapdescriptor/maxcompatibleplacementsparsepagesize.md) at least as large as the [MTLSparsePageSize](../mtlsparsepagesize.md) value you assign to this property.

This value is 0 by default.
