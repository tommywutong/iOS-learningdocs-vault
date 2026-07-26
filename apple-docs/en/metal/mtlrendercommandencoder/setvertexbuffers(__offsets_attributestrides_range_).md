---
title: 'setVertexBuffers(_:offsets:attributeStrides:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setvertexbuffers(_:offsets:attributestrides:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexbuffers(_:offsets:attributestrides:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setvertexbuffers%28_%3Aoffsets%3Aattributestrides%3Arange%3A%29.json'
content_hash: 'sha256:83e54156cb450539'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setVertexBuffers(_:offsets:attributeStrides:range:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVertexBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)
```

## See Also

### Assigning buffers

- [- setVertexBuffer:offset:atIndex:](<setvertexbuffer(__offset_index_).md>) — Assigns a buffer to an entry in the vertex shader argument table.
- [- setVertexBuffer:offset:attributeStride:atIndex:](<setvertexbuffer(__offset_attributestride_index_).md>)
- [setVertexBuffers(_:offsets:range:)](<setvertexbuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the vertex shader argument table.
- [- setVertexBytes:length:atIndex:](<setvertexbytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the vertex shader argument table.
- [- setVertexBytes:length:attributeStride:atIndex:](<setvertexbytes(__length_attributestride_index_).md>)
- [- setVertexBufferOffset:atIndex:](<setvertexbufferoffset(__index_).md>) — Updates an entry in the vertex shader argument table with a new location within the entry’s current buffer.
- [- setVertexBufferOffset:attributeStride:atIndex:](<setvertexbufferoffset(offset_attributestride_index_).md>)
