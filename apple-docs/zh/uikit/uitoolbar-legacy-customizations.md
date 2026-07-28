---
title: 旧版自定义
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitoolbar-legacy-customizations
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar-legacy-customizations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar-legacy-customizations.json'
content_hash: 'sha256:84f353219f4447dd'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图与控制](views-and-controls.md) · [UIToolbar](uitoolbar.md)

# 旧版自定义

<sub>API 集合</sub>

直接在工具栏对象上自定义外观信息。

## 概述

在 iOS 13 及更高版本中，使用 [standardAppearance](uitoolbar/standardappearance.md) 和 [compactAppearance](uitoolbar/compactappearance.md) 属性来自定义你的工具栏。你可以继续使用这些旧版存取方法来直接自定义工具栏的外观，但必须自行为不同的栏配置更新外观。

## 主题

### 设置栏的样式

- [barStyle](uitoolbar/barstyle.md) — 指定工具栏外观的工具栏样式。
- [UIBarStyle](uibarstyle.md) — 定义不同类型视图的样式外观。

### 配置栏按钮条目

- [tintColor](uitoolbar/tintcolor.md) — 应用于栏按钮条目的色调颜色。

### 更改背景

- [barTintColor](uitoolbar/bartintcolor.md) — 应用于工具栏背景的色调颜色。
- [- backgroundImageForToolbarPosition:barMetrics:](<uitoolbar/backgroundimage(fortoolbarposition_barmetrics_).md>) — 返回在给定位置和给定度量下用于背景的图像。
- [- setBackgroundImage:forToolbarPosition:barMetrics:](<uitoolbar/setbackgroundimage(__fortoolbarposition_barmetrics_).md>) — 设置在给定位置和给定度量下用于背景的图像。

### 添加阴影

- [- shadowImageForToolbarPosition:](<uitoolbar/shadowimage(fortoolbarposition_).md>) — 返回在给定位置用于工具栏阴影的图像。
- [- setShadowImage:forToolbarPosition:](<uitoolbar/setshadowimage(__fortoolbarposition_).md>) — 设置在给定位置用于工具栏阴影的图像。

## 另请参阅

### 自定义外观

- [standardAppearance](uitoolbar/standardappearance.md) — 标准高度工具栏使用的外观设置。
- [compactAppearance](uitoolbar/compactappearance.md) — 紧凑高度工具栏使用的外观设置。
- [scrollEdgeAppearance](uitoolbar/scrolledgeappearance.md) — 当可滚动内容的边缘与工具栏的边缘对齐时，标准高度工具栏的外观设置。
- [compactScrollEdgeAppearance](uitoolbar/compactscrolledgeappearance.md) — 当任何可滚动内容的边缘与紧凑高度工具栏的边缘对齐时，紧凑高度工具栏的外观设置。
- [translucent](uitoolbar/istranslucent.md) — 一个布尔值，表示工具栏是否为半透明。
