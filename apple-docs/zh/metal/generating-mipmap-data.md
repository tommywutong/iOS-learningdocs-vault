---
title: 生成 mipmap 数据
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/generating-mipmap-data
source_url: 'https://developer.apple.com/documentation/metal/generating-mipmap-data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/generating-mipmap-data.json'
content_hash: 'sha256:8d61a373fcfde470'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Textures](textures.md)

# 生成 mipmap 数据

<sub>文章</sub>

在创作内容时或在运行时创建你的 mipmap。

## 概述

你可以通过对原始图像应用滤镜来创建用于纹理采样的 mipmap。不同的滤镜算法在处理时间和输出质量上各有差异。你需要综合考虑文件大小、质量和运行时性能，为你的内容确定合适的权衡方案。

创建 mipmap 有以下几种选择：

**让设备对象在运行时为你生成 mipmap。** 这是为彩色图像创建 mipmap 最简单的方法。在用数据初始化 mipmap `0` 之后，创建一个 blit 命令编码器，并编码一条命令，使用 [- generateMipmapsForTexture:](<mtlblitcommandencoder/generatemipmaps(for_).md>) 方法生成其余的 mipmap。

**Swift**

```swift
if let encoder = commandBuffer.makeBlitCommandEncoder() {
    encoder.generateMipmaps(for: texture)
    encoder.endEncoding()
}
```

**Objective-C**

```objective-c
id <MTLBlitCommandEncoder> encoder = [commandBuffer blitCommandEncoder];
[encoder generateMipmapsForTexture: myTexture];
[encoder endEncoding];
```

与其他 GPU 命令一样，GPU 会在命令缓冲区提交到命令队列之后的某个时刻，异步创建这些 mipmap。设备对象用于生成 mipmap 的过滤方式取决于具体实现，不同 GPU 之间可能有所不同。

**从你的源纹理生成高质量的 mipmap。** 许多工具都能够从你的源纹理生成高质量的 mipmap。在这种情况下，你需要将所有 mipmap 存储在你的源数据中，并在运行时加载它们。这种方式让你能够使用更高质量的滤镜和工具来构建你的 mipmap，但会增加文件大小，从而增加你的 App 的分发体积。

**使用自定滤镜或 Metal Performance Shaders 生成更好的 mipmap。** 你也可以创建自己的工具，使用自定滤镜或 Metal Performance Shaders 来生成更好的 mipmap。具体取决于你为自己的工具所采用的解决方案，你可能会在运行时创建 mipmap 数据，也可能将其作为在创作内容时运行的离线流程来处理。

## 另请参阅

### Texture mipmapping

- [使用 mipmap 提升纹理采样质量和性能](improving-texture-sampling-quality-and-performance-with-mipmaps.md) — 通过创建纹理的较小版本，避免纹理渲染瑕疵并减轻 GPU 的工作负载。
- [创建带 mipmap 的纹理](creating-a-mipmapped-texture.md) — 决定你正在创建的纹理是否需要 mipmap。
- [向 mipmap 内外复制数据](copying-data-into-or-out-of-mipmaps.md) — 指定数据传输影响哪些 mipmap。
- [为采样器添加 mipmap 过滤](adding-mipmap-filtering-to-samplers.md) — 指定 GPU 如何对你纹理中的 mipmap 进行采样。
- [限制对特定 mipmap 的访问](restricting-access-to-specific-mipmaps.md) — 设置某个采样器可以访问的 mipmap 级别范围。
- [通过细节层级查询预测 GPU 会采样哪些 mip](predicting-which-mips-the-gpu-samples-with-level-of-detail-queries.md) — 提前确定 GPU 对某个纹理采样时需要哪些 mipmap 级别。
- [动态调整纹理细节层级](dynamically-adjusting-texture-level-of-detail.md) — 推迟生成或加载更大的 mipmap，直到需要该细节层级时再进行。
