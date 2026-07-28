---
title: 触摸、按压与手势
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/touches-presses-and-gestures
source_url: 'https://developer.apple.com/documentation/uikit/touches-presses-and-gestures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/touches-presses-and-gestures.json'
content_hash: 'sha256:8cc72810953f442d'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md)

# 触摸、按压与手势

<sub>API 集合</sub>

将你 App 的事件处理逻辑封装在手势识别器中，以便在整个 App 中复用这些代码。

## 概述

如果你使用标准的 UIKit 视图和控制来构建 App，UIKit 会自动为你处理触摸事件（包括多点触控事件）。但如果你使用自定义视图来显示内容，就必须自行处理视图中发生的所有触摸事件。有两种方式可以自行处理触摸事件。

- 使用手势识别器来跟踪触摸；参见 [Handling UIKit gestures](handling-uikit-gestures.md)。
- 直接在你的 [UIView](uiview.md) 子类中跟踪触摸；参见 [Handling touches in your view](handling-touches-in-your-view.md)。

## 主题

### 基础

- [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md) — 了解如何处理在你 App 中传播的事件。
- [UIResponder](uiresponder.md) — 一个用于响应和处理事件的抽象接口。
- [UIEvent](uievent.md) — 一个对象，描述用户与你 App 的一次交互。

### Touches

- [Handling touches in your view](handling-touches-in-your-view.md) — 如果触摸处理与视图内容紧密相关，可直接在视图子类上使用触摸事件。
- [Handling input from Apple Pencil](handling-input-from-apple-pencil.md) — 了解如何检测并响应来自 Apple Pencil 的触摸。
- [Tracking the force of 3D Touch events](tracking-the-force-of-3d-touch-events.md) — 根据触摸的力度来操控你的内容。
- [Illustrating the force, altitude, and azimuth properties of touch input](illustrating-the-force-altitude-and-azimuth-properties-of-touch-input.md) — 在视图中捕获 Apple Pencil 和触摸输入。
- [Leveraging touch input for drawing apps](leveraging-touch-input-for-drawing-apps.md) — 将触摸捕获为一系列笔画，并在绘图画布上高效渲染它们。
- [UITouch](uitouch.md) — 一个对象，表示屏幕上一次触摸的位置、大小、移动和力度。

### Button presses

- [UIPress](uipress.md) — 一个对象，表示屏幕上针对某个特定事件的按钮按压的出现或移动情况。
- [UIPressesEvent](uipressesevent.md) — 一个事件，描述设备可用的一组物理按钮的状态，例如关联遥控器或游戏控制器上的按钮。

### Standard gestures

- [Handling UIKit gestures](handling-uikit-gestures.md) — 使用手势识别器简化触摸处理，打造一致的用户体验。
- [Coordinating multiple gesture recognizers](coordinating-multiple-gesture-recognizers.md) — 了解如何在同一视图上使用多个手势识别器。
- [Adopting hover support for Apple Pencil](adopting-hover-support-for-apple-pencil.md) — 通过为 Apple Pencil 输入提供悬停预览，增强你 iPadOS App 的用户反馈。
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md) — 通过支持标准和自定义手势交互，丰富你 App 的用户体验。
- [UIHoverGestureRecognizer](uihovergesturerecognizer.md) — 一个连续型手势识别器，用于解读指针在视图上方的移动。
- [UILongPressGestureRecognizer](uilongpressgesturerecognizer.md) — 一个连续型手势识别器，用于解读长按手势。
- [UIPanGestureRecognizer](uipangesturerecognizer.md) — 一个连续型手势识别器，用于解读平移手势。
- [UIPinchGestureRecognizer](uipinchgesturerecognizer.md) — 一个连续型手势识别器，用于解读涉及两次触摸的捏合手势。
- [UIRotationGestureRecognizer](uirotationgesturerecognizer.md) — 一个连续型手势识别器，用于解读涉及两次触摸的旋转手势。
- [UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md) — 一个连续型手势识别器，用于解读从屏幕边缘附近开始的平移手势。
- [UISwipeGestureRecognizer](uiswipegesturerecognizer.md) — 一个离散型手势识别器，用于解读一个或多个方向上的滑动手势。
- [UITapGestureRecognizer](uitapgesturerecognizer.md) — 一个离散型手势识别器，用于解读单次或多次点按。

### Custom gestures

- [Implementing a custom gesture recognizer](implementing-a-custom-gesture-recognizer.md) — 了解何时以及如何构建你自己的手势识别器。
- [UIGestureRecognizer](uigesturerecognizer.md) — 各种具体手势识别器的基类。
- [UIGestureRecognizerDelegate](uigesturerecognizerdelegate.md) — 一组由手势识别器的委托实现的方法，用于精细调整 App 的手势识别行为。
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md) — 通过支持标准和自定义手势交互，丰富你 App 的用户体验。

### 3D Touch interactions

- [UIPreviewInteraction](uipreviewinteraction.md) — 一个类，用于注册某个视图，使其能够响应 3D Touch 交互，提供自定义的用户体验。
- [UIPreviewInteractionDelegate](uipreviewinteractiondelegate.md) — 一组方法，用于传达预览交互的进度。
- [UIPreviewActionItem](uipreviewactionitem.md) — 一组方法，定义了你可以应用于 peek 快速操作和 peek 快速操作分组的样式，并定义了一个用于获取 peek 快速操作用户可见标题的只读访问器。

## 另请参阅

### 用户交互

- [Menus and shortcuts](menus-and-shortcuts.md) — 使用菜单系统、上下文菜单、主屏幕快速操作和键盘快捷键，简化与你 App 的交互。
- [Drag and drop](drag-and-drop.md) — 通过在视图中使用交互 API，为你的 App 带来拖放功能。
- [Pointer interactions](pointer-interactions.md) — 在你的自定义控制和视图中支持指针交互。
- [Apple Pencil interactions](apple-pencil-interactions.md) — 处理 Apple Pencil 上双击和挤压等用户交互。
- [Focus-based navigation](focus-based-navigation.md) — 使用遥控器、游戏控制器或键盘导览你 UIKit App 的界面。
- [Accessibility for UIKit](accessibility-for-uikit.md) — 让使用 iOS 和 tvOS 的每个人都能无障碍地使用你的 UIKit App。
