---
title: 'setIndirectCommandBuffers:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setindirectcommandbuffers:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setindirectcommandbuffers:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setindirectcommandbuffers%3Awithrange%3A.json'
content_hash: 'sha256:8b1262bafc1e04eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setIndirectCommandBuffers:withRange:

<sub>Instance Method</sub>

Encodes an array of indirect command buffers into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setIndirectCommandBuffers:(id<MTLIndirectCommandBuffer> const[]) buffers withRange:(NSRange) range;
```

## Parameters

- `buffers` — An array of indirect command buffers the method encodes.

- `range` — A range of indices within the argument buffer for each element in `buffers`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding indirect command buffers

- [- setIndirectCommandBuffer:atIndex:](<setindirectcommandbuffer(__index_).md>) — Encodes a reference to an indirect command buffer into the argument buffer.
