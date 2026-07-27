---
title: 动画与触感反馈
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/animation-and-haptics
source_url: 'https://developer.apple.com/documentation/uikit/animation-and-haptics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/animation-and-haptics.json'
content_hash: 'sha256:01565e93673f6b23'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md)

# 动画与触感反馈

<sub>API 集合</sub>

使用基于视图的动画和触感反馈（haptics）向用户提供反馈。

## 主题

### 内容动画

- [基于属性的动画](property-based-animations.md) — 通过更改视图的属性来创建动画。
- [视图控制器过渡](view-controller-transitions.md) — 定义从一个视图控制器（view controller）到另一个视图控制器的自定义过渡。
- [统一 App 的动画](../swiftui/unifying-your-app-s-animations.md) — 在 SwiftUI、UIKit 和 AppKit 中打造一致的 UI 动画体验。
- [优化 iPhone 和 iPad App 以支持 ProMotion 显示屏](../quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md) — 通过请求首选刷新率并使动画与系统同步，改善 App 的视觉外观并节省电量。

### 基于物理效果的动画

- [UIKit Dynamics](uikit-dynamics.md) — 将基于物理效果的动画应用到视图。

### 视差效果

- [动态效果](motion-effects.md) — 为视图添加细微的动态效果，以呈现 3D 外观。

### 触感反馈

- [在 App 中播放触感反馈](../applepencil/playing-haptic-feedback-in-your-app.md) — 当用户在 App 中执行特定操作时提供触感反馈。
- [UIFeedbackGenerator](uifeedbackgenerator.md) — 所有反馈生成器的抽象超类（superclass）。
- [UIImpactFeedbackGenerator](uiimpactfeedbackgenerator.md) — 一个具体的反馈生成器子类（subclass），用于创建模拟物理冲击的触感反馈。
- [UINotificationFeedbackGenerator](uinotificationfeedbackgenerator.md) — 一个具体的反馈生成器子类，用于创建传达成功、失败和警告的触感反馈。
- [UISelectionFeedbackGenerator](uiselectionfeedbackgenerator.md) — 一个具体的反馈生成器子类，用于创建表示选择发生变化的触感反馈。
- [UICanvasFeedbackGenerator](uicanvasfeedbackgenerator.md) — 一个具体的反馈生成器子类，用于创建表示绘图画布上所发生事件的触感反馈。

## 另请参阅

### 用户界面

- [视图与控制](views-and-controls.md) — 在屏幕上呈现内容，并定义允许与这些内容进行的交互。
- [视图控制器](view-controllers.md) — 使用视图控制器管理界面，并帮助用户在 App 内容中导览。
- [视图布局](view-layout.md) — 使用叠放视图来自动布置界面中的视图。需要精确放置视图时，请使用 Auto Layout。
- [外观自定义](appearance-customization.md) — 将 Liquid Glass 应用于视图，在 App 中支持深色模式（Dark Mode），自定义栏的外观，并使用外观代理（appearance proxy）修改 UI。
- [窗口与屏幕](windows-and-screens.md) — 为视图层级结构（view hierarchy）和其他内容提供容器。
