---
title: 视图控制器过渡
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/view-controller-transitions
source_url: 'https://developer.apple.com/documentation/uikit/view-controller-transitions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/view-controller-transitions.json'
content_hash: 'sha256:a10d95f762ef4923'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [动画与触觉](animation-and-haptics.md)

# 视图控制器过渡

<sub>API 集合</sub>

定义从一个视图控制器到另一个视图控制器的自定过渡效果。

## 主题

### 基础

- [通过流畅的过渡增强你的 App](enhancing-your-app-with-fluid-transitions.md) — 使用流畅的缩放过渡来为你的 App 提供持续交互且响应灵敏的体验。

### 动画委托

- [UIViewControllerTransitioningDelegate](uiviewcontrollertransitioningdelegate.md) — 一组方法，用于提供对象来管理视图控制器之间的固定时长或交互式过渡。

### 非交互式过渡

- [UIViewControllerAnimatedTransitioning](uiviewcontrolleranimatedtransitioning.md) — 一组方法，用于实现自定视图控制器过渡的动画。
- [UIViewControllerContextTransitioning](uiviewcontrollercontexttransitioning.md) — 一组方法，为视图控制器之间的过渡动画提供上下文信息。

### 交互式过渡

- [UIPercentDrivenInteractiveTransition](uipercentdriveninteractivetransition.md) — 一个对象，用于驱动一个视图控制器与另一个之间的交互式动画。
- [UIViewControllerInteractiveTransitioning](uiviewcontrollerinteractivetransitioning.md) — 一组方法，使对象（例如导览控制器）能够驱动视图控制器的过渡。
- [UIViewImplicitlyAnimating](uiviewimplicitlyanimating.md) — 用于在动画运行时修改它的接口。

### 过渡协调器

- [UIViewControllerTransitionCoordinator](uiviewcontrollertransitioncoordinator.md) — 一组方法，为与视图控制器过渡相关的动画提供支持。
- [UIViewControllerTransitionCoordinatorContext](uiviewcontrollertransitioncoordinatorcontext.md) — 一组方法，提供关于进行中的视图控制器过渡的信息。

## 另请参阅

### 内容动画

- [基于属性的动画](property-based-animations.md) — 通过更改视图的属性来创建动画。
- [统一你的 App 中的动画](../swiftui/unifying-your-app-s-animations.md) — 在 SwiftUI、UIKit 和 AppKit 中创建一致的 UI 动画体验。
- [优化 iPhone 和 iPad App 以支持 ProMotion 显示器](../quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md) — 通过请求首选刷新率并使动画与系统同步，改善 App 的视觉外观并节省电量。
