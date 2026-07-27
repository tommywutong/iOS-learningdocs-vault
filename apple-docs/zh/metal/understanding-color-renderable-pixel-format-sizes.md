---
title: 理解可渲染颜色的像素格式大小
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/understanding-color-renderable-pixel-format-sizes
source_url: 'https://developer.apple.com/documentation/metal/understanding-color-renderable-pixel-format-sizes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/understanding-color-renderable-pixel-format-sizes.json'
content_hash: 'sha256:2ec0ce5ea8de94ba'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Textures](textures.md)

# 理解可渲染颜色的像素格式大小

<sub>文章</sub>

根据颜色渲染目标的像素格式，了解 Apple GPU 中颜色渲染目标的大小限制。

## 概述

_颜色渲染目标_是一种纹理，作为渲染流程生成的颜色数据的输出目的地。可以为这些颜色渲染目标指定的像素格式，就是_可渲染颜色的像素格式_。

每种像素格式的存储大小取决于其各分量之和。例如，[MTLPixelFormatBGRA8Unorm](mtlpixelformat/bgra8unorm.md) 的存储大小为每像素 32 位（由四个 8 位分量组成）。[MTLPixelFormatBGR5A1Unorm](mtlpixelformat/bgr5a1unorm.md) 的存储大小为每像素 16 位（由三个 5 位分量和一个 1 位分量组成）。当你在单个渲染流程中使用多个渲染目标时，该渲染流程的组合存储大小等于这些渲染目标在该渲染流程中所使用像素格式的组合大小。

根据你为渲染目标指定的可渲染颜色的像素格式，Apple GPU 对颜色渲染目标存储大小的解读方式，在瓦片内存中与在系统内存中是不同的。由于瓦片内存的大小有限，单个渲染流程中所有颜色渲染目标的组合大小需要符合瓦片内存的大小限制。

> [!important] 重要
> 要查看每种 Apple GPU 的瓦片内存大小，请参阅 [Metal 特性集表格](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf)。

在非 Apple GPU 上，你可以在每个渲染流程使用最多八个颜色渲染目标，并可搭配任意可渲染颜色的像素格式。由于非 Apple GPU 没有瓦片内存，它们对颜色渲染目标没有组合大小限制。

## 另请参阅

### 纹理基础

- [优化纹理数据](optimizing-texture-data.md) — 优化纹理的数据，以提升 GPU 或 CPU 的访问速度。
- [MTLTexture](mtltexture.md) — 一种保存格式化图像数据的资源。
- [MTLTextureCompressionType](mtltexturecompressiontype.md)
- [MTLTextureDescriptor](mtltexturedescriptor.md) — 用于配置新 Metal 纹理实例的一个实例。
- [MTKTextureLoader](../metalkit/mtktextureloader.md) — 一种可从常见图像格式的现有数据创建纹理的对象。
- [MTLSharedTextureHandle](mtlsharedtexturehandle.md) — 一种可跨进程地址空间边界共享的纹理句柄。
- [MTLPixelFormat](mtlpixelformat.md) — 描述纹理中各个像素组织方式和特性的数据格式。
