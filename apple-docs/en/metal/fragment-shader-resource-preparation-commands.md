---
title: Fragment shader resource preparation commands
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/fragment-shader-resource-preparation-commands
source_url: 'https://developer.apple.com/documentation/metal/fragment-shader-resource-preparation-commands'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/fragment-shader-resource-preparation-commands.json'
content_hash: 'sha256:16e8072c69b564af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Render passes](render-passes.md) · [MTLRenderCommandEncoder](mtlrendercommandencoder.md)

# Fragment shader resource preparation commands

<sub>API Collection</sub>

Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.

## Overview

Fragment shaders share argument tables for each resource type, such as buffers, textures, and sampler states. Each shader type has its own argument tables, separate from fragment shaders and other shader types.

## Topics

### Assigning buffers

- [- setFragmentBuffer:offset:atIndex:](<mtlrendercommandencoder/setfragmentbuffer(__offset_index_).md>) — Assigns a buffer to an entry in the fragment shader argument table.
- [setFragmentBuffers(_:offsets:range:)](<mtlrendercommandencoder/setfragmentbuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the fragment shader argument table.
- [- setFragmentBytes:length:atIndex:](<mtlrendercommandencoder/setfragmentbytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the fragment shader argument table.
- [- setFragmentBufferOffset:atIndex:](<mtlrendercommandencoder/setfragmentbufferoffset(__index_).md>) — Updates an entry in the fragment shader argument table with a new location within the entry’s current buffer.

### Assigning textures

- [- setFragmentTexture:atIndex:](<mtlrendercommandencoder/setfragmenttexture(__index_).md>) — Assigns a texture to an entry in the fragment shader argument table.
- [setFragmentTextures(_:range:)](<mtlrendercommandencoder/setfragmenttextures(__range_).md>) — Assigns multiple textures to a range of entries in the fragment shader argument table.

### Assigning sampler states

- [- setFragmentSamplerState:atIndex:](<mtlrendercommandencoder/setfragmentsamplerstate(__index_).md>) — Assigns a sampler state to an entry in the fragment shader argument table.
- [- setFragmentSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<mtlrendercommandencoder/setfragmentsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the fragment shader argument table.
- [setFragmentSamplerStates(_:range:)](<mtlrendercommandencoder/setfragmentsamplerstates(__range_).md>) — Assigns multiple sampler states to a range of entries in the fragment shader argument table.
- [setFragmentSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<mtlrendercommandencoder/setfragmentsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Assigns multiple sampler states and clamp values to a range of entries in the fragment shader argument table.

### Assigning acceleration structures

- [- setFragmentAccelerationStructure:atBufferIndex:](<mtlrendercommandencoder/setfragmentaccelerationstructure(__bufferindex_).md>) — Assigns an acceleration structure to an entry in the fragment shader argument table.

### Assigning visible function tables

- [- setFragmentVisibleFunctionTable:atBufferIndex:](<mtlrendercommandencoder/setfragmentvisiblefunctiontable(__bufferindex_).md>) — Assigns a visible function table to an entry in the fragment shader argument table.
- [setFragmentVisibleFunctionTables(_:bufferRange:)](<mtlrendercommandencoder/setfragmentvisiblefunctiontables(__bufferrange_).md>) — Assigns multiple visible function tables to a range of entries in the fragment shader argument table.

### Assigning intersection function tables

- [- setFragmentIntersectionFunctionTable:atBufferIndex:](<mtlrendercommandencoder/setfragmentintersectionfunctiontable(__bufferindex_).md>) — Assigns an intersection function table to an entry in the fragment shader argument table.
- [setFragmentIntersectionFunctionTables(_:bufferRange:)](<mtlrendercommandencoder/setfragmentintersectionfunctiontables(__bufferrange_).md>) — Assigns multiple intersection function tables to a range of entries in the fragment shader argument table.

## See Also

### Resource preparation commands

- [Mesh and object shader resource preparation commands](mesh-and-object-shader-resource-preparation-commands.md) — Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Vertex shader resource preparation commands](vertex-shader-resource-preparation-commands.md) — Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Tile shaders resource preparation commands](tile-shaders-resource-preparation-commands.md) — Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Argument buffer resource preparation commands](argument-buffer-resource-preparation-commands.md) — Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.
