---
title: 外观自定义
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/appearance-customization
source_url: 'https://developer.apple.com/documentation/uikit/appearance-customization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/appearance-customization.json'
content_hash: 'sha256:b0575097b429da6d'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md)

# 外观自定义

<sub>API 集合</sub>

将 Liquid Glass 应用于视图，在 App 中支持深色模式（Dark Mode），自定义栏的外观，并使用外观代理（appearance proxy）修改 UI。

## 主题

### Liquid Glass 效果

- [UIGlassEffect](uiglasseffect.md) — 一种渲染玻璃材质的视觉效果。
- [UIGlassContainerEffect](uiglasscontainereffect.md) — `UIGlassContainerEffect` 将多个玻璃元素渲染为一个组合效果。

### 与相邻视图交互

- [UIBackgroundExtensionView](uibackgroundextensionview.md) — 一个扩展内容以填充自身边界的视图。
- [UIScrollEdgeElementContainerInteraction](uiscrolledgeelementcontainerinteraction.md) — 将此交互添加到覆盖在滚动视图边缘上的视图所处的容器视图。此视图中所有应影响边缘效果形状的后代元素（例如标签、图像、玻璃视图和控制）都会自动产生相应影响。

### 深色模式

- [在界面中支持深色模式](supporting-dark-mode-in-your-interface.md) — 更新颜色、图像和行为，使 App 在深色模式启用时自动适配。
- [采用 iOS 深色模式](adopting-ios-dark-mode.md) — 使用动态颜色和视觉效果，在你的 iOS App 中采用深色模式。

### 外观与内容

- [配置](configurations.md) — 使用配置指定视图和单元格的外观与内容。

### 导航栏外观

- [UINavigationBarAppearance](uinavigationbarappearance.md) — 一个用于自定义导航栏外观的对象。

### 工具栏外观

- [UIToolbarAppearance](uitoolbarappearance.md) — 一个用于自定义工具栏外观的对象。

### 标签页栏外观

- [UITabBarAppearance](uitabbarappearance.md) — 一个用于自定义标签页栏外观的对象。
- [UITabBarItemAppearance](uitabbaritemappearance.md) — 一个用于自定义标签页栏项目外观的对象。
- [UITabBarItemStateAppearance](uitabbaritemstateappearance.md) — 一个数据对象，包含特定状态下标签页栏项目的具体自定义设置。

### 共享外观

- [UIBarAppearance](uibarappearance.md) — 一个用于自定义系统栏基本外观的对象。
- [UIBarButtonItemAppearance](uibarbuttonitemappearance.md) — 一个用于自定义栏按钮项目外观的对象。
- [UIBarButtonItemStateAppearance](uibarbuttonitemstateappearance.md) — 一个数据对象，包含特定状态下栏按钮项目的具体自定义设置。

### 外观代理

- [UIAppearance](uiappearance.md) — 一组方法，让你能够访问某个类的外观代理。
- [UIAppearanceContainer](uiappearancecontainer.md) — 一个类为允许使用 [UIAppearance](uiappearance.md) API 进行外观自定义而必须采用的协议。

## 另请参阅

### 用户界面

- [视图与控制](views-and-controls.md) — 在屏幕上呈现内容，并定义允许与这些内容进行的交互。
- [视图控制器](view-controllers.md) — 使用视图控制器（view controller）管理界面，并帮助用户在 App 内容中导览。
- [视图布局](view-layout.md) — 使用叠放视图来自动布置界面中的视图。需要精确放置视图时，请使用 Auto Layout。
- [动画与触感反馈](animation-and-haptics.md) — 使用基于视图的动画和触感反馈（haptics）向用户提供反馈。
- [窗口与屏幕](windows-and-screens.md) — 为视图层级结构（view hierarchy）和其他内容提供容器。
