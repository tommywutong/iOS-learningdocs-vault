---
title: 自定义布局
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/custom-layout
source_url: 'https://developer.apple.com/documentation/swiftui/custom-layout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/custom-layout.json'
content_hash: 'sha256:ea49ab74d42dc29a'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 自定义布局

<sub>API 集合</sub>

以自定排列方式放置视图，并在布局类型之间创建动画过渡。

## 概述

你可以使用 SwiftUI 提供的内置布局容器和布局视图修饰符创建复杂的视图布局。但是，如果你需要内置布局工具无法实现的行为，可以使用 [Layout](layout.md) 协议创建自定布局容器类型。你定义的容器会询问其所有子视图的大小，然后指示在自身边界内的什么位置放置这些子视图。

![](../../../attachments/098af88e7ef1601f537924b942ecfb67/custom-layout-hero@2x.png)

你还可以在符合 [Layout](layout.md) 协议的布局类型之间创建动画过渡，包括内置布局和自定布局。

有关设计指引，请参阅《人机界面指南》中的 [Layout](../design/human-interface-guidelines/layout.md)。

## 主题

### 创建自定布局容器

- [Composing custom layouts with SwiftUI](composing-custom-layouts-with-swiftui.md) — 使用 SwiftUI 提供的布局工具在 App 界面中排列视图。
- [Layout](layout.md) — 一种定义一组视图几何属性的类型。
- [LayoutSubview](layoutsubview.md) — 表示布局中某个子视图的代理。
- [LayoutSubviews](layoutsubviews.md) — 表示布局视图的子视图的一组代理值的集合。

### 配置自定布局

- [LayoutProperties](layoutproperties.md) — 布局容器的布局专属属性。
- [ProposedViewSize](proposedviewsize.md) — 对视图大小的一个提议。
- [ViewSpacing](viewspacing.md) — 视图的几何间距偏好集合。

### 在自定布局中将值与视图关联

- [layoutValue(key:value:)](<view/layoutvalue(key_value_).md>) — 将一个值与自定义布局属性关联起来。
- [LayoutValueKey](layoutvaluekey.md) — 用于访问布局容器子视图布局值的键。

### 在布局类型之间过渡

- [AnyLayout](anylayout.md) — Layout 协议的一个类型擦除实例。
- [HStackLayout](hstacklayout.md) — 一种可在条件布局中使用的水平容器。
- [VStackLayout](vstacklayout.md) — 一种可在条件布局中使用的垂直容器。
- [ZStackLayout](zstacklayout.md) — 一种可在条件布局中使用的叠层容器。
- [GridLayout](gridlayout.md) — 一种可在条件布局中使用的网格。

## 另请参阅

### 视图布局

- [Layout fundamentals](layout-fundamentals.md) — 在内置布局容器（如叠放和网格）内排列视图。
- [Layout adjustments](layout-adjustments.md) — 微调对齐、间距、内边距 (padding) 和其他布局参数。
- [Lists](lists.md) — 显示一个结构化的、可滚动的信息列。
- [Tables](tables.md) — 显示按行和列排列的可选择、可排序的数据。
- [View groupings](view-groupings.md) — 在不同类型的专用容器中呈现视图，例如表单或控制组。
- [Scroll views](scroll-views.md) — 让人们能够滚动查看不适合当前显示的内容。
