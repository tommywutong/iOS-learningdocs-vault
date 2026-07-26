---
title: 配置网络扩展
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-network-extensions
source_url: 'https://developer.apple.com/documentation/xcode/configuring-network-extensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-network-extensions.json'
content_hash: 'sha256:7a101f92676af680'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Capabilities](capabilities.md)

# 配置网络扩展

<sub>文章</sub>

自定义你 App 网络栈的各种能力，例如代理 DNS 查询或创建数据包隧道。

## 概述

网络扩展（Network Extensions）让你能够自定义和扩展 iOS 与 macOS 的核心网络特性。例如，你的 App 可以为面向流或面向数据包的自定义 VPN 协议实现一个虚拟专用网络（VPN）客户端，企业可能需要它来为无法通过公共互联网访问的资源提供安全的远程访问。

在实现自定义网络栈之前，请按照 [Adding capabilities to your app](adding-capabilities-to-your-app.md) 中 [Add a capability](adding-capabilities-to-your-app.md#Add-a-capability) 一节的步骤，为你的 iOS 或 macOS App 添加该能力，并从 Xcode 的 Capabilities 库中选择 Network Extensions 能力。

![](../../../attachments/7d148d18e1c6244bdd44445075f71d11/network-extensions@2x.png)

<sub>Xcode Capabilities 库的屏幕截图，左侧是可用能力列表，右侧是信息面板。列表展示了从 Near Field Communication Tag Reading 到 Wireless Accessory Configuration 的一系列能力，其中 Network Extensions 能力处于选中状态。信息面板上的文字说明：启用 Network Extensions 后，你的 App 可以创建网络扩展，扩展和自定义用户设备的网络能力。</sub>

添加 Network Extensions 能力后，Xcode 会更新你 App 的 entitlements 文件，加入 [Network Extensions Entitlement](../bundleresources/entitlements/com.apple.developer.networking.networkextension.md)，这是一个由你启用的各项 App 能力组成的数组。如果 Xcode 自动管理你 App 的签名，它还会在你的开发者账户中为你 App 的 App ID 启用 Network Extensions 能力。

> [!note] 注意
> 如果你在 Xcode 中移除了 Network Extensions 能力，你必须在开发者账户中手动更新你 App 的 App ID 配置，以禁用 Network Extensions。

### 启用所需的 App 能力

在你的 App 能够使用 [Network Extension](../networkextension.md) 框架、通过实现特定的 App 能力来自定义和扩展 iOS 与 macOS 的核心网络特性之前，你必须按以下步骤配置 Xcode 项目，加入必要的 entitlement：

1. 在 Xcode 的 Project navigator 中选择你的项目。
2. 在 Targets 列表中选择该 App 的 target。
3. 在项目编辑器中点击 Signing & Capabilities 标签页。
4. 找到 Network Extensions 能力。
5. 通过勾选对应的复选框，启用一个或多个 App 能力。

![](../../../attachments/91f991a03baacb30ee9d12e1d7e537e5/network-extensions-capabilities@2x.png)

<sub>将 Network Extensions 能力添加到你 App 的 target 后的屏幕截图。Content Filter App 能力处于启用状态。</sub>

Xcode 会自动更新你 App entitlements 文件中的 [Network Extensions Entitlement](../bundleresources/entitlements/com.apple.developer.networking.networkextension.md) 数组，加入已启用的 App 能力。

> [!important] 重要
> App 能力可能带有特定的限制和使用场景，例如仅在受监管的 iOS 设备上可用。更多信息，请参阅每项能力各自的文档。

下表列出了 Network Extensions 支持的 App 能力：

| 名称 | 描述 |
|---|---|
| App Proxy | 你的 App 为面向流的自定义 VPN 协议提供虚拟专用网络（VPN）客户端。更多信息，请参阅 [App proxy provider](../networkextension/app-proxy-provider.md)。 |
| Content Filter | 你的 App 在用户内容经过网络栈时对其进行检查，并判断系统应当放行还是阻止。更多信息，请参阅 [Content filter providers](../networkextension/content-filter-providers.md) 以及示例代码 [Filtering Network Traffic](../networkextension/filtering-network-traffic.md)。 |
| Packet Tunnel | 你的 App 为面向数据包的自定义 VPN 协议提供 VPN 客户端。更多信息，请参阅 [Packet tunnel provider](../networkextension/packet-tunnel-provider.md)。 |
| DNS Proxy | 你的 App 负责使用自定义协议在设备本地解析所有 DNS 查询。更多信息，请参阅 [DNS proxy provider](../networkextension/dns-proxy-provider.md)。 |
| DNS Settings | 你的 App 使用 DNS-over-TLS 和 DNS-over-HTTP 这两种 DNS 协议创建并管理系统级的 DNS 配置。更多信息，请参阅 [DNS settings](../networkextension/dns-settings.md)。 |

> [!tip] 提示
> 要进一步了解用于创建扩展和自定义设备网络能力的 App 所使用的 API，请参阅 WWDC 视频 [Network Extensions for the Modern Mac](https://developer.apple.com/videos/play/wwdc2019/714)、[Advances in Networking, Part 1](https://developer.apple.com/videos/play/wwdc2019/712) 以及 [What's New in Network Extension and VPN](https://developer.apple.com/videos/play/wwdc2015/717)。

## 另请参阅

### Network

- [Registering your app with APNs](../usernotifications/registering-your-app-with-apns.md) — 与 Apple Push Notification service（APNs）通信，接收用于标识你 App 的唯一设备令牌。
- [Configuring Group Activities](configuring-group-activities.md) — 利用 FaceTime 基础设施，创建用户可以共享的协同体验。
- [Configuring media device discovery](configuring-media-device-discovery.md) — 将第三方媒体设备或协议添加为与 AirPlay 同一系统菜单中的流媒体播放选项。
