---
title: 通知中心消息
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/notification-center-messages
source_url: 'https://developer.apple.com/documentation/foundation/notification-center-messages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notification-center-messages.json'
content_hash: 'sha256:7122f7dd714cbe81'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [通知](notifications.md) · [NotificationCenter](notificationcenter.md)

# 通知中心消息

<sub>API 集合</sub>

将 Foundation 的通知中心与 Swift 并发（Swift concurrency）配合使用。

## 概述

在 Swift 中，即使 [Notification](notification.md) 发布到已知隔离域，其类型仍然是 `nonisolated`。为了提供具体的隔离信息并更好地支持 Swift 并发，`NotificationCenter` 定义了两种消息类型。[MainActorMessage](notificationcenter/mainactormessage.md) 绑定到主要 Actor（main actor），而 [AsyncMessage](notificationcenter/asyncmessage.md) 使用任意隔离域。框架扩展这些类型以定义不同的消息；这些消息通常对应某个现有的 [Name](notification/name-swift.typealias.md)，并为其值声明实例属性，而不是使用 `userInfo` 字典。因此，当消息不使用属性或只包含可发送的属性时，它们可以符合 [Sendable](../swift/sendable.md)。

如果你的项目只需支持 Swift，可以只使用 `Message` 类型。对于同时包含 Objective-C 和 Swift 代码的项目，请同时定义 [Notification](notification.md) 及对应的 `Message` 类型。

### 发布和观察消息

你可以使用 `post(_:subject:)` 方法发布消息，传入一个消息实例，并可选择提供主题。要接收消息，请使用 `addObserver(of:for:using:)` 方法添加观察者。此方法的重载允许你观察来自单个对象或给定类型任意对象的消息。当你丢弃 `addObserver(of:for:using:)` 返回的令牌，或显式调用 [removeObserver(_:)](<notificationcenter/removeobserver(__)-2gmm0.md>) 后，观察便会结束。

你也可以使用 `messages(of:for:bufferSize:)` 方法，以 [AsyncSequence](../swift/asyncsequence.md) 形式接收消息。

`addObserver(of:for:using:)` 和 `messages(of:for:bufferSize:)` 的若干变体接受 [MessageIdentifier](notificationcenter/messageidentifier.md)。框架可以实现该类型，以便像 [SE-0299](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0299-extend-generic-static-member-lookup.md) 所述，在调用点提供类型化且易于使用的便捷体验。

### 将消息与 SDK 配合使用

许多系统框架（包括 Foundation、UIKit 和 AppKit）都采纳 [MainActorMessage](notificationcenter/mainactormessage.md) 和 [AsyncMessage](notificationcenter/asyncmessage.md) 类型，以方便在并发安全的 Swift 代码中使用其通知。以下示例展示如何观察 Foundation 的 [TimeZone](timezone.md) 类型所发出的 [systemTimeZoneDidChange](notificationcenter/messageidentifier/systemtimezonedidchange.md) 消息，该消息包含 [previousTimeZone](timezone/systemtimezonedidchangemessage/previoustimezone.md) 属性。

```
/// 注意：只要你打算继续观察，就应将 `token` 存储在属性中。
token = NotificationCenter.default.addObserver(of: TimeZone.self,
                                               for: .systemTimeZoneDidChange)
{ message in
    let identifier = message.previousTimeZone?.identifier ?? "(unknown)"
    print("Time zone changed from \(identifier).")
}
```

为了与现有通知代码配合使用，[MainActorMessage](notificationcenter/mainactormessage.md) 和 [AsyncMessage](notificationcenter/asyncmessage.md) 定义了辅助方法，符合这些协议的类型需实现这些方法，以便在消息与对应通知之间相互转换。

## 主题

### 声明消息

- [MainActorMessage](notificationcenter/mainactormessage.md) — 一种协议，用于创建可发布到通知中心并绑定到主要 Actor 的类型。
- [AsyncMessage](notificationcenter/asyncmessage.md) — 一种协议，用于创建可发布到通知中心的类型，并将其发布到任意隔离域。

### 使用消息标识符

- [MessageIdentifier](notificationcenter/messageidentifier.md) — 用于将给定消息与给定类型关联的可选标识符。
- [BaseMessageIdentifier](notificationcenter/basemessageidentifier.md) — 定义可选 Message 标识符时使用的类型。

### 观察并发安全通知

- [addObserver(of:for:using:)](<notificationcenter/addobserver(of_for_using_)-4d19x.md>) — 向中心添加观察者，以观察在主要 Actor 上传递的、具有给定主题和标识符的消息。
- [addObserver(of:for:using:)](<notificationcenter/addobserver(of_for_using_)-90os.md>) — 向中心添加观察者，以观察在主要 Actor 上传递的、具有给定主题和标识符的消息。
- [addObserver(of:for:using:)](<notificationcenter/addobserver(of_for_using_)-56bn4.md>) — 向中心添加观察者，以观察在主要 Actor 上传递的、具有给定主题和消息类型的消息。
- [addObserver(of:for:using:)](<notificationcenter/addobserver(of_for_using_)-twm3.md>) — 向中心添加观察者，以观察异步传递的、具有给定主题和标识符的消息。
- [addObserver(of:for:using:)](<notificationcenter/addobserver(of_for_using_)-t1wr.md>) — 向中心添加观察者，以观察异步传递的、具有给定主题和消息类型的消息。
- [addObserver(of:for:using:)](<notificationcenter/addobserver(of_for_using_)-64uw3.md>) — 向中心添加观察者，以观察异步传递的、具有给定主题和消息类型的消息。
- [removeObserver(_:)](<notificationcenter/removeobserver(__)-2gmm0.md>) — 停止由给定观察令牌表示的观察。
- [ObservationToken](notificationcenter/observationtoken.md) — 表示在通知中心进行的一次观察者注册的唯一令牌。

### 以异步序列形式接收通知

- [messages(of:for:bufferSize:)](<notificationcenter/messages(of_for_buffersize_)-4tof0.md>) — 返回此中心针对给定主题和标识符生成的消息异步序列。
- [messages(of:for:bufferSize:)](<notificationcenter/messages(of_for_buffersize_)-1ub69.md>) — 返回此中心针对给定主题类型和标识符生成的消息异步序列。
- [messages(of:for:bufferSize:)](<notificationcenter/messages(of_for_buffersize_)-623kg.md>) — 返回此中心针对给定主题和消息类型生成的消息异步序列。

### 发布通知消息

- [post(_:subject:)](<notificationcenter/post(__subject_)-87dbk.md>) — 将给定主要 Actor 消息发布到通知中心。
- [post(_:)](<notificationcenter/post(__)-19s7b.md>) — 将给定主要 Actor 消息发布到通知中心。
- [post(_:subject:)](<notificationcenter/post(__subject_)-5271w.md>) — 将给定异步消息发布到通知中心。
- [post(_:)](<notificationcenter/post(__)-7ia4j.md>) — 将给定异步消息发布到通知中心。
