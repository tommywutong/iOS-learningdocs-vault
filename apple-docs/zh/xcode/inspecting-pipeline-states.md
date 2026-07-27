---
title: 检查管线状态
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/inspecting-pipeline-states
source_url: 'https://developer.apple.com/documentation/xcode/inspecting-pipeline-states'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/inspecting-pipeline-states.json'
content_hash: 'sha256:1218cbbc7c454f9b'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Metal debugger](metal-debugger.md)

# 检查管线状态

<sub>文章</sub>

通过检查渲染和计算通道的属性，确定它们的行为方式。

## 概述

Metal 调试器允许你使用管线状态查看器检查管线状态。双击某个管线状态即可将其打开，并在表格中查看其相关属性。

![显示管线状态属性层级结构的管线状态查看器截图。](../../../attachments/a2d962b77ee79e65a5e5da43d72e15bf/gputools-metal-debugger-psov-overview@2x.png)

在上面的截图中，管线状态的名称 G-buffer Creation 显示在表格上方。在名称右侧，你可以点击「在内存中显示」按钮或「在时间线中显示」按钮，分别打开内存查看器或性能时间线，二者都会高亮显示该管线状态。

该表格以逻辑层级结构显示你的管线状态的属性。点击左侧的显示控制以展开分组，查看更多信息。借助该表格，你可以快速检查 [MTLRenderPipelineState](../metal/mtlrenderpipelinestate.md) 或 [MTLComputePipelineState](../metal/mtlcomputepipelinestate.md) 的属性。

### 用筛选条件缩小范围

使用管线状态查看器底部的筛选栏，通过输入筛选词来调整筛选条件。随后表格会显示匹配筛选词的相关管线状态属性，并高亮显示匹配项。

![](../../../attachments/c6e5b1c88ae2addf42882088df8c2a80/gputools-metal-debugger-psov-filter@2x.png)

<sub>管线状态查看器正在筛选术语 pixel 的截图。列表以层级结构显示匹配的属性。</sub>

当存在两个或更多筛选词时，你可以点击筛选按钮，选择匹配任一词还是全部词。

## 另请参阅

### Metal 资源检查

- [Inspecting acceleration structures](inspecting-acceleration-structures.md) — 通过检查加速结构，揭示光线相交的性能瓶颈。
- [Inspecting buffers](inspecting-buffers.md) — 通过检查缓冲区内容，确认你的缓冲区格式。
- [Inspecting sampler states](inspecting-sampler-states.md) — 通过检查采样器状态的属性，验证其配置。
- [Inspecting shaders](inspecting-shaders.md) — 通过检查和编辑着色器，提升 App 的着色器性能。
- [Inspecting textures](inspecting-textures.md) — 通过检查纹理内容，发现纹理中的问题。
