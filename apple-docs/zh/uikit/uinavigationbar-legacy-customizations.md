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
doc_path: /documentation/uikit/uinavigationbar-legacy-customizations
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar-legacy-customizations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar-legacy-customizations.json'
content_hash: 'sha256:d23a7bc380d726f9'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [UINavigationBar](uinavigationbar.md)

# 旧版自定义

<sub>API 集合</sub>

直接在导航栏对象上自定义外观信息。

## 概述

在 iOS 13 及更高版本中，使用 [standardAppearance](uinavigationbar/standardappearance.md)、[compactAppearance](uinavigationbar/compactappearance.md) 和 [scrollEdgeAppearance](uinavigationbar/scrolledgeappearance.md) 属性来自定义你的导航栏。你可以继续使用这些旧版存取方法（accessor）来直接自定义导航栏的外观，但必须自行为不同的栏配置更新外观。

## 主题

### 配置导航栏

- [Customizing your app’s navigation bar](customizing-your-app-s-navigation-bar.md) — 在你的 App 的导航栏中创建自定义标题、提示和按钮。

### 设置栏的样式

- [barStyle](uinavigationbar/barstyle.md) — 指定导航栏外观的导航栏样式。
- [UIBarStyle](uibarstyle.md) — 定义不同类型视图的样式外观。

### 配置标题

- [titleTextAttributes](uinavigationbar/titletextattributes.md) — 栏标题文本的显示特性。
- [largeTitleTextAttributes](uinavigationbar/largetitletextattributes.md) — 栏大标题文本的显示特性。
- [- titleVerticalPositionAdjustmentForBarMetrics:](<uinavigationbar/titleverticalpositionadjustment(for_).md>) — 返回给定栏度量（bar metrics）下标题的垂直位置调整量。
- [- setTitleVerticalPositionAdjustment:forBarMetrics:](<uinavigationbar/settitleverticalpositionadjustment(__for_).md>) — 设置给定栏度量下标题的垂直位置调整量。

### 配置栏按钮条目

- [tintColor](uinavigationbar/tintcolor.md) — 应用于导航条目和栏按钮条目的色调颜色（tint color）。

### 配置返回按钮

- [backIndicatorImage](uinavigationbar/backindicatorimage.md) — 显示在返回按钮旁边的图像。
- [backIndicatorTransitionMaskImage](uinavigationbar/backindicatortransitionmaskimage.md) — 在推入和弹出过渡（push and pop transitions）期间用作内容遮罩（mask）的图像。

### 更改背景

- [barTintColor](uinavigationbar/bartintcolor.md) — 应用于导航栏背景的色调颜色。
- [- backgroundImageForBarMetrics:](<uinavigationbar/backgroundimage(for_).md>) — 返回给定栏度量下的背景图像。
- [- setBackgroundImage:forBarMetrics:](<uinavigationbar/setbackgroundimage(__for_).md>) — 设置给定栏度量下的背景图像。
- [- backgroundImageForBarPosition:barMetrics:](<uinavigationbar/backgroundimage(for_barmetrics_).md>) — 返回在给定栏位置和一组度量下使用的背景图像。
- [- setBackgroundImage:forBarPosition:barMetrics:](<uinavigationbar/setbackgroundimage(__for_barmetrics_).md>) — 设置在给定栏位置和一组度量下使用的背景图像。

### 添加阴影

- [shadowImage](uinavigationbar/shadowimage.md) — 用于导航栏的阴影图像。

## 另请参阅

### 自定义栏的外观

- [prefersLargeTitles](uinavigationbar/preferslargetitles.md) — 一个布尔值，表示标题是否以大号格式显示。
- [standardAppearance](uinavigationbar/standardappearance.md) — 标准高度导航栏的外观设置。
- [compactAppearance](uinavigationbar/compactappearance.md) — 紧凑高度导航栏的外观设置。
- [scrollEdgeAppearance](uinavigationbar/scrolledgeappearance.md) — 当可滚动内容的边缘与导航栏的边缘对齐时，导航栏的外观设置。
- [compactScrollEdgeAppearance](uinavigationbar/compactscrolledgeappearance.md) — 当可滚动内容的边缘与导航栏的边缘对齐时，紧凑高度导航栏的外观设置。
- [translucent](uinavigationbar/istranslucent.md) — 一个布尔值，表示导航栏是否为半透明（translucent）。
