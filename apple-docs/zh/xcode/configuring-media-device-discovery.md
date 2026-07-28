---
title: 配置媒体设备发现
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-media-device-discovery
source_url: 'https://developer.apple.com/documentation/xcode/configuring-media-device-discovery'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-media-device-discovery.json'
content_hash: 'sha256:e12f076c5ff0dcf9'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [能力](capabilities.md)

# 配置媒体设备发现

<sub>文章</sub>

将第三方媒体设备或协议添加为与 AirPlay 同一系统菜单中的流媒体播放选项。

## 概述

> [!important] 重要
> Media Device Discovery Extension 在 iOS 27.0 和 visionOS 27.0 中已废弃。有关设备发现，请参阅[将媒体路由并流式传输到远程设备](../avsystemrouting/routing-and-streaming-media-to-remote-devices.md)。

在 iOS App 扩展中启用 Media Device Discovery 能力，以表明它打算在本地网络或配对的蓝牙设备中搜索第三方媒体接收器。此能力对应 [Media Device Discovery Extension](../bundleresources/entitlements/com.apple.developer.media-device-discovery-extension.md) entitlement。启用 Media Device Discovery 时，Xcode 会将该 entitlement 添加到扩展 target 的代码签名 entitlements 文件中。

运行时，当用户调用用于播放媒体的 UI 时，App 会呈现 [AVRoutePickerView](../avkit/avroutepickerview.md)，提供用户可以流式传输到的设备。系统会在 App bundle 中搜索具有此 entitlement 的扩展，以检查 App 是否提供这样的设备。如果提供，系统会在选择器中把第三方设备添加到所有可用 AirPlay 设备旁边，为用户提供统一的媒体流式传输体验。

## 将 Media Device Discovery 能力添加到 target

若要添加该能力，请针对扩展 target 按照[向 App 添加能力](adding-capabilities-to-your-app.md)中[添加能力](adding-capabilities-to-your-app.md#Add-a-capability)一节的步骤操作。如果你在 Xcode 项目中使用 Media Device Discovery 模板添加新 target，Xcode 会自动启用此能力。

![Xcode Capabilities 库的屏幕截图，其中 Media Device Discovery 能力处于选中状态。](../../../attachments/c10ab39afa443f9626552b73e0e2ef9f/media-device-discovery@2x.png)

## 编写扩展代码

使用 [DeviceDiscoveryExtension](../devicediscoveryextension.md) 框架编写扩展代码，以在本地网络或配对的蓝牙设备中搜索特定媒体接收器。如果搜索成功，扩展会将发现的设备传给系统。有关演示媒体设备发现的示例 App，请参阅[发现第三方媒体流式传输设备](../devicediscoveryextension/discovering-a-third-party-media-streaming-device.md)。

## 另请参阅

### 网络

- [配置网络扩展](configuring-network-extensions.md) — 自定义 App 网络栈的各种能力，例如代理 DNS 查询或创建数据包隧道。
- [向 APNs 注册 App](../usernotifications/registering-your-app-with-apns.md) — 与 Apple Push Notification service（APNs）通信，并接收用于标识 App 的唯一设备令牌。
- [配置 Group Activities](configuring-group-activities.md) — 利用 FaceTime 基础设施创建用户可以共享的协调体验。
