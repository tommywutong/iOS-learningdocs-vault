---
title: 已废弃符号
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplicationdelegate-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate-deprecated-symbols.json'
content_hash: 'sha256:e01a2224a11f474f'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md) · [UIApplicationDelegate](uiapplicationdelegate.md)

# 已废弃符号

<sub>API 集合</sub>

不再受支持的符号。

## 主题

### 已废弃

- [- application:didRegisterUserNotificationSettings:](<uiapplicationdelegate/application(__didregister_).md>) — 调用此方法以告知委托（delegate），可用于引起用户注意的本地和远程通知类型。_（已废弃）_
- [- application:didReceiveLocalNotification:](<uiapplicationdelegate/application(__didreceive_).md>) — 正在运行的 App 收到本地通知时发送给委托。_（已废弃）_
- [- application:didReceiveRemoteNotification:](<uiapplicationdelegate/application(__didreceiveremotenotification_).md>) — 当 App 收到远程通知时调用。_（已废弃）_
- [- application:handleActionWithIdentifier:forLocalNotification:completionHandler:](<uiapplicationdelegate/application(__handleactionwithidentifier_for_completionhandler_).md>) — 当用户从本地通知的提醒面板中选择自定义操作而激活 App 时调用。_（已废弃）_
- [- application:handleActionWithIdentifier:forLocalNotification:withResponseInfo:completionHandler:](<uiapplicationdelegate/application(__handleactionwithidentifier_for_withresponseinfo_completionhandler_).md>) — 当用户从本地通知中选择操作而激活 App 时调用。_（已废弃）_
- [- application:handleActionWithIdentifier:forRemoteNotification:completionHandler:](<uiapplicationdelegate/application(__handleactionwithidentifier_forremotenotification_completionhandler_).md>) — 告知 App 委托执行远程通知指定的自定义操作。_（已废弃）_
- [- application:handleActionWithIdentifier:forRemoteNotification:withResponseInfo:completionHandler:](<uiapplicationdelegate/application(__handleactionwithidentifier_forremotenotification_withresponseinfo_completionhandler_).md>) — 当用户从远程通知中选择操作而激活 App 时调用。_（已废弃）_
- [- application:handleOpenURL:](<uiapplicationdelegate/application(__handleopen_).md>) — 要求委托打开 URL 所标识的资源。_（已废弃）_
- [- application:openURL:sourceApplication:annotation:](<uiapplicationdelegate/application(__open_sourceapplication_annotation_).md>) — 要求委托打开 URL 所标识的资源。_（已废弃）_
- [- application:willChangeStatusBarOrientation:duration:](<uiapplicationdelegate/application(__willchangestatusbarorientation_duration_).md>) — 在状态栏的界面方向即将发生变化时告知委托。_（已废弃）_
- [- application:didChangeStatusBarOrientation:](<uiapplicationdelegate/application(__didchangestatusbarorientation_).md>) — 在状态栏的界面方向发生变化时告知委托。_（已废弃）_
- [- application:willChangeStatusBarFrame:](<uiapplicationdelegate/application(__willchangestatusbarframe_).md>) — 在状态栏的 frame 即将发生变化时告知委托。_（已废弃）_
- [- application:didChangeStatusBarFrame:](<uiapplicationdelegate/application(__didchangestatusbarframe_).md>) — 在状态栏的 frame 发生变化时告知委托。_（已废弃）_
- [- application:handleIntent:completionHandler:](<uiapplicationdelegate/application(__handle_completionhandler_).md>) — 要求委托直接处理指定的 SiriKit 意图（intent）。_（已废弃）_
- [- application:performFetchWithCompletionHandler:](<uiapplicationdelegate/application(__performfetchwithcompletionhandler_).md>) — 告知 App，如果有数据要下载，可以开始获取操作。_（已废弃）_
- [- application:shouldSaveApplicationState:](<uiapplicationdelegate/application(__shouldsaveapplicationstate_).md>) — 询问委托是否保留 App 状态。_（已废弃）_
- [- application:shouldRestoreApplicationState:](<uiapplicationdelegate/application(__shouldrestoreapplicationstate_).md>) — 询问委托是否恢复 App 已存储的状态。_（已废弃）_

## 另请参阅

### 已废弃

- [- applicationDidFinishLaunching:](<uiapplicationdelegate/applicationdidfinishlaunching(__).md>) — 在 App 完成启动时告知委托。_（已废弃）_
