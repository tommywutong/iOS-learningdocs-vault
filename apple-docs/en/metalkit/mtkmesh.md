---
title: MTKMesh
framework: MetalKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metalkit/mtkmesh
source_url: 'https://developer.apple.com/documentation/metalkit/mtkmesh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtkmesh.json'
content_hash: 'sha256:5f5f17c3809e5fcc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetalKit](../metalkit.md)

# MTKMesh

<sub>Class</sub>

A container for the vertex data of a Model I/O mesh, suitable for use in a Metal app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTKMesh
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initialization

- [- initWithMesh:device:error:](<mtkmesh/init(mesh_device_).md>) — Initializes a MetalKit mesh and its submeshes from a Model I/O mesh.

### Loading Meshes from an Asset

- [newMeshes(asset:device:)](<mtkmesh/newmeshes(asset_device_).md>)

### Submeshes

- [submeshes](mtkmesh/submeshes.md) — An array of submeshes containing index buffers referencing the mesh vertices.

### Vertex Properties

- [vertexBuffers](mtkmesh/vertexbuffers.md) — An array of buffers in which mesh vertex data resides.
- [vertexCount](mtkmesh/vertexcount.md) — The number of vertices in the vertex buffers.
- [vertexDescriptor](mtkmesh/vertexdescriptor.md) — A Model I/O vertex descriptor specifying the data layout in the vertex buffers.

### Identifying Properties

- [name](mtkmesh/name.md) — The name of the mesh.

### Constants

- [Mesh Error Handling](mesh-error-handling.md) — Strings used when handling [NSError](../foundation/nserror.md) messages returned from a mesh initialization method.

## See Also

### Model Handling

- [MTKMeshBuffer](mtkmeshbuffer.md) — A buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [MTKMeshBufferAllocator](mtkmeshbufferallocator.md) — An interface for allocating a MetalKit buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [MTKSubmesh](mtksubmesh.md) — A container for the index data of a Model I/O submesh, suitable for use in a Metal app.
- [Conversion Functions](conversion-functions.md) — Convert between Metal and Model I/O vertex representations.
- [Model Errors](model-errors.md) — Learn about errors thrown by model handling methods.
