---
title: 渲染通道配置
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/render-pass-configuration
source_url: 'https://developer.apple.com/documentation/metal/render-pass-configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/render-pass-configuration.json'
content_hash: 'sha256:4b3f0d8b81222c19'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md) · [渲染通道](render-passes.md) · [MTLRenderCommandEncoder](mtlrendercommandencoder.md)

# 渲染通道配置

<sub>API 集合</sub>

设置渲染通道的管线状态、附加项动作、视口等，这些设置会影响后续的绘制命令。

## 概述

这些方法会编码出一些命令，用于配置渲染通道，使其作用于后续所有绘制命令。其中最重要的配置是管线状态（参见 [MTLRenderPipelineState](mtlrenderpipelinestate.md)），你可以通过调用 [- setRenderPipelineState:](<mtlrendercommandencoder/setrenderpipelinestate(__).md>) 方法来配置它。

## 主题

### 配置管线状态

- [- setRenderPipelineState:](<mtlrendercommandencoder/setrenderpipelinestate(__).md>) — 使用一个渲染管线或图块管线状态来配置编码器，该状态将应用于后续的绘制命令。

### 配置附加项的动作

- [- setColorStoreAction:atIndex:](<mtlrendercommandencoder/setcolorstoreaction(__index_).md>) — 配置某个颜色附加项的存储动作。
- [- setColorStoreActionOptions:atIndex:](<mtlrendercommandencoder/setcolorstoreactionoptions(__index_).md>) — 配置某个颜色附加项的存储动作选项。_(已废弃)_
- [- setDepthStoreAction:](<mtlrendercommandencoder/setdepthstoreaction(__).md>) — 配置深度附加项的存储动作。
- [- setDepthStoreActionOptions:](<mtlrendercommandencoder/setdepthstoreactionoptions(__).md>) — 配置深度附加项的存储动作选项。_(已废弃)_
- [- setStencilStoreAction:](<mtlrendercommandencoder/setstencilstoreaction(__).md>) — 配置模板附加项的存储动作。
- [- setStencilStoreActionOptions:](<mtlrendercommandencoder/setstencilstoreactionoptions(__).md>) — 配置模板附加项的存储动作选项。_(已废弃)_

### 配置混合行为

- [- setBlendColorRed:green:blue:alpha:](<mtlrendercommandencoder/setblendcolor(red_green_blue_alpha_).md>) — 配置渲染管线常量混合颜色的每个像素分量值（包括 alpha 值）。
- [- setColorAttachmentMap:](<mtlrendercommandencoder/setcolorattachmentmap(__).md>) — 设置从逻辑着色器颜色输出到物理渲染通道颜色附加项的映射。

### 配置渲染行为

- [- setTriangleFillMode:](<mtlrendercommandencoder/settrianglefillmode(__).md>) — 配置后续绘制命令如何光栅化（rasterize）三角形和三角形带图元。
- [- setFrontFacingWinding:](<mtlrendercommandencoder/setfrontfacing(__).md>) — 配置图元（例如三角形）的哪个面是正面。
- [- setCullMode:](<mtlrendercommandencoder/setcullmode(__).md>) — 配置渲染管线如何确定要移除哪些图元。

### 配置深度和模板行为

- [- setDepthStencilState:](<mtlrendercommandencoder/setdepthstencilstate(__).md>) — 配置组合的深度和模板状态。
- [- setDepthBias:slopeScale:clamp:](<mtlrendercommandencoder/setdepthbias(__slopescale_clamp_).md>) — 配置渲染通道对片段函数产生的深度值进行的调整，包括缩放因子和偏移量。
- [- setDepthClipMode:](<mtlrendercommandencoder/setdepthclipmode(__).md>) — 配置渲染管线如何处理位于视图平截头体（view frustum）近平面和远平面之外的片段。
- [setDepthTestBounds(_:)](<mtlrendercommandencoder/setdepthtestbounds(__).md>) — 配置深度边界测试的范围。
- [- setStencilReferenceValue:](<mtlrendercommandencoder/setstencilreferencevalue(__).md>) — 为正面和背面图元配置相同的比较值。
- [- setStencilFrontReferenceValue:backReferenceValue:](<mtlrendercommandencoder/setstencilreferencevalues(front_back_).md>) — 为正面和背面图元配置不同的比较值。

### 配置视口和裁剪行为

- [- setViewport:](<mtlrendercommandencoder/setviewport(__).md>) — 为渲染管线配置一个视口，该视口应用变换和裁剪矩形。
- [setViewports(_:)](<mtlrendercommandencoder/setviewports(__).md>) — 为渲染管线配置多个视口，这些视口应用变换和裁剪矩形。
- [- setScissorRect:](<mtlrendercommandencoder/setscissorrect(__).md>) — 配置用于片段裁剪测试的矩形。
- [setScissorRects(_:)](<mtlrendercommandencoder/setscissorrects(__).md>) — 配置用于片段裁剪测试的多个矩形。

### 配置可见性测试

- [- setVisibilityResultMode:offset:](<mtlrendercommandencoder/setvisibilityresultmode(__offset_).md>) — 配置 GPU 运行哪种可见性测试，以及其结果写入的目标位置。

### 配置顶点放大

- [- setVertexAmplificationCount:viewMappings:](<mtlrendercommandencoder/setvertexamplificationcount(__viewmappings_).md>) — 配置渲染管线为每个输入顶点生成的输出顶点数量，并可选择性地配置渲染目标和视口偏移。

### 配置曲面细分因子

- [- setTessellationFactorScale:](<mtlrendercommandencoder/settessellationfactorscale(__).md>) — 配置逐片（patch）曲面细分因子的缩放因子。
- [- setTessellationFactorBuffer:offset:instanceStride:](<mtlrendercommandencoder/settessellationfactorbuffer(__offset_instancestride_).md>) — 为后续任何片绘制命令配置逐片曲面细分因子。

### 配置持久线程组内存

- [- setObjectThreadgroupMemoryLength:atIndex:](<mtlrendercommandencoder/setobjectthreadgroupmemorylength(__index_).md>) — 为对象参数表中的某个条目配置线程组内存缓冲区的大小。
- [- setThreadgroupMemoryLength:offset:atIndex:](<mtlrendercommandencoder/setthreadgroupmemorylength(__offset_index_).md>) — 为片段或图块着色器参数表中的某个条目配置线程组内存缓冲区的大小。
