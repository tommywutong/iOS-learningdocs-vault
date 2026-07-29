---
title: 使用 Metal 显示链接实现流畅帧率
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, Xcode 26.3+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/achieving-smooth-frame-rates-with-a-metal-display-link
source_url: 'https://developer.apple.com/documentation/metal/achieving-smooth-frame-rates-with-a-metal-display-link'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/achieving-smooth-frame-rates-with-a-metal-display-link.json'
content_hash: 'sha256:5aa548acd1821b46'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md) · [Metal 示例代码库](metal-sample-code-library.md)

# 使用 Metal 显示链接实现流畅帧率

<sub>示例代码</sub>

在向操作系统提供必要信息以实现高效节能渲染、热缓解和可持续工作负载调度的同时，以最低输入延迟调节渲染。

## 概述

> [!note] 注意
> 本示例代码项目与 WWDC23 讲座 10123 相关联：[将你的游戏带到 Mac：制定游戏计划](https://developer.apple.com/wwdc23/10123/)。

## 另请参阅

### 渲染工作流

- [使用 Metal 绘制视图内容](using-metal-to-draw-a-view's-contents.md) —— 创建 MetalKit 视图和一个渲染 pass 来绘制视图的内容。
- [使用 Metal 4 绘制三角形](drawing-a-triangle-with-metal-4.md) —— 通过在 GPU 上使用渲染管线运行绘制命令，渲染一个彩色、旋转的 2D 三角形。
- [选择用于图形渲染的设备对象](selecting-device-objects-for-graphics-rendering.md) —— 在多个 GPU 之间动态切换，以高效渲染到显示器。
- [自定义渲染 pass 设置](customizing-render-pass-setup.md) —— 通过创建自定义渲染 pass，渲染到离屏纹理。
- [创建自定义 Metal 视图](creating-a-custom-metal-view.md) —— 实现一个轻量级视图，用于 Metal 渲染，并根据你的 App 需求进行定制。
- [使用深度测试计算图元可见性](calculating-primitive-visibility-using-depth-testing.md) —— 通过使用深度纹理确定场景中哪些像素可见。
- [在 CPU 上编码间接命令缓冲区](encoding-indirect-command-buffers-on-the-cpu.md) —— 通过重用命令来减少 CPU 开销并简化命令执行。
- [使用图像块实现无序独立透明度](implementing-order-independent-transparency-with-image-blocks.md) —— 使用 tile 着色器和图像块，以任意顺序绘制重叠的透明表面。
- [使用 Metal 快速资源加载来加载纹理和模型](loading-textures-and-models-using-metal-fast-resource-loading.md) —— 使用快速资源加载，将纹理和缓冲区数据直接从磁盘流式传输到 Metal 资源中。
- [使用 Metal 网格着色器调整细节级别](adjusting-the-level-of-detail-using-metal-mesh-shaders.md) —— 使用对象和网格着色器选择并渲染具有多个细节级别的网格。
- [使用 Hydra 渲染创建 3D 应用程序](creating-a-3d-application-with-hydra-rendering.md) —— 构建一个与 Hydra 和 USD 集成的 3D 应用程序。
- [使用可见性结果缓冲区剔除遮挡几何体](culling-occluded-geometry-using-the-visibility-result-buffer.md) —— 通过检查场景中每个对象是否可见，绘制场景而不渲染隐藏的几何体。
- [使用多重采样抗锯齿 (MSAA) 提高边缘渲染质量](improving-edge-rendering-quality-with-multisample-antialiasing-msaa.md) —— 应用 MSAA 通过自定义解析选项以及即时和基于 tile 的解析路径来增强边缘渲染。

## 下载

- [AchievingSmoothFrameRatesWithMetalsDisplayLink.zip](https://docs-assets.developer.apple.com/published/37aa0e2a751f/AchievingSmoothFrameRatesWithMetalsDisplayLink.zip)
