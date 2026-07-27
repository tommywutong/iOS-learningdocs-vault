---
title: 通知
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/notifications
source_url: 'https://developer.apple.com/documentation/foundation/notifications'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notifications.json'
content_hash: 'sha256:e9162d4b4dbd90cc'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 通知

<sub>API 集合</sub>

用于广播信息和订阅广播的设计模式。

## 主题

### 键值观察

- [NSKeyValueObserving](../objectivec/nskeyvalueobserving.md) — 对象为接收其他对象指定属性发生更改的通知而采纳的非正式协议。

### 通知

- [Notification](notification.md) — 通过通知中心广播给所有已注册观察者（observer）的信息容器。
- [NotificationCenter](notificationcenter.md) — 一种通知分派机制，可以向已注册的观察者广播信息。
- [NotificationQueue](notificationqueue.md) — 通知中心缓冲区。

### 跨进程通知

- [DistributedNotificationCenter](distributednotificationcenter.md) — 一种通知分派机制，可跨任务边界广播通知。

## 另请参阅

### App 支持

- [任务管理](task-management.md) — 管理 App 的工作及其与 Handoff 和“快捷指令”等系统服务的交互方式。
- [资源](resources.md) — 访问与你的 App 捆绑在一起的资源及其他数据。
- [App 扩展支持](app-extension-support.md) — 管理 App 扩展与托管它的 App 之间的交互。
- [错误与异常](errors-and-exceptions.md) — 响应与 API 交互时出现的问题，并微调 App 以改善调试体验。
- [脚本支持](scripting-support.md) — 允许用户使用 AppleScript 和其他自动化技术控制你的 App，或从 App 内运行脚本。
