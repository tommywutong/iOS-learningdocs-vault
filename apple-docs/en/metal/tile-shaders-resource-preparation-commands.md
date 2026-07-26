---
title: Tile shaders resource preparation commands
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/tile-shaders-resource-preparation-commands
source_url: 'https://developer.apple.com/documentation/metal/tile-shaders-resource-preparation-commands'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/tile-shaders-resource-preparation-commands.json'
content_hash: 'sha256:9e4943504550c1e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Render passes](render-passes.md) · [MTLRenderCommandEncoder](mtlrendercommandencoder.md)

# Tile shaders resource preparation commands

<sub>API Collection</sub>

Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.

## Overview

Tile shaders share argument tables for each resource type, such as buffers, textures, and sampler states. Each shader type has its own argument tables, separate from tile shaders and other shader types.

## Topics

### Assigning buffers

- [- setTileBuffer:offset:atIndex:](<mtlrendercommandencoder/settilebuffer(__offset_index_).md>) — Assigns a buffer to an entry in the tile shader argument table.
- [setTileBuffers(_:offsets:range:)](<mtlrendercommandencoder/settilebuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the tile shader argument table.
- [- setTileBytes:length:atIndex:](<mtlrendercommandencoder/settilebytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the tile shader argument table.
- [- setTileBufferOffset:atIndex:](<mtlrendercommandencoder/settilebufferoffset(__index_).md>) — Updates an entry in the tile shader argument table with a new location within the entry’s current buffer.

### Assigning textures

- [- setTileTexture:atIndex:](<mtlrendercommandencoder/settiletexture(__index_).md>) — Assigns a texture to an entry in the tile shader argument table.
- [setTileTextures(_:range:)](<mtlrendercommandencoder/settiletextures(__range_).md>) — Assigns multiple textures to a range of entries in the tile shader argument table.

### Assigning sampler states

- [- setTileSamplerState:atIndex:](<mtlrendercommandencoder/settilesamplerstate(__index_).md>) — Assigns a sampler state to an entry in the tile shader argument table.
- [- setTileSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<mtlrendercommandencoder/settilesamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the tile shader argument table.
- [setTileSamplerStates(_:range:)](<mtlrendercommandencoder/settilesamplerstates(__range_).md>) — Assigns multiple sampler states to a range of entries in the tile shader argument table.
- [setTileSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<mtlrendercommandencoder/settilesamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Assigns multiple sampler states and clamp values to a range of entries in the tile shader argument table.

### Assigning acceleration structures

- [- setTileAccelerationStructure:atBufferIndex:](<mtlrendercommandencoder/settileaccelerationstructure(__bufferindex_).md>) — Assigns an acceleration structure to an entry in the tile shader argument table.

### Assigning visible function tables

- [- setTileVisibleFunctionTable:atBufferIndex:](<mtlrendercommandencoder/settilevisiblefunctiontable(__bufferindex_).md>) — Assigns a visible function table to an entry in the tile shader argument table.
- [setTileVisibleFunctionTables(_:bufferRange:)](<mtlrendercommandencoder/settilevisiblefunctiontables(__bufferrange_).md>) — Assigns multiple visible function tables to a range of entries in the tile shader argument table.

### Assigning intersection function tables

- [- setTileIntersectionFunctionTable:atBufferIndex:](<mtlrendercommandencoder/settileintersectionfunctiontable(__bufferindex_).md>) — Assigns an intersection function table to an entry in the tile shader argument table.
- [setTileIntersectionFunctionTables(_:bufferRange:)](<mtlrendercommandencoder/settileintersectionfunctiontables(__bufferrange_).md>) — Assigns multiple intersection function tables to a range of entries in the tile shader argument table.

## See Also

### Resource preparation commands

- [Mesh and object shader resource preparation commands](mesh-and-object-shader-resource-preparation-commands.md) — Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Vertex shader resource preparation commands](vertex-shader-resource-preparation-commands.md) — Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Fragment shader resource preparation commands](fragment-shader-resource-preparation-commands.md) — Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Argument buffer resource preparation commands](argument-buffer-resource-preparation-commands.md) — Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.
