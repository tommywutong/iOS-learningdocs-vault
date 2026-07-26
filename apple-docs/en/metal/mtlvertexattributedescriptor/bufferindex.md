---
title: bufferIndex
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexattributedescriptor/bufferindex
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor/bufferindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexattributedescriptor/bufferindex.json'
content_hash: 'sha256:2299f6a6258cc5fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexAttributeDescriptor](../mtlvertexattributedescriptor.md)

# bufferIndex

<sub>Instance Property</sub>

The index in the argument table for the associated vertex buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var bufferIndex: Int { get set }
```

## See Also

### Related Documentation

- [- setVertexBuffer:offset:atIndex:](<../mtlrendercommandencoder/setvertexbuffer(__offset_index_).md>) — Assigns a buffer to an entry in the vertex shader argument table.

### Organizing the vertex attribute

- [format](format.md) — The format of the vertex attribute.
- [offset](offset.md) — The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.
- [MTLVertexFormat](../mtlvertexformat.md) — The vertex data format options for render pipelines.
