---
title: MTL4UpdateSparseBufferMappingOperation
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4updatesparsebuffermappingoperation
source_url: 'https://developer.apple.com/documentation/metal/mtl4updatesparsebuffermappingoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4updatesparsebuffermappingoperation.json'
content_hash: 'sha256:6d54b9b9954f4698'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4UpdateSparseBufferMappingOperation

<sub>Structure</sub>

Groups together arguments for an operation to update a sparse buffer mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTL4UpdateSparseBufferMappingOperation
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtl4updatesparsebuffermappingoperation/init().md>)
- [init(mode:bufferRange:heapOffset:)](<mtl4updatesparsebuffermappingoperation/init(mode_bufferrange_heapoffset_).md>)

### Instance Properties

- [bufferRange](mtl4updatesparsebuffermappingoperation/bufferrange.md) — The range in the buffer, in tiles.
- [heapOffset](mtl4updatesparsebuffermappingoperation/heapoffset.md) — The starting offset in the heap, in tiles.
- [mode](mtl4updatesparsebuffermappingoperation/mode.md) — The mode of the mapping operation to perform.

## See Also

### Sparse resources

- [MTLBufferSparseTier](mtlbuffersparsetier.md) — Enumerates the different support levels for sparse buffers.
- [MTL4CopySparseBufferMappingOperation](mtl4copysparsebuffermappingoperation.md) — Groups together arguments for an operation to copy a sparse buffer mapping.
- [MTLTextureSparseTier](mtltexturesparsetier.md) — Enumerates the different support levels for sparse textures.
- [MTL4CopySparseTextureMappingOperation](mtl4copysparsetexturemappingoperation.md) — Groups together arguments for an operation to copy a sparse texture mapping.
- [MTL4UpdateSparseTextureMappingOperation](mtl4updatesparsetexturemappingoperation.md) — Groups together arguments for an operation to update a sparse texture mapping.
