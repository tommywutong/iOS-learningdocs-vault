---
title: 使用键盘导览 App 的用户界面
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, Xcode 13.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/navigating-an-app-s-user-interface-using-a-keyboard
source_url: 'https://developer.apple.com/documentation/uikit/navigating-an-app-s-user-interface-using-a-keyboard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/navigating-an-app-s-user-interface-using-a-keyboard.json'
content_hash: 'sha256:31faac6fd91df991'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Focus-based navigation](focus-based-navigation.md)

# 使用键盘导览 App 的用户界面

<sub>示例代码</sub>

在 iPad App 和使用 Mac Catalyst 构建的 App 中，使用键盘和可聚焦 UI 元素在用户界面元素之间进行导览。

## 概述

> [!note] 注意
> 此示例代码项目与 WWDC21 会话相关：[10260: Focus on iPad Keyboard Navigation](https://developer.apple.com/wwdc21/10260/)

## 另请参阅

### 焦点交互

- [About focus interactions for Apple TV](about-focus-interactions-for-apple-tv.md) — 为菜单和交互式用户界面布局设计并实现直观的控制方案。
- [Adding user-focusable elements to a tvOS app](adding-user-focusable-elements-to-a-tvos-app.md) — 为 tvOS App 创建直观且易于操控的用户交互控制。
- [UIFocusEnvironment](uifocusenvironment.md) — 定义视图层级结构分支焦点行为的一组方法。
- [UIFocusSystem](uifocussystem.md) — 查询并重新评估当前聚焦的项目。
- [UIFocusUpdateContext](uifocusupdatecontext.md) — 提供与从一个视图到另一个视图的特定焦点更新相关信息的对象。
- [UIFocusItem](uifocusitem.md) — 可获得焦点的对象。
- [UIFocusMovementHint](uifocusmovementhint.md) — 提供聚焦项目移动提示信息。
- [UIFocusItemContainer](uifocusitemcontainer.md) — 负责为给定焦点环境内的焦点项目提供几何上下文的容器。
- [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md) — 支持可聚焦内容自动滚动的焦点项目容器类型。
- [UIFocusGroupPriority](uifocusgrouppriority.md) — 焦点组内项目的优先级，焦点系统用它来确定该组的主项目。

## 下载

- [NavigatingAnAppsUserInterfaceUsingAKeyboard.zip](https://docs-assets.developer.apple.com/published/1fe9bc497b3c/NavigatingAnAppsUserInterfaceUsingAKeyboard.zip)
