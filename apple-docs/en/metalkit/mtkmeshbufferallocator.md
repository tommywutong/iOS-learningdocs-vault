---
title: MTKMeshBufferAllocator
framework: MetalKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metalkit/mtkmeshbufferallocator
source_url: 'https://developer.apple.com/documentation/metalkit/mtkmeshbufferallocator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtkmeshbufferallocator.json'
content_hash: 'sha256:3dcf7a0d37069e6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetalKit](../metalkit.md)

# MTKMeshBufferAllocator

<sub>Class</sub>

An interface for allocating a MetalKit buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTKMeshBufferAllocator
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MDLMeshBufferAllocator](../modelio/mdlmeshbufferallocator.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initialization

- [- initWithDevice:](<mtkmeshbufferallocator/init(device_).md>) — Initializes a new allocator object.

### Device

- [device](mtkmeshbufferallocator/device.md) — The device used to create Metal objects.

## See Also

### Model Handling

- [MTKMesh](mtkmesh.md) — A container for the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [MTKMeshBuffer](mtkmeshbuffer.md) — A buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [MTKSubmesh](mtksubmesh.md) — A container for the index data of a Model I/O submesh, suitable for use in a Metal app.
- [Conversion Functions](conversion-functions.md) — Convert between Metal and Model I/O vertex representations.
- [Model Errors](model-errors.md) — Learn about errors thrown by model handling methods.
