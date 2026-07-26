---
title: 'setIndirectCommandBuffer(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setindirectcommandbuffer(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setindirectcommandbuffer(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setindirectcommandbuffer%28_%3Aindex%3A%29.json'
content_hash: 'sha256:ed8b91a8b7bb1dba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setIndirectCommandBuffer(_:index:)

<sub>Instance Method</sub>

Encodes a reference to an indirect command buffer into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setIndirectCommandBuffer(_ indirectCommandBuffer: (any MTLIndirectCommandBuffer)?, index: Int)
```

## Parameters

- `indirectCommandBuffer` — An indirect command-buffer the method encodes.

- `index` — The index of an inline, constant-data argument within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of an [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instance.

## See Also

### Encoding indirect command buffers

- [setIndirectCommandBuffers(_:range:)](<setindirectcommandbuffers(__range_).md>) — Encodes an array of indirect command buffers into the argument buffer.
