---
title: 'copy(sourceBuffer:sourceOffset:destinationBuffer:destinationOffset:size:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/copy(sourcebuffer:sourceoffset:destinationbuffer:destinationoffset:size:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcebuffer:sourceoffset:destinationbuffer:destinationoffset:size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/copy%28sourcebuffer%3Asourceoffset%3Adestinationbuffer%3Adestinationoffset%3Asize%3A%29.json'
content_hash: 'sha256:114d104197209a09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# copy(sourceBuffer:sourceOffset:destinationBuffer:destinationOffset:size:)

<sub>Instance Method</sub>

Encodes a command that copies data from a buffer instance into another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copy(sourceBuffer: any MTLBuffer, sourceOffset: Int, destinationBuffer: any MTLBuffer, destinationOffset: Int, size: Int)
```

## Parameters

- `sourceBuffer` — An [MTLBuffer](../mtlbuffer.md) instance the command copies data from.

- `sourceOffset` — A byte offset within `sourceBuffer` the command copies from.

- `destinationBuffer` — An [MTLBuffer](../mtlbuffer.md) instance the command copies data to.

- `destinationOffset` — A byte offset within `destinationBuffer` the command copies to.

- `size` — The number of bytes the command copies from `sourceBuffer` to `destinationBuffer`.
