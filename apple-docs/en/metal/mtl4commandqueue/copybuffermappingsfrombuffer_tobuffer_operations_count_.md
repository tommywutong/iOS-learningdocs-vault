---
title: 'copyBufferMappingsFromBuffer:toBuffer:operations:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/copybuffermappingsfrombuffer:tobuffer:operations:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/copybuffermappingsfrombuffer:tobuffer:operations:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/copybuffermappingsfrombuffer%3Atobuffer%3Aoperations%3Acount%3A.json'
content_hash: 'sha256:3872846651a175a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# copyBufferMappingsFromBuffer:toBuffer:operations:count:

<sub>Instance Method</sub>

Copies multiple offsets within a source placement sparse buffer to a destination placement sparse buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) copyBufferMappingsFromBuffer:(id<MTLBuffer>) sourceBuffer toBuffer:(id<MTLBuffer>) destinationBuffer operations:(const MTL4CopySparseBufferMappingOperation[]) operations count:(NSUInteger) count;
```

## Parameters

- `sourceBuffer` — The source placement sparse [MTLBuffer](../mtlbuffer.md).

- `destinationBuffer` — The destination placement sparse [MTLBuffer](../mtlbuffer.md).

- `operations` — An array of [MTL4CopySparseBufferMappingOperation](../mtl4copysparsebuffermappingoperation.md) instances to perform.

- `count` — Number of operations to perform.

## Discussion

You are responsible for ensuring the source destination sparse buffers have the same `placementSparsePageSize` when you create them via [- newBufferWithLength:options:placementSparsePageSize:](<../mtldevice/makebuffer(length_options_placementsparsepagesize_).md>).

Additionally, you are responsible for ensuring both the source and destination sparse buffers don’t use the same aliased tiles at the same time.

> [!note] Note
> If a sparse texture and a sparse buffer share the same backing tiles, these don’t provide you with meaningful views of the other resource’s data.
