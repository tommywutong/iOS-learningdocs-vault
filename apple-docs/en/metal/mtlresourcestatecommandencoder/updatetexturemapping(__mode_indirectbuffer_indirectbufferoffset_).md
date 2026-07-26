---
title: 'updateTextureMapping(_:mode:indirectBuffer:indirectBufferOffset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlresourcestatecommandencoder/updatetexturemapping(_:mode:indirectbuffer:indirectbufferoffset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlresourcestatecommandencoder/updatetexturemapping(_:mode:indirectbuffer:indirectbufferoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourcestatecommandencoder/updatetexturemapping%28_%3Amode%3Aindirectbuffer%3Aindirectbufferoffset%3A%29.json'
content_hash: 'sha256:4ab61b8049793f99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceStateCommandEncoder](../mtlresourcestatecommandencoder.md)

# updateTextureMapping(_:mode:indirectBuffer:indirectBufferOffset:)

<sub>Instance Method</sub>

Encodes a command to update a texture’s memory mappings, specifying the parameters indirectly.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateTextureMapping(_ texture: any MTLTexture, mode: MTLSparseTextureMappingMode, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)
```

<sub>Mac Catalyst, macOS</sub>

```swift
optional func updateTextureMapping(_ texture: any MTLTexture, mode: MTLSparseTextureMappingMode, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)
```

## Parameters

- `texture` — The sparse texture to update.

- `mode` — A mode that indicates whether the method allocates or frees a memory tile in the texture.

- `indirectBuffer` — A buffer that contains an array of mapping arguments that are instances of the [MTLMapIndirectArguments](../mtlmapindirectarguments.md) structure.

- `indirectBufferOffset` — The offset, in bytes, where the first argument begins in the `indirectBuffer` parameter.

## Discussion

When the GPU executes the command that updates the texture’s memory mapping, the GPU gets details about the region to update from the `indirectBuffer` parameter.

To allocate tiles from the heap, pass [MTLSparseTextureMappingModeMap](../mtlsparsetexturemappingmode/map.md) as the `mode` parameter, and to free files back to the heap, pass [MTLSparseTextureMappingModeUnmap](../mtlsparsetexturemappingmode/unmap.md).

If you encode other commands that use the texture’s contents, such as rendering to the texture or sampling from a texture, synchronize the texture’s mapping updates with those commands to avoid race conditions. See [Resource synchronization](../resource-synchronization.md).

If you encode commands with multiple resource state passes, synchronize the resources to run the commands in the passes sequentially. See the [MTLResourceStateCommandEncoder](../mtlresourcestatecommandencoder.md) protocol.
