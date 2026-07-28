---
title: App 与环境
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/app-and-environment
source_url: 'https://developer.apple.com/documentation/uikit/app-and-environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/app-and-environment.json'
content_hash: 'sha256:469628688f6cdadc'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md)

# App 与环境

<sub>API 集合</sub>

管理生命周期事件和 App 的 UI 场景，并获取有关特性（trait）以及 App 运行环境的信息。

## 概述

从用户打开 App 的那一刻起，可能发生许多需要 App 处理或适应的情况，例如切换到另一个 App、接听电话、打开或关闭深色模式（Dark Mode），或旋转设备。UIKit 会将其中一些变化作为生命周期事件传达，将另一些变化作为特性变化传达。

你的 App 会在一个或多个场景（scene）中显示界面。在 iPhone 上，App 只显示一个场景。在 iPad、Mac 和 Apple Vision Pro 上，用户可以在不同窗口中或并排同时创建和管理 App 用户界面的多个实例。每个 UI 实例会显示不同内容，或以不同方式显示相同内容。例如，用户可以显示一个展现特定日期的「日历」App 实例，同时显示另一个展现整月的实例。

UIKit 使用_特性集合（trait collection）_传达当前环境的详细信息；特性集合反映设备设置、界面设置和用户偏好的组合。例如，你可以使用特性检测当前视图或视图控制器（view controller）是否启用了深色模式。如果你想根据当前环境自定义 App，并根据特性变化更新 App，请参阅[在特性发生变化时适配 App](adapting-your-app-when-traits-change.md)。若要使用自定义特性在视图层级结构（view hierarchy）中共享数据，请阅读[使用自定义特性向视图层级结构提供数据](providing-data-to-the-view-hierarchy-with-custom-traits.md)。

在 iOS 18 及更高版本中，将 Swift Observation 与 UIKit 的自动跟踪结合使用，可在模型数据发生变化时自动更新视图。使用 `@Observable` 宏标记模型类，然后在受支持的方法中引用可观察属性。之后，UIKit 会自动跟踪属性访问，并在这些属性发生变化时更新视图。

通过 [UIDevice](uidevice.md) 访问电池状态、距离传感器数据和设备方向等设备特定信息，并使用 [UIStatusBarManager](uistatusbarmanager.md) 检查状态栏配置。

## 主题

### 生命周期

- [管理 App 的生命周期](managing-your-app-s-life-cycle.md) — 在 App 处于前台或后台时响应系统通知，并处理其他重要的系统相关事件。
- [响应 App 的启动](responding-to-the-launch-of-your-app.md) — 初始化 App 的数据结构，为 App 运行做好准备，并响应系统发出的任何启动时请求。
- [UIApplication](uiapplication.md) — 在 iOS 中运行的 App 的集中控制与协调点。
- [UIApplicationDelegate](uiapplicationdelegate.md) — 一组用于管理 App 共享行为的方法。
- [场景](scenes.md) — 同时管理 App UI 的多个实例，并将资源引导至合适的 UI 实例。
- [迁移到基于 UIKit 场景的生命周期](transitioning-to-the-uikit-scene-based-life-cycle.md) — 采用基于场景的生命周期，以取代 UIKit 中的 App 委托（app delegate）生命周期。

### 设备环境

- [UIDevice](uidevice.md) — 当前设备的表示形式。
- [UIStatusBarManager](uistatusbarmanager.md) — 一个描述状态栏配置的对象。

### 数据观察

- [使用 UIKit 中的观察跟踪自动更新视图](updating-views-automatically-with-observation-tracking-in-uikit.md) — 使用 Swift Observation 和自动跟踪，在模型数据更新时更新视图。
- [自动观察跟踪](automatic-observation-tracking.md) — 在支持自动观察跟踪的方法中进行更新，从而简化数据变化时的视图更新。

### 适配性与特性

- [特性与特性环境](traits-and-the-trait-environment.md) — 获取有关特性以及 App 运行环境的信息，并与视图层级结构共享数据。
- [响应 Apple TV 上不断变化的显示模式](responding-to-changing-display-modes-on-apple-tv.md) — 在设备的屏幕色域发生变化时动态更换图像和资源。

### iPad、Mac 与 Apple Vision Pro

- [构建桌面级 iPad App](building-a-desktop-class-ipad-app.md) — 采用桌面级增强功能，优化 iPad App 在台前调度、文稿交互、文本编辑、搜索等多任务处理场景中的用户体验。
- [使用标签页栏和边栏提升 iPad App](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md) — 提供紧凑、符合人体工程学的标签页栏，以快速访问 App 的关键部分，并提供用于深入导览的边栏。
- [在 iPad App 中支持桌面级功能](supporting-desktop-class-features-in-your-ipad-app.md) — 添加桌面级功能和文稿支持，增强 iPad App。
- [在 iPad、Mac 和 Apple Vision Pro 上进行多任务处理](multitasking-on-ipad-mac-and-apple-vision-pro.md) — 实现多任务处理 API，让 App 与 iPadOS、macOS 和 visionOS 无缝集成。

### 引导式访问

- [UIGuidedAccessRestrictionDelegate](uiguidedaccessrestrictiondelegate.md) — 一组方法，用于为 iOS 中的「引导式访问」功能添加自定义限制。
- [UIGuidedAccessRestrictionStateForIdentifier](<uiaccessibility/guidedaccessrestrictionstate(foridentifier_).md>) — 返回指定引导式访问限制的限制状态。

### 架构

- [将 App 从 32 位架构更新到 64 位架构](updating-your-app-from-32-bit-to-64-bit-architecture.md) — 通过适配 App 以支持较新版本的操作系统，确保 App 按预期运行。
- [UIApplicationMain](<uiapplicationmain(________)-1yub7.md>) — 创建 App 对象和 App 委托，并设置事件循环。

## 另请参阅

### App 结构

- [文稿、数据与粘贴板](documents-data-and-pasteboard.md) — 整理 App 的数据，并在粘贴板上共享这些数据。
- [资源管理](resource-management.md) — 管理用于实现 App 界面的图像、字符串、Storyboard 和 nib 文件。
- [App 扩展](app-extensions.md) — 将 App 的基本功能扩展到系统的其他部分。
- [进程间通信](interprocess-communication.md) — 向用户显示基于活动的服务。
- [Mac Catalyst](mac-catalyst.md) — 创建可供用户在 Mac 上运行的 iPad App 版本。
