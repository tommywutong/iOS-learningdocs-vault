---
title: 任务管理
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/task-management
source_url: 'https://developer.apple.com/documentation/foundation/task-management'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/task-management.json'
content_hash: 'sha256:4b386fa5c95cb9cd'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 任务管理

<sub>API 集合</sub>

管理 App 的工作及其与 Handoff 和「快捷指令」等系统服务的交互方式。

## 主题

### 撤销

- [UndoManager](undomanager.md) — 一个通用的操作记录器，支持撤销和重做。

### 进度

- [ProgressReporting](progressreporting.md) — 使用单一进度实例报告进度的对象的接口。
- [Progress](progress.md) — 一个向用户传达指定任务正在进行中的进度的对象。

### 操作

- [Operation](operation.md) — 表示与单个任务相关的代码和数据的抽象类。
- [OperationQueue](operationqueue.md) — 调节操作执行的队列。
- [BlockOperation](blockoperation.md) — 管理一个或多个 block 并发执行的操作。

### 调度

- [Timer](timer.md) — 经过特定时间间隔后触发，并向目标对象发送指定消息的定时器。

### 活动共享

- [Creating a user activity object](creating-a-user-activity-object.md) — 确定关键的用户交互，并包含用于在之后恢复它们的信息。
- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md) — 直接创建、发送和接收用户活动。
- [Continuing User Activities with Handoff](continuing-user-activities-with-handoff.md) — 定义并管理你 App 的哪些活动可以在设备之间继续。
- [Increasing App Usage with Suggestions Based on User Activities](increasing-app-usage-with-suggestions-based-on-user-activities.md) — 从 App 中捕获信息并将其作为主动建议展示在整个系统中，从而提供连续的用户体验。
- [Supporting the creation of Quick Notes](supporting-the-creation-of-quick-notes.md) — 支持创建包含你 App 内容的备忘录。
- [NSUserActivity](nsuseractivity.md) — 你的 App 在某一时刻状态的表示形式。
- [NSUserActivityDelegate](nsuseractivitydelegate.md) — 用户活动实例通过其向委托通知更新的接口。

### 系统交互

- [ProcessInfo](processinfo.md) — 有关当前进程的信息集合。
- [NSBackgroundActivityScheduler](nsbackgroundactivityscheduler.md) — 一种任务调度器，适合可在后台运行的低优先级操作。

### 用户通知

- [NSUserNotification](nsusernotification.md) — 一种可安排在通知中心显示的通知。_(已废弃)_
- [NSUserNotificationAction](nsusernotificationaction.md) — 用户可采取的响应收到通知的操作。_(已废弃)_
- [NSUserNotificationCenter](nsusernotificationcenter.md) — 一个将通知从 App 交付给用户的对象。_(已废弃)_
- [NSUserNotificationCenterDelegate](nsusernotificationcenterdelegate.md) — 一个可用于自定默认通知中心行为的接口。

### Combine 集成

- [Published](published.md) — Combine 框架中一种类型的类型别名，用于发布标记了某种特性的属性。
- [ObservableObject](observableobject.md) — Combine 框架中一种类型的类型别名，对应拥有在对象变化之前发出通知的发布者的对象。

## 另请参阅

### App 支持

- [Resources](resources.md) — 访问与你的 App 捆绑在一起的资源及其他数据。
- [Notifications](notifications.md) — 用于广播信息和订阅广播的设计模式。
- [App Extension Support](app-extension-support.md) — 管理 App 扩展与托管它的 App 之间的交互。
- [Errors and Exceptions](errors-and-exceptions.md) — 响应与 API 交互时出现的问题，并微调 App 以改善调试体验。
- [Scripting Support](scripting-support.md) — 允许用户使用 AppleScript 和其他自动化技术控制你的 App，或从 App 内运行脚本。
