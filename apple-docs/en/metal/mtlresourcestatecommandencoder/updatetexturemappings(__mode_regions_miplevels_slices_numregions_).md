---
title: 'updateTextureMappings(_:mode:regions:mipLevels:slices:numRegions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlresourcestatecommandencoder/updatetexturemappings(_:mode:regions:miplevels:slices:numregions:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlresourcestatecommandencoder/updatetexturemappings(_:mode:regions:miplevels:slices:numregions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourcestatecommandencoder/updatetexturemappings%28_%3Amode%3Aregions%3Amiplevels%3Aslices%3Anumregions%3A%29.json'
content_hash: 'sha256:2a2606851fc60fbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceStateCommandEncoder](../mtlresourcestatecommandencoder.md)

# updateTextureMappings(_:mode:regions:mipLevels:slices:numRegions:)

<sub>Instance Method</sub>

Encodes a command to update memory mappings for multiple regions inside a texture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateTextureMappings(_ texture: any MTLTexture, mode: MTLSparseTextureMappingMode, regions: UnsafePointer<MTLRegion>, mipLevels: UnsafePointer<Int>, slices: UnsafePointer<Int>, numRegions: Int)
```

<sub>Mac Catalyst, macOS</sub>

```swift
optional func updateTextureMappings(_ texture: any MTLTexture, mode: MTLSparseTextureMappingMode, regions: UnsafePointer<MTLRegion>, mipLevels: UnsafePointer<Int>, slices: UnsafePointer<Int>, numRegions: Int)
```

## Parameters

- `texture` — The sparse texture to update.

- `mode` — The change to make to the texture mapping.

- `regions` — A pointer to an array of regions to change. You need to provide as many regions as you specify in the `numRegions` parameter.

- `mipLevels` — A pointer to an array of mipmap levels to change. You need to provide as many entries as you specify in the `numRegions` parameter.

- `slices` — A pointer to an array of slices to change. You need to provide as many entries as you specify in the `numRegions` parameter.

- `numRegions` — The number of regions to update.

## See Also

### Updating texture memory assignments

- [- updateTextureMapping:mode:region:mipLevel:slice:](<updatetexturemapping(__mode_region_miplevel_slice_).md>) — Encodes a command to update the texture mappings for a region in a single texture mipmap.
- [MTLSparseTextureMappingMode](../mtlsparsetexturemappingmode.md) — Options for sparse texture mapping.
