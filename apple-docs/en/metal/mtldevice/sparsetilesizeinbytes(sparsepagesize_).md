---
title: 'sparseTileSizeInBytes(sparsePageSize:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/sparsetilesizeinbytes(sparsepagesize:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/sparsetilesizeinbytes(sparsepagesize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/sparsetilesizeinbytes%28sparsepagesize%3A%29.json'
content_hash: 'sha256:9e071017f1c46a87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# sparseTileSizeInBytes(sparsePageSize:)

<sub>Instance Method</sub>

Returns the size, in bytes, of a sparse tile the GPU device creates with a specific page size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func sparseTileSizeInBytes(sparsePageSize: MTLSparsePageSize) -> Int
```

## Parameters

- `sparsePageSize` — An [MTLSparsePageSize](../mtlsparsepagesize.md) instance.

## See Also

### Working with sparse textures

- [- sparseTileSizeWithTextureType:pixelFormat:sampleCount:sparsePageSize:](<sparsetilesize(texturetype_pixelformat_samplecount_sparsepagesize_).md>) — Returns the dimensions of a sparse tile for a texture that has a specific sparse page size.
- [- sparseTileSizeWithTextureType:pixelFormat:sampleCount:](<sparsetilesize(with_pixelformat_samplecount_).md>) — Returns the dimensions of a sparse tile for a texture.
- [sparseTileSizeInBytes](sparsetilesizeinbytes.md) — Returns the size, in bytes, of a sparse tile the GPU device creates using a default page size.
- [- convertSparsePixelRegions:toTileRegions:withTileSize:alignmentMode:numRegions:](<convertsparsepixelregions(__totileregions_withtilesize_alignmentmode_numregions_).md>) — Converts a list of sparse pixel regions to tile regions.
- [- convertSparseTileRegions:toPixelRegions:withTileSize:numRegions:](<convertsparsetileregions(__topixelregions_withtilesize_numregions_).md>) — Converts a list of sparse tile regions to pixel regions.
- [MTLSparsePageSize](../mtlsparsepagesize.md) — The page size options, in kilobytes, for sparse textures.
- [MTLSparseTextureRegionAlignmentMode](../mtlsparsetextureregionalignmentmode.md) — Options used when converting between a pixel-based region within a texture to a tile-based region.
