---
title: 'updateTextureMappings:heap:operations:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/updatetexturemappings:heap:operations:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/updatetexturemappings:heap:operations:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/updatetexturemappings%3Aheap%3Aoperations%3Acount%3A.json'
content_hash: 'sha256:00fe53b892aca979'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# updateTextureMappings:heap:operations:count:

<sub>Instance Method</sub>

Updates multiple regions within a placement sparse texture to alias specific tiles of a Metal heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) updateTextureMappings:(id<MTLTexture>) texture heap:(id<MTLHeap>) heap operations:(const MTL4UpdateSparseTextureMappingOperation[]) operations count:(NSUInteger) count;
```

## Parameters

- `texture` — A placement sparse [MTLTexture](../mtltexture.md).

- `heap` — [MTLHeap](../mtlheap.md) you allocate with type [MTLHeapTypePlacement](../mtlheaptype/placement.md).

- `operations` — An array of [MTL4UpdateSparseTextureMappingOperation](../mtl4updatesparsetexturemappingoperation.md) instances to perform.

- `count` — Number of operations to perform.

## Discussion

You can provide a `nil` parameter to the `heap` argument only if when you perform unmap operations. Otherwise, you are responsible for ensuring the heap is non-nil and has a [maxCompatiblePlacementSparsePageSize](../mtlheapdescriptor/maxcompatibleplacementsparsepagesize.md) of at least the texture’s [placementSparsePageSize](../mtltexturedescriptor/placementsparsepagesize.md).

When performing a sparse mapping update, you are responsible for issuing a barrier against stage `MTLStageResourceState`.

You can determine the sparse texture tier by calling `MTLTexture/sparseTextureTier`.
