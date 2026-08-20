---
title: 协调多个手势识别器
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/coordinating-multiple-gesture-recognizers
source_url: 'https://developer.apple.com/documentation/uikit/coordinating-multiple-gesture-recognizers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/coordinating-multiple-gesture-recognizers.json'
content_hash: 'sha256:2c76580c3a7da6a3'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [触控、按压与手势](touches-presses-and-gestures.md)

# 协调多个手势识别器

了解如何在同一个视图上使用多个手势识别器（gesture recognizer）。

## 概述

手势识别器会分别跟踪传入的触控事件，但 UIKit 通常只允许在单个视图上一次识别一个手势。通常，一次只识别一个手势更为可取，因为它能防止用户输入一次触发多个操作。然而，这种默认行为可能会带来意外的副作用。例如，在一个同时包含平移（pan）和轻扫（swipe）手势识别器的视图中，轻扫手势永远不会被识别。由于平移手势识别器是连续的（continuous），它总会在离散的（discrete）轻扫手势识别器之前识别其手势。

为了防止默认识别行为带来的意外副作用，你可以使用委托（delegate）对象告诉 UIKit 按特定顺序识别手势。UIKit 会使用你的委托对象中的方法来确定某个手势识别器必须出现在其他手势识别器之前还是之后。例如，你的委托可以告诉 UIKit，在允许平移手势识别器触发之前，轻扫手势识别器必须先失败（fail）。你的委托还可以告诉 UIKit 两个手势可以同时被识别。

## 主题

### 同时手势

- [优先选择某个手势而非另一个](preferring-one-gesture-over-another.md) — 使用手势识别器委托对象来确定视图中手势被识别的顺序。
- [允许多个手势同时识别](allowing-the-simultaneous-recognition-of-multiple-gestures.md) — 了解如何使用委托对象来允许同时检测多个手势。
- [将手势识别器附加到 UIKit 控制（control）](attaching-gesture-recognizers-to-uikit-controls.md) — 了解手势识别器如何与 UIKit 控制（如按钮、开关和滑块）交互。

## 另请参阅

### 标准手势

- [处理 UIKit 手势](handling-uikit-gestures.md) — 使用手势识别器简化触控处理并创建一致的用户体验。
- [为 Apple Pencil 采用悬停支持](adopting-hover-support-for-apple-pencil.md) — 通过为 Apple Pencil 输入提供悬停预览来增强 iPadOS App 的用户反馈。
- [在 App 中支持手势交互](supporting-gesture-interaction-in-your-apps.md) — 通过支持标准和自定义手势交互来丰富 App 的用户体验。
- [UIHoverGestureRecognizer](uihovergesturerecognizer.md) — 一个连续手势识别器，用于解读视图上的指针移动。
- [UILongPressGestureRecognizer](uilongpressgesturerecognizer.md) — 一个连续手势识别器，用于解读长按手势。
- [UIPanGestureRecognizer](uipangesturerecognizer.md) — 一个连续手势识别器，用于解读平移手势。
- [UIPinchGestureRecognizer](uipinchgesturerecognizer.md) — 一个连续手势识别器，用于解读涉及两次触摸的捏合手势。
- [UIRotationGestureRecognizer](uirotationgesturerecognizer.md) — 一个连续手势识别器，用于解读涉及两次触摸的旋转手势。
- [UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md) — 一个连续手势识别器，用于解读从屏幕边缘附近开始的平移手势。
- [UISwipeGestureRecognizer](uiswipegesturerecognizer.md) — 一个离散手势识别器，用于解读一个或多个方向的轻扫手势。
- [UITapGestureRecognizer](uitapgesturerecognizer.md) — 一个离散手势识别器，用于解读单次或多次轻点手势。
