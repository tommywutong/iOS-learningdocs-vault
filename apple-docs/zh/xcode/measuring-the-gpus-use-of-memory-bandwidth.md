---
title: 测量 GPU 对内存带宽的使用
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/measuring-the-gpus-use-of-memory-bandwidth
source_url: 'https://developer.apple.com/documentation/xcode/measuring-the-gpus-use-of-memory-bandwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/measuring-the-gpus-use-of-memory-bandwidth.json'
content_hash: 'sha256:a2b936f49283b5fc'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Metal developer workflows](metal-developer-workflows.md)

# 测量 GPU 对内存带宽的使用

<sub>文章</sub>

通过测量 GPU 的内存带宽，检查你的 Metal App 是否正确读取和写入内存。

## 概述

Instruments 开发者工具和 Metal 调试器的 Performance 时间线提供了带宽计数器（分别参阅[分析 Metal App 的性能](analyzing-the-performance-of-your-metal-app.md)和[使用可视化时间线分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-a-visual-timeline.md)）。GPU 带宽计数器会测量 GPU 每秒读取和写入（即_访问_）内存的数据量，单位为 GB。

对于某些活动，你可能希望 App 使用较高的带宽，例如快速复制数据以节省时间；对于其他活动，则希望使用较低的带宽，以节省能耗或让 CPU 和其他进程能够访问内存。如果 GPU 的内存带宽使用量在你未预期的情况下很高，可能会妨碍 CPU 访问内存。

你可以在各个 pass 中使用以下策略来降低 GPU 的内存带宽：

- 只读取该 pass 所需的数据。
- 只写入后续 pass 所需的数据。
- 只加载和存储渲染 pass 所需的附件。
- 创建仅使用适当 [MTLTextureUsage](../metal/mtltextureusage.md) 特性（attribute）的纹理。

Metal 可以通过优化对具有正确使用特性的纹理所进行的内存访问，降低 App 的内存带宽。若要适当地设置纹理的用途，请配置 [MTLTextureDescriptor](../metal/mtltexturedescriptor.md) 实例（instance）的 [usage](../metal/mtltexturedescriptor/usage.md) 属性，并使用它创建纹理。

缓冲区和纹理操作也可能增加 App 的内存带宽。若要检查缓冲区或纹理操作的限制因素计数器是否过高，并了解可以采取哪些措施降低它们的影响，请参阅[减少着色器瓶颈](reducing-shader-bottlenecks.md)。

> [!tip] 提示
> Metal 调试器中的 Dependencies 查看器可以帮助你找出减少渲染和计算 pass 内存带宽的机会。请参阅[分析资源依赖关系](analyzing-resource-dependencies.md)。

## 另请参阅

### 计数器

- [查找 Metal App 的 GPU 占用率](finding-your-metal-apps-gpu-occupancy.md) — 通过占用率了解执行着色器时的 GPU 使用情况。
- [减少着色器瓶颈](reducing-shader-bottlenecks.md) — 通过检查 GPU 子系统的限制因素和利用率计数器，识别并尽量减少拥塞点。
