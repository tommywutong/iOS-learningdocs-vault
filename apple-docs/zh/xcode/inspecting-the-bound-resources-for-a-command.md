---
title: 检查命令的绑定资源
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/inspecting-the-bound-resources-for-a-command
source_url: 'https://developer.apple.com/documentation/xcode/inspecting-the-bound-resources-for-a-command'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/inspecting-the-bound-resources-for-a-command.json'
content_hash: 'sha256:89f767ba3f3195e0'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Metal debugger](metal-debugger.md)

# 检查命令的绑定资源

<sub>文章</sub>

通过检查编码器中任意点的绑定资源来发现问题。

## 概述

Metal 的渲染和计算编码器允许你设置管线状态、绑定资源、指定参数，并编码 GPU 命令。绑定资源查看器可帮助你确定编码器中任意点的绑定资源。

![绑定资源查看器的屏幕截图，列出了绑定资源。](../../../attachments/bd76301bd2465d45548820e9ecad9db0/gputools-metal-debugger-brv-overview@2x.png)

### 检查绑定资源

绑定资源查看器会显示编码器中当前的绑定资源集合。你可以双击某一资源行以进一步检查该资源。

![某条绘制命令的绑定资源表格的屏幕截图。](../../../attachments/914557cf4b19766e6162850ff6aca9ba/gputools-metal-debugger-brv-table-bound@2x.png)

对于渲染通道，绑定资源查看器会将资源分为以下几个部分：

- **Render Pipeline（渲染管线）：** 指定的渲染管线状态。
- **Execute Indirect（间接执行）：** 该命令据以执行的间接命令缓冲区（ICB）。
- **Vertex/Object/Mesh/Tile/Fragment Stage（顶点/对象/网格/图块/片元阶段）：** 相应阶段中的资源。此外，还包括着色器函数。对于顶点阶段和网格阶段，还包括索引缓冲区和输出几何图形。
- **Attachments（附件）：** 附件纹理。
- **Indirect（间接）：** 已使用的间接资源以及来自同一堆的资源。要使用某个资源，请调用 [useResource(_:usage:stages:)](<../metal/mtlrendercommandencoder/useresource(__usage_stages_).md>) 或 [useHeap(_:stages:)](<../metal/mtlrendercommandencoder/useheap(__stages_).md>)。

对于计算通道，绑定资源查看器会将资源分为以下几个部分：

- **Compute Pipeline（计算管线）：** 指定的计算管线状态。
- **Execute Indirect（间接执行）：** 该命令据以执行的间接命令缓冲区（ICB）。
- **Compute（计算）：** 计算通道中的资源。
- **Indirect（间接）：** 已使用的间接资源以及来自同一堆的资源。要使用某个资源，请调用 [useResource(_:usage:)](<../metal/mtlcomputecommandencoder/useresource(__usage_).md>)、[useResources(_:usage:)](<../metal/mtlcomputecommandencoder/useresources(__usage_).md>)、[useHeap(_:)](<../metal/mtlcomputecommandencoder/useheap(__).md>) 或 [useHeaps(_:)](<../metal/mtlcomputecommandencoder/useheaps(__).md>)。

绑定资源查看器为所有资源类型提供以下信息：

| 列 | 属性 | 说明 |
|---|---|---|
| Label（标签） | [label](../metal/mtlresource/label.md) | 你在创建资源时设置的标签。使用此信息来识别你的 App 中的特定资源。要了解如何为你的资源命名，请参阅 [Naming resources and commands](naming-resources-and-commands.md)。 |
| Type（类型） |  | 用于标识参数在着色器中位置的属性：缓冲区、纹理、采样器或线程组缓冲区索引。 |
| Allocated Size（已分配大小） | [allocatedSize](../metal/mtlresource/allocatedsize.md) | 该资源的实际已分配内存大小。 |
| Parameter Name（参数名称） |  | 着色器中绑定到该资源的变量名称。 |
| Resource Usage（资源用途） |  | 表示着色器是否可以读取或写入该资源的指示符。 |
| Access（访问） |  | 表示着色器在绘制命令或计算调度中是否实际访问了该资源的指示符。 |
| Insights（洞察） |  | 可能改善资源使用情况的潜在问题或优化建议。 |
| Shader Stages（着色器阶段） |  | 使用该资源的着色器阶段（参阅 [MTLRenderStages](../metal/mtlrenderstages.md)）。 |

对于纹理，你可以添加以下列：

| 列 | 属性 | 说明 |
|---|---|---|
| Pixel Format（像素格式） | [pixelFormat](../metal/mtltexture/pixelformat.md) | 你在创建纹理时选择的 Metal 像素格式。 |
| Type（类型） | [textureType](../metal/mtltexture/texturetype.md) | 该纹理的子类型。 |
| Width（宽度） | [width](../metal/mtltexture/width.md) | 该纹理基础 mipmap 的宽度，以像素为单位。 |
| Height（高度） | [height](../metal/mtltexture/height.md) | 该纹理基础 mipmap 的高度，以像素为单位。 |
| Depth（深度） | [depth](../metal/mtltexture/depth.md) | 该纹理基础 mipmap 的深度，以像素为单位。 |
| Slice（切片） | [slice](../metal/mtlrenderpassattachmentdescriptor/slice.md) | 渲染通道附件所使用的纹理切片。 |
| Level（级别） | [level](../metal/mtlrenderpassattachmentdescriptor/level.md) | 渲染通道附件所使用的纹理 mipmap 级别。 |
| Depth Plane（深度平面） | [depthPlane](../metal/mtlrenderpassattachmentdescriptor/depthplane.md) | 渲染通道附件所使用的纹理深度平面。 |
| Array Length（数组长度） | [arrayLength](../metal/mtltexture/arraylength.md) | 纹理数组中的切片数量。 |
| Mipmap Count（Mipmap 数量） | [mipmapLevelCount](../metal/mtltexture/mipmaplevelcount.md) | 该纹理存储的 mipmap 级别数量。 |
| Sample Count（采样点数量） | [sampleCount](../metal/mtltexture/samplecount.md) | 每个像素存储的采样点数量。 |
| Usage（用途） | [usage](../metal/mtltexture/usage.md) | 表示着色器或 App 可对该纹理执行哪些操作的标志。列表限制越严格，Metal 能对该纹理应用的优化就越多。 |

对于缓冲区，你可以添加以下列：

| 列 | 属性 | 说明 |
|---|---|---|
| Length（长度） | [length](../metal/mtlbuffer/length.md) | 该缓冲区的逻辑长度，以字节为单位。 |
| Offset（偏移量） |  | 数据起始位置相对于缓冲区起点的偏移量，以字节为单位。 |

对于函数，你可以添加 Library（库）列，以显示 App 用于创建该函数的库。

### 使用洞察提升你的 Metal 工作负载

点击右下角的洞察按钮，打开一个针对绑定资源的建议弹出窗口。

![洞察弹出窗口的屏幕截图，显示了两条与冗余缓冲区绑定相关的建议。](../../../attachments/7e66ed5cba8048eaa3f349535d9ae96a/gputools-metal-debugger-brv-insights@2x.png)

### 检查着色器访问的资源

着色器不一定会访问绘制命令或计算调度中的每一个绑定资源。这在无绑定（bindless）工作流程中非常常见，此类工作流程中着色器只会从一个大型堆中访问一小部分资源。绑定资源查看器为着色器实际访问的资源提供了一个顶层过滤器。

要应用该过滤器，请点击表格上方的已访问按钮，仅查看已访问的资源。

![绑定资源查看器的屏幕截图，突出显示了已访问按钮。](../../../attachments/7263ad3152f14d3dc02403e3749f138e/gputools-metal-debugger-brv-table-accessed@2x.png)

### 使用过滤器限定范围

使用绑定资源查看器底部的过滤字段，通过输入过滤条件来调整过滤标准。表格会显示匹配过滤条件的相关资源。

你还可以点击过滤按钮，为特定类型的资源或已使用的间接资源添加过滤器。

当存在两个或更多过滤条件时，你可以点击过滤按钮来选择匹配任意条件还是全部条件。对于任意过滤条件，你都可以点击它来选择包含或排除匹配该条件的资源。

## 另请参阅

### Metal 命令分析

- [Inspecting the geometry of a draw command](inspecting-the-geometry-of-a-draw-command.md) — 通过检查当前几何图形，找出你的 App 的顶点、对象或网格函数中的问题。
- [Inspecting the attachments of a draw command](inspecting-the-attachments-of-a-draw-command.md) — 通过检查各个像素和采样点来发现附件问题。
- [Debugging the shaders within a draw command or compute dispatch](debugging-the-shaders-within-a-draw-command-or-compute-dispatch.md) — 使用着色器调试器识别并修复你的 App 中有问题的着色器。
- [Analyzing draw command and compute dispatch performance with GPU counters](analyzing-draw-command-and-compute-dispatch-performance-with-gpu-counters.md) — 通过检查性能计数器来识别帧捕获中的问题。
- [Analyzing draw command and compute dispatch performance with pipeline statistics](analyzing-draw-command-and-compute-dispatch-performance-with-pipeline-statistics.md) — 通过检查管线统计信息来识别帧捕获中的问题。
