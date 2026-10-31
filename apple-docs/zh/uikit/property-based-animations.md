---
title: 基于属性的动画
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/property-based-animations
source_url: 'https://developer.apple.com/documentation/uikit/property-based-animations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/property-based-animations.json'
content_hash: 'sha256:10002da51f49be7a'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Animation and haptics](animation-and-haptics.md)

# 基于属性的动画

<sub>API 集合</sub>

通过更改视图的属性来创建动画。

## 主题

### 基础

- [UIViewPropertyAnimator](uiviewpropertyanimator.md) — 一个对视图进行动画并允许动态修改这些动画的类。
- [UIViewAnimating](uiviewanimating.md) — 用于实现自定义动画对象的接口。

### Timing curves

- [UITimingCurveProvider](uitimingcurveprovider.md) — 为执行动画提供所需 timing 信息的接口。
- [UISpringTimingParameters](uispringtimingparameters.md) — 模拟弹簧行为的动画 timing 信息。
- [UICubicTimingParameters](uicubictimingparameters.md) — 以三次 Bézier 曲线形式表示的动画 timing 信息。

### In-progress animations

- [UIViewImplicitlyAnimating](uiviewimplicitlyanimating.md) — 用于在动画运行时修改动画的接口。

## 另请参阅

### Content animations

- [View controller transitions](view-controller-transitions.md) — 定义从一个视图控制器到另一个视图控制器的自定义过渡。
- [Unifying your app’s animations](../swiftui/unifying-your-app-s-animations.md) — 在 SwiftUI、UIKit 和 AppKit 之间创建一致的 UI 动画体验。
- [Optimizing iPhone and iPad apps to support ProMotion displays](../quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md) — 通过请求首选刷新率并使你的动画与系统同步，改善 App 的视觉外观并节省电量。
