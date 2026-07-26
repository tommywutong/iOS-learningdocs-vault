---
title: MTLTextureSparseTier
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexturesparsetier
source_url: 'https://developer.apple.com/documentation/metal/mtltexturesparsetier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexturesparsetier.json'
content_hash: 'sha256:ee297268403a2db2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTextureSparseTier

<sub>Enumeration</sub>

Enumerates the different support levels for sparse textures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLTextureSparseTier
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MTLTextureSparseTier1](mtltexturesparsetier/tier1.md) — Indicates support for sparse textures tier 1.
- [MTLTextureSparseTier2](mtltexturesparsetier/tier2.md) — Indicates support for sparse textures tier 2.
- [MTLTextureSparseTierNone](mtltexturesparsetier/tiernone.md) — Indicates that the texture is not sparse.

### Initializers

- [init(rawValue:)](<mtltexturesparsetier/init(rawvalue_).md>)

## See Also

### Sparse resources

- [MTLBufferSparseTier](mtlbuffersparsetier.md) — Enumerates the different support levels for sparse buffers.
- [MTL4CopySparseBufferMappingOperation](mtl4copysparsebuffermappingoperation.md) — Groups together arguments for an operation to copy a sparse buffer mapping.
- [MTL4UpdateSparseBufferMappingOperation](mtl4updatesparsebuffermappingoperation.md) — Groups together arguments for an operation to update a sparse buffer mapping.
- [MTL4CopySparseTextureMappingOperation](mtl4copysparsetexturemappingoperation.md) — Groups together arguments for an operation to copy a sparse texture mapping.
- [MTL4UpdateSparseTextureMappingOperation](mtl4updatesparsetexturemappingoperation.md) — Groups together arguments for an operation to update a sparse texture mapping.
