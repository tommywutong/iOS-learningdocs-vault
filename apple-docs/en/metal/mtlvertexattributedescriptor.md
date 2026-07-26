---
title: MTLVertexAttributeDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexattributedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexattributedescriptor.json'
content_hash: 'sha256:d1f8602555aad1e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLVertexAttributeDescriptor

<sub>Class</sub>

An object that determines how to store attribute data in memory and map it to the arguments of a vertex function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLVertexAttributeDescriptor
```

## Overview

A vertex attribute descriptor provides organization information so a vertex shader function can locate and load data into its arguments. The descriptor maps memory locations to attribute locations. It supports access to multiple attributes (such as vertex coordinates, surface normals, and texture coordinates) that are interleaved within the same buffer.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Organizing the vertex attribute

- [format](mtlvertexattributedescriptor/format.md) — The format of the vertex attribute.
- [offset](mtlvertexattributedescriptor/offset.md) — The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.
- [bufferIndex](mtlvertexattributedescriptor/bufferindex.md) — The index in the argument table for the associated vertex buffer.
- [MTLVertexFormat](mtlvertexformat.md) — The vertex data format options for render pipelines.

## See Also

### Render pass inputs

- [MTLVertexDescriptor](mtlvertexdescriptor.md) — An instance that describes how to organize and map data to a vertex function.
- [MTLVertexAttributeDescriptorArray](mtlvertexattributedescriptorarray.md) — An array of vertex attribute descriptor instances.
- [MTLVertexBufferLayoutDescriptor](mtlvertexbufferlayoutdescriptor.md) — An object that configures how a render pipeline fetches data to send to the vertex function.
- [MTLVertexBufferLayoutDescriptorArray](mtlvertexbufferlayoutdescriptorarray.md) — An array of vertex buffer layout descriptor instances.
- [MTLBufferLayoutStrideDynamic](mtlbufferlayoutstridedynamic.md)
