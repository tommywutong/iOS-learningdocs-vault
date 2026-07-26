---
title: 'updateBufferMappings:heap:operations:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/updatebuffermappings:heap:operations:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/updatebuffermappings:heap:operations:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/updatebuffermappings%3Aheap%3Aoperations%3Acount%3A.json'
content_hash: 'sha256:3be9c69f969d9392'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# updateBufferMappings:heap:operations:count:

<sub>Instance Method</sub>

Updates multiple regions within a placement sparse buffer to alias specific tiles from a Metal heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) updateBufferMappings:(id<MTLBuffer>) buffer heap:(id<MTLHeap>) heap operations:(const MTL4UpdateSparseBufferMappingOperation[]) operations count:(NSUInteger) count;
```

## Parameters

- `buffer` — A placement sparse [MTLBuffer](../mtlbuffer.md).

- `heap` — An [MTLHeap](../mtlheap.md) you allocate with type [MTLHeapTypePlacement](../mtlheaptype/placement.md).

- `operations` — An array of [MTL4UpdateSparseBufferMappingOperation](../mtl4updatesparsebuffermappingoperation.md) instances to perform.

- `count` — Number of operations to perform.

## Discussion

You can provide a `nil` parameter to the `heap` argument only when you perform unmap operations. Otherwise, you are responsible for ensuring parameter `heap` references an [MTLHeap](../mtlheap.md) that has a [maxCompatiblePlacementSparsePageSize](../mtlheapdescriptor/maxcompatibleplacementsparsepagesize.md) of at least the buffer’s `placementSparsePageSize` you assign when creating the sparse buffer via [- newBufferWithLength:options:placementSparsePageSize:](<../mtldevice/makebuffer(length_options_placementsparsepagesize_).md>).
