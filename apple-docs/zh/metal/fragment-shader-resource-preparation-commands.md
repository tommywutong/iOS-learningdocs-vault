---
title: 片段着色器资源准备命令
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
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Render passes](render-passes.md) · [MTLRenderCommandEncoder](mtlrendercommandencoder.md)

# 片段着色器资源准备命令

<sub>API 集合</sub>

将资源分配给片段着色器，包括缓冲区、纹理、加速结构、采样器状态和函数表。

## 概述

片段着色器为每种资源类型（例如缓冲区、纹理和采样器状态）共享各自的参数表。每种着色器类型都有自己的参数表，与片段着色器和其他着色器类型的参数表相互独立。

## 主题

### Assigning buffers

- [- setFragmentBuffer:offset:atIndex:](<mtlrendercommandencoder/setfragmentbuffer(__offset_index_).md>) — 将一个缓冲区分配给片段着色器参数表中的某个条目。
- [setFragmentBuffers(_:offsets:range:)](<mtlrendercommandencoder/setfragmentbuffers(__offsets_range_).md>) — 将多个缓冲区分配给片段着色器参数表中的一段条目范围。
- [- setFragmentBytes:length:atIndex:](<mtlrendercommandencoder/setfragmentbytes(__length_index_).md>) — 从字节数据创建一个缓冲区，并将其分配给片段着色器参数表中的某个条目。
- [- setFragmentBufferOffset:atIndex:](<mtlrendercommandencoder/setfragmentbufferoffset(__index_).md>) — 使用某个条目当前缓冲区内的新位置，更新片段着色器参数表中的该条目。

### Assigning textures

- [- setFragmentTexture:atIndex:](<mtlrendercommandencoder/setfragmenttexture(__index_).md>) — 将一张纹理分配给片段着色器参数表中的某个条目。
- [setFragmentTextures(_:range:)](<mtlrendercommandencoder/setfragmenttextures(__range_).md>) — 将多张纹理分配给片段着色器参数表中的一段条目范围。

### Assigning sampler states

- [- setFragmentSamplerState:atIndex:](<mtlrendercommandencoder/setfragmentsamplerstate(__index_).md>) — 将一个采样器状态分配给片段着色器参数表中的某个条目。
- [- setFragmentSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<mtlrendercommandencoder/setfragmentsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — 将一个采样器状态及其钳制值分配给片段着色器参数表中的某个条目。
- [setFragmentSamplerStates(_:range:)](<mtlrendercommandencoder/setfragmentsamplerstates(__range_).md>) — 将多个采样器状态分配给片段着色器参数表中的一段条目范围。
- [setFragmentSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<mtlrendercommandencoder/setfragmentsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — 将多个采样器状态及其钳制值分配给片段着色器参数表中的一段条目范围。

### Assigning acceleration structures

- [- setFragmentAccelerationStructure:atBufferIndex:](<mtlrendercommandencoder/setfragmentaccelerationstructure(__bufferindex_).md>) — 将一个加速结构分配给片段着色器参数表中的某个条目。

### Assigning visible function tables

- [- setFragmentVisibleFunctionTable:atBufferIndex:](<mtlrendercommandencoder/setfragmentvisiblefunctiontable(__bufferindex_).md>) — 将一个可见函数表分配给片段着色器参数表中的某个条目。
- [setFragmentVisibleFunctionTables(_:bufferRange:)](<mtlrendercommandencoder/setfragmentvisiblefunctiontables(__bufferrange_).md>) — 将多个可见函数表分配给片段着色器参数表中的一段条目范围。

### Assigning intersection function tables

- [- setFragmentIntersectionFunctionTable:atBufferIndex:](<mtlrendercommandencoder/setfragmentintersectionfunctiontable(__bufferindex_).md>) — 将一个相交函数表分配给片段着色器参数表中的某个条目。
- [setFragmentIntersectionFunctionTables(_:bufferRange:)](<mtlrendercommandencoder/setfragmentintersectionfunctiontables(__bufferrange_).md>) — 将多个相交函数表分配给片段着色器参数表中的一段条目范围。

## 另请参阅

### Resource preparation commands

- [网格与对象着色器资源准备命令](mesh-and-object-shader-resource-preparation-commands.md) — 将资源分配给网格与对象着色器，包括缓冲区、纹理、加速结构、采样器状态和函数表。
- [顶点着色器资源准备命令](vertex-shader-resource-preparation-commands.md) — 将资源分配给顶点着色器，包括缓冲区、纹理、加速结构、采样器状态和函数表。
- [图块着色器资源准备命令](tile-shaders-resource-preparation-commands.md) — 将资源分配给图块着色器，包括缓冲区、纹理、加速结构、采样器状态和函数表。
- [参数缓冲区资源准备命令](argument-buffer-resource-preparation-commands.md) — 将单个资源以及堆内的多个资源加载到 GPU 内存中，以便着色器可以通过参数缓冲区访问它们。
