---
title: Mesh and object shader resource preparation commands
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mesh-and-object-shader-resource-preparation-commands
source_url: 'https://developer.apple.com/documentation/metal/mesh-and-object-shader-resource-preparation-commands'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mesh-and-object-shader-resource-preparation-commands.json'
content_hash: 'sha256:ba3142e0203cb8e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Render passes](render-passes.md) · [MTLRenderCommandEncoder](mtlrendercommandencoder.md)

# Mesh and object shader resource preparation commands

<sub>API Collection</sub>

Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.

## Overview

Mesh shaders share argument tables for each resource type, such as buffers, textures, and sampler states. Object shaders share their own separate argument tables, distinct from mesh shaders and other shader types.

## Topics

### Assigning buffers for object shaders

- [- setObjectBuffer:offset:atIndex:](<mtlrendercommandencoder/setobjectbuffer(__offset_index_).md>) — Assigns a buffer to an entry in the object shader argument table.
- [setObjectBuffers(_:offsets:range:)](<mtlrendercommandencoder/setobjectbuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the object shader argument table.
- [- setObjectBytes:length:atIndex:](<mtlrendercommandencoder/setobjectbytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the object shader argument table.
- [- setObjectBufferOffset:atIndex:](<mtlrendercommandencoder/setobjectbufferoffset(__index_).md>) — Updates an entry in the object shader argument table with a new location within the entry’s current buffer.

### Assigning textures for object shaders

- [- setObjectTexture:atIndex:](<mtlrendercommandencoder/setobjecttexture(__index_).md>) — Assigns a texture to an entry in the object shader argument table.
- [setObjectTextures(_:range:)](<mtlrendercommandencoder/setobjecttextures(__range_).md>) — Assigns multiple textures to a range of entries in the object shader argument table.

### Assigning sampler states for object shaders

- [- setObjectSamplerState:atIndex:](<mtlrendercommandencoder/setobjectsamplerstate(__index_).md>) — Assigns a sampler state to an entry in the object shader argument table.
- [- setObjectSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<mtlrendercommandencoder/setobjectsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the object shader argument table.
- [setObjectSamplerStates(_:range:)](<mtlrendercommandencoder/setobjectsamplerstates(__range_).md>) — Assigns multiple sampler states to a range of entries in the object shader argument table.
- [setObjectSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<mtlrendercommandencoder/setobjectsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Assigns multiple sampler states and clamp values to a range of entries in the object shader argument table.

### Assigning buffers for mesh shaders

- [- setMeshBuffer:offset:atIndex:](<mtlrendercommandencoder/setmeshbuffer(__offset_index_).md>) — Assigns a buffer to an entry in the mesh shader argument table.
- [setMeshBuffers(_:offsets:range:)](<mtlrendercommandencoder/setmeshbuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the mesh shader argument table.
- [- setMeshBytes:length:atIndex:](<mtlrendercommandencoder/setmeshbytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the mesh shader argument table.
- [- setMeshBufferOffset:atIndex:](<mtlrendercommandencoder/setmeshbufferoffset(__index_).md>) — Updates an entry in the mesh shader argument table with a new location within the entry’s current buffer.

### Assigning textures for mesh shaders

- [- setMeshTexture:atIndex:](<mtlrendercommandencoder/setmeshtexture(__index_).md>) — Assigns a texture to an entry in the mesh shader argument table.
- [setMeshTextures(_:range:)](<mtlrendercommandencoder/setmeshtextures(__range_).md>) — Assigns multiple textures to a range of entries in the mesh shader argument table.

### Assigning sampler states for mesh shaders

- [- setMeshSamplerState:atIndex:](<mtlrendercommandencoder/setmeshsamplerstate(__index_).md>) — Assigns a sampler state to an entry in the mesh shader argument table.
- [- setMeshSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<mtlrendercommandencoder/setmeshsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the mesh shader argument table.
- [setMeshSamplerStates(_:range:)](<mtlrendercommandencoder/setmeshsamplerstates(__range_).md>) — Assigns multiple sampler states to a range of entries in the mesh shader argument table.
- [setMeshSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<mtlrendercommandencoder/setmeshsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Assigns multiple sampler states and clamp values to a range of entries in the mesh shader argument table.

## See Also

### Resource preparation commands

- [Vertex shader resource preparation commands](vertex-shader-resource-preparation-commands.md) — Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Fragment shader resource preparation commands](fragment-shader-resource-preparation-commands.md) — Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Tile shaders resource preparation commands](tile-shaders-resource-preparation-commands.md) — Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Argument buffer resource preparation commands](argument-buffer-resource-preparation-commands.md) — Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.
