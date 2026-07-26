---
title: 使用瓦片着色器以前向+光照渲染场景
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 26.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/rendering-a-scene-with-forward-plus-lighting-using-tile-shaders
source_url: 'https://developer.apple.com/documentation/metal/rendering-a-scene-with-forward-plus-lighting-using-tile-shaders'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/rendering-a-scene-with-forward-plus-lighting-using-tile-shaders.json'
content_hash: 'sha256:39645ca0220eac42'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Metal sample code library](metal-sample-code-library.md)

# 使用瓦片着色器以前向+光照渲染场景

<sub>示例代码</sub>

使用 Apple GPU 上的最新特性实现一个前向+渲染器。

## 概述

> [!note] 注意
> 本示例代码项目与 WWDC 2019 场次 [601: Modern Rendering with Metal](https://developer.apple.com/videos/play/wwdc19/601/) 相关联。

### 配置示例代码项目

要运行此 App：

- 使用 Xcode 11 或更高版本构建该项目。
- 面向搭载 A11 或更新芯片、运行 iOS 11 或更高版本的 iOS 设备。

## 另请参阅

### 光照技术

- [Rendering a scene with deferred lighting in Objective-C](rendering-a-scene-with-deferred-lighting-in-objective-c.md) — 通过实现一个针对即时模式渲染器和基于瓦片的延迟渲染器 GPU 进行优化的延迟光照渲染器，避免昂贵的光照计算。
- [Rendering a scene with deferred lighting in Swift](rendering-a-scene-with-deferred-lighting-in-swift.md) — 通过实现一个针对即时模式渲染器和基于瓦片的延迟渲染器 GPU 进行优化的延迟光照渲染器，避免昂贵的光照计算。
- [Rendering a scene with deferred lighting in C++](rendering-a-scene-with-deferred-lighting-in-c++.md) — 通过实现一个针对即时模式渲染器和基于瓦片的延迟渲染器 GPU 进行优化的延迟光照渲染器，避免昂贵的光照计算。
- [Rendering reflections with fewer render passes](rendering-reflections-with-fewer-render-passes.md) — 使用图层选择来减少生成环境贴图所需的渲染通道数量。

## 下载

- [RenderingASceneWithForwardPlusLightingUsingTileShaders.zip](https://docs-assets.developer.apple.com/published/73528988a5ff/RenderingASceneWithForwardPlusLightingUsingTileShaders.zip)
