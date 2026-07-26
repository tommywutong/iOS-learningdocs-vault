---
title: 'sparseTileSize(textureType:pixelFormat:sampleCount:sparsePageSize:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/sparsetilesize(texturetype:pixelformat:samplecount:sparsepagesize:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/sparsetilesize(texturetype:pixelformat:samplecount:sparsepagesize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/sparsetilesize%28texturetype%3Apixelformat%3Asamplecount%3Asparsepagesize%3A%29.json'
content_hash: 'sha256:2b14960324abc95e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# sparseTileSize(textureType:pixelFormat:sampleCount:sparsePageSize:)

<sub>Instance Method</sub>

Returns the dimensions of a sparse tile for a texture that has a specific sparse page size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func sparseTileSize(textureType: MTLTextureType, pixelFormat: MTLPixelFormat, sampleCount: Int, sparsePageSize: MTLSparsePageSize) -> MTLSize
```

## Parameters

- `textureType` — An [MTLTextureType](../mtltexturetype.md) instance.

- `pixelFormat` — An [MTLPixelFormat](../mtlpixelformat.md) instance.

- `sampleCount` — The number of samples for each pixel.

- `sparsePageSize` — An [MTLSparsePageSize](../mtlsparsepagesize.md) instance.

## Return Value

A new [MTLSize](../mtlsize.md) instance.

## See Also

### Working with sparse textures

- [- sparseTileSizeWithTextureType:pixelFormat:sampleCount:](<sparsetilesize(with_pixelformat_samplecount_).md>) — Returns the dimensions of a sparse tile for a texture.
- [- sparseTileSizeInBytesForSparsePageSize:](<sparsetilesizeinbytes(sparsepagesize_).md>) — Returns the size, in bytes, of a sparse tile the GPU device creates with a specific page size.
- [sparseTileSizeInBytes](sparsetilesizeinbytes.md) — Returns the size, in bytes, of a sparse tile the GPU device creates using a default page size.
- [- convertSparsePixelRegions:toTileRegions:withTileSize:alignmentMode:numRegions:](<convertsparsepixelregions(__totileregions_withtilesize_alignmentmode_numregions_).md>) — Converts a list of sparse pixel regions to tile regions.
- [- convertSparseTileRegions:toPixelRegions:withTileSize:numRegions:](<convertsparsetileregions(__topixelregions_withtilesize_numregions_).md>) — Converts a list of sparse tile regions to pixel regions.
- [MTLSparsePageSize](../mtlsparsepagesize.md) — The page size options, in kilobytes, for sparse textures.
- [MTLSparseTextureRegionAlignmentMode](../mtlsparsetextureregionalignmentmode.md) — Options used when converting between a pixel-based region within a texture to a tile-based region.
