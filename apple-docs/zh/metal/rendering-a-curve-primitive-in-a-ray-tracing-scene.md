---
title: 在光线追踪场景中渲染曲线图元
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 26.3+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/rendering-a-curve-primitive-in-a-ray-tracing-scene
source_url: 'https://developer.apple.com/documentation/metal/rendering-a-curve-primitive-in-a-ray-tracing-scene'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/rendering-a-curve-primitive-in-a-ray-tracing-scene.json'
content_hash: 'sha256:494f082b06ad5a68'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Metal sample code library](metal-sample-code-library.md)

# 在光线追踪场景中渲染曲线图元

<sub>示例代码</sub>

使用基于 GPU 的并行处理实现光线追踪渲染。

## 概述

> [!note] 注意
> 该示例代码项目与 WWDC23 场次 [10128: Your guide to Metal ray tracing](https://developer.apple.com/wwdc23/10128) 相关。

### 配置示例代码项目

该示例需要以下系统和软件配置：

- macOS 14 或更高版本
- iOS 17 或更高版本
- Xcode 15 或更高版本

## 另请参阅

### 光线追踪

- [Rendering reflections in real time using ray tracing](rendering-reflections-in-real-time-using-ray-tracing.md) — 通过编码光线追踪计算流程动态生成反射贴图，实现逼真的实时光照效果。
- [Accelerating ray tracing using Metal](accelerating-ray-tracing-using-metal.md) — 使用基于 GPU 的并行处理实现光线追踪渲染。
- [Control the ray tracing process using intersection queries](control-the-ray-tracing-process-using-intersection-queries.md) — 通过创建相交查询对象，显式枚举光线与加速结构的相交点。
- [Accelerating ray tracing and motion blur using Metal](accelerating-ray-tracing-and-motion-blur-using-metal.md) — 使用基于 GPU 的并行处理生成带运动模糊的光线追踪图像。

## 下载

- [RenderingACurvePrimitiveInARayTracingScene.zip](https://docs-assets.developer.apple.com/published/8df3074149f0/RenderingACurvePrimitiveInARayTracingScene.zip)
