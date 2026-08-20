---
title: 管理 App 的生命周期
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/managing-your-app-s-life-cycle
source_url: 'https://developer.apple.com/documentation/uikit/managing-your-app-s-life-cycle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/managing-your-app-s-life-cycle.json'
content_hash: 'sha256:fa09113da3765953'
translated: true
---

> 导航： [技术](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md)

# 管理 App 的生命周期

当 App 位于前台或后台时响应系统通知，并处理其他重要的系统相关事件。

## 概述

App 的当前状态决定了它在任何时候能做什么、不能做什么。例如，前台 App 拥有用户的注意，因此它对 CPU 等系统资源拥有更高优先级。相反，后台 App 必须尽可能少地工作，最好什么都不做，因为它处于屏幕之外。随着 App 在不同状态之间切换，你必须相应地调整其行为。

当 App 的状态发生变化时，UIKit 会调用相应委托（delegate）对象的方法来通知你：

- 在 iOS 13 及更高版本中，使用 [UISceneDelegate](uiscenedelegate.md) 对象来响应生命周期事件。
- 在 iOS 12 及更早版本中，使用 [UIApplicationDelegate](uiapplicationdelegate.md) 对象来响应生命周期事件。

> [!note] 注意
> 当你在 App 中启用场景（scene）支持后，iOS 13 及更高版本会始终使用你的场景委托（scene delegate）。在 iOS 12 及更早版本中，系统会使用你的 App 委托（app delegate）。

### 响应基于场景的生命周期事件

UIKit 会为每个场景分别提供独立的生命周期事件。一个场景代表 App 用户界面在设备上的一个实例。用户可以为每个 App 创建多个场景，并分别显示和隐藏它们。由于每个场景都有自己的生命周期，因此它们可以处于不同的执行状态。例如，一个场景可能在前台，而其他场景在后台或被挂起。

> [!important] 重要
> 场景支持是一项可选加入（opt-in）功能。要启用基本支持，请将 [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md) 键添加到 App 的 `Info.plist` 文件中，如 [指定你的 App 支持的场景](specifying-the-scenes-your-app-supports.md) 中所述。

下图展示了场景的状态转换。当用户或系统为你的 App 请求一个新场景时，UIKit 会创建它并将其置于未连接（unattached）状态。用户请求的场景会快速移至前台并显示在屏幕上。系统请求的场景通常会移至后台以便处理事件。例如，系统可能会在后台启动该场景以处理位置事件。当用户关闭你的 App 的用户界面时，UIKit 会将关联的场景移至后台状态，并最终移至挂起（suspended）状态。UIKit 可以随时断开后台或挂起场景的连接以回收其资源，并将该场景返回到未连接状态。

![](../../../attachments/bb875ff5b6507138789b710fc57afaf1/media-3233330@2x.png)

<sub>一个示意图，展示了基于场景的 App 的状态转换。场景从未连接状态开始，然后移至前台活跃或后台状态。前台非活跃状态充当过渡状态。</sub>

使用场景转换来执行以下任务：

- 当 UIKit 将一个场景连接到你的 App 时，配置场景的初始 UI 并加载场景所需的数据。
- 在转换到前台活跃状态时，配置你的 UI 并准备与用户交互。请参阅 [准备你的 UI 在前台运行](preparing-your-ui-to-run-in-the-foreground.md)。
- 在离开前台活跃状态时，保存数据并让 App 的行为安静下来。请参阅 [准备你的 UI 在后台运行](preparing-your-ui-to-run-in-the-background.md)。
- 在进入后台状态时，完成关键任务，尽可能多地释放内存，并为你的 App 快照（snapshot）做好准备。请参阅 [准备你的 UI 在后台运行](preparing-your-ui-to-run-in-the-background.md)。
- 在场景断开连接时，清理与该场景关联的所有共享资源。
- 除了场景相关的事件外，你还必须使用 [UIApplicationDelegate](uiapplicationdelegate.md) 对象响应 App 的启动。关于 App 启动时该做什么的信息，请参阅 [响应你的 App 的启动](responding-to-the-launch-of-your-app.md)。

### 响应基于 App 的生命周期事件

在 iOS 12 及更早版本中，UIKit 会将所有生命周期事件传递给 [UIApplicationDelegate](uiapplicationdelegate.md) 对象。App 委托（app delegate）管理 App 的所有窗口，包括显示在外接显示器上的窗口。因此，App 状态转换会影响你的整个 UI，包括外部显示器上的内容。

下图展示了涉及 App 委托对象的状态转换。启动后，系统会将 App 置于非活跃或后台状态，具体取决于 UI 是否即将出现在屏幕上。当启动到前台时，系统会自动将 App 转换为活跃状态。之后，状态会在活跃和后台之间波动，直到 App 终止。

![](../../../attachments/9c1b7e06f4aafb7cb32cf9a923f84e01/media-3233333@2x.png)

<sub>一个示意图，展示了无场景的 App 的状态转换。App 启动到活跃或后台状态。App 会经过非活跃状态进行转换。</sub>

使用 App 转换来执行以下任务：

- 在启动时，初始化 App 的数据结构和 UI。请参阅 [响应你的 App 的启动](responding-to-the-launch-of-your-app.md)。
- 在激活时，完成 UI 的配置并准备与用户交互。请参阅 [准备你的 UI 在前台运行](preparing-your-ui-to-run-in-the-foreground.md)。
- 在失活时，保存数据并让 App 的行为安静下来。请参阅 [准备你的 UI 在后台运行](preparing-your-ui-to-run-in-the-background.md)。
- 在进入后台状态时，完成关键任务，尽可能多地释放内存，并为你的 App 快照做好准备。请参阅 [准备你的 UI 在后台运行](preparing-your-ui-to-run-in-the-background.md)。
- 在终止时，立即停止所有工作并释放任何共享资源。请参阅 [- applicationWillTerminate:](<uiapplicationdelegate/applicationwillterminate(__).md>)。

### 响应其他重要事件

除了处理生命周期事件外，App 还必须准备好处理下表中列出的事件。使用你的 [UIApplicationDelegate](uiapplicationdelegate.md) 对象来处理大部分这些事件。在某些情况下，你也可以使用通知（notification）来处理它们，从而能够从 App 的其他部分做出响应。

| 事件 | 响应 |
|---|---|
| 内存警告 | 当 App 的内存使用量过高时收到。减少 App 使用的内存量；请参阅 [响应内存警告](responding-to-memory-warnings.md)。 |
| 受保护数据变为可用/不可用 | 当用户锁定或解锁其设备时收到。请参阅 [- applicationProtectedDataDidBecomeAvailable:](<uiapplicationdelegate/applicationprotecteddatadidbecomeavailable(__).md>) 和 [- applicationProtectedDataWillBecomeUnavailable:](<uiapplicationdelegate/applicationprotecteddatawillbecomeunavailable(__).md>)。 |
| 接力任务 | 当 [NSUserActivity](../foundation/nsuseractivity.md) 对象需要被处理时收到。请参阅 [- application:didUpdateUserActivity:](<uiapplicationdelegate/application(__didupdate_).md>)。 |
| 时间变更 | 针对几种不同的时间变更（例如手机运营商发送时间更新时）收到。请参阅 [- applicationSignificantTimeChange:](<uiapplicationdelegate/applicationsignificanttimechange(__).md>)。 |
| 打开 URL | 当你的 App 需要打开一个资源时收到。请参阅 [- application:openURL:options:](<uiapplicationdelegate/application(__open_options_).md>)。 |

## 主题

### 行为事件

- [响应内存警告](responding-to-memory-warnings.md) — 当系统要求时释放内存。

## 另请参阅

### 生命周期

- [响应你的 App 的启动](responding-to-the-launch-of-your-app.md) — 初始化 App 的数据结构，准备 App 运行，并响应系统在启动时发出的任何请求。
- [UIApplication](uiapplication.md) — 针对在 iOS 中运行的 App 的集中控制和协调点。
- [UIApplicationDelegate](uiapplicationdelegate.md) — 一组用于管理 App 共享行为的方法。
- [场景](scenes.md) — 同时管理 App UI 的多个实例，并将资源引导至 UI 的适当实例。
- [过渡到基于 UIKit 场景的生命周期](transitioning-to-the-uikit-scene-based-life-cycle.md) — 采用基于场景的生命周期来替换 UIKit 中的 App 委托生命周期。
