---
title: 渲染流程
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/render-passes
source_url: 'https://developer.apple.com/documentation/metal/render-passes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/render-passes.json'
content_hash: 'sha256:f1dd696eb2f95dfa'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md)

# 渲染流程

<sub>API 集合</sub>

编码一个渲染流程（render pass），将图形绘制到图像中。

## 概述

渲染流程（render pass）使用渲染管线（render pipeline）处理并光栅化几何图形，将结果输出到一个或多个输出附件（attachment）。

渲染流程由以下部分组成：

- 一组输入资源，例如缓冲区和纹理
- 一个渲染管线，用于配置处理这些输入资源的 GPU
- 绘制命令
- 顶点着色器（vertex shader），即处理并变换场景几何图形的 GPU 核心函数
- 一个可选的曲面细分（tessellation）阶段，用于为场景几何图形添加细节
- 片段着色器（fragment shader），即为每个像素生成最终颜色值的 GPU 核心函数
- 可选的输出，可以包括颜色、深度和模板附件，以及它们的加载和存储操作

有关实现细节，参见 [Customizing render pass setup](customizing-render-pass-setup.md) 示例。

## 主题

### 编码渲染流程

- [MTL4RenderCommandEncoder](mtl4rendercommandencoder.md) — 将单个渲染流程的配置和绘制命令编码到命令缓冲区中。
- [MTLRenderCommandEncoder](mtlrendercommandencoder.md) — 将单个渲染流程的配置和绘制命令编码到命令缓冲区中。
- [MTL4RenderEncoderOptions](mtl4renderencoderoptions.md) — 在创建编码器时指定的自定义渲染流程选项。
- [MTLTriangleFillMode](mtltrianglefillmode.md) — 指定如何光栅化三角形和三角形带图元。
- [MTLWinding](mtlwinding.md) — 决定正面图元的顶点环绕规则。
- [MTLCullMode](mtlcullmode.md) — 决定是否执行剔除以及剔除哪种图元类型的模式。
- [MTLPrimitiveType](mtlprimitivetype.md) — 用于绘制命令的几何图元类型。
- [MTLIndexType](mtlindextype.md) — 索引缓冲区的索引类型，该缓冲区引用几何图元的顶点。
- [MTLDepthClipMode](mtldepthclipmode.md) — 决定如何处理近平面或远平面之外的片段的模式。
- [MTLVisibilityResultMode](mtlvisibilityresultmode.md) — 决定 GPU 执行渲染流程后向结果缓冲区写入内容（如果有）的模式。
- [MTLVisibilityResultType](mtlvisibilityresulttype.md) — 该枚举控制 Metal 是在渲染编码器之间累积可见性结果还是重置它们。

### 并行编码渲染流程

- [MTLParallelRenderCommandEncoder](mtlparallelrendercommandencoder.md) — 一个将单个渲染流程拆分开的实例，以便可以从多个线程同时编码。
- [MTLLoadAction](mtlloadaction.md) — 渲染流程开始时对附件执行的操作类型。
- [MTLStoreAction](mtlstoreaction.md) — 渲染流程结束时对附件执行的操作类型。
- [MTLStoreActionOptions](mtlstoreactionoptions.md) — 修改存储操作的选项。_(已废弃)_

### 配置渲染命令编码器

- [MTL4RenderPassDescriptor](mtl4renderpassdescriptor.md) — 描述一个渲染流程。
- [MTLRenderPassDescriptor](mtlrenderpassdescriptor.md) — 一组保存渲染流程结果的渲染目标。
- [MTLRenderPassAttachmentDescriptor](mtlrenderpassattachmentdescriptor.md) — 作为渲染流程生成的像素的输出目的地的渲染目标。
- [MTLRenderPassColorAttachmentDescriptorArray](mtlrenderpasscolorattachmentdescriptorarray.md) — 渲染流程颜色附件描述符对象的数组。
- [MTLRenderPassColorAttachmentDescriptor](mtlrenderpasscolorattachmentdescriptor.md) — 作为渲染流程生成的颜色像素的输出目的地的颜色渲染目标。
- [MTLClearColor](mtlclearcolor.md) — 用于颜色像素的 RGBA 值。
- [MTLRenderPassDepthAttachmentDescriptor](mtlrenderpassdepthattachmentdescriptor.md) — 作为渲染流程生成的深度像素的输出目的地的深度渲染目标。
- [MTLMultisampleDepthResolveFilter](mtlmultisampledepthresolvefilter.md) — 用于控制 MSAA 深度解析操作的过滤选项。
- [MTL4RenderPipelineColorAttachmentDescriptorArray](mtl4renderpipelinecolorattachmentdescriptorarray.md) — 渲染管线的颜色附件描述数组。
- [MTLTileRenderPipelineColorAttachmentDescriptorArray](mtltilerenderpipelinecolorattachmentdescriptorarray.md) — 分块渲染管线的颜色附件描述符数组。
- [MTLRenderPassStencilAttachmentDescriptor](mtlrenderpassstencilattachmentdescriptor.md) — 作为渲染流程生成的模板像素的输出目的地的模板渲染目标。
- [MTLMultisampleStencilResolveFilter](mtlmultisamplestencilresolvefilter.md) — 用于控制多重采样模板解析操作的常量。
- [MTLRenderPassSampleBufferAttachmentDescriptorArray](mtlrenderpasssamplebufferattachmentdescriptorarray.md) — 渲染流程的采样缓冲区附件数组。
- [MTLRenderPassSampleBufferAttachmentDescriptor](mtlrenderpasssamplebufferattachmentdescriptor.md) — 描述在渲染流程开始和结束时存储 GPU 计数器信息的位置。
- [MTLLogicalToPhysicalColorAttachmentMap](mtllogicaltophysicalcolorattachmentmap.md) — 让你能够轻松指定从逻辑索引到物理索引的颜色附件重映射。
- [MTLDispatchThreadsIndirectArguments](mtldispatchthreadsindirectarguments.md)

### 渲染管线状态

- [MTLRenderPipelineState](mtlrenderpipelinestate.md) — 表示渲染流程的图形管线配置的接口，该流程会将其应用于你编码的绘制命令。
- [MTL4RenderPipelineDescriptor](mtl4renderpipelinedescriptor.md) — 将属性组合在一起以创建渲染管线状态对象。
- [MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md) — 你传递给 GPU 设备以获取渲染管线状态的一组选项参数。
- [MTLRenderPipelineFunctionsDescriptor](mtlrenderpipelinefunctionsdescriptor.md) — 用于更新渲染管线的函数集合。
- [MTL4MeshRenderPipelineDescriptor](mtl4meshrenderpipelinedescriptor.md) — 将你用于创建网格渲染管线状态对象的属性组合在一起。
- [MTLMeshRenderPipelineDescriptor](mtlmeshrenderpipelinedescriptor.md) — 为网格着色配置新渲染管线状态对象的对象。
- [MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md) — 渲染或计算管线使用的缓冲区的可变性选项。
- [MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md) — 管线缓冲区描述符的数组。
- [MTL4RenderPipelineColorAttachmentDescriptor](mtl4renderpipelinecolorattachmentdescriptor.md)
- [MTLRenderPipelineColorAttachmentDescriptor](mtlrenderpipelinecolorattachmentdescriptor.md) — 为渲染管线指定颜色配置和颜色操作的颜色渲染目标。
- [MTLRenderPipelineColorAttachmentDescriptorArray](mtlrenderpipelinecolorattachmentdescriptorarray.md) — 渲染管线颜色附件描述符对象的数组。
- [MTL4TileRenderPipelineDescriptor](mtl4tilerenderpipelinedescriptor.md) — 将你用于创建分块渲染管线状态对象的属性组合在一起。
- [MTLTileRenderPipelineDescriptor](mtltilerenderpipelinedescriptor.md) — 为分块着色配置新渲染管线状态对象的对象。
- [MTLTileRenderPipelineColorAttachmentDescriptor](mtltilerenderpipelinecolorattachmentdescriptor.md) — 分块着色渲染管线的颜色渲染目标的描述。
- [MTLPipelineOption](mtlpipelineoption.md) — 决定 Metal 如何准备管线的选项。
- [MTL4RenderPipelineBinaryFunctionsDescriptor](mtl4renderpipelinebinaryfunctionsdescriptor.md) — 让你能够指定要链接到渲染管线每个阶段的额外二进制函数。
- [MTL4RenderPipelineDynamicLinkingDescriptor](mtl4renderpipelinedynamiclinkingdescriptor.md) — 将为渲染管线提供链接属性的属性组合在一起。

### 动态渲染管线状态

- [MTLViewport](mtlviewport.md) — 用于视口裁剪的三维矩形区域。
- [MTLScissorRect](mtlscissorrect.md) — 用于剪裁片段测试的矩形。
- [MTLVertexAmplificationViewMapping](mtlvertexamplificationviewmapping.md) — 应用于渲染目标索引和视口索引的偏移量。
- [MTLQuadTessellationFactorsHalf](mtlquadtessellationfactorshalf.md) — 四边形面片的逐面片曲面细分因子。
- [MTLTriangleTessellationFactorsHalf](mtltriangletessellationfactorshalf.md) — 三角形面片的逐面片曲面细分因子。

### 渲染流程输入

- [MTLVertexDescriptor](mtlvertexdescriptor.md) — 描述如何组织数据并将数据映射到顶点函数的实例。
- [MTLVertexAttributeDescriptor](mtlvertexattributedescriptor.md) — 决定如何在内存中存储属性数据并将其映射到顶点函数参数的对象。
- [MTLVertexAttributeDescriptorArray](mtlvertexattributedescriptorarray.md) — 顶点属性描述符实例的数组。
- [MTLVertexBufferLayoutDescriptor](mtlvertexbufferlayoutdescriptor.md) — 配置渲染管线如何获取要发送给顶点函数的数据的对象。
- [MTLVertexBufferLayoutDescriptorArray](mtlvertexbufferlayoutdescriptorarray.md) — 顶点缓冲区布局描述符实例的数组。
- [MTLBufferLayoutStrideDynamic](mtlbufferlayoutstridedynamic.md)

### 渲染流程输出

- [MTLDrawable](mtldrawable.md) — 一个可以渲染或写入的可显示资源。
- [MTLDrawablePresentedHandler](mtldrawablepresentedhandler.md) — 在可绘制对象呈现后被调用的代码块。

### 深度测试

- [Calculating primitive visibility using depth testing](calculating-primitive-visibility-using-depth-testing.md) — 通过使用深度纹理确定场景中哪些像素可见。
- [MTLDepthStencilState](mtldepthstencilstate.md) — 指定渲染流程中所用深度和模板配置及操作的深度和模板状态实例。
- [MTLDepthStencilDescriptor](mtldepthstencildescriptor.md) — 配置新的 [MTLDepthStencilState](mtldepthstencilstate.md) 实例的实例。
- [MTLStencilDescriptor](mtlstencildescriptor.md) — 定义深度和模板状态对象的正面或背面模板操作的对象。

### 光栅化设置

- [Rendering at different rasterization rates](rendering-at-different-rasterization-rates.md) — 配置光栅化速率映射，根据所需的细节量改变光栅化速率。
- [Creating a rasterization rate map](creating-a-rasterization-rate-map.md) — 为渲染目标的每个部分定义光栅化速率。
- [Rendering with a rasterization rate map](rendering-with-a-rasterization-rate-map.md) — 创建离屏纹理以保存中间光栅化数据。
- [Scaling variable rasterization rate content](scaling-variable-rasterization-rate-content.md) — 使用速率映射数据缩放内容以填充目标纹理。
- [MTLRasterizationRateMapDescriptor](mtlrasterizationratemapdescriptor.md) — 用于配置新光栅化速率映射的对象。
- [MTLRasterizationRateMap](mtlrasterizationratemap.md) — 决定渲染时如何应用可变光栅化速率的已编译只读实例。
- [MTLCoordinate2D](mtlcoordinate2d.md) — 视口中的一个坐标。
- [MTLCoordinate2DMake](<mtlcoordinate2dmake(____).md>) — 返回具有指定坐标的新二维点。

### 优化技术

- [Specifying drawing and dispatch arguments indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md) — 如果你在编码命令时不知道绘制或调度调用的参数，可以使用间接命令。
- [Rendering to multiple viewports in a draw command](rendering-to-multiple-viewports-in-a-draw-command.md) — 在顶点着色器中选择视口及其对应的剪裁矩形。
- [Rendering to multiple texture slices in a draw command](rendering-to-multiple-texture-slices-in-a-draw-command.md) — 在顶点着色器中选择目标纹理切片。

### 高级多重采样

- [Positioning samples programmatically](positioning-samples-programmatically.md) — 在渲染到多重采样渲染目标时配置采样点的位置。
- [Storing data a pass makes with custom sample positions for a subsequent pass](storing-data-a-pass-makes-with-custom-sample-positions-for-a-subsequent-pass.md) — 在你的 App 为其深度渲染目标使用可编程采样位置或复制 MSAA 深度数据时通知 Metal。

### 应用渲染技术

- [Drawing a triangle with Metal 4](drawing-a-triangle-with-metal-4.md) — 通过在 GPU 上使用渲染管线运行绘制命令，渲染一个彩色的旋转二维三角形。
- [Customizing render pass setup](customizing-render-pass-setup.md) — 通过创建自定义渲染流程渲染到离屏纹理中。
- [Setting load and store actions](setting-load-and-store-actions.md) — 设置定义渲染流程如何加载和存储渲染目标的操作。
- [Improving rendering performance with vertex amplification](improving-rendering-performance-with-vertex-amplification.md) — 运行绘制命令，使用相同的顶点数据多次渲染到不同的输出。

## 另请参阅

### 命令编码器

- [Compute passes](compute-passes.md) — 编码一个计算流程，在线程网格上并行运行计算，在 GPU 的多个核心上处理和操作 Metal 资源数据。
- [Machine learning passes](machine-learning-passes.md) — 将机器学习模型推理添加到你的 Metal App 的 GPU 工作流程中。
- [Blit passes](blit-passes.md) — 编码一个块信息传输流程，用于在 GPU 资源（例如缓冲区和纹理）之间调整和复制数据。
- [Indirect command encoding](indirect-command-encoding.md) — 将绘制命令存储在 Metal 缓冲区中，并在之后的某个时间在 GPU 上运行它们，可以运行一次或重复运行。
- [Ray tracing with acceleration structures](ray-tracing-with-acceleration-structures.md) — 使用三角形和边界体构建场景几何图形的表示，以便快速追踪穿过场景的光线。
