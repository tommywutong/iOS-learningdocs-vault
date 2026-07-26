---
title: 'setVertexBufferOffset(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.3+, iPadOS 8.3+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setvertexbufferoffset(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexbufferoffset(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setvertexbufferoffset%28_%3Aindex%3A%29.json'
content_hash: 'sha256:5a7106563c98fbfb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setVertexBufferOffset(_:index:)

<sub>Instance Method</sub>

Updates an entry in the vertex shader argument table with a new location within the entry’s current buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVertexBufferOffset(_ offset: Int, index: Int)
```

## Parameters

- `offset` — An integer that represents the location, in bytes, from the start of `buffer` where the vertex shader argument data begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

- `index` — An integer that represents the entry in the vertex shader argument table for buffers that already stores a record of an [MTLBuffer](../mtlbuffer.md).

## Discussion

The command this method encodes changes the offset for a fragment buffer that already has a previous assignment from one of your earlier commands.

For more information, see:

- [- setVertexBuffer:offset:atIndex:](<setvertexbuffer(__offset_index_).md>)
- [setVertexBuffers(_:offsets:range:)](<setvertexbuffers(__offsets_range_).md>) (Swift)
- [setVertexBuffers:offsets:withRange:](setvertexbuffers_offsets_withrange_.md) (Objective-C)

The command can also adjust the offset for an entry that you previously set with the [- setVertexBytes:length:atIndex:](<setvertexbytes(__length_index_).md>) method.

> [!tip] Tip
> If you’re only updating an offset, this method is typically more efficient than rebinding a buffer or byte block with the methods above.

By default, the buffer at each index is `nil`.

## See Also

### Assigning buffers

- [- setVertexBuffer:offset:atIndex:](<setvertexbuffer(__offset_index_).md>) — Assigns a buffer to an entry in the vertex shader argument table.
- [- setVertexBuffer:offset:attributeStride:atIndex:](<setvertexbuffer(__offset_attributestride_index_).md>)
- [setVertexBuffers(_:offsets:range:)](<setvertexbuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the vertex shader argument table.
- [setVertexBuffers(_:offsets:attributeStrides:range:)](<setvertexbuffers(__offsets_attributestrides_range_).md>)
- [- setVertexBytes:length:atIndex:](<setvertexbytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the vertex shader argument table.
- [- setVertexBytes:length:attributeStride:atIndex:](<setvertexbytes(__length_attributestride_index_).md>)
- [- setVertexBufferOffset:attributeStride:atIndex:](<setvertexbufferoffset(offset_attributestride_index_).md>)
