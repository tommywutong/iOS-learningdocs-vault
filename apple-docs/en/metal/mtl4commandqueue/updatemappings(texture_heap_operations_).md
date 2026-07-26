---
title: 'updateMappings(texture:heap:operations:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/updatemappings(texture:heap:operations:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/updatemappings(texture:heap:operations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/updatemappings%28texture%3Aheap%3Aoperations%3A%29.json'
content_hash: 'sha256:06d0dd45b55878d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# updateMappings(texture:heap:operations:)

<sub>Instance Method</sub>

Updates multiple regions within a placement sparse texture to alias specific tiles of a Metal heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func updateMappings(texture: any MTLTexture, heap: (any MTLHeap)?, operations: [MTL4UpdateSparseTextureMappingOperation])
```

## Parameters

- `texture` — A placement sparse [MTLTexture](../mtltexture.md).

- `heap` — [MTLHeap](../mtlheap.md) you allocate with type [MTLHeapTypePlacement](../mtlheaptype/placement.md).

- `operations` — An array of [MTL4UpdateSparseTextureMappingOperation](../mtl4updatesparsetexturemappingoperation.md) instances to perform.

## Discussion

You can provide a `nil` parameter to the `heap` argument only if when you perform unmap operations. Otherwise, you are responsible for ensuring the heap is non-nil and has a [maxCompatiblePlacementSparsePageSize](../mtlheapdescriptor/maxcompatibleplacementsparsepagesize.md) of at least the texture’s [placementSparsePageSize](../mtltexturedescriptor/placementsparsepagesize.md).

When performing a sparse mapping update, you are responsible for issuing a barrier against stage `MTLStageResourceState`.

You can determine the sparse texture tier by calling `MTLTexture/sparseTextureTier`.
