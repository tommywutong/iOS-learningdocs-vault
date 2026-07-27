---
title: HDR 内容
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/hdr-content
source_url: 'https://developer.apple.com/documentation/metal/hdr-content'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/hdr-content.json'
content_hash: 'sha256:aa0e0591d1ed7ec8'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md)

# HDR 内容

利用高动态范围技术，在你的 App 和游戏中呈现更鲜艳的色彩。

## 概述

高动态范围（HDR）内容比标清内容具有更宽的亮度范围。某些显示器（macOS 称之为扩展动态范围（EDR）显示器）可以在屏幕上物理再现那些额外的亮度值。你可以使用 Metal 检测 EDR 显示器，并处理 HDR 内容，例如来自视频资源的内容，或直接来自你的 App 的内容。

## 主题

### 高动态范围内容

- [Processing HDR images with Metal](processing-hdr-images-with-metal.md) — 使用 Apple GPU 的最新特性实现一个后处理管线。
- [Displaying HDR content in a Metal layer](displaying-hdr-content-in-a-metal-layer.md) — 将你的高动态范围（HDR）内容呈现到兼容的 Mac 显示器上。
- [Determining support for EDR values](determining-support-for-edr-values.md) — 检查某个显示器是否支持 EDR。
- [Using color spaces to display HDR content](using-color-spaces-to-display-hdr-content.md) — 当你不需要编辑或处理像素数据时，使用色彩空间。
- [Using system tone mapping on video content](using-system-tone-mapping-on-video-content.md) — 使用 EDR 元数据将系统默认色调映射应用于某个层。
- [Performing your own tone mapping](performing-your-own-tone-mapping.md) — 应用你自己的色调映射以获得你想要的确切效果。
- [Implementing tone mapping on reference displays](implementing-tone-mapping-on-reference-displays.md) — 检测参考显示器，并将你的内容保持在显示硬件能力范围之内。

## 另请参阅

### 呈现

- [Managing your game window for Metal in macOS](managing-your-game-window-for-metal-in-macos.md) — 设置一个窗口和视图，以最佳方式显示你的 Metal 内容。
- [Managing your Metal app window in iPadOS](managing-your-metal-app-window-in-ipados.md) — 设置一个能够动态调整你的 Metal 内容大小的窗口。
- [Adapting your game interface for smaller screens](adapting-your-game-interface-for-smaller-screens.md) — 让文本在玩家选择运行你游戏的所有设备上都清晰可读。
- [Onscreen presentation](onscreen-presentation.md) — 在你的 App 中向用户展示 GPU 渲染流程的输出。
