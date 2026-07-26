---
title: 'updateMappings(buffer:heap:operations:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/updatemappings(buffer:heap:operations:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/updatemappings(buffer:heap:operations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/updatemappings%28buffer%3Aheap%3Aoperations%3A%29.json'
content_hash: 'sha256:51e0f348ee93009e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# updateMappings(buffer:heap:operations:)

<sub>Instance Method</sub>

Updates multiple regions within a placement sparse buffer to alias specific tiles from a Metal heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func updateMappings(buffer: any MTLBuffer, heap: (any MTLHeap)?, operations: [MTL4UpdateSparseBufferMappingOperation])
```

## Parameters

- `buffer` — A placement sparse [MTLBuffer](../mtlbuffer.md).

- `heap` — An [MTLHeap](../mtlheap.md) you allocate with type [MTLHeapTypePlacement](../mtlheaptype/placement.md).

- `operations` — An array of [MTL4UpdateSparseBufferMappingOperation](../mtl4updatesparsebuffermappingoperation.md) instances to perform.

## Discussion

You can provide a `nil` parameter to the `heap` argument only when you perform unmap operations. Otherwise, you are responsible for ensuring parameter `heap` references an [MTLHeap](../mtlheap.md) that has a [maxCompatiblePlacementSparsePageSize](../mtlheapdescriptor/maxcompatibleplacementsparsepagesize.md) of at least the buffer’s `placementSparsePageSize` you assign when creating the sparse buffer via [- newBufferWithLength:options:placementSparsePageSize:](<../mtldevice/makebuffer(length_options_placementsparsepagesize_).md>).
