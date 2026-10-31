---
title: 准备你的 UI 在前台运行
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/preparing-your-ui-to-run-in-the-foreground
source_url: 'https://developer.apple.com/documentation/uikit/preparing-your-ui-to-run-in-the-foreground'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/preparing-your-ui-to-run-in-the-foreground.json'
content_hash: 'sha256:b5669967faec746c'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [Scenes](scenes.md)

# 准备你的 UI 在前台运行

配置你的 App 以出现在屏幕上。

## 概述

使用前台过渡来准备你的 App 的 UI 出现在屏幕上。App 过渡到前台通常是响应用户动作。例如，当用户轻点 App 图标时，系统启动 App 并将其带到前台。使用前台过渡来更新你的 App 的 UI、获取资源以及启动处理用户请求所需的服务。

所有状态过渡都会导致 UIKit 向相应的委托对象发送通知：

- 在 iOS 13 及更高版本 —— 一个 [UISceneDelegate](uiscenedelegate.md) 对象。
- 在 iOS 12 及更早版本 —— [UIApplicationDelegate](uiapplicationdelegate.md) 对象。

你可以同时支持两种委托对象，但 UIKit 在场景委托对象可用时总是使用它们。UIKit 只通知与正在进入前台的特定场景关联的场景委托。有关如何配置场景支持的信息，参见 [Specifying the scenes your app supports](specifying-the-scenes-your-app-supports.md)。

### 进入前台时更新你的 App 的数据模型

在启动时，系统在把 App 过渡到前台之前，先在非活跃状态启动它。使用你的 App 的启动时方法来执行那时所需的任何工作。对于处于后台的 App，UIKit 通过调用以下方法之一把你的 App 移动到非活跃状态：

- 对于支持场景的 App —— 相应场景委托对象的 [- sceneWillEnterForeground:](<uiscenedelegate/scenewillenterforeground(__).md>) 方法。
- 对于所有其他 App —— [- applicationWillEnterForeground:](<uiapplicationdelegate/applicationwillenterforeground(__).md>) 方法。

从后台过渡到前台时，使用这些方法从磁盘加载资源并从网络获取数据。

有关如何在启动时准备你的 App 的信息，参见 [Responding to the launch of your app](responding-to-the-launch-of-your-app.md)。

### 在激活时配置你的用户界面和初始任务

系统在显示 App 的 UI 之前立即把你的 App 移动到活跃状态。激活是配置你的 App 的 UI 和运行时行为的好时机；具体来说：

- 如有需要，显示你的 App 的窗口。
- 如有需要，更改当前可见的视图控制器。
- 更新视图和控制的数值与状态。
- 显示恢复已暂停游戏的控制。
- 启动或恢复你用于执行任务的任何调度队列。
- 更新数据源对象。
- 为周期性任务启动计时器。

把你的配置代码放在以下方法之一中：

- 对于基于场景的 UI —— 相应场景委托对象的 [- sceneDidBecomeActive:](<uiscenedelegate/scenedidbecomeactive(__).md>) 方法。
- 对于所有其他 App —— 你的 App 委托对象的 [- applicationDidBecomeActive:](<uiapplicationdelegate/applicationdidbecomeactive(__).md>) 方法。

激活也是在向用户显示 UI 之前为 UI 添加最后润色的时机。不要运行任何可能阻塞激活方法的代码。相反，确保你提前拥有所需的一切。例如，如果数据在 App 外频繁变化，请在 App 返回前台之前使用后台任务从网络获取更新。否则，准备好在你异步获取更改时显示现有数据。

### 视图出现时启动特定于 UI 的任务

当你的激活方法返回时，UIKit 显示你设为可见的所有窗口。它还通知任何相关的视图控制器它们的视图即将出现。使用视图控制器的 [- viewWillAppear:](<uiviewcontroller/viewwillappear(__).md>) 方法对你的界面执行任何最终更新。例如：

- 适当地启动用户界面动画。
- 如果启用了自动播放，开始播放媒体文件。
- 开始以完整帧率显示游戏和沉浸式内容的图形。

不要尝试显示不同的视图控制器或对用户界面进行重大更改。到视图控制器出现在屏幕上时，你的界面应该已经准备好显示。

## 主题

### 状态更改通知

- [Processing queued notifications](processing-queued-notifications.md) — 从挂起状态恢复时响应通知。

## 另请参阅

### 基础

- [Preparing your UI to run in the background](preparing-your-ui-to-run-in-the-background.md) — 准备你的 App 被挂起。
