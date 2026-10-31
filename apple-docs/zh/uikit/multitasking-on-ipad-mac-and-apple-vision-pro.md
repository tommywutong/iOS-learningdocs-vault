---
title: 在 iPad、Mac 和 Apple Vision Pro 上进行多任务处理
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/multitasking-on-ipad-mac-and-apple-vision-pro
source_url: 'https://developer.apple.com/documentation/uikit/multitasking-on-ipad-mac-and-apple-vision-pro'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/multitasking-on-ipad-mac-and-apple-vision-pro.json'
content_hash: 'sha256:080d8f16ea6f1f5a'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md)

# 在 iPad、Mac 和 Apple Vision Pro 上进行多任务处理

<sub>API 集合</sub>

实现多任务处理 API，让你的 App 与 iPadOS、macOS 和 visionOS 无缝集成。

## 概述

当你的 App 的场景在 iPad、Mac 或 Apple Vision Pro 上于前台运行时，其他 App 很可能也在其旁边运行。了解你的 App 可能运行于其中的环境，并采用多任务处理 API，是把你的 App 与 iPadOS、macOS 和 visionOS 集成起来的重要组成部分。

### 适应不同的窗口大小

为人们打造出色多任务处理体验的第一步，是确保你的 App 的场景能够适应不同的窗口大小。首先阅读[人机界面指南](https://developer.apple.com/design/human-interface-guidelines/)中的[布局](https://developer.apple.com/design/human-interface-guidelines/layout)。

要考虑到你的 App 可能运行在较小的窗口中而不是全屏。使用 [UITraitCollection](uitraitcollection.md) 探查你的 App 的环境，并使用 Auto Layout 或[自动特性跟踪](automatic-trait-tracking.md)来适应该环境。或者，使用 [UITraitChangeObservable](uitraitchangeobservable-67e94.md) 方法，在你的视图或视图控制器上注册以观察特定的特性变化。由于人们可以调整你的 App 窗口的大小，请使用 [UISceneSizeRestrictions](uiscenesizerestrictions.md) 为你的窗口设置最小尺寸。

要观察场景几何形状的变化，请使用 [- windowScene:didUpdateEffectiveGeometry:](<uiwindowscenedelegate/windowscene(__didupdateeffectivegeometry_).md>) 并比较两个几何形状的 `coordinateSpace.bounds`。检查 [interactivelyResizing](uiwindowscene/geometry/isinteractivelyresizing.md) 以确定某人当前是否正在调整场景大小，并调整你在调整大小期间更新哪些资源以提升性能。

### 支持多个场景

你可以通过设置 [UIApplicationSupportsMultipleScenes](../bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md) 属性列表键，选择允许你的 App 的 UI 中同时运行多个场景。实现 [Scenes](scenes.md) 并阅读[管理你 App 的生命周期](managing-your-app-s-life-cycle.md)，了解 [UISceneDelegate](uiscenedelegate.md) 如何与系统多任务处理事件交互的概述。关于采用基于场景的生命周期的信息，参见 [TN3187：迁移到基于 UIKit 场景的生命周期](../technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)。

### 支持不同的界面方向

设计你的 App 的场景，使其在任何界面方向上都能正确显示。在你希望把 App 的界面锁定到当前方向的情况下，调用 [- setNeedsUpdateOfPrefersInterfaceOrientationLocked](<uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked().md>)，然后把 [prefersInterfaceOrientationLocked](uiviewcontroller/prefersinterfaceorientationlocked.md) 的值返回为 [true](../swift/true.md)，或者重写 [childViewControllerForInterfaceOrientationLock](uiviewcontroller/childforinterfaceorientationlock.md) 把决定委托给子视图控制器。实现 [- windowScene:didUpdateEffectiveGeometry:](<uiwindowscenedelegate/windowscene(__didupdateeffectivegeometry_).md>) 以观察方向变化，因为即使你发出了锁定方向的偏好，系统也可能更改界面方向。锁定界面方向的偏好会持续到你的 App 停止呈现该场景，或者你再次调用 `setNeedsUpdateOfPrefersInterfaceOrientationLocked()` 并把 `prefersInterfaceOrientationLocked` 的值返回为 [false](../swift/false.md)。

## 主题

### 自适应

- [UITraitCollection](uitraitcollection.md) — 表示你的 App 用户界面中单个元素环境的数据集合。
- [UITraitEnvironment](uitraitenvironment.md) — 一组使 iOS 界面环境对你的 App 可用的方法。
- [自动特性跟踪](automatic-trait-tracking.md) — 当你在支持自动特性跟踪的方法或闭包中使用特性时，减少手动注册特性变化的需要。
- [UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md) — 一组与呈现控制器结合使用的方法，决定如何响应你的 App 中的特性变化。
- [UIContentContainer](uicontentcontainer.md) — 一组用于让视图控制器的内容适应大小和特性变化的方法。

### 场景管理

- [Scenes](scenes.md) — 同时管理你的 App 的 UI 的多个实例，并把资源导向 UI 的相应实例。
- [在 iPad 上支持多个窗口](supporting-multiple-windows-on-ipad.md) — 支持你的 App 界面的并排实例并创建新窗口。

## 另请参阅

### iPad、Mac 和 Apple Vision Pro

- [构建桌面级 iPad App](building-a-desktop-class-ipad-app.md) — 通过采用台前调度（Stage Manager）多任务处理、文稿交互、文本编辑、搜索等方面的桌面级增强功能，优化你的 iPad App 的用户体验。
- [通过标签页栏和边栏提升你的 iPad App](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md) — 提供紧凑、符合人体工学的标签页栏，便于快速访问 App 的关键部分；并提供边栏用于深入导览。
- [为你的 iPad App 支持桌面级功能](supporting-desktop-class-features-in-your-ipad-app.md) — 通过添加桌面级功能和文稿支持来增强你的 iPad App。
