---
title: MTL4CopySparseBufferMappingOperation
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4copysparsebuffermappingoperation
source_url: 'https://developer.apple.com/documentation/metal/mtl4copysparsebuffermappingoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4copysparsebuffermappingoperation.json'
content_hash: 'sha256:1ad963700f588ae7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4CopySparseBufferMappingOperation

<sub>Structure</sub>

Groups together arguments for an operation to copy a sparse buffer mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTL4CopySparseBufferMappingOperation
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtl4copysparsebuffermappingoperation/init().md>)
- [init(sourceRange:destinationOffset:)](<mtl4copysparsebuffermappingoperation/init(sourcerange_destinationoffset_).md>)

### Instance Properties

- [destinationOffset](mtl4copysparsebuffermappingoperation/destinationoffset.md) — The origin in the destination buffer, in tiles.
- [sourceRange](mtl4copysparsebuffermappingoperation/sourcerange.md) — The range in the source buffer, in tiles.

## See Also

### Sparse resources

- [MTLBufferSparseTier](mtlbuffersparsetier.md) — Enumerates the different support levels for sparse buffers.
- [MTL4UpdateSparseBufferMappingOperation](mtl4updatesparsebuffermappingoperation.md) — Groups together arguments for an operation to update a sparse buffer mapping.
- [MTLTextureSparseTier](mtltexturesparsetier.md) — Enumerates the different support levels for sparse textures.
- [MTL4CopySparseTextureMappingOperation](mtl4copysparsetexturemappingoperation.md) — Groups together arguments for an operation to copy a sparse texture mapping.
- [MTL4UpdateSparseTextureMappingOperation](mtl4updatesparsetexturemappingoperation.md) — Groups together arguments for an operation to update a sparse texture mapping.
