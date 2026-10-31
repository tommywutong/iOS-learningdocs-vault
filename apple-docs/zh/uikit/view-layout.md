---
title: 视图布局
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/view-layout
source_url: 'https://developer.apple.com/documentation/uikit/view-layout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/view-layout.json'
content_hash: 'sha256:31db0f3a85b3678b'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md)

# 视图布局

<sub>API 集合</sub>

使用叠放视图自动布局界面的视图。需要精确放置视图时使用 Auto Layout。

## 概述

在设计 App 界面时，你把视图和其他界面元素放置在 App 的窗口中，并为其设置合适的大小。然而，这些视图的大小和位置可能需要在运行时因各种原因而改变：

- 用户可以调整包含视图的窗口大小。
- iOS 设备屏幕尺寸的差异（包括竖屏与横屏方向的不同）要求为每种设备和方向提供不同的布局。
- iPad 上的 App 必须适应不同的屏幕空间大小，从三分之一屏幕到整个屏幕不等。
- 语言更改可能需要更改标签和其他基于文本的视图的大小。
- 动态字体允许更改文本大小，从而影响视图的大小。

[UIStackView](uistackview.md) 对象在界面尺寸变化时自动调整其包含视图的位置。或者，Auto Layout 约束允许你指定决定界面视图大小和位置的规则。

## 主题

### 基础

- [UIStackView](uistackview.md) — 用于在列或行中布局一组视图的简化界面。

### 本地化

- [Autosizing views for localization in iOS](../xcode/autosizing-views-for-localization-in-ios.md) — 为 App 添加自动布局约束以实现可本地化的视图。

### 约束

- [Positioning content within layout margins](positioning-content-within-layout-margins.md) — 定位视图，使其不被其他内容拥挤。
- [Positioning content relative to the safe area](positioning-content-relative-to-the-safe-area.md) — 定位视图，使其不被其他内容遮挡。
- [NSLayoutConstraint](nslayoutconstraint.md) — 必须由基于约束的布局系统满足的两个用户界面对象之间的关系。
- [UILayoutSupport](uilayoutsupport.md) — 提供布局支持和访问布局锚点的一组方法。

### 布局指南

- [UILayoutGuide](uilayoutguide.md) — 可与 Auto Layout 交互的矩形区域。
- [NSLayoutDimension](nslayoutdimension.md) — 使用流畅 API 创建基于大小的布局约束对象的工厂类。

### 锚点

- [NSLayoutAnchor](nslayoutanchor.md) — 使用流畅 API 创建布局约束对象的工厂类。
- [NSLayoutXAxisAnchor](nslayoutxaxisanchor.md) — 使用流畅 API 创建水平布局约束对象的工厂类。
- [NSLayoutYAxisAnchor](nslayoutyaxisanchor.md) — 使用流畅 API 创建垂直布局约束对象的工厂类。
- [NSLAYOUTANCHOR_H](nslayoutanchor_h.md)

## 另请参阅

### 用户界面

- [视图与控制](views-and-controls.md) — 在屏幕上呈现内容并定义与该内容允许的交互。
- [视图控制器](view-controllers.md) — 使用视图控制器管理界面，并在 App 内容间进行导览。
- [外观自定](appearance-customization.md) — 为视图应用 Liquid Glass，支持 App 中的深色模式，自定栏的外观，并使用外观代理修改 UI。
- [动画与触感反馈](animation-and-haptics.md) — 使用基于视图的动画和触感反馈向用户传递反馈。
- [窗口与屏幕](windows-and-screens.md) — 为你的视图层级结构和其他内容提供容器。
