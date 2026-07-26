---
title: MTLSparsePageSize
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsparsepagesize
source_url: 'https://developer.apple.com/documentation/metal/mtlsparsepagesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsparsepagesize.json'
content_hash: 'sha256:062eadca27c0487f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSparsePageSize

<sub>Enumeration</sub>

The page size options, in kilobytes, for sparse textures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLSparsePageSize
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Sparse texture page sizes

- [MTLSparsePageSize16](mtlsparsepagesize/size16.md) — Represents a sparse texture’s page size of 16 kilobytes.
- [MTLSparsePageSize64](mtlsparsepagesize/size64.md) — Represents a sparse texture’s page size of 64 kilobytes.
- [MTLSparsePageSize256](mtlsparsepagesize/size256.md) — Represents a sparse texture’s page size of 256 kilobytes.

### Initializers

- [init(rawValue:)](<mtlsparsepagesize/init(rawvalue_).md>)

## See Also

### Working with sparse textures

- [- sparseTileSizeWithTextureType:pixelFormat:sampleCount:sparsePageSize:](<mtldevice/sparsetilesize(texturetype_pixelformat_samplecount_sparsepagesize_).md>) — Returns the dimensions of a sparse tile for a texture that has a specific sparse page size.
- [- sparseTileSizeWithTextureType:pixelFormat:sampleCount:](<mtldevice/sparsetilesize(with_pixelformat_samplecount_).md>) — Returns the dimensions of a sparse tile for a texture.
- [- sparseTileSizeInBytesForSparsePageSize:](<mtldevice/sparsetilesizeinbytes(sparsepagesize_).md>) — Returns the size, in bytes, of a sparse tile the GPU device creates with a specific page size.
- [sparseTileSizeInBytes](mtldevice/sparsetilesizeinbytes.md) — Returns the size, in bytes, of a sparse tile the GPU device creates using a default page size.
- [- convertSparsePixelRegions:toTileRegions:withTileSize:alignmentMode:numRegions:](<mtldevice/convertsparsepixelregions(__totileregions_withtilesize_alignmentmode_numregions_).md>) — Converts a list of sparse pixel regions to tile regions.
- [- convertSparseTileRegions:toPixelRegions:withTileSize:numRegions:](<mtldevice/convertsparsetileregions(__topixelregions_withtilesize_numregions_).md>) — Converts a list of sparse tile regions to pixel regions.
- [MTLSparseTextureRegionAlignmentMode](mtlsparsetextureregionalignmentmode.md) — Options used when converting between a pixel-based region within a texture to a tile-based region.
