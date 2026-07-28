---
title: 通知中心
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter.json'
content_hash: 'sha256:441719807c829835'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 通知中心

<sub>类</sub>

一种用于向已注册观察者广播信息的通知调度机制。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NotificationCenter
```

## 概述

调用方通过向通知中心（NotificationCenter）注册，以接收下述一种或两种内容：

- [NSNotification](nsnotification.md) 对象——当使用 Objective‑C 或仅支持 [NSNotification](nsnotification.md) 的框架时使用。对象通过 `[- addObserver:selector:name:object:](<notificationcenter/addobserver(__selector_name_object_).md>)` 或 `[- addObserverForName:object:queue:usingBlock:](<notificationcenter/addobserver(forname_object_queue_using_).md>)` 方法向通知中心注册，以接收通知（[NSNotification](nsnotification.md) 对象），需指定通知名称以及可选的源对象。当调用方将自己添加为观察者时，它会指定其应接收哪些通知。
- [MainActorMessage](notificationcenter/mainactormessage.md) 和 [AsyncMessage](notificationcenter/asyncmessage.md) 实例——用于 Swift 代码，提供强类型、恰当的 Actor 隔离以及更地道的 Swift 体验。调用方通过使用各种形式的 `addObserver(of:for:using:)` 方法向通知中心注册，并指定一个消息类型或便捷的 [MessageIdentifier](notificationcenter/messageidentifier.md) 来标识要接收的通知消息。有关此 API 的更多信息，请参阅[通知中心消息](notification-center-messages.md)。

调用方可以为许多不同的通知添加观察者，甚至可以为来自不同源对象的同一通知名称或消息类型添加观察者。

每个正在运行的 App 都有一个 [defaultCenter](notificationcenter/default.md) 通知中心，你还可以创建新的通知中心以在特定上下文中组织通信。

一个通知中心只能在同一程序内传递通知。在 macOS 上，如果你想向其他进程发布通知或接收来自其他进程的通知，请改用 [DistributedNotificationCenter](distributednotificationcenter.md)。

## 关系

- **继承自**：[NSObject](../objectivec/nsobject-swift.class.md)

- **被继承者**：[DistributedNotificationCenter](distributednotificationcenter.md)

- **遵循**：[CVarArg](../swift/cvararg.md)、[CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)、[CustomStringConvertible](../swift/customstringconvertible.md)、[Equatable](../swift/equatable.md)、[Hashable](../swift/hashable.md)、[NSObjectProtocol](../objectivec/nsobjectprotocol.md)、[Sendable](../swift/sendable.md)、[SendableMetatype](../swift/sendablemetatype.md)

## 主题

### 获取默认通知中心

- [defaultCenter](notificationcenter/default.md) — App 的默认通知中心。

### 添加和移除通知观察者

- [`- addObserverForName:object:queue:usingBlock:`](<notificationcenter/addobserver(forname_object_queue_using_).md>) — 在通知中心添加一条条目，以接收传递给所提供 block 的通知。
- [`- addObserver:selector:name:object:`](<notificationcenter/addobserver(__selector_name_object_).md>) — 在通知中心添加一条条目，以使用所提供的选择器（selector）调用通知。
- [`- removeObserver:name:object:`](<notificationcenter/removeobserver(__name_object_).md>) — 从通知中心的调度表中移除匹配的条目。
- [`- removeObserver:`](<notificationcenter/removeobserver(__)-2yciv.md>) — 从通知中心的调度表中移除指定观察者的所有条目。

### 发布通知

- [`- postNotification:`](<notificationcenter/post(__)-3x2st.md>) — 将给定的通知发布到通知中心。
- [`- postNotificationName:object:userInfo:`](<notificationcenter/post(name_object_userinfo_).md>) — 使用给定的名称、发送者和信息创建一条通知，并将其发布到通知中心。
- [`- postNotificationName:object:`](<notificationcenter/post(name_object_).md>) — 使用给定的名称和发送者创建一条通知，并将其发布到通知中心。

### 以异步序列接收通知

- [notifications(named:object:)](<notificationcenter/notifications(named_object_).md>) — 返回一个异步序列，其中包含此通知中心针对给定通知名称和可选源对象所生成的通知。
- [Notifications](notificationcenter/notifications.md) — 由通知中心生成的异步通知序列。

### 以 Combine 发布者接收通知

- [publisher(for:object:)](<notificationcenter/publisher(for_object_).md>) — 返回一个发布者，该发布者在广播通知时发出事件。
- [Publisher](notificationcenter/publisher.md) — 一个发布者，在广播通知时发出元素。

### 将通知中心与 Actor 隔离配合使用

- [通知中心消息](notification-center-messages.md) — 将 Foundation 的通知中心与 Swift 并发（Swift concurrency）配合使用。

## 另请参阅

### 通知

- [Notification](notification.md) — 一种容器，用于存放通过通知中心广播给所有已注册观察者的信息。
- [NotificationQueue](notificationqueue.md) — 一个通知中心缓冲区。
