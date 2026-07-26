---
title: 'setIndirectCommandBuffers(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setindirectcommandbuffers(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setindirectcommandbuffers(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setindirectcommandbuffers%28_%3Arange%3A%29.json'
content_hash: 'sha256:d91fb8da537e3ca7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setIndirectCommandBuffers(_:range:)

<sub>Instance Method</sub>

Encodes an array of indirect command buffers into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setIndirectCommandBuffers(_ buffers: [(any MTLIndirectCommandBuffer)?], range: Range<Int>)
```

## Parameters

- `buffers` — An array of indirect command buffers the method encodes.

- `range` — A range of indices within the argument buffer for each element in `buffers`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding indirect command buffers

- [- setIndirectCommandBuffer:atIndex:](<setindirectcommandbuffer(__index_).md>) — Encodes a reference to an indirect command buffer into the argument buffer.
