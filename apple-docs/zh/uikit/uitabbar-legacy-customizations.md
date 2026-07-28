---
title: 旧版自定义
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar-legacy-customizations
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar-legacy-customizations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar-legacy-customizations.json'
content_hash: 'sha256:0ad76e5cc11d1f93'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [视图控制器](view-controllers.md) · [UITabBar](uitabbar.md)

# 旧版自定义

<sub>API 集合</sub>

直接在标签页栏对象上自定义外观信息。

## 概述

在 iOS 13 及更高版本中，使用 [standardAppearance](uitabbar/standardappearance.md) 属性来自定义你的标签页栏。你也可以继续使用这些旧版存取方法来直接自定义标签页栏的外观。

## 主题

### 设置栏的样式

- [barStyle](uitabbar/barstyle.md) — 指定标签页栏外观的标签页栏样式。
- [UIBarStyle](uibarstyle.md) — 定义不同类型视图的样式外观。

### 配置标签页栏项

- [tintColor](uitabbar/tintcolor.md) — 应用于标签页栏项的色调颜色。

### 自定义项间距

- [itemPositioning](uitabbar/itempositioning-swift.property.md) — 标签页栏中各项的定位方案。
- [ItemPositioning](uitabbar/itempositioning-swift.enum.md) — 指定标签页栏项定位方式的常量。
- [itemSpacing](uitabbar/itemspacing.md) — 标签页栏项之间使用的间距量（以点为单位）。
- [itemWidth](uitabbar/itemwidth.md) — 标签页栏项的宽度（以点为单位）。

### 配置选中状态外观

- [unselectedItemTintColor](uitabbar/unselecteditemtintcolor.md) — 应用于未选中标签页的色调颜色。
- [selectionIndicatorImage](uitabbar/selectionindicatorimage.md) — 用于选中指示符的图像。
- [selectedImageTintColor](uitabbar/selectedimagetintcolor.md) — 应用于选中标签页栏项的色调颜色。 _(已废弃)_

### 更改背景

- [barTintColor](uitabbar/bartintcolor.md) — 应用于标签页栏背景的色调颜色。
- [backgroundImage](uitabbar/backgroundimage.md) — 标签页栏的自定义背景图像。

### 添加阴影

- [shadowImage](uitabbar/shadowimage.md) — 用于标签页栏的阴影图像。

## 另请参阅

### 自定义标签页栏外观

- [standardAppearance](uitabbar/standardappearance.md) — 标准高度标签页栏的外观设置。
- [scrollEdgeAppearance](uitabbar/scrolledgeappearance.md) — 当可滚动内容的边缘与标签页栏的边缘对齐时，标签页栏的外观设置。
- [leadingAccessoryView](uitabbar/leadingaccessoryview.md) — tvOS 上位于标签页栏前缘的视图。
- [trailingAccessoryView](uitabbar/trailingaccessoryview.md) — tvOS 上位于标签页栏后缘的视图。
- [translucent](uitabbar/istranslucent.md) — 一个布尔值，表示标签页栏是否为半透明。
