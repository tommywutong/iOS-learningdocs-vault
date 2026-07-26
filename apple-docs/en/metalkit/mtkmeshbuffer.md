---
title: MTKMeshBuffer
framework: MetalKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metalkit/mtkmeshbuffer
source_url: 'https://developer.apple.com/documentation/metalkit/mtkmeshbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtkmeshbuffer.json'
content_hash: 'sha256:97c8d35daf83f0b8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetalKit](../metalkit.md)

# MTKMeshBuffer

<sub>Class</sub>

A buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTKMeshBuffer
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MDLMeshBuffer](../modelio/mdlmeshbuffer.md), [MDLNamed](../modelio/mdlnamed.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Originating Objects

- [allocator](mtkmeshbuffer/allocator.md) — The allocator object used to create this mesh buffer.
- [type](mtkmeshbuffer/type.md) — The type of data contained in the originating Model I/O buffer.

### Metal Buffer Properties

- [buffer](mtkmeshbuffer/buffer.md) — The Metal buffer backing all vertex and index data.
- [length](mtkmeshbuffer/length.md) — The logical size of the Metal buffer, in bytes.
- [offset](mtkmeshbuffer/offset.md) — The byte offset of the data within the Metal buffer.

### Instance Methods

- [zone()](<mtkmeshbuffer/zone().md>)

## See Also

### Model Handling

- [MTKMesh](mtkmesh.md) — A container for the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [MTKMeshBufferAllocator](mtkmeshbufferallocator.md) — An interface for allocating a MetalKit buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [MTKSubmesh](mtksubmesh.md) — A container for the index data of a Model I/O submesh, suitable for use in a Metal app.
- [Conversion Functions](conversion-functions.md) — Convert between Metal and Model I/O vertex representations.
- [Model Errors](model-errors.md) — Learn about errors thrown by model handling methods.
