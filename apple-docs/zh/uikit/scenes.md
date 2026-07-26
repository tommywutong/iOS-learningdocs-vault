---
title: 场景
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/scenes
source_url: 'https://developer.apple.com/documentation/uikit/scenes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/scenes.json'
content_hash: 'sha256:f6fd2136d0226ae8'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md)

# 场景

<sub>API 集合</sub>

同时管理你 App 界面的多个实例，并将资源引导至合适的界面实例。

## 概述

UIKit 使用一个 [UIWindowScene](uiwindowscene.md) 对象来管理你 App 界面的每个实例。一个 _场景（scene）_ 包含用于呈现一个界面实例的窗口和视图控制器。每个场景还有一个对应的 [UIWindowSceneDelegate](uiwindowscenedelegate.md) 对象，你可以用它来协调 UIKit 与你的 App 之间的交互。多个场景彼此并发运行，共享同一块内存和 App 进程空间。因此，同一个 App 可能同时存在多个活跃的场景和场景委托对象。

![一张显示两个 Notes App 实例在 iPad 上并排运行的图像。](../../../attachments/2ca9357918eb89b8fdb96cf9e324b12a/media-3335652@2x.png)

从你的 [UIApplicationDelegate](uiapplicationdelegate.md) 对象中管理新场景的配置。

## 主题

### 基础

- [Preparing your UI to run in the foreground](preparing-your-ui-to-run-in-the-foreground.md) — 配置你的 App，使其能够显示在屏幕上。
- [Preparing your UI to run in the background](preparing-your-ui-to-run-in-the-background.md) — 准备你的 App 以便被挂起。

### 窗口场景

- [Supporting multiple windows on iPad](supporting-multiple-windows-on-ipad.md) — 支持 App 界面的并排实例，并创建新窗口。
- [UIWindowSceneDelegate](uiwindowscenedelegate.md) — 你用来管理场景中发生的特定于 App 的任务的附加方法。
- [UIWindowScene](uiwindowscene.md) — 一个为你的 App 管理一个或多个窗口的场景。
- [UIScene](uiscene.md) — 一个代表你 App 用户界面的一个实例的对象。
- [UISceneDelegate](uiscenedelegate.md) — 你用来响应场景内发生的生命周期事件的核心方法。

### 配置

- [Specifying the scenes your app supports](specifying-the-scenes-your-app-supports.md) — 告知系统你 App 的场景，包括你用来管理每个场景及其初始用户界面的对象。
- [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md) — 有关 App 基于场景的生命周期支持的信息。
- [UISceneConfiguration](uisceneconfiguration.md) — UIKit 在创建特定场景时所使用的对象和 Storyboard 的信息。
- [UISceneSession](uiscenesession.md) — 一个包含你 App 某个场景相关信息的对象。

### 激活与销毁

- [UISceneActivationConditions](uisceneactivationconditions.md) — 定义 UIKit 何时激活当前场景的一组条件。
- [ActivationRequestOptions](uiscene/activationrequestoptions.md) — 一个对象，包含你希望系统在激活与某个场景关联的会话时使用的信息。
- [UIWindowSceneDestructionRequestOptions](uiwindowscenedestructionrequestoptions.md) — 一个对象，包含从你的 App 中移除窗口场景时要使用的信息。
- [UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md) — 一个你传递给 UIKit、用于从你的 App 中永久移除某个场景及其关联会话的对象。
- [UISceneClosureConfirmation](uisceneclosureconfirmation.md) — 一项配置，指定在用户操作导致场景会话被销毁、场景断开连接之前显示的确认对话框。 _(beta)_

### 场景配件

- [UISceneAccessory](uisceneaccessory.md) — 一种可用于为特定类型的场景配件呈现进行注册的类型。 _(beta)_
- [UISceneAccessoryRegistration](uisceneaccessoryregistration.md) — 一种表示给定场景配件注册信息的类型。 _(beta)_

### 场景配件

- [Presenting content on a connected display](presenting-content-on-a-connected-display.md) — 用来自你 App 的附加内容填充已连接的显示器。
- [UISceneAccessory](uisceneaccessory.md) — 一种可用于为特定类型的场景配件呈现进行注册的类型。 _(beta)_
- [UISceneAccessoryRegistration](uisceneaccessoryregistration.md) — 一种表示给定场景配件注册信息的类型。 _(beta)_

### URL 管理

- [UIOpenURLContext](uiopenurlcontext.md) — 一个系统提供的对象，包含打开单个 URL 所需的信息。
- [OpenExternalURLOptions](uiscene/openexternalurloptions.md) — 你在请求某个场景打开 URL 时指定的选项。

### 错误

- [Code](uisceneerror/code.md) — 与场景相关问题的错误代码。
- [UISceneError](uisceneerror.md) — 创建或管理场景过程中返回的错误。
- [UISceneErrorDomain](uisceneerrordomain.md) — 场景相关错误的域。

## 另请参阅

### 生命周期

- [Managing your app’s life cycle](managing-your-app-s-life-cycle.md) — 在 App 处于前台或后台时响应系统通知，并处理其他重要的系统相关事件。
- [Responding to the launch of your app](responding-to-the-launch-of-your-app.md) — 初始化 App 的数据结构，为 App 运行做好准备，并响应系统发出的任何启动时请求。
- [UIApplication](uiapplication.md) — 在 iOS 中运行的 App 的集中控制与协调点。
- [UIApplicationDelegate](uiapplicationdelegate.md) — 一组用于管理 App 共享行为的方法。
- [Transitioning to the UIKit scene-based life cycle](transitioning-to-the-uikit-scene-based-life-cycle.md) — 采用基于场景的生命周期，以取代 UIKit 中的 App 委托生命周期。
