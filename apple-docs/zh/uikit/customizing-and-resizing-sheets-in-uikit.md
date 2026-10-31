---
title: 在 UIKit 中自定和调整表单大小
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

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [UIViewController](uiviewcontroller.md)

# 在 UIKit 中自定和调整表单大小

<sub>示例代码</sub>

探索如何在 UIKit 中创建分层且自定的表单体验。

## 概述

> [!note] 注意
> 此示例代码项目与 WWDC22 会话相关：[10068: What’s new in UIKit](https://developer.apple.com/wwdc22/10068/)。

## 另请参阅

### 添加自定过渡或呈现

- [transitioningDelegate](uiviewcontroller/transitioningdelegate.md) — 提供过渡动画器、交互控制器和自定呈现控制器对象的委托对象。
- [transitionCoordinator](uiviewcontroller/transitioncoordinator.md) — 返回活动的过渡协调器对象。
- [- targetViewControllerForAction:sender:](<uiviewcontroller/targetviewcontroller(foraction_sender_).md>) — 返回响应该操作的视图控制器。
- [presentationController](uiviewcontroller/presentationcontroller.md) — 管理当前视图控制器的呈现控制器。
- [popoverPresentationController](uiviewcontroller/popoverpresentationcontroller.md) — 管理当前视图控制器的最近弹出呈现控制器。
- [sheetPresentationController](uiviewcontroller/sheetpresentationcontroller.md) — 视图控制器的表单呈现控制器。
- [activePresentationController](uiviewcontroller/activepresentationcontroller.md) — 管理视图控制器的呈现控制器。
- [restoresFocusAfterTransition](uiviewcontroller/restoresfocusaftertransition.md) — 指示先前聚焦的项目在项目的视图控制器变为可见且可聚焦时是否应再次获得焦点的布尔值。

## 下载

- [CustomizingAndResizingSheetsInUIKit.zip](https://docs-assets.developer.apple.com/published/9f8e34adc2d3/CustomizingAndResizingSheetsInUIKit.zip)
