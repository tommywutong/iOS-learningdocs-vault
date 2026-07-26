---
title: 'convertSparsePixelRegions(_:toTileRegions:withTileSize:alignmentMode:numRegions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/convertsparsepixelregions(_:totileregions:withtilesize:alignmentmode:numregions:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/convertsparsepixelregions(_:totileregions:withtilesize:alignmentmode:numregions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/convertsparsepixelregions%28_%3Atotileregions%3Awithtilesize%3Aalignmentmode%3Anumregions%3A%29.json'
content_hash: 'sha256:0111c59219ca0170'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# convertSparsePixelRegions(_:toTileRegions:withTileSize:alignmentMode:numRegions:)

<sub>Instance Method</sub>

Converts a list of sparse pixel regions to tile regions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func convertSparsePixelRegions(_ pixelRegions: UnsafePointer<MTLRegion>, toTileRegions tileRegions: UnsafeMutablePointer<MTLRegion>, withTileSize tileSize: MTLSize, alignmentMode mode: MTLSparseTextureRegionAlignmentMode, numRegions: Int)
```

## Parameters

- `pixelRegions` — A pointer to a C array of pixel [MTLRegion](../mtlregion.md) instances.

- `tileRegions` — A pointer to a C array of tile [MTLRegion](../mtlregion.md) instances.

- `tileSize` — An [MTLSize](../mtlsize.md) instance that represents a sparse tile’s size, in pixels.

- `mode` — An [MTLSparseTextureRegionAlignmentMode](../mtlsparsetextureregionalignmentmode.md) instance.

- `numRegions` — The number of regions you want the method to convert.

## See Also

### Working with sparse textures

- [- sparseTileSizeWithTextureType:pixelFormat:sampleCount:sparsePageSize:](<sparsetilesize(texturetype_pixelformat_samplecount_sparsepagesize_).md>) — Returns the dimensions of a sparse tile for a texture that has a specific sparse page size.
- [- sparseTileSizeWithTextureType:pixelFormat:sampleCount:](<sparsetilesize(with_pixelformat_samplecount_).md>) — Returns the dimensions of a sparse tile for a texture.
- [- sparseTileSizeInBytesForSparsePageSize:](<sparsetilesizeinbytes(sparsepagesize_).md>) — Returns the size, in bytes, of a sparse tile the GPU device creates with a specific page size.
- [sparseTileSizeInBytes](sparsetilesizeinbytes.md) — Returns the size, in bytes, of a sparse tile the GPU device creates using a default page size.
- [- convertSparseTileRegions:toPixelRegions:withTileSize:numRegions:](<convertsparsetileregions(__topixelregions_withtilesize_numregions_).md>) — Converts a list of sparse tile regions to pixel regions.
- [MTLSparsePageSize](../mtlsparsepagesize.md) — The page size options, in kilobytes, for sparse textures.
- [MTLSparseTextureRegionAlignmentMode](../mtlsparsetextureregionalignmentmode.md) — Options used when converting between a pixel-based region within a texture to a tile-based region.
