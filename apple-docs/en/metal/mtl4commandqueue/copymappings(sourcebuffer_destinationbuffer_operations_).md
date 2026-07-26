---
title: 'copyMappings(sourceBuffer:destinationBuffer:operations:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/copymappings(sourcebuffer:destinationbuffer:operations:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/copymappings(sourcebuffer:destinationbuffer:operations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/copymappings%28sourcebuffer%3Adestinationbuffer%3Aoperations%3A%29.json'
content_hash: 'sha256:04d8b23193132878'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# copyMappings(sourceBuffer:destinationBuffer:operations:)

<sub>Instance Method</sub>

Copies multiple offsets within a source placement sparse buffer to a destination placement sparse buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copyMappings(sourceBuffer: any MTLBuffer, destinationBuffer: any MTLBuffer, operations: [MTL4CopySparseBufferMappingOperation])
```

## Parameters

- `sourceBuffer` — The source placement sparse [MTLBuffer](../mtlbuffer.md).

- `destinationBuffer` — The destination placement sparse [MTLBuffer](../mtlbuffer.md).

- `operations` — An array of [MTL4CopySparseBufferMappingOperation](../mtl4copysparsebuffermappingoperation.md) instances to perform.

## Discussion

You are responsible for ensuring the source destination sparse buffers have the same `placementSparsePageSize` when you create them via [- newBufferWithLength:options:placementSparsePageSize:](<../mtldevice/makebuffer(length_options_placementsparsepagesize_).md>).

Additionally, you are responsible for ensuring both the source and destination sparse buffers don’t use the same aliased tiles at the same time.

> [!note] Note
> If a sparse texture and a sparse buffer share the same backing tiles, these don’t provide you with meaningful views of the other resource’s data.
