---
title: MTKSubmesh
framework: MetalKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metalkit/mtksubmesh
source_url: 'https://developer.apple.com/documentation/metalkit/mtksubmesh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtksubmesh.json'
content_hash: 'sha256:5089808d8b3b4f31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetalKit](../metalkit.md)

# MTKSubmesh

<sub>Class</sub>

A container for the index data of a Model I/O submesh, suitable for use in a Metal app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTKSubmesh
```

## Overview

The [MTKSubmesh](mtksubmesh.md) class provides a container for a segment of mesh data that can be rendered in a single draw call. A submesh can only be initialized as part of a [MTKMesh](mtkmesh.md) object. Each submesh contains an index buffer with which the parent’s mesh data can be rendered. Actual submesh vertex data resides in the submesh’s parent mesh. For more information on Model I/O submeshes, see [MDLSubmesh](../modelio/mdlsubmesh.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Parent Mesh

- [mesh](mtksubmesh/mesh.md) — The parent mesh containing the vertex data of this submesh.

### Properties used to Draw Indexed Primitives

- [indexBuffer](mtksubmesh/indexbuffer.md) — The index buffer used to render the submesh object.
- [indexCount](mtksubmesh/indexcount.md) — The number of indices in the index buffer.
- [indexType](mtksubmesh/indextype.md) — The type of index data in the index buffer.
- [primitiveType](mtksubmesh/primitivetype.md) — The primitive type with which to draw the submesh object.

### Identifying Properties

- [name](mtksubmesh/name.md) — The name of the submesh.

## See Also

### Model Handling

- [MTKMesh](mtkmesh.md) — A container for the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [MTKMeshBuffer](mtkmeshbuffer.md) — A buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [MTKMeshBufferAllocator](mtkmeshbufferallocator.md) — An interface for allocating a MetalKit buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [Conversion Functions](conversion-functions.md) — Convert between Metal and Model I/O vertex representations.
- [Model Errors](model-errors.md) — Learn about errors thrown by model handling methods.
