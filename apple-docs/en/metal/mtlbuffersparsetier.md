---
title: MTLBufferSparseTier
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbuffersparsetier
source_url: 'https://developer.apple.com/documentation/metal/mtlbuffersparsetier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbuffersparsetier.json'
content_hash: 'sha256:383f9c2bf7f1a7b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBufferSparseTier

<sub>Enumeration</sub>

Enumerates the different support levels for sparse buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLBufferSparseTier
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MTLBufferSparseTier1](mtlbuffersparsetier/tier1.md) — Indicates support for sparse buffers tier 1.
- [MTLBufferSparseTierNone](mtlbuffersparsetier/tiernone.md) — Indicates that the buffer is not sparse.

### Initializers

- [init(rawValue:)](<mtlbuffersparsetier/init(rawvalue_).md>)

## See Also

### Sparse resources

- [MTL4CopySparseBufferMappingOperation](mtl4copysparsebuffermappingoperation.md) — Groups together arguments for an operation to copy a sparse buffer mapping.
- [MTL4UpdateSparseBufferMappingOperation](mtl4updatesparsebuffermappingoperation.md) — Groups together arguments for an operation to update a sparse buffer mapping.
- [MTLTextureSparseTier](mtltexturesparsetier.md) — Enumerates the different support levels for sparse textures.
- [MTL4CopySparseTextureMappingOperation](mtl4copysparsetexturemappingoperation.md) — Groups together arguments for an operation to copy a sparse texture mapping.
- [MTL4UpdateSparseTextureMappingOperation](mtl4updatesparsetexturemappingoperation.md) — Groups together arguments for an operation to update a sparse texture mapping.
