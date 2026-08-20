---
title: 自定义渲染通道设置
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, Xcode 26.3+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/customizing-render-pass-setup
source_url: 'https://developer.apple.com/documentation/metal/customizing-render-pass-setup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/customizing-render-pass-setup.json'
content_hash: 'sha256:5bd06a3a2ecb6b84'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md) · [Metal 示例代码库](metal-sample-code-library.md)

# 自定义渲染通道设置

<sub>示例代码</sub>

通过创建自定义渲染通道，渲染到离屏纹理。

## 概述

渲染通道（render pass）是一系列渲染命令的序列，这些命令会绘制到一组纹理中。此示例执行一对渲染通道来渲染一个视图的内容。对于第一个通道，示例创建了一个自定义渲染通道，用于将图像渲染到一个纹理中。这个通道是一个**离屏渲染通道**，因为示例渲染到的是一个常规纹理，而不是由显示子系统创建的纹理。第二个渲染通道使用由 [MTKView](../metalkit/mtkview.md) 对象提供的渲染通道描述符（render pass descriptor），来渲染并显示最终图像。示例将离屏渲染通道生成的纹理，用作第二个渲染通道中绘图命令的源数据。

离屏渲染通道是更大或更复杂的渲染程序的基础构建模块。例如，许多光照和阴影算法需要一个离屏渲染通道来渲染阴影信息，以及第二个通道来计算最终的场景光照。离屏渲染通道在批量处理那些无需显示在屏幕上的数据时也很有用。

### 为离屏渲染通道创建纹理

[MTKView](../metalkit/mtkview.md) 对象会自动创建可绘制纹理用于渲染。示例还需要一个纹理，用于在离屏渲染通道期间进行渲染。为此，它首先创建一个 [MTLTextureDescriptor](mtltexturedescriptor.md) 对象并配置其属性。

**AAPLRenderer.m**

```objective-c
MTLTextureDescriptor *texDescriptor = [MTLTextureDescriptor new];
texDescriptor.textureType = MTLTextureType2D;
texDescriptor.width = 512;
texDescriptor.height = 512;
texDescriptor.pixelFormat = MTLPixelFormatRGBA8Unorm;
texDescriptor.usage = MTLTextureUsageRenderTarget |
                      MTLTextureUsageShaderRead;
```

示例配置了 [usage](mtltexturedescriptor/usage.md) 属性，以准确说明它打算如何使用新纹理。它需要在离屏渲染通道中将数据渲染到纹理中，并在第二个通道中从纹理读取数据。示例通过设置 [MTLTextureUsageRenderTarget](mtltextureusage/rendertarget.md) 和 [MTLTextureUsageShaderRead](mtltextureusage/shaderread.md) 标志来指定这种用途。

精确设置 usage 标志可以提高性能，因为 Metal 可以仅为指定的用途配置纹理的底层数据。

### 创建渲染管线

渲染管线（render pipeline）指定了如何执行一个绘图命令，包括要执行的顶点函数和片段函数，以及它所作用的任何渲染目标（render target）的像素格式。之后，当示例创建自定义渲染通道时，它需要使用相同的像素格式。

此示例为每个渲染通道创建一个渲染管线，离屏渲染管线的代码如下所示：

**AAPLRenderer.m**

```objective-c
pipelineStateDescriptor.label = @"Offscreen Render Pipeline";
pipelineStateDescriptor.sampleCount = 1;
pipelineStateDescriptor.vertexFunction =  [defaultLibrary newFunctionWithName:@"simpleVertexShader"];
pipelineStateDescriptor.fragmentFunction =  [defaultLibrary newFunctionWithName:@"simpleFragmentShader"];
pipelineStateDescriptor.colorAttachments[0].pixelFormat = _renderTargetTexture.pixelFormat;
_renderToTextureRenderPipeline = [_device newRenderPipelineStateWithDescriptor:pipelineStateDescriptor error:&error];
```

用于创建可绘制渲染管线的代码与[使用 Metal 4 绘制三角形](drawing-a-triangle-with-metal-4.md)中的代码类似。为了确保两种像素格式匹配，示例将描述符的像素格式设置为视图的 `colorPixelFormat`。类似地，在创建离屏渲染管线时，示例将描述符的像素格式设置为离屏纹理的格式。

### 设置离屏渲染通道描述符

为了渲染到离屏纹理，示例配置了一个新的渲染通道描述符。它创建了一个 [MTLRenderPassDescriptor](mtlrenderpassdescriptor.md) 对象并配置其属性。此示例渲染到一个单一颜色纹理，因此它将 `colorAttachment[0].texture` 设置为指向离屏纹理：

**AAPLRenderer.m**

```objective-c
_renderToTextureRenderPassDescriptor.colorAttachments[0].texture = _renderTargetTexture;
```

示例还需要为此渲染目标配置一个**加载动作（load action）** 和一个**存储动作（store action）**。

**AAPLRenderer.m**

```objective-c
_renderToTextureRenderPassDescriptor.colorAttachments[0].loadAction = MTLLoadActionClear;
_renderToTextureRenderPassDescriptor.colorAttachments[0].clearColor = MTLClearColorMake(1, 1, 1, 1);

_renderToTextureRenderPassDescriptor.colorAttachments[0].storeAction = MTLStoreActionStore;
```

加载动作决定了在渲染通道开始时、GPU 执行任何绘图命令之前纹理的初始内容。类似地，存储动作在渲染通道完成后执行，并决定 GPU 是否将最终图像写回纹理。示例配置了一个加载动作来清除渲染目标的内容，以及一个存储动作来将渲染后的数据存储回纹理。它需要做后者，因为第二个渲染通道中的绘图命令会采样这些数据。

Metal 使用加载和存储动作来优化 GPU 管理纹理数据的方式。大纹理消耗大量内存，而处理这些纹理可能会消耗大量内存带宽。正确设置渲染目标动作可以减少 GPU 用于访问纹理的内存带宽，从而提高性能和电池续航。有关指导，请参阅[设置加载和存储动作](setting-load-and-store-actions.md)。

渲染通道描述符还有其他未在此示例中使用的属性，它们可以进一步修改渲染过程。关于自定义渲染通道描述符的其他方式，请参阅 [MTLRenderPassDescriptor](mtlrenderpassdescriptor.md)。

### 渲染到离屏纹理

示例现在已经拥有了编码两个渲染通道所需的一切。在了解示例如何编码渲染通道之前，理解 Metal 如何在 GPU 上调度命令是很重要的。

当一个 App 将命令缓冲区提交到命令队列时，默认情况下，Metal 需要表现得好像它是按顺序执行命令的。为了提高性能并更好地利用 GPU，Metal 可以并发运行命令，只要这样做不会产生与顺序执行不一致的结果。为此，当一个通道写入资源而后续通道从该资源读取时（如此示例所示），Metal 会检测到依赖关系并自动延迟后续通道的执行，直到第一个通道完成。因此，与[同步 CPU 和 GPU 工作](synchronizing-cpu-and-gpu-work.md)（其中 CPU 和 GPU 需要显式同步）不同，此示例不需要做任何特殊处理。它只是按顺序编码两个通道，而 Metal 确保它们按该顺序运行。

示例将两个渲染通道编码到一个命令缓冲区中，从离屏渲染通道开始。它使用之前创建的离屏渲染通道描述符来创建一个渲染命令编码器。

**AAPLRenderer.m**

```objective-c
id<MTLRenderCommandEncoder> renderEncoder =
    [commandBuffer renderCommandEncoderWithDescriptor:_renderToTextureRenderPassDescriptor];
renderEncoder.label = @"Offscreen Render Pass";
[renderEncoder setRenderPipelineState:_renderToTextureRenderPipeline];
```

渲染通道中的其他一切类似于[使用 Metal 4 绘制三角形](drawing-a-triangle-with-metal-4.md)。它配置了管线和任何必要的参数，然后对绘图命令进行编码。对命令进行编码后，它调用 [- endEncoding](<mtlcommandencoder/endencoding().md>) 来完成编码过程。

**AAPLRenderer.m**

```objective-c
[renderEncoder endEncoding];
```

多个通道需要按顺序编码到一个命令缓冲区中，因此示例需要在开始下一个渲染通道之前完成对第一个渲染通道的编码。

### 渲染到可绘制纹理

第二个渲染通道需要渲染最终图像。可绘制渲染管线的片段着色器从一个纹理中采样数据，并将该采样值作为最终颜色返回：

**AAPLShaders.metal**

```metal
// 对纹理进行采样并输出采样颜色的片段着色器。
fragment float4 textureFragmentShader(TexturePipelineRasterizerData in      [[stage_in]],
                                      texture2d<float>              texture [[texture(AAPLTextureInputIndexColor)]])
{
    sampler simpleSampler;

    // 从纹理中采样数据。
    float4 colorSample = texture.sample(simpleSampler, in.texcoord);

    // 将颜色采样结果作为最终颜色返回。
    return colorSample;
}
```

代码使用视图的渲染通道描述符来创建第二个渲染通道，并对一个绘制带纹理四边形的绘图命令进行编码。它指定离屏纹理作为该命令的纹理参数。

**AAPLRenderer.m**

```objective-c
id<MTLRenderCommandEncoder> renderEncoder =
    [commandBuffer renderCommandEncoderWithDescriptor:drawableRenderPassDescriptor];
renderEncoder.label = @"Drawable Render Pass";

[renderEncoder setRenderPipelineState:_drawableRenderPipeline];

[renderEncoder setVertexBytes:&quadVertices
                       length:sizeof(quadVertices)
                      atIndex:AAPLVertexInputIndexVertices];

[renderEncoder setVertexBytes:&_aspectRatio
                       length:sizeof(_aspectRatio)
                      atIndex:AAPLVertexInputIndexAspectRatio];

// 将离屏纹理设置为源纹理。
[renderEncoder setFragmentTexture:_renderTargetTexture atIndex:AAPLTextureInputIndexColor];
```

当示例提交命令缓冲区时，Metal 会顺序执行这两个渲染通道。在这种情况下，Metal 检测到第一个渲染通道写入离屏纹理，而第二个通道从中读取。当 Metal 检测到这样的依赖关系时，它会阻止后续通道执行，直到 GPU 完成第一个通道的执行。

## 另请参阅

### 渲染工作流

- [使用 Metal 绘制视图的内容](using-metal-to-draw-a-view's-contents.md) — 创建一个 MetalKit 视图和一个渲染通道来绘制视图的内容。
- [使用 Metal 4 绘制三角形](drawing-a-triangle-with-metal-4.md) — 通过在 GPU 上使用渲染管线运行绘图命令，渲染一个色彩鲜艳、旋转的 2D 三角形。
- [选择用于图形渲染的设备对象](selecting-device-objects-for-graphics-rendering.md) — 在多个 GPU 之间动态切换，以高效地渲染到显示器。
- [创建自定义 Metal 视图](creating-a-custom-metal-view.md) — 实现一个轻量级的、为你的 App 需求量身定制的 Metal 渲染视图。
- [使用深度测试计算图元可见性](calculating-primitive-visibility-using-depth-testing.md) — 通过使用深度纹理来确定场景中哪些像素是可见的。
- [在 CPU 上编码间接命令缓冲区](encoding-indirect-command-buffers-on-the-cpu.md) — 通过重用命令来减少 CPU 开销并简化命令执行。
- [使用图像块实现顺序无关的透明效果](implementing-order-independent-transparency-with-image-blocks.md) — 通过使用 tile 着色器和图像块，以任意顺序绘制重叠的半透明表面。
- [使用 Metal 快速资源加载来加载纹理和模型](loading-textures-and-models-using-metal-fast-resource-loading.md) — 使用快速资源加载，将纹理和缓冲区数据直接从磁盘流式传输到 Metal 资源中。
- [使用 Metal 网格着色器调整细节级别](adjusting-the-level-of-detail-using-metal-mesh-shaders.md) — 使用对象和网格着色器选择并渲染具有多个细节级别的网格。
- [使用 Hydra 渲染创建 3D 应用程序](creating-a-3d-application-with-hydra-rendering.md) — 构建一个与 Hydra 和 USD 集成的 3D 应用程序。
- [使用可见性结果缓冲区剔除遮挡几何体](culling-occluded-geometry-using-the-visibility-result-buffer.md) — 通过检查场景中每个对象是否可见，来绘制一个不渲染隐藏几何体的场景。
- [使用多重采样抗锯齿（MSAA）提升边缘渲染质量](improving-edge-rendering-quality-with-multisample-antialiasing-msaa.md) — 应用 MSAA，通过自定义解析选项以及即时和基于 tile 的解析路径来增强边缘渲染效果。
- [使用 Metal 显示链接实现平滑帧率](achieving-smooth-frame-rates-with-a-metal-display-link.md) — 以最小输入延迟进行渲染节奏控制，同时向操作系统提供关键信息，以实现能效渲染、热缓解和可持续工作负载的调度。

## 下载

- [CustomizingRenderPassSetup.zip](https://docs-assets.developer.apple.com/published/b88a5bf6a382/CustomizingRenderPassSetup.zip)
