---
title: 图像
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/images
source_url: 'https://developer.apple.com/documentation/swiftui/images'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/images.json'
content_hash: 'sha256:11783d2a6c782ec8'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 图像

<sub>API 集合</sub>

向 App 的用户界面添加图像和符号。

## 概述

使用 [Image](image.md) 视图显示图像，包括 [SF Symbols](../design/human-interface-guidelines/sf-symbols.md)、存储在资源目录中的图像以及存储在磁盘上的图像。

![](../../../attachments/4fb32811fff960a104407b1f3b81a0f0/images-hero@2x.png)

对于需要较长时间获取的图像——例如从网络端点加载图像时——请使用 [AsyncImage](asyncimage.md) 异步加载图像。你可以指示该视图在加载操作期间显示占位符。

有关设计指引，请参阅《人机界面指南》中的 [Images](../design/human-interface-guidelines/images.md)。

## 主题

### 创建图像

- [Image](image.md) — 一个显示图像的视图。

### 配置图像

- [Fitting images into available space](fitting-images-into-available-space.md) — 通过应用视图修饰符来调整 App 用户界面中图像的大小和形状。
- [imageScale(_:)](<view/imagescale(__).md>) — 根据可用的相对尺寸（包括小、中、大图像尺寸）缩放视图内的图像。
- [imageScale](environmentvalues/imagescale.md) — 此环境的图像缩放比例。
- [Scale](image/scale.md) — 相对于文本应用于矢量图像的缩放比例。
- [Orientation](image/orientation.md) — 图像的方向。
- [ResizingMode](image/resizingmode.md) — SwiftUI 用来调整图像大小以适配其包含视图的各种模式。

### 异步加载图像

- [AsyncImage](asyncimage.md) — 一个异步加载并显示图像的视图。
- [AsyncImagePhase](asyncimagephase.md) — 异步图像加载操作的当前阶段。

### 设置符号变体

- [symbolVariant(_:)](<view/symbolvariant(__).md>) — 让视图内的符号显示特定的变体。
- [symbolVariants](environmentvalues/symbolvariants.md) — 此环境中要使用的符号变体。
- [SymbolVariants](symbolvariants.md) — 符号的一种变体。

### 管理符号效果

- [symbolEffect(_:options:isActive:)](<view/symboleffect(__options_isactive_).md>) — 返回一个添加了符号效果的新视图。
- [symbolEffect(_:options:value:)](<view/symboleffect(__options_value_).md>) — 返回一个添加了符号效果的新视图。
- [symbolEffectsRemoved(_:)](<view/symboleffectsremoved(__).md>) — 返回一个新视图，其继承的符号图像效果被移除或保持不变。
- [SymbolEffectTransition](symboleffecttransition.md) — 创建一种过渡，对插入或移除的视图层级结构中的符号图像应用 Appear、Disappear、DrawOn 或 DrawOff 符号动画。

### 设置符号渲染模式

- [symbolRenderingMode(_:)](<view/symbolrenderingmode(__).md>) — 设置此视图内符号图像的渲染模式。
- [symbolRenderingMode](environmentvalues/symbolrenderingmode.md) — 当前的符号渲染模式；为 `nil` 表示以当前图像和前景样式为参数自动选择模式。
- [SymbolRenderingMode](symbolrenderingmode.md) — 一种符号渲染模式。
- [SymbolColorRenderingMode](symbolcolorrenderingmode.md) — 填充符号图像中图层的一种方法。
- [SymbolVariableValueMode](symbolvariablevaluemode.md) — 渲染符号图像变量值的一种方法。

### 从视图渲染图像

- [ImageRenderer](imagerenderer.md) — 一个从 SwiftUI 视图创建图像的对象。

## 另请参阅

### Views

- [View fundamentals](view-fundamentals.md) — 使用视图层级结构定义 App 的视觉元素。
- [View configuration](view-configuration.md) — 调整层级结构中视图的特性。
- [View styles](view-styles.md) — 为不同类型的视图应用内置和自定义的外观与行为。
- [Animations](animations.md) — 创建流畅的视觉更新以响应状态变化。
- [Text input and output](text-input-and-output.md) — 显示格式化的文本并获取用户的文本输入。
- [Controls and indicators](controls-and-indicators.md) — 显示值并获取用户的选择。
- [Menus and commands](menus-and-commands.md) — 以节省空间、依赖上下文的方式提供对命令和控制的访问。
- [Shapes](shapes.md) — 用颜色、渐变或其他图案描边和填充内置及自定形状。
- [Drawing and graphics](drawing-and-graphics.md) — 用图形效果和自定义绘图增强你的视图。
