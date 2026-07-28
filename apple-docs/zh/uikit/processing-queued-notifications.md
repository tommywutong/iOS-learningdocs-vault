---
title: 处理排队的通知
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/processing-queued-notifications
source_url: 'https://developer.apple.com/documentation/uikit/processing-queued-notifications'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/processing-queued-notifications.json'
content_hash: 'sha256:ee2c50293411f934'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md) · [场景](scenes.md) · [准备在前台运行 UI](preparing-your-ui-to-run-in-the-foreground.md)

# 处理排队的通知

<sub>文章</sub>

从挂起状态恢复时响应通知。

## 概述

当设置或设备条件发生变化时，系统会生成通知，以便 App 做出相应响应。这些通知会立即递送给正在运行的 App，但对于已挂起的 App，递送会延迟。对于已挂起的 App，会在 App 再次开始运行（无论是在前台还是后台）后尽快递送待处理通知。

下表列出了 App 再次开始运行后可能收到的通知。你必须显式为这些通知添加观察者才能接收它们。系统会合并多个相关通知，使 App 仅收到一条包含净变化的通知。

| 事件 | 通知 |
|---|---|
| 用户更改了 App 的偏好设置 | [didChangeNotification](../foundation/userdefaults/didchangenotification.md) |
| 当前语言或区域设置发生变化 | [currentLocaleDidChangeNotification](../foundation/nslocale/currentlocaledidchangenotification.md) |
| 显示器的屏幕模式发生变化 | [UIScreenModeDidChangeNotification](uiscreen/modedidchangenotification.md) |
| 外接显示器已连接或断开连接 | [UIScreenDidConnectNotification](uiscreen/didconnectnotification.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [UIScreenDidDisconnectNotification](uiscreen/diddisconnectnotification.md) |
| 配件已连接或断开连接 | [EAAccessoryDidConnect](../foundation/nsnotification/name-swift.struct/eaaccessorydidconnect.md) (Swift) 或 [EAAccessoryDidConnectNotification](../externalaccessory/eaaccessorydidconnectnotification.md) (Objective-C) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [EAAccessoryDidDisconnect](../foundation/nsnotification/name-swift.struct/eaaccessorydiddisconnect.md) (Swift) 或 [EAAccessoryDidDisconnectNotification](../externalaccessory/eaaccessorydiddisconnectnotification.md) (Objective-C) |
| 用户的 iCloud 账户状态发生变化 | [NSUbiquityIdentityDidChange](../foundation/nsnotification/name-swift.struct/nsubiquityidentitydidchange.md) |
| 设备方向发生变化 | [UIDeviceOrientationDidChangeNotification](uidevice/orientationdidchangenotification.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)（UIKit 会在适当时自动更新视图控制器（view controller）的界面方向。） |
| 出现显著的时间变化 | [UIApplicationSignificantTimeChangeNotification](uiapplication/significanttimechangenotification.md) |
| 电池电量或电池状态发生变化 | [UIDeviceBatteryLevelDidChangeNotification](uidevice/batteryleveldidchangenotification.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [UIDeviceBatteryStateDidChangeNotification](uidevice/batterystatedidchangenotification.md) |
| 设备与用户之间的距离发生变化 | [UIDeviceProximityStateDidChangeNotification](uidevice/proximitystatedidchangenotification.md) |

已挂起的 App 再次开始运行时，系统会先在 App 的主线程（main thread）上递送所有排队的通知，然后才递送任何触控事件或用户输入。请尽快处理所有通知。
