---
title: 基于焦点的导览
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/focus-based-navigation
source_url: 'https://developer.apple.com/documentation/uikit/focus-based-navigation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/focus-based-navigation.json'
content_hash: 'sha256:d5fab8c7e6bf8dcb'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md)

# 基于焦点的导览

<sub>API 集合</sub>

使用遥控器、游戏控制器或键盘来导览你的 UIKit App 界面。

## 主题

### 焦点交互

- [使用键盘导览 App 的用户界面](navigating-an-app-s-user-interface-using-a-keyboard.md) — 在 iPad App 和使用 Mac Catalyst 构建的 App 中，使用键盘和可获得焦点的 UI 元素在用户界面元素之间导览。
- [关于 Apple TV 的焦点交互](about-focus-interactions-for-apple-tv.md) — 为菜单和交互式用户界面布局设计并实现直观的控制方案。
- [向 tvOS App 添加用户可聚焦元素](adding-user-focusable-elements-to-a-tvos-app.md) — 为你的 tvOS App 创建直观且易于操作的用户交互控制。
- [UIFocusEnvironment](uifocusenvironment.md) — 一组用于定义视图层级结构某一分支焦点行为的方法。
- [UIFocusSystem](uifocussystem.md) — 查询并重新评估当前获得焦点的项目。
- [UIFocusUpdateContext](uifocusupdatecontext.md) — 一个对象，提供与从一个视图到另一个视图的特定焦点更新相关的信息。
- [UIFocusItem](uifocusitem.md) — 一个可以获得焦点的对象。
- [UIFocusMovementHint](uifocusmovementhint.md) — 为获得焦点的项目提供移动提示信息。
- [UIFocusItemContainer](uifocusitemcontainer.md) — 负责为给定焦点环境内的焦点项目提供几何上下文的容器。
- [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md) — 一种支持可聚焦内容自动滚动的焦点项目容器。
- [UIFocusGroupPriority](uifocusgrouppriority.md) — 焦点组中某一项目的重要性，焦点系统用它来确定该组的主要项目。

### 焦点指南

- [创建自定导览交互](creating-custom-navigation-interactions.md) — 构建将焦点移动到所需位置的非标准导览交互。
- [UIFocusGuide](uifocusguide.md) — 一个将非视图区域公开为可聚焦区域的对象。

### 焦点调试

- [调试 App 中的焦点问题](debugging-focus-issues-in-your-app.md) — 查找错误并确定下一个获得焦点的项目为何不是你所期望的。
- [UIFocusDebugger](uifocusdebugger.md) — 一个用于调试焦点相关交互的运行时对象。

### 动画

- [UIFocusAnimationCoordinator](uifocusanimationcoordinator.md) — 一个在焦点更新期间协调焦点相关动画的协调器。

### 焦点效果

- [UIFocusEffect](uifocuseffect.md) — 用于定义可视焦点效果的基类。
- [UIFocusHaloEffect](uifocushaloeffect.md) — 一种在焦点项目周围绘制光环的可视焦点效果。
- [Position](uifocushaloeffect/position-swift.enum.md) — 描述绘制光环焦点效果所用位置的常量。

## 另请参阅

### 用户交互

- [触摸、按压与手势](touches-presses-and-gestures.md) — 将 App 的事件处理逻辑封装在手势识别器中，以便在整个 App 中复用该代码。
- [菜单与快捷键](menus-and-shortcuts.md) — 使用菜单系统、上下文菜单、主屏幕快速操作和键盘快捷键来简化与你 App 的交互。
- [拖放](drag-and-drop.md) — 通过在视图上使用交互 API，为你的 App 加入拖放功能。
- [指针交互](pointer-interactions.md) — 在自定控制和视图中支持指针交互。
- [Apple Pencil 交互](apple-pencil-interactions.md) — 处理用户在 Apple Pencil 上的交互，例如双击和捏压。
- [UIKit 的辅助功能](accessibility-for-uikit.md) — 让使用 iOS 和 tvOS 的每个人都能访问你的 UIKit App。
