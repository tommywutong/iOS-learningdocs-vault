---
title: 准备让你的界面在后台运行
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/preparing-your-ui-to-run-in-the-background
source_url: 'https://developer.apple.com/documentation/uikit/preparing-your-ui-to-run-in-the-background'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/preparing-your-ui-to-run-in-the-background.json'
content_hash: 'sha256:7f3d7630a9478f9f'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [Scenes](scenes.md)

# 准备让你的界面在后台运行

准备让你的 App 被挂起。

## 概述

App 会因为许多原因转入后台状态。当用户退出一个处于前台的 App 时，该 App 会先短暂转入后台状态，然后才被 UIKit 挂起。系统也可能直接把某个 App 启动到后台状态，或把一个已挂起的 App 转入后台，并给它一些时间来执行重要任务。

当你的 App 处于后台时，应尽可能少做事情，最好什么都不做。如果你的 App 此前处于前台，请利用转入后台这个时机停止任务并释放任何共享资源。如果你的 App 是为了处理某个重要事件而进入后台，请处理该事件并尽快退出。

所有状态转换都会导致 UIKit 向相应的委托对象发送通知：

- 在 iOS 13 及更高版本中——一个 [UISceneDelegate](uiscenedelegate.md) 对象。
- 在 iOS 12 及更早版本中——[UIApplicationDelegate](uiapplicationdelegate.md) 对象。

你可以同时支持这两种委托对象，但只要场景委托对象可用，UIKit 就总是会使用它们。UIKit 只会通知与正在转入后台的特定场景相关联的场景委托。

### 在停用时让你的 App 安静下来

系统会因为多种原因停用 App。当用户退出处于前台的 App 时，系统会在把它转入后台之前立即停用该 App。系统还会在需要临时打断某个 App 时将其停用——例如，为了显示系统提醒。在系统面板的情况下，当用户关闭该面板后，系统会重新激活该 App。

在停用期间，UIKit 会调用你 App 中下列方法之一：

- 对于支持场景的 App——相应场景委托对象的 [- sceneWillResignActive:](<uiscenedelegate/scenewillresignactive(__).md>) 方法。
- 对于其他所有 App——App 委托对象的 [- applicationWillResignActive:](<uiapplicationdelegate/applicationwillresignactive(__).md>) 方法。

利用停用这个时机来保存用户的数据，并通过暂停所有主要工作让你的 App 进入安静状态；具体来说：

- 把用户数据保存到磁盘，并关闭任何打开的文件。
- 挂起调度队列和操作队列。
- 不要安排任何新任务执行。
- 使任何活跃的定时器失效。
- 自动暂停游戏进程。
- 不要提交任何要处理的新 Metal 工作。
- 不要提交任何新的 OpenGL 命令。

### 在进入后台时释放资源

当你的 App 转入后台时，请释放内存，并释放你 App 持有的任何共享资源。对于从前台转入后台的 App 来说，释放内存尤为重要。前台在内存和其他系统资源上拥有优先权，系统会按需终止后台 App，以腾出这些资源。即使你的 App 之前并不处于前台，也请执行检查，确保它消耗的资源尽可能少。

在进入后台时，UIKit 会调用你 App 中下列方法之一：

- 对于支持场景的 App——相应场景委托对象的 [- sceneDidEnterBackground:](<uiscenedelegate/scenedidenterbackground(__).md>) 方法。
- 对于其他所有 App——App 委托对象的 [- applicationDidEnterBackground:](<uiapplicationdelegate/applicationdidenterbackground(__).md>) 方法。

在转入后台期间，请根据你的 App 的实际情况尽可能执行下列任务：

- 丢弃任何你直接从文件读取的图像或媒体内容。
- 丢弃任何你可以从磁盘重新创建或重新加载的大型内存对象。
- 释放对相机和其他共享硬件资源的访问权限。
- 在你 App 的用户界面中隐藏敏感信息（例如密码）。
- 关闭提醒和其他临时界面。
- 关闭与任何共享系统数据库的连接。
- 注销 Bonjour 服务，并关闭与之关联的任何监听套接字。
- 确保所有 Metal 命令缓冲区都已被调度。更多信息，请参阅[准备让你的 Metal App 在后台运行](../metal/preparing-your-metal-app-to-run-in-the-background.md)。
- 确保你此前提交的所有 OpenGL 命令都已完成。

你不需要丢弃从你 App 的素材目录中加载的具名图像。同样，你也不需要释放采用 [NSDiscardableContent](../foundation/nsdiscardablecontent.md) 协议的对象，或是你用 [NSCache](../foundation/nscache.md) 对象管理的对象。系统会自动处理这些对象的清理工作。

请确保你的 App 在转入后台时没有持有任何共享系统资源。如果它在转入后台之后继续访问相机或共享系统数据库之类的资源，系统会终止你的 App 以释放该资源。如果你使用某个系统框架来访问某项资源，请查阅该框架的文档，了解应该怎么做。

### 为 App 快照准备好你的界面

在你的 App 进入后台、且你的委托方法返回之后，UIKit 会为你 App 当前的用户界面拍摄一张快照。系统会在 App 切换器中显示生成的图像。在把你的 App 带回前台时，系统也会临时显示该图像。

你 App 的界面中不得包含任何敏感用户信息，例如密码或信用卡号。如果你的界面中包含此类信息，请在进入后台时把它从你的视图中移除。同时，请关闭提醒、临时界面，以及遮挡你 App 内容的系统视图控制器。该快照代表着你 App 的界面，应当让用户能够辨认出来。当你的 App 返回前台时，你可以按需恢复数据和视图。

> [!note] 注意
> 对于支持状态保存与恢复的 App，系统会在你的委托方法返回后不久开始保存过程。移除敏感数据同样可以防止这些信息被保存到你 App 的保存归档中。更多信息，请参阅[在多次启动之间保留 App 的界面](preserving-your-app-s-ui-across-launches.md)。

### 在后台响应重要事件

App 在进入后台之后通常不会获得任何额外的执行时间。不过，对于支持下列任一时间敏感能力的 App，UIKit 确实会为其授予执行时间：

- 使用 AirPlay 进行音频通信，或使用画中画视频。
- 面向用户的位置敏感服务。
- 网络电话（VoIP）。
- 与外部配件通信。
- 与蓝牙低功耗配件通信，或把设备转变为蓝牙低功耗配件。
- 来自服务器的定期更新。
- 对 Apple 推送通知服务（APNs）的支持。

如果你的 App 支持后台功能，请在 Xcode 中启用 Background Modes 功能。每种后台任务都有不同的要求；有关如何实现相应功能的详情，请参阅对应的框架。有关如何调度伺机而动的后台任务的信息，请参阅 [Background Tasks](../backgroundtasks.md)。

## 主题

### Background execution

- [Using background tasks to update your app](using-background-tasks-to-update-your-app.md) — 配置你的 App，使其在后台执行任务，以高效利用处理时间和电量。
- [Extending your app's background execution time](extending-your-app-s-background-execution-time.md) — 确保关键任务在你的 App 转入后台时能够完成。
- [About the background execution sequence](about-the-background-execution-sequence.md) — 了解你 App 转入后台时，你的自定代码被执行的顺序。

## 另请参阅

### 基础

- [Preparing your UI to run in the foreground](preparing-your-ui-to-run-in-the-foreground.md) — 配置你的 App，使其显示在屏幕上。
