---
title: 资源管理
framework: xcode
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/asset-management
source_url: 'https://developer.apple.com/documentation/xcode/asset-management'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/asset-management.json'
content_hash: 'sha256:52f265b2a43663a0'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md)

# 资源管理

向项目添加 App 图标、图像、字符串、数据文件、机器学习模型和其他资源，并管理运行时加载它们的方式。

## 概述

App 依靠多种类型的资源来营造丰富、动态且极具视觉吸引力的用户体验。Xcode 提供了工具和设置，帮助你添加、整理和优化 App 使用的不同资源类型。

Xcode 通过资源目录简化了大多数类型资源的管理。使用*资源目录（asset catalog）*来整理和管理图像、颜色、App 图标、纹理、贴纸和数据等资源。

![](../../../attachments/510957b38e01629af8d00419934db5ea/asset-management-1@2x.png)

<sub>三个表示资源目录中常见资源类型的图标。从左到右依次是标有 images 的图像叠放图标、标有 colors 的颜色选择器（picker）图标，以及标有 data 的 CSV 图标。</sub>

Xcode 还为粒子效果等特定类型的资源提供交互式编辑器，让你可以试验、进行更改并立即查看结果。

## 主题

### App 图标与启动屏幕

- [使用 Icon Composer 创建 App 图标](creating-your-app-icon-using-icon-composer.md) — 使用 Icon Composer 为不同平台和外观设计 App 图标的样式。
- [配置 App 以使用备用 App 图标](configuring-your-app-to-use-alternate-app-icons.md) — 向 App 添加备用 App 图标，并让用户选择要显示的图标。
- [使用资源目录配置 App 图标](configuring-your-app-icon.md) — 向资源目录添加 App 图标变体，用于在 App Store、主屏幕、设置和搜索结果等位置表示 App。
- [指定 App 的启动屏幕](specifying-your-apps-launch-screen.md) — 通过自定义启动屏幕，让 iOS App 的启动体验更快、响应更灵敏。

### 资源目录

- [使用资源目录管理资源](managing-assets-with-asset-catalogs.md) — 使用资源目录在 Xcode 项目中添加、整理和编辑资源集。

### 图像

- [向 Xcode 项目添加图像](adding-images-to-your-xcode-project.md) — 将图像导入项目，管理其外观和变体，并在运行时加载。
- [为 App 创建自定义符号图像](../uikit/creating-custom-symbol-images-for-your-app.md) — 使用 SF Symbols 创建、整理和标注符号图像。

### 颜色

- [指定 App 的配色方案](specifying-your-apps-color-scheme.md) — 使用资源目录为 App 设置全局强调色。
- [在界面中支持深色模式](../uikit/supporting-dark-mode-in-your-interface.md) — 更新颜色、图像和行为，使 App 在深色模式启用时自动适配。

### 增强现实资源

- [在 AR 体验中检测图像](../arkit/detecting-images-in-an-ar-experience.md) — 响应用户环境中的已知 2D 图像，并使用其位置放置 AR 内容。
- [扫描和检测 3D 对象](../arkit/scanning-and-detecting-3d-objects.md) — 记录现实世界对象的空间特征，然后使用结果在用户环境中查找这些对象并触发 AR 内容。
- [使用 RealityKit 和 Reality Composer Pro 编排交互式 3D 内容](../realitykit/composing-interactive-3d-content-with-realitykit-and-reality-composer-pro.md) — 使用动画时间线构建交互式场景（scene）。

### 机器学习模型

- [Create ML](../createml.md) — 创建供 App 使用的机器学习模型。

### 粒子效果

- [在 Xcode 中创建 SpriteKit 粒子发射器](creating-a-spritekit-particle-emitter-in-xcode.md) — 通过创建可重复的粒子，为 App 添加粒子效果。

## 另请参阅

### 界面

- [本地化](localization.md) — 通过支持多种语言和地区，拓展 App 的市场。
- [Accessibility Inspector](../accessibility/accessibility-inspector.md) — 揭示 App 如何向使用辅助功能的用户呈现自身。
