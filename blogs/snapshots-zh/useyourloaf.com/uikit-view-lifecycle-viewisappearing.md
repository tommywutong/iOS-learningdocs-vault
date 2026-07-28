---
title: UIKit 视图生命周期——viewIsAppearing
source_url: 'https://useyourloaf.com/blog/uikit-view-lifecycle-viewisappearing/'
source_domain: useyourloaf.com
source_group: single-site
original_language: en
published: 2023-09-25
archived_at: 2026-07-27
content_hash: 'sha256:5771218ce7a25ca9'
plan_ref: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 5｜生命周期必须按场景观测（对应 W5-06）
plan_week: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期
plan_day: Day 5｜生命周期必须按场景观测（对应 W5-06）
container: '//*[contains(@class,''article-content'')]'
container_source: guess
translated: true
---

> 原文：[UIKit View Lifecycle - viewIsAppearing](https://useyourloaf.com/blog/uikit-view-lifecycle-viewisappearing/)

Apple 在 iOS 17 中新增了一个视图控制器生命周期回调，并可向后部署至 iOS 13。以下是 `viewIsAppearing` 的快速指南。

### 视图控制器生命周期

`UIViewController` 有多个方法，UIKit 会在将视图控制器的视图移入或移出屏幕时调用：

- **viewDidLoad**：在视图控制器加载了视图、但尚未将其添加到视图层级结构后调用。在视图控制器的生命周期中仅调用**一次**。
- **viewWillAppear**：当视图控制器的视图即将添加到视图层级结构时调用。与 `viewDidLoad` 不同，随着视图移入和移出屏幕，这个方法在视图控制器的生命周期中可能被调用**多次**。视图即将从视图层级结构中移除时，会调用对应的 **viewWillDisappear**。
- **viewDidAppear**：在视图控制器的视图被添加到视图层级结构并显示在屏幕上之后调用。与 `viewWillAppear` 一样，这个方法在视图每次出现在屏幕上时都会调用，且有一个对应方法 `viewDidDisappear`，在视图移除后调用。

关于这些方法，需要记住的要点是：视图的 frame（大小和位置）以及 traits（如水平/垂直尺寸类别）在视图被添加到视图层级结构之前不会更新。

如果你希望基于视图的大小或 traits 来更新视图，这就会导致问题。在 `viewDidLoad` 或 `viewWillAppear` 中执行时为时过早，因为视图尚未被添加到视图层级结构；而如果等到 `viewDidAppear`，视图已经在屏幕上可见了。

### 预测 trait 变化？

此时我需要说明一点。在 iOS 13 中，Apple 做了一项更改：UIKit 在你创建视图时会为其预测初始 traits。请参阅 [在 iOS 13 中预测尺寸类别](https://useyourloaf.com/blog/predicting-size-classes-in-ios-13/)。这意味着你可以基于预测的 traits 在 `viewDidLoad` 中更新视图或布局：

```swift
override func viewDidLoad() {
  super.viewDidLoad()
  enableConstraintsForWidth(traitCollection.horizontalSizeClass)
}
```

如果系统预测的 traits 有误，你仍然会收到 `traitCollectionDidChange` 的调用，从而进行必要的调整：

```swift
override func traitCollectionDidChange(previousTraitCollection: UITraitCollection?) {
  super.traitCollectionDidChange(previousTraitCollection)
  if traitCollection.horizontalSizeClass != previousTraitCollection?.horizontalSizeClass {
    enableConstraintsForWidth(traitCollection.horizontalSizeClass)
  }
}
```

这种做法可行，但有些令人困惑，且容易出错。

注意：**`traitCollectionDidChange` 在 iOS 17 中已废弃**，取而代之的是更灵活的 API，你可以注册特定的 trait 变化。我将在后续文章中介绍。

### viewIsAppearing

Apple 在 iOS 17 中添加了一个新方法 **viewIsAppearing**，解决了上述困惑。更棒的是，这个新方法**可向后部署至 iOS 13**。你无需等到必须要求 iOS 17 时才能采用这个新 API。

**viewIsAppearing** 方法在 **viewWillAppear** 之后、**viewDidAppear** 之前调用。关键区别在于，它是在视图被添加到层级结构之后、但尚未显示在屏幕上时调用的。此时视图控制器的视图已经布局完成，因此你可以依赖其大小和 traits。

**这使得它成为在视图即将出现在屏幕之前更新任何 UI 的绝佳位置**。

```swift
override func viewIsAppearing(_ animated: Bool) {
  super.viewIsAppearing(animated)
  enableConstraintsForWidth(traitCollection.horizontalSizeClass)
}
```

### 你应该怎么做？

如果你之前依赖预测的 traits 在 **viewDidLoad** 中更新 UI，可能需要将该代码移至 **viewIsAppearing**。请注意，如果视图多次出现（例如由于导航导致），这个新回调可能会被调用**多次**。

### 了解更多

- [WWDC23 UIKit 的新特性](https://developer.apple.com/videos/play/wwdc2023/10055/)
