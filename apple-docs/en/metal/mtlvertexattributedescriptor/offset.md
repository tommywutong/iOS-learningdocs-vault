---
title: offset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexattributedescriptor/offset
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor/offset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexattributedescriptor/offset.json'
content_hash: 'sha256:8f61b68015670b39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexAttributeDescriptor](../mtlvertexattributedescriptor.md)

# offset

<sub>Instance Property</sub>

The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var offset: Int { get set }
```

## Discussion

Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

### Organizing the vertex attribute

- [format](format.md) — The format of the vertex attribute.
- [bufferIndex](bufferindex.md) — The index in the argument table for the associated vertex buffer.
- [MTLVertexFormat](../mtlvertexformat.md) — The vertex data format options for render pipelines.
