---
title: 使用 Multipath TCP 提升网络可靠性
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/improving-network-reliability-using-multipath-tcp
source_url: 'https://developer.apple.com/documentation/foundation/improving-network-reliability-using-multipath-tcp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/improving-network-reliability-using-multipath-tcp.json'
content_hash: 'sha256:b5a92eb6332ae0ce'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md) · [URLSession](urlsession.md) · [URLSessionConfiguration](urlsessionconfiguration.md)

# 使用 Multipath TCP 提升网络可靠性

<sub>文章</sub>

利用 iOS 设备上可用的射频模块，提升你的 App 的网络可靠性和性能。

## 概述

当用户在 iOS 设备上使用你的 App 时，他们很可能会在 Wi-Fi 覆盖范围内外移动，从而在蜂窝网络和 Wi-Fi 之间来回切换。

当用户所处位置的 Wi-Fi 信号有限、且设备正在蜂窝数据和 Wi-Fi 之间过渡时，Multipath TCP 能提升你的 App 的性能。在默认配置下，URL 会话在一次网络调用中只使用单个射频模块，优先选择 Wi-Fi 而非蜂窝网络。但是，启用 Multipath TCP 后，URL 会话会同时通过两个射频模块发起请求，并优先选择响应更快的一个，同时仍偏向 Wi-Fi。

### 在你的 App 中启用 Multipath TCP

需要执行以下步骤：

- 在 Xcode 的 Capabilities 面板中，为你的 App target 启用 [Multipath Entitlement](../bundleresources/entitlements/com.apple.developer.networking.multipath.md)。
- 将 [URLSessionConfiguration](urlsessionconfiguration.md) 中的 [multipathServiceType](urlsessionconfiguration/multipathservicetype-swift.property.md) 属性设置为除 `none` 以外的模式。在大多数情况下，切换（handover）模式是最佳选择。该模式能让你的用户在 Wi-Fi 和蜂窝网络之间无缝切换，从而不中断地使用你的 App。（有关其他模式的信息，请参阅 [MultipathServiceType](urlsessionconfiguration/multipathservicetype-swift.enum.md)。）

当用户的设备连接到可靠的 Wi-Fi 网络时，你的 App 只会使用 Wi-Fi，不会消耗任何蜂窝数据。当用户离开该 Wi-Fi 网络的覆盖范围、信号开始变差时，Multipath TCP 会开始将数据使用切换到蜂窝网络，以提供无缝的过渡体验。

> [!important] 重要
> Multipath TCP 要求目标服务器已启用 Multipath TCP。许多商用负载均衡器已经支持 Multipath TCP，你可以在配置中启用它。对于基于 Linux 的服务器，可以在 [Multipath TCP](https://multipath-tcp.org) 网站获取支持 Multipath TCP 的 Linux 内核。

### 将 Multipath TCP 与 Wi-Fi Assist 结合使用时的限制

由于 Wi-Fi Assist 是一个用户可选的、面向整个设备的选项，在启用该选项的情况下将 Multipath TCP 与其结合使用时会有一些限制：

- 当你的 App 处于后台时，Wi-Fi Assist 会阻止数据流使用蜂窝数据。
- Wi-Fi Assist 会限制你的 App 通过蜂窝网络发送的数据量。达到该限制后，Multipath TCP 会被禁用。

Wi-Fi Assist 已集成到 [URLSession](urlsession.md) API 中，无需对会话配置做任何改动。在每个 URL 会话任务开始时，Wi-Fi Assist 会决定该连接使用 Wi-Fi 还是蜂窝数据。

URL 会话任务开始后，Wi-Fi Assist 不会再将其从 Wi-Fi 切换到蜂窝网络，或从蜂窝网络切换到 Wi-Fi。Multipath TCP 扩展了 Wi-Fi Assist 提升性能的能力，从而提供无缝的射频切换和更高的吞吐量。

> [!note] 注意
> 在使用面向开发者启用的设备进行测试时，你可以在“设置”App 的开发者部分中禁用 Wi-Fi Assist 的数据限制。

## 另请参阅

### Supporting Multipath TCP

- [multipathServiceType](urlsessionconfiguration/multipathservicetype-swift.property.md) — 一种服务类型，用于指定通过 Wi-Fi 和蜂窝网络接口传输数据时的 Multipath TCP 连接策略。
- [MultipathServiceType](urlsessionconfiguration/multipathservicetype-swift.enum.md) — 指定 Multipath TCP 所使用服务类型的常量。
- [Multipath Entitlement](../bundleresources/entitlements/com.apple.developer.networking.multipath.md) — 一个布尔值，指示你的 App 是否可以使用 Multipath 协议在 Wi-Fi 和蜂窝网络之间无缝切换。
