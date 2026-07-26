---
title: 'updateTextureMapping(_:mode:region:mipLevel:slice:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlresourcestatecommandencoder/updatetexturemapping(_:mode:region:miplevel:slice:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlresourcestatecommandencoder/updatetexturemapping(_:mode:region:miplevel:slice:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourcestatecommandencoder/updatetexturemapping%28_%3Amode%3Aregion%3Amiplevel%3Aslice%3A%29.json'
content_hash: 'sha256:7f3149dceccd8e93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceStateCommandEncoder](../mtlresourcestatecommandencoder.md)

# updateTextureMapping(_:mode:region:mipLevel:slice:)

<sub>Instance Method</sub>

Encodes a command to update the texture mappings for a region in a single texture mipmap.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateTextureMapping(_ texture: any MTLTexture, mode: MTLSparseTextureMappingMode, region: MTLRegion, mipLevel: Int, slice: Int)
```

<sub>Mac Catalyst, macOS</sub>

```swift
optional func updateTextureMapping(_ texture: any MTLTexture, mode: MTLSparseTextureMappingMode, region: MTLRegion, mipLevel: Int, slice: Int)
```

## Parameters

- `texture` — The sparse texture to update.

- `mode` — A mode that indicates whether the method allocates or frees a memory tile in the texture.

- `region` — A region, in tile coordinates, that describes the part of the mipmap to update.

- `mipLevel` — The mipmap to update.

- `slice` — The slice in the texture to update.

## Discussion

When the GPU executes the command that updates the texture’s memory mapping, the GPU gets details about the region from the `region` parameter.

To allocate tiles from the heap, pass [MTLSparseTextureMappingModeMap](../mtlsparsetexturemappingmode/map.md) as the `mode` parameter, and to free files back to the heap, pass [MTLSparseTextureMappingModeUnmap](../mtlsparsetexturemappingmode/unmap.md).

If you encode other commands that use the texture’s contents, such as rendering to the texture or sampling from a texture, synchronize the texture’s mapping updates with those commands to avoid race conditions. See [Resource synchronization](../resource-synchronization.md).

If you encode commands with multiple resource state passes, synchronize the resources to run the commands in the passes sequentially. See the [MTLResourceStateCommandEncoder](../mtlresourcestatecommandencoder.md) protocol.

## See Also

### Updating texture memory assignments

- [- updateTextureMappings:mode:regions:mipLevels:slices:numRegions:](<updatetexturemappings(__mode_regions_miplevels_slices_numregions_).md>) — Encodes a command to update memory mappings for multiple regions inside a texture.
- [MTLSparseTextureMappingMode](../mtlsparsetexturemappingmode.md) — Options for sparse texture mapping.
