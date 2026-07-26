---
title: MTL4CopySparseTextureMappingOperation
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4copysparsetexturemappingoperation
source_url: 'https://developer.apple.com/documentation/metal/mtl4copysparsetexturemappingoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4copysparsetexturemappingoperation.json'
content_hash: 'sha256:2d6d1da603948d60'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4CopySparseTextureMappingOperation

<sub>Structure</sub>

Groups together arguments for an operation to copy a sparse texture mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTL4CopySparseTextureMappingOperation
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtl4copysparsetexturemappingoperation/init().md>)
- [init(sourceRegion:sourceLevel:sourceSlice:destinationOrigin:destinationLevel:destinationSlice:)](<mtl4copysparsetexturemappingoperation/init(sourceregion_sourcelevel_sourceslice_destinationorigin_destinationlevel_destinationslice_).md>)

### Instance Properties

- [destinationLevel](mtl4copysparsetexturemappingoperation/destinationlevel.md) — The index of the mipmap level in the destination texture.
- [destinationOrigin](mtl4copysparsetexturemappingoperation/destinationorigin.md) — The origin in the destination texture to copy into, in tiles.
- [destinationSlice](mtl4copysparsetexturemappingoperation/destinationslice.md) — The index of the array slice in the destination texture to copy into.
- [sourceLevel](mtl4copysparsetexturemappingoperation/sourcelevel.md) — The index of the mipmap level in the source texture.
- [sourceRegion](mtl4copysparsetexturemappingoperation/sourceregion.md) — The region in the source texture, in tiles.
- [sourceSlice](mtl4copysparsetexturemappingoperation/sourceslice.md) — The index of the array slice in the texture source of the copy operation.

## See Also

### Sparse resources

- [MTLBufferSparseTier](mtlbuffersparsetier.md) — Enumerates the different support levels for sparse buffers.
- [MTL4CopySparseBufferMappingOperation](mtl4copysparsebuffermappingoperation.md) — Groups together arguments for an operation to copy a sparse buffer mapping.
- [MTL4UpdateSparseBufferMappingOperation](mtl4updatesparsebuffermappingoperation.md) — Groups together arguments for an operation to update a sparse buffer mapping.
- [MTLTextureSparseTier](mtltexturesparsetier.md) — Enumerates the different support levels for sparse textures.
- [MTL4UpdateSparseTextureMappingOperation](mtl4updatesparsetexturemappingoperation.md) — Groups together arguments for an operation to update a sparse texture mapping.
