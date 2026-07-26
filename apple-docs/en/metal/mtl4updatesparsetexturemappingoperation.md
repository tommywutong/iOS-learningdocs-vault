---
title: MTL4UpdateSparseTextureMappingOperation
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4updatesparsetexturemappingoperation
source_url: 'https://developer.apple.com/documentation/metal/mtl4updatesparsetexturemappingoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4updatesparsetexturemappingoperation.json'
content_hash: 'sha256:a5343907f99b8339'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4UpdateSparseTextureMappingOperation

<sub>Structure</sub>

Groups together arguments for an operation to update a sparse texture mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTL4UpdateSparseTextureMappingOperation
```

## Overview

When performing a sparse mapping update, you are responsible for issuing a barrier against stage `MTLStageResourceState`.

You can determine the sparse texture tier by calling [sparseTextureTier](mtltexture/sparsetexturetier.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtl4updatesparsetexturemappingoperation/init().md>)
- [init(mode:textureRegion:textureLevel:textureSlice:heapOffset:)](<mtl4updatesparsetexturemappingoperation/init(mode_textureregion_texturelevel_textureslice_heapoffset_).md>)

### Instance Properties

- [heapOffset](mtl4updatesparsetexturemappingoperation/heapoffset.md) — The starting offset in the heap, in tiles.
- [mode](mtl4updatesparsetexturemappingoperation/mode.md) — The mode of the mapping operation to perform.
- [textureLevel](mtl4updatesparsetexturemappingoperation/texturelevel.md) — The index of the mipmap level in the texture to update.
- [textureRegion](mtl4updatesparsetexturemappingoperation/textureregion.md) — The region in the texture to update, in tiles.
- [textureSlice](mtl4updatesparsetexturemappingoperation/textureslice.md) — The index of the array slice in the texture to update.

## See Also

### Sparse resources

- [MTLBufferSparseTier](mtlbuffersparsetier.md) — Enumerates the different support levels for sparse buffers.
- [MTL4CopySparseBufferMappingOperation](mtl4copysparsebuffermappingoperation.md) — Groups together arguments for an operation to copy a sparse buffer mapping.
- [MTL4UpdateSparseBufferMappingOperation](mtl4updatesparsebuffermappingoperation.md) — Groups together arguments for an operation to update a sparse buffer mapping.
- [MTLTextureSparseTier](mtltexturesparsetier.md) — Enumerates the different support levels for sparse textures.
- [MTL4CopySparseTextureMappingOperation](mtl4copysparsetexturemappingoperation.md) — Groups together arguments for an operation to copy a sparse texture mapping.
