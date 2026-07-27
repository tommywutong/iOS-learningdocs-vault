---
title: 屏幕呈现
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/onscreen-presentation
source_url: 'https://developer.apple.com/documentation/metal/onscreen-presentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/onscreen-presentation.json'
content_hash: 'sha256:9def4574007a42b3'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md)

# 屏幕呈现

在你的 App 中把 GPU 渲染流程的输出呈现给用户查看。

## 概述

纹理中包含你可能想要在屏幕上显示的视觉数据，比如经过滤镜处理的图像，或者游戏中动画的一帧。要在设备屏幕上显示某个纹理，你需要从 [Core Animation](../quartzcore.md) 创建或获取一个可绘制纹理。

在 Metal 中，_可绘制对象_（drawable）是一种纹理，在 [Core Animation](../quartzcore.md) 内部的显示子系统与 Metal 之间建立桥接。你可以把某个可绘制对象用作渲染流程的输出，然后通过它的 [MTLDrawable](mtldrawable.md) 协议将其呈现到显示器上。

> [!note] 注意
> 你无法直接呈现在 Metal 中创建的纹理，除非你使用 blit 流程（参阅 [Blit passes](blit-passes.md)）把该纹理的内容拷贝到一个可绘制对象中。

要在设备屏幕上显示内容，请在你的 Metal App 中添加以下两者之一：

- 在自定义视图类中包含一个 [CAMetalLayer](../quartzcore/cametallayer.md) 实例
- 一个 [MTKView](../metalkit/mtkview.md) 实例

借助 [CAMetalLayer](../quartzcore/cametallayer.md) 实例，你的 App 可以通过调用其 [nextDrawable()](<../quartzcore/cametallayer/nextdrawable().md>) 方法来获取可绘制对象实例。每个可绘制对象都遵循 [CAMetalDrawable](../quartzcore/cametaldrawable.md) 协议，该协议具有一个 [texture](../quartzcore/cametaldrawable/texture.md) 属性，渲染流程可以将其用作输出。更多信息请参阅[创建自定义 Metal 视图](creating-a-custom-metal-view.md)。

你的 App 也可以改用 [MTKView](../metalkit/mtkview.md) 及其 [currentDrawable](../metalkit/mtkview/currentdrawable.md) 属性。这个 [MetalKit](../metalkit.md) 类提供了一个感知 Metal 的视图的默认实现，其底层使用了一个 [CAMetalLayer](../quartzcore/cametallayer.md) 实例。[MetalKit](../metalkit.md) 视图为呈现 App 的内容提供了一种快捷简便的方式，但相较于直接使用 [CAMetalLayer](../quartzcore/cametallayer.md)，可控性更低。更多信息请参阅[使用 Metal 绘制视图内容](using-metal-to-draw-a-view's-contents.md)。

无论你选择哪种机制，都要密切关注你的 App 如何处理可绘制对象。每个可绘制对象都来自一个有限且可重用的资源池。当你的 App 请求一个可绘制对象时，它并不总是可用的。这种情况发生时，[Core Animation](../quartzcore.md) 会阻塞调用线程，直到某个可绘制对象可用为止——通常是在显示器的下一个刷新间隔。

## 主题

### 使用 Core Animation 进行呈现

- [创建自定义 Metal 视图](creating-a-custom-metal-view.md) — 实现一个根据 App 需求定制的轻量级视图，用于 Metal 渲染。
- [从可绘制纹理中读取像素数据](reading-pixel-data-from-a-drawable-texture.md) — 通过将纹理数据拷贝到缓冲区，从 CPU 访问该数据。
- [借助 Metal 显示链路实现平滑帧率](achieving-smooth-frame-rates-with-a-metal-display-link.md) — 以最小的输入延迟控制渲染节奏，同时为操作系统提供必要信息，以实现节能渲染、热管理，以及对可持续工作负载的调度。
- [CAMetalLayer](../quartzcore/cametallayer.md) — 一个 Metal 可以渲染进去的 Core Animation 图层，通常显示在屏幕上。
- [CAMetalDrawable](../quartzcore/cametaldrawable.md) — 与某个 Core Animation 图层相关联的 Metal 可绘制对象。

### 使用 MetalKit 进行呈现

- [使用 Metal 绘制视图内容](using-metal-to-draw-a-view's-contents.md) — 创建一个 MetalKit 视图和一个渲染流程来绘制该视图的内容。
- [MTKView](../metalkit/mtkview.md) — 一种专门用于创建、配置并显示 Metal 对象的视图。
- [MTKViewDelegate](../metalkit/mtkviewdelegate.md) — 用于响应 MetalKit 视图的绘制与尺寸调整事件的方法。

## 另请参阅

### 呈现

- [在 macOS 中管理你的 Metal 游戏窗口](managing-your-game-window-for-metal-in-macos.md) — 设置一个窗口和视图，以最佳方式显示你的 Metal 内容。
- [在 iPadOS 中管理你的 Metal App 窗口](managing-your-metal-app-window-in-ipados.md) — 设置一个能动态调整你 Metal 内容尺寸的窗口。
- [为更小的屏幕调整你的游戏界面](adapting-your-game-interface-for-smaller-screens.md) — 让文本在玩家选择运行你游戏的所有设备上都清晰可读。
- [HDR content](hdr-content.md) — 利用高动态范围，在你的 App 和游戏中呈现更鲜艳的色彩。
