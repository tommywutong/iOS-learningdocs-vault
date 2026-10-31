---
title: 性能分析
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/performance-analysis
source_url: 'https://developer.apple.com/documentation/swiftui/performance-analysis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/performance-analysis.json'
content_hash: 'sha256:e679589474c0026b'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 性能分析

测量并改进你的 App 的响应能力。

## 概述

使用 Instruments 来检测你的 App 中的挂起和卡顿，并分析可能导致挂起和卡顿的长时间视图 body 更新以及频繁发生的 SwiftUI 更新。

## 主题

### 基础

- [理解用户界面响应能力](../xcode/understanding-user-interface-responsiveness.md) — 通过检查事件处理和渲染循环，让你的 App 更具响应能力。
- [理解你的 App 中的挂起](../xcode/understanding-hangs-in-your-app.md) — 通过检查主线程和主运行循环，确定用户交互延迟的原因。
- [理解你的 App 中的卡顿](../xcode/understanding-hitches-in-your-app.md) — 通过检查渲染循环，确定运动中断的原因。

### 分析 SwiftUI 性能

- [理解并改进 SwiftUI 性能](../xcode/understanding-and-improving-swiftui-performance.md) — 识别并解决长时间运行的视图更新，并降低更新的频率。

## 另请参阅

### 工具支持

- [Xcode 中的预览](previews-in-xcode.md) — 为你的自定义视图生成动态、可交互的预览。
- [Xcode 资源库自定](xcode-library-customization.md) — 在 Xcode 资源库中公开自定义视图和修饰符。
