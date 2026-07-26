---
title: App Store Server Notifications
framework: App Store Server Notifications
symbol_kind: module
role: collection
role_heading: Web Service
platforms: [App Store Server Notifications 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/appstoreservernotifications
source_url: 'https://developer.apple.com/documentation/appstoreservernotifications'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appstoreservernotifications.json'
content_hash: 'sha256:8cf29d22e2979dd0'
translated: true
---

> 导航： [技术](technologies.md)

# App Store Server Notifications

<sub>Web Service</sub>

借助 App Store 的服务器通知实时监控 App 内购买事件，并了解未上报的外部购买 token。

## 概述

App Store Server Notifications 是一项服务器到服务器的服务，为 App 内购买事件及未上报的外部购买 token 发送实时通知。使用通知中的数据来更新你的用户账户数据库，并监控和响应 App 内购买退款。有关与 [External Purchase](storekit/external-purchase.md) API 相关的通知，请参阅 [externalPurchaseToken](appstoreservernotifications/externalpurchasetoken.md)。

> [!important] 重要
> [App Store Server Notifications V1](appstoreservernotifications/app-store-server-notifications-v1.md) 端点以及版本 1 通知 [notification_type](appstoreservernotifications/notification_type.md) 已废弃。请在你的服务器上实现 [App Store Server Notifications V2](appstoreservernotifications/app-store-server-notifications-v2.md) 端点，改为接收版本 2 通知。

要接收来自 App Store 的服务器通知，请在 App Store Connect 中提供你服务器的 HTTPS URL。选择接收生产环境和沙盒环境的通知。有关更多信息，请参阅 [启用 App Store Server Notifications](appstoreservernotifications/enabling-app-store-server-notifications.md)。

你的服务器负责解析、解读服务器到服务器的通知投递，并做出响应。有关更多信息，请参阅 [接收 App Store Server Notifications](appstoreservernotifications/receiving-app-store-server-notifications.md) 和 [响应 App Store Server Notifications](appstoreservernotifications/responding-to-app-store-server-notifications.md)。

### 处理 App 内购买通知

通知涵盖 App 内购买生命周期中的各类事件，包括购买、订阅续订、优惠兑换、退款等。有关通知类型的完整列表，请参阅 [App Store Server Notifications V2](appstoreservernotifications/app-store-server-notifications-v2.md) 的 [notificationType](appstoreservernotifications/notificationtype.md)。

结合通知类型以及交易和订阅续订信息，来更新客户的服务，或根据你的业务逻辑呈现促销优惠。

### 处理外部购买 token 通知

[notificationType](appstoreservernotifications/notificationtype.md) 为 `EXTERNAL_PURCHASE_TOKEN`，且 [subtype](appstoreservernotifications/subtype.md) 为 `UNREPORTED` 表示 Apple 已为你的 App 生成了一个外部购买 token，但尚未收到该 token 的上报。该通知在 [responseBodyV2DecodedPayload](appstoreservernotifications/responsebodyv2decodedpayload.md) 的 [externalPurchaseToken](appstoreservernotifications/externalpurchasetoken.md) 字段中包含该 token。使用该 token 信息向 Apple 上报，即使你在系统中无法识别该 token 也要上报。要上报 token（无论是否关联交易），请调用 [External Purchase Server API](externalpurchaseserverapi.md) 的 [Send External Purchase Report](externalpurchaseserverapi/send-external-purchase-report.md) 端点。

有关 token 上报要求的更多信息，请参阅 [在欧盟地区的 App Store 上使用替代性付款方式](https://developer.apple.com/support/apps-using-alternative-payment-providers-in-the-eu/)。

### 测试你的服务器设置

要确定你的服务器是否正在接收通知，请在 [App Store Server API](appstoreserverapi.md) 中调用 [Request a Test Notification](appstoreserverapi/request-a-test-notification.md) 端点，要求 App Store 服务器发送一个 [notificationType](appstoreservernotifications/notificationtype.md) 为 `TEST` 的通知。使用收到的 `testNotificationToken` 调用 [Get Test Notification Status](appstoreserverapi/get-test-notification-status.md) 端点，了解你的服务器对该测试通知的响应情况。

App Store 服务器以版本 2 通知格式发送 `TEST` 通知，无论你在 App Store Connect 中配置的是版本 1 还是版本 2 的通知 URL，都会向你的服务器发送该通知。有关在 App Store Connect 中配置 URL 的更多信息，请参阅 [为 App Store 服务器通知输入 URL](https://help.apple.com/app-store-connect/#/dev0067a330b)。

## 主题

### 基础知识

- [启用 App Store Server Notifications](appstoreservernotifications/enabling-app-store-server-notifications.md) — 配置你的服务器并提供 HTTPS URL，以接收关于 App 内购买事件和未上报外部购买 token 的通知。
- [接收 App Store Server Notifications](appstoreservernotifications/receiving-app-store-server-notifications.md) — 实现服务器端代码来接收和解析通知投递。
- [响应 App Store Server Notifications](appstoreservernotifications/responding-to-app-store-server-notifications.md) — 发送 HTTP 状态码以表明通知投递是否成功。
- [App Store Server Notifications 更新日志](appstoreservernotifications/app-store-server-notifications-changelog.md) — 了解 App Store Server Notifications 服务的变更内容。

### 服务器通知版本 2

- [App Store Server Notifications V2](appstoreservernotifications/app-store-server-notifications-v2.md) — 在 App Store Connect 中指定你安全服务器的 URL，以接收版本 2 通知。
- [responseBodyV2](appstoreservernotifications/responsebodyv2.md) — App Store 在版本 2 服务器通知中发送的响应体。
- [responseBodyV2DecodedPayload](appstoreservernotifications/responsebodyv2decodedpayload.md) — 包含版本 2 通知数据的已解码有效负载。
- [notificationType](appstoreservernotifications/notificationtype.md) — 描述 App Store 发送版本 2 通知所针对的 App 内购买或外部购买事件的类型。
- [subtype](appstoreservernotifications/subtype.md) — 一个字符串，提供版本 2 中特定通知类型的详细信息。

### 已废弃

- [App Store Server Notifications Version 1](appstoreservernotifications/app-store-server-notifications-version-1.md) — 接收、解析和解读 App Store Server Notifications 版本 1。

## 另请参阅

### 相关文档

- [In-App Purchase](storekit/in-app-purchase.md) — 借助基于 Swift 的接口，在你的 App 中跨 Apple 平台提供内容和服务。
- [App Store Server API](appstoreserverapi.md) — 从你的服务器管理客户的 App Store 交易。
- [App Store Receipts](appstorereceipts.md) — 借助 App Store 验证 App 和 App 内购买收据。 _(已废弃)_
