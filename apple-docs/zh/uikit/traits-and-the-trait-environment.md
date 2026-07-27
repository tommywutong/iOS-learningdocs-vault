---
title: 特性与特性环境
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/traits-and-the-trait-environment
source_url: 'https://developer.apple.com/documentation/uikit/traits-and-the-trait-environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/traits-and-the-trait-environment.json'
content_hash: 'sha256:41a62b46fbc11295'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md)

# 特性与特性环境

<sub>API 集合</sub>

获取关于你 App 运行所在特性（trait）和环境的信息，并与你的视图层级结构共享数据。

## 概述

特性（trait）代表一些独立的数据，UIKit 会自动在你 App 的视图和视图控制器层级结构中分发这些数据。特性系统提供了一种统一的方式来共享配置信息，让你更容易构建能够响应设备方向、外观模式、辅助功能设置以及自定义 App 状态变化的自适应界面。

特性系统会将值从层级结构的顶层向下传播。当你使用特性覆盖在任意层级修改某个特性时，该变更会影响被修改的对象及其所有后代。在窗口场景上设置特性覆盖，会影响该场景内的所有视图控制器和视图。在某个特定视图上设置特性覆盖，则只会影响该视图及其子视图。

在数据需要流经视图层级结构中以下这些部分时，使用自定义特性来传播数据：

- 窗口场景（[UIWindowScene](uiwindowscene.md)）
- 窗口（[UIWindow](uiwindow.md)）
- 呈现控制器（[UIPresentationController](uipresentationcontroller.md)）
- 视图控制器（[UIViewController](uiviewcontroller.md)）
- 视图（[UIView](uiview.md)）
- 子视图（[UIView](uiview.md)）

自定义特性尤其适用于以下场景：

- 影响界面整个区块的配置设置
- 需要在视图层级结构中层层传递的外观状态
- 自定义 App 主题或样式模式
- 用于启用或禁用 UI 元素的功能开关

在可以直接在视图控制器、视图或子视图上设置属性的情况下，请避免使用自定义特性。

## 主题

### 基础

- [Adapting your app when traits change](adapting-your-app-when-traits-change.md) — 了解系统何时发生会影响你 App 的变化，然后高效地更新你的 App。

### Observing and managing traits

- [Automatic trait tracking](automatic-trait-tracking.md) — 当你在支持自动特性跟踪的方法或闭包中使用特性时，减少手动注册特性变化的需求。
- [UITraitCollection](uitraitcollection.md) — 一组数据，代表你 App 用户界面中单个元素所处的环境。
- [UITraitEnvironment](uitraitenvironment.md) — 一组方法，让你的 App 能够获取 iOS 界面环境的相关信息。
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md) — 一种类型，用于在特性环境发生变化时调用你的代码。
- [UIMutableTraits](uimutabletraits-13ja5.md) — 一个可变的特性容器。
- [UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md) — 一组方法，与某个呈现控制器配合使用，决定如何响应你 App 中的特性变化。
- [UIContentContainer](uicontentcontainer.md) — 一组方法，用于使你视图控制器的内容适配尺寸和特性的变化。

### Custom traits

- [Providing data to the view hierarchy with custom traits](providing-data-to-the-view-hierarchy-with-custom-traits.md) — 共享需要在你视图层级结构的多个层级之间按层级流动的数据。
- [UIMutableTraits](uimutabletraits-13ja5.md) — 一个可变的特性容器。
- [UITrait](uitrait-9423.md) — 一种表示特性集合中某个特性的类型。
- [UITraitDefinition](uitraitdefinition-64c15.md) — 一种表示特性集合中某个特性的类型。

## 另请参阅

### Adaptivity and traits

- [Responding to changing display modes on Apple TV](responding-to-changing-display-modes-on-apple-tv.md) — 在你设备的屏幕色域发生变化时，动态更换图像和资源。
