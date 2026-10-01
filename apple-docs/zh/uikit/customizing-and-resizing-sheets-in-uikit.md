---
title: 在 UIKit 中自定义与调整 sheet 的大小
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, Xcode 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/customizing-and-resizing-sheets-in-uikit
source_url: 'https://developer.apple.com/documentation/uikit/customizing-and-resizing-sheets-in-uikit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/customizing-and-resizing-sheets-in-uikit.json'
content_hash: 'sha256:5e65d8ea7c460ee3'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图控制器](view-controllers.md) · [UIViewController](uiviewcontroller.md)

# 在 UIKit 中自定义与调整 sheet 的大小

<sub>示例代码</sub>

了解如何在 UIKit 中创建分层且自定义的 sheet 体验。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC22 场次 [10068: What’s new in UIKit](https://developer.apple.com/wwdc22/10068/)。

## 另请参阅

### 添加自定义转场或呈现

- [transitioningDelegate](uiviewcontroller/transitioningdelegate.md) — 提供转场动画器、交互控制器和自定义呈现控制器对象的委托对象。
- [transitionCoordinator](uiviewcontroller/transitioncoordinator.md) — 返回当前活动的转场协调器对象。
- [- targetViewControllerForAction:sender:](<uiviewcontroller/targetviewcontroller(foraction_sender_).md>) — 返回响应该操作的视图控制器。
- [presentationController](uiviewcontroller/presentationcontroller.md) — 正在管理当前视图控制器的呈现控制器。
- [popoverPresentationController](uiviewcontroller/popoverpresentationcontroller.md) — 正在管理当前视图控制器的最近的弹出窗口呈现控制器。
- [sheetPresentationController](uiviewcontroller/sheetpresentationcontroller.md) — 该视图控制器的 sheet 呈现控制器。
- [activePresentationController](uiviewcontroller/activepresentationcontroller.md) — 正在管理该视图控制器的呈现控制器。
- [restoresFocusAfterTransition](uiviewcontroller/restoresfocusaftertransition.md) — 一个布尔值，表示当条目的视图控制器变得可见且可获得焦点时，之前获得焦点的条目是否应重新获得焦点。

## 下载

- [CustomizingAndResizingSheetsInUIKit.zip](https://docs-assets.developer.apple.com/published/9f8e34adc2d3/CustomizingAndResizingSheetsInUIKit.zip)
