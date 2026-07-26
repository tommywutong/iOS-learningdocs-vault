---
title: 'sparseTileSize(with:pixelFormat:sampleCount:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/sparsetilesize(with:pixelformat:samplecount:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/sparsetilesize(with:pixelformat:samplecount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/sparsetilesize%28with%3Apixelformat%3Asamplecount%3A%29.json'
content_hash: 'sha256:3bdbd60cd7dc462b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# sparseTileSize(with:pixelFormat:sampleCount:)

<sub>Instance Method</sub>

Returns the dimensions of a sparse tile for a texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func sparseTileSize(with textureType: MTLTextureType, pixelFormat: MTLPixelFormat, sampleCount: Int) -> MTLSize
```

## Parameters

- `textureType` — An [MTLTextureType](../mtltexturetype.md) instance.

- `pixelFormat` — An [MTLPixelFormat](../mtlpixelformat.md) instance.

- `sampleCount` — The number of samples for each pixel.

## Return Value

A new [MTLSize](../mtlsize.md) instance.

## Discussion

The size of a sparse tile, in bytes, is the same for all sparse textures on a GPU device object. Because the size of pixels may vary, the actual dimensions of a sparse tile vary based on the texture and the pixel format. Use this method to get the dimensions of the tile for a particular format. Use these dimensions when converting regions from pixel-based units to sparse tile units and vice versa.

## See Also

### Working with sparse textures

- [- sparseTileSizeWithTextureType:pixelFormat:sampleCount:sparsePageSize:](<sparsetilesize(texturetype_pixelformat_samplecount_sparsepagesize_).md>) — Returns the dimensions of a sparse tile for a texture that has a specific sparse page size.
- [- sparseTileSizeInBytesForSparsePageSize:](<sparsetilesizeinbytes(sparsepagesize_).md>) — Returns the size, in bytes, of a sparse tile the GPU device creates with a specific page size.
- [sparseTileSizeInBytes](sparsetilesizeinbytes.md) — Returns the size, in bytes, of a sparse tile the GPU device creates using a default page size.
- [- convertSparsePixelRegions:toTileRegions:withTileSize:alignmentMode:numRegions:](<convertsparsepixelregions(__totileregions_withtilesize_alignmentmode_numregions_).md>) — Converts a list of sparse pixel regions to tile regions.
- [- convertSparseTileRegions:toPixelRegions:withTileSize:numRegions:](<convertsparsetileregions(__topixelregions_withtilesize_numregions_).md>) — Converts a list of sparse tile regions to pixel regions.
- [MTLSparsePageSize](../mtlsparsepagesize.md) — The page size options, in kilobytes, for sparse textures.
- [MTLSparseTextureRegionAlignmentMode](../mtlsparsetextureregionalignmentmode.md) — Options used when converting between a pixel-based region within a texture to a tile-based region.
