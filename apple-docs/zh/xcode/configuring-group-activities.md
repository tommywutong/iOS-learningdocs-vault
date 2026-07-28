---
title: 配置 Group Activities
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-group-activities
source_url: 'https://developer.apple.com/documentation/xcode/configuring-group-activities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-group-activities.json'
content_hash: 'sha256:9ecb1ab704d82bab'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [能力](capabilities.md)

# 配置 Group Activities

<sub>文章</sub>

利用 FaceTime 基础设施创建用户可以共享的协调体验。

## 概述

使用 [Group Activities](../groupactivities.md)，让 App 用户聚在一起享受构建于[同播共享（SharePlay）](https://developer.apple.com/shareplay)和 FaceTime 基础设施之上的新颖共享体验。例如，卡拉 OK App 可以提供卡拉 OK 派对，让多位参与者通过各自的设备同时参加。

通过创建符合 [GroupActivity](../groupactivities/groupactivity.md) 协议的对象来表示可共享活动；共享活动开始后，使用 [GroupSession](../groupactivities/groupsession.md) 在参与者的设备间同步该活动。

### 将 Group Activities 能力添加到 target

按照[添加能力](adding-capabilities-to-your-app.md#Add-a-capability)中的步骤将该能力添加到 App target，并确保从 Xcode 的 Capabilities 库中选择 Group Activities 能力。此能力适用于 watchOS 以外的所有平台，而且必须将其添加到 App target；Group Activities 不适用于小组件、扩展或轻 App。

![](../../../attachments/165af9aad4e78c823c8a90bad8168183/group-activities@2x.png)

<sub>Xcode Capabilities 库的屏幕截图，左侧是可用能力列表，右侧是信息面板。列表展示了从 Group Activities 到 Maps 的一系列能力，其中 Group Activities 能力处于选中状态。信息面板上的文字说明：Group Activities 允许一个 App 与一台或多台其他设备上的同一 App 通信，以便在 FaceTime 通话中创建群组活动；FaceTime 上的 Group Activities 让用户能够一起观看视频、聆听音乐或享受其他同步活动。</sub>

添加 Group Activities 能力后，Xcode 会更新 target 的 entitlements 文件，加入 [com.apple.developer.group-session](../bundleresources/entitlements/com.apple.developer.group-session.md) entitlement。如果 Xcode 自动管理 App 签名，它还会为 App 的 App ID 启用 Group Activities。

> [!note] 注意
> 如果你在 Xcode 中移除 Group Activities 能力，必须在开发者账户中手动更新 App ID 配置，以停用 Group Activities。

添加 Group Activities 能力后，你还必须完成其他步骤，App 用户才能开始体验共享活动；有关这些步骤的更多信息，请参阅[定义 App 的同播共享活动](../groupactivities/defining-your-apps-shareplay-activities.md)和[加入并管理共享活动](../groupactivities/joining-and-managing-a-shared-activity.md)。

## 另请参阅

### 网络

- [配置网络扩展](configuring-network-extensions.md) — 自定义 App 网络栈的各种能力，例如代理 DNS 查询或创建数据包隧道。
- [向 APNs 注册 App](../usernotifications/registering-your-app-with-apns.md) — 与 Apple Push Notification service（APNs）通信，并接收用于标识 App 的唯一设备令牌。
- [配置媒体设备发现](configuring-media-device-discovery.md) — 将第三方媒体设备或协议添加为与 AirPlay 同一系统菜单中的流媒体播放选项。
