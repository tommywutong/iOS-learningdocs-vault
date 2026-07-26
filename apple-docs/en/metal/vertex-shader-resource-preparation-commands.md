---
title: Vertex shader resource preparation commands
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/vertex-shader-resource-preparation-commands
source_url: 'https://developer.apple.com/documentation/metal/vertex-shader-resource-preparation-commands'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/vertex-shader-resource-preparation-commands.json'
content_hash: 'sha256:8c9992f31df3f7dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Render passes](render-passes.md) · [MTLRenderCommandEncoder](mtlrendercommandencoder.md)

# Vertex shader resource preparation commands

<sub>API Collection</sub>

Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.

## Overview

Vertex shaders share argument tables for each resource type, such as buffers, textures, and sampler states. Each shader type has its own argument tables, separate from vertex shaders and other shader types.

## Topics

### Assigning buffers

- [- setVertexBuffer:offset:atIndex:](<mtlrendercommandencoder/setvertexbuffer(__offset_index_).md>) — Assigns a buffer to an entry in the vertex shader argument table.
- [- setVertexBuffer:offset:attributeStride:atIndex:](<mtlrendercommandencoder/setvertexbuffer(__offset_attributestride_index_).md>)
- [setVertexBuffers(_:offsets:range:)](<mtlrendercommandencoder/setvertexbuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the vertex shader argument table.
- [setVertexBuffers(_:offsets:attributeStrides:range:)](<mtlrendercommandencoder/setvertexbuffers(__offsets_attributestrides_range_).md>)
- [- setVertexBytes:length:atIndex:](<mtlrendercommandencoder/setvertexbytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the vertex shader argument table.
- [- setVertexBytes:length:attributeStride:atIndex:](<mtlrendercommandencoder/setvertexbytes(__length_attributestride_index_).md>)
- [- setVertexBufferOffset:atIndex:](<mtlrendercommandencoder/setvertexbufferoffset(__index_).md>) — Updates an entry in the vertex shader argument table with a new location within the entry’s current buffer.
- [- setVertexBufferOffset:attributeStride:atIndex:](<mtlrendercommandencoder/setvertexbufferoffset(offset_attributestride_index_).md>)

### Assigning textures

- [- setVertexTexture:atIndex:](<mtlrendercommandencoder/setvertextexture(__index_).md>) — Assigns a texture to an entry in the vertex shader argument table.
- [setVertexTextures(_:range:)](<mtlrendercommandencoder/setvertextextures(__range_).md>) — Assigns multiple textures to a range of entries in the vertex shader argument table.

### Assigning sampler states

- [- setVertexSamplerState:atIndex:](<mtlrendercommandencoder/setvertexsamplerstate(__index_).md>) — Assigns a sampler state to an entry in the vertex shader argument table.
- [- setVertexSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<mtlrendercommandencoder/setvertexsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the vertex shader argument table.
- [setVertexSamplerStates(_:range:)](<mtlrendercommandencoder/setvertexsamplerstates(__range_).md>) — Assigns multiple sampler states to a range of entries in the vertex shader argument table.
- [setVertexSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<mtlrendercommandencoder/setvertexsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Assigns multiple sampler states and clamp values to a range of entries in the vertex shader argument table.

### Assigning acceleration structures

- [- setVertexAccelerationStructure:atBufferIndex:](<mtlrendercommandencoder/setvertexaccelerationstructure(__bufferindex_).md>) — Assigns an acceleration structure to an entry in the vertex shader argument table.

### Assigning visible function tables

- [- setVertexVisibleFunctionTable:atBufferIndex:](<mtlrendercommandencoder/setvertexvisiblefunctiontable(__bufferindex_).md>) — Assigns a visible function table to an entry in the vertex shader argument table.
- [setVertexVisibleFunctionTables(_:bufferRange:)](<mtlrendercommandencoder/setvertexvisiblefunctiontables(__bufferrange_).md>) — Assigns multiple visible function tables to a range of entries in the vertex shader argument table.

### Assigning intersection function tables

- [- setVertexIntersectionFunctionTable:atBufferIndex:](<mtlrendercommandencoder/setvertexintersectionfunctiontable(__bufferindex_).md>) — Assigns an intersection function table to an entry in the vertex shader argument table.
- [setVertexIntersectionFunctionTables(_:bufferRange:)](<mtlrendercommandencoder/setvertexintersectionfunctiontables(__bufferrange_).md>) — Assigns multiple intersection function tables to a range of entries in the vertex shader argument table.

## See Also

### Resource preparation commands

- [Mesh and object shader resource preparation commands](mesh-and-object-shader-resource-preparation-commands.md) — Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Fragment shader resource preparation commands](fragment-shader-resource-preparation-commands.md) — Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Tile shaders resource preparation commands](tile-shaders-resource-preparation-commands.md) — Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Argument buffer resource preparation commands](argument-buffer-resource-preparation-commands.md) — Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.
