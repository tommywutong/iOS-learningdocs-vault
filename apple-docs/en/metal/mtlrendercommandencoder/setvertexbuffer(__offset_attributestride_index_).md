---
title: 'setVertexBuffer(_:offset:attributeStride:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setvertexbuffer(_:offset:attributestride:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexbuffer(_:offset:attributestride:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setvertexbuffer%28_%3Aoffset%3Aattributestride%3Aindex%3A%29.json'
content_hash: 'sha256:039620e38168c68b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setVertexBuffer(_:offset:attributeStride:index:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVertexBuffer(_ buffer: (any MTLBuffer)?, offset: Int, attributeStride stride: Int, index: Int)
```

## See Also

### Assigning buffers

- [- setVertexBuffer:offset:atIndex:](<setvertexbuffer(__offset_index_).md>) — Assigns a buffer to an entry in the vertex shader argument table.
- [setVertexBuffers(_:offsets:range:)](<setvertexbuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the vertex shader argument table.
- [setVertexBuffers(_:offsets:attributeStrides:range:)](<setvertexbuffers(__offsets_attributestrides_range_).md>)
- [- setVertexBytes:length:atIndex:](<setvertexbytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the vertex shader argument table.
- [- setVertexBytes:length:attributeStride:atIndex:](<setvertexbytes(__length_attributestride_index_).md>)
- [- setVertexBufferOffset:atIndex:](<setvertexbufferoffset(__index_).md>) — Updates an entry in the vertex shader argument table with a new location within the entry’s current buffer.
- [- setVertexBufferOffset:attributeStride:atIndex:](<setvertexbufferoffset(offset_attributestride_index_).md>)
