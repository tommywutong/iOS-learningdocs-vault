---
title: Mesh 与 object shader 资源准备命令
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
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Render passes](render-passes.md) · [MTLRenderCommandEncoder](mtlrendercommandencoder.md)

# Mesh 与 object shader 资源准备命令

<sub>API 集合</sub>

为 mesh shader 和 object shader 分配资源，包括缓冲区、纹理、加速结构、采样器状态和函数表。

## 概述

Mesh shader 会为每种资源类型（例如缓冲区、纹理和采样器状态）共享参数表。Object shader 拥有各自独立的参数表，与 mesh shader 及其他类型的 shader 有所区分。

## 主题

### 为 object shader 分配缓冲区

- [- setObjectBuffer:offset:atIndex:](<mtlrendercommandencoder/setobjectbuffer(__offset_index_).md>) — 将一个缓冲区分配给 object shader 参数表中的一个条目。
- [setObjectBuffers(_:offsets:range:)](<mtlrendercommandencoder/setobjectbuffers(__offsets_range_).md>) — 将多个缓冲区分配给 object shader 参数表中的一段条目范围。
- [- setObjectBytes:length:atIndex:](<mtlrendercommandencoder/setobjectbytes(__length_index_).md>) — 从字节创建一个缓冲区，并将其分配给 object shader 参数表中的一个条目。
- [- setObjectBufferOffset:atIndex:](<mtlrendercommandencoder/setobjectbufferoffset(__index_).md>) — 用该条目当前缓冲区内的一个新位置，更新 object shader 参数表中的一个条目。

### 为 object shader 分配纹理

- [- setObjectTexture:atIndex:](<mtlrendercommandencoder/setobjecttexture(__index_).md>) — 将一个纹理分配给 object shader 参数表中的一个条目。
- [setObjectTextures(_:range:)](<mtlrendercommandencoder/setobjecttextures(__range_).md>) — 将多个纹理分配给 object shader 参数表中的一段条目范围。

### 为 object shader 分配采样器状态

- [- setObjectSamplerState:atIndex:](<mtlrendercommandencoder/setobjectsamplerstate(__index_).md>) — 将一个采样器状态分配给 object shader 参数表中的一个条目。
- [- setObjectSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<mtlrendercommandencoder/setobjectsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — 将一个采样器状态及钳位值分配给 object shader 参数表中的一个条目。
- [setObjectSamplerStates(_:range:)](<mtlrendercommandencoder/setobjectsamplerstates(__range_).md>) — 将多个采样器状态分配给 object shader 参数表中的一段条目范围。
- [setObjectSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<mtlrendercommandencoder/setobjectsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — 将多个采样器状态及钳位值分配给 object shader 参数表中的一段条目范围。

### 为 mesh shader 分配缓冲区

- [- setMeshBuffer:offset:atIndex:](<mtlrendercommandencoder/setmeshbuffer(__offset_index_).md>) — 将一个缓冲区分配给 mesh shader 参数表中的一个条目。
- [setMeshBuffers(_:offsets:range:)](<mtlrendercommandencoder/setmeshbuffers(__offsets_range_).md>) — 将多个缓冲区分配给 mesh shader 参数表中的一段条目范围。
- [- setMeshBytes:length:atIndex:](<mtlrendercommandencoder/setmeshbytes(__length_index_).md>) — 从字节创建一个缓冲区，并将其分配给 mesh shader 参数表中的一个条目。
- [- setMeshBufferOffset:atIndex:](<mtlrendercommandencoder/setmeshbufferoffset(__index_).md>) — 用该条目当前缓冲区内的一个新位置，更新 mesh shader 参数表中的一个条目。

### 为 mesh shader 分配纹理

- [- setMeshTexture:atIndex:](<mtlrendercommandencoder/setmeshtexture(__index_).md>) — 将一个纹理分配给 mesh shader 参数表中的一个条目。
- [setMeshTextures(_:range:)](<mtlrendercommandencoder/setmeshtextures(__range_).md>) — 将多个纹理分配给 mesh shader 参数表中的一段条目范围。

### 为 mesh shader 分配采样器状态

- [- setMeshSamplerState:atIndex:](<mtlrendercommandencoder/setmeshsamplerstate(__index_).md>) — 将一个采样器状态分配给 mesh shader 参数表中的一个条目。
- [- setMeshSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<mtlrendercommandencoder/setmeshsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — 将一个采样器状态及钳位值分配给 mesh shader 参数表中的一个条目。
- [setMeshSamplerStates(_:range:)](<mtlrendercommandencoder/setmeshsamplerstates(__range_).md>) — 将多个采样器状态分配给 mesh shader 参数表中的一段条目范围。
- [setMeshSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<mtlrendercommandencoder/setmeshsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — 将多个采样器状态及钳位值分配给 mesh shader 参数表中的一段条目范围。

## 另请参阅

### 资源准备命令

- [Vertex shader resource preparation commands](vertex-shader-resource-preparation-commands.md) — 为 vertex shader 分配资源，包括缓冲区、纹理、加速结构、采样器状态和函数表。
- [Fragment shader resource preparation commands](fragment-shader-resource-preparation-commands.md) — 为 fragment shader 分配资源，包括缓冲区、纹理、加速结构、采样器状态和函数表。
- [Tile shaders resource preparation commands](tile-shaders-resource-preparation-commands.md) — 为 tile shader 分配资源，包括缓冲区、纹理、加速结构、采样器状态和函数表。
- [Argument buffer resource preparation commands](argument-buffer-resource-preparation-commands.md) — 将堆中的单个资源和多个资源加载到 GPU 内存中，使其可以通过参数缓冲区供 shader 使用。
