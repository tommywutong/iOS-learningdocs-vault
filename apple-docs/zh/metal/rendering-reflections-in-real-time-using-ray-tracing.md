---
title: 使用光线追踪实时渲染反射
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 26.3+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/rendering-reflections-in-real-time-using-ray-tracing
source_url: 'https://developer.apple.com/documentation/metal/rendering-reflections-in-real-time-using-ray-tracing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/rendering-reflections-in-real-time-using-ray-tracing.json'
content_hash: 'sha256:006e82b809d34a78'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Metal sample code library](metal-sample-code-library.md)

# 使用光线追踪实时渲染反射

<sub>示例代码</sub>

通过编码光线追踪计算流程动态生成反射贴图，实现逼真的实时光照效果。

## 概述

该示例代码项目与多个 WWDC 场次相关，包括：

- [10089: Bring your advanced games to Apple platforms](https://developer.apple.com/wwdc24/10089/)
- [10101: Go bindless with Metal 3](https://developer.apple.com/wwdc22/10101/)
- [10286: Explore bindless rendering in Metal](https://developer.apple.com/wwdc21/10286/)
- [10150: Explore hybrid rendering with Metal ray tracing](https://developer.apple.com/wwdc21/10150/)

### 配置示例代码项目

要运行此示例 App，你需要：

- 一台运行 macOS 13 或更高版本、Xcode 15.3 或更高版本的 Mac
- 一台运行 iOS 16 或更高版本的 iOS 设备

> [!note] 注意
> 该示例不支持在模拟器中运行。

## 另请参阅

### 光线追踪

- [Accelerating ray tracing using Metal](accelerating-ray-tracing-using-metal.md) — 使用基于 GPU 的并行处理实现光线追踪渲染。
- [Control the ray tracing process using intersection queries](control-the-ray-tracing-process-using-intersection-queries.md) — 通过创建相交查询对象，显式枚举光线与加速结构的相交点。
- [Accelerating ray tracing and motion blur using Metal](accelerating-ray-tracing-and-motion-blur-using-metal.md) — 使用基于 GPU 的并行处理生成带运动模糊的光线追踪图像。
- [Rendering a curve primitive in a ray tracing scene](rendering-a-curve-primitive-in-a-ray-tracing-scene.md) — 使用基于 GPU 的并行处理实现光线追踪渲染。

## 下载

- [RenderingReflectionsInRealTimeUsingRayTracing.zip](https://docs-assets.developer.apple.com/published/695c551a3aa3/RenderingReflectionsInRealTimeUsingRayTracing.zip)
