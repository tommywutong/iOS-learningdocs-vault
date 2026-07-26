---
title: MTLSparseTextureMappingMode
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsparsetexturemappingmode
source_url: 'https://developer.apple.com/documentation/metal/mtlsparsetexturemappingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsparsetexturemappingmode.json'
content_hash: 'sha256:f908069d72fae18a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSparseTextureMappingMode

<sub>Enumeration</sub>

Options for sparse texture mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLSparseTextureMappingMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Specifying the mapping mode

- [MTLSparseTextureMappingModeMap](mtlsparsetexturemappingmode/map.md) — A request to map sparse tiles from the heap to a region in the texture.
- [MTLSparseTextureMappingModeUnmap](mtlsparsetexturemappingmode/unmap.md) — A request to remove any mappings for a region in the texture.

### Initializers

- [init(rawValue:)](<mtlsparsetexturemappingmode/init(rawvalue_).md>)

## See Also

### Updating texture memory assignments

- [- updateTextureMapping:mode:region:mipLevel:slice:](<mtlresourcestatecommandencoder/updatetexturemapping(__mode_region_miplevel_slice_).md>) — Encodes a command to update the texture mappings for a region in a single texture mipmap.
- [- updateTextureMappings:mode:regions:mipLevels:slices:numRegions:](<mtlresourcestatecommandencoder/updatetexturemappings(__mode_regions_miplevels_slices_numregions_).md>) — Encodes a command to update memory mappings for multiple regions inside a texture.
