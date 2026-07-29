---
title: 网络链路调节器
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/network-link-conditioner/'
original_language: en
published: 2013-09-09
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:4f9a7eda81cdea63'
translated: true
---

> 原文：[Network Link Conditioner](https://nshipster.com/network-link-conditioner/)　·　NSHipster (Mattt)

# [网络链路调节器](https://nshipster.com/network-link-conditioner/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　2019 年 7 月 29 日（[修订版](https://github.com/nshipster/articles/commits/master/2013-09-09-network-link-conditioner.md)）

产品设计关乎同理心。知道用户想要什么、喜欢什么、不喜欢什么、什么会让他们感到沮丧，并学会理解和体现这些动机——这就是做出卓越产品的关键。

为此，我们努力超越自身对世界的运作模式。我们为[不同地区](https://nshipster.com/nslocalizedstring/)量身定制体验。我们考虑[屏幕阅读器或其他辅助技术](https://nshipster.com/uiaccessibility/)对可用性的影响。我们[持续评估](https://nshipster.com/unit-testing/)自己的实现是否满足这些期望。

然而，有一个关键因素经常被 App 开发者忽略：**网络条件（network condition）**，更具体地说，是网络连接的延迟和带宽。

对于这样一个对用户体验至关重要的因素，不幸的是，大多数开发者在不同条件下对 App 进行实地测试时，都只是临时凑合一下（如果测了的话）。

本周的 NSHipster，我们将讨论[网络链路调节器（Network Link Conditioner）](https://developer.apple.com/download/more/?q=Additional%20Tools)，这是一个允许 macOS 和 iOS 设备准确且一致地模拟恶劣网络环境的实用工具。

## 安装

网络链路调节器可以在“Xcode 的附加工具 (Additional Tools for Xcode)”包中找到。你可以从 [Apple 开发者下载](https://developer.apple.com/download/more/?q=Additional%20Tools)页面下载它。

搜索“Additional Tools”并选择该包的适当版本。

![Additional Tools - 硬件](https://nshipster.com/assets/network-link-conditioner-dmg--light-4786c923da7defd77df5d0d1123781278d0321f4c3d645001baebe4512fb897da0202278a4769a3e9483c30e369464859e011d7703eb662688d8de09a02a4bf1.png)

下载完成后，打开 DMG，导航到“Hardware”目录，然后双击“Network Link Condition.prefPane”。

![安装网络链路调节器](https://nshipster.com/assets/network-link-conditioner-install--light-5742743446fec494023649d0d38341ad4df3a39c81dd0a66f4c779eff597a4fe3636f6cb42aa10ea1e130c75555842bdcbdebb04858d4b08257488aa6e4dbe76.png)

在系统偏好设置底部点击网络链路调节器偏好设置面板。

![网络链路调节器](https://nshipster.com/assets/network-link-conditioner-preference-pane--light-0fdd2adf0b2df413eb5b68f2ef3210fcd95a47dac5622a057f065217e49edebd46cc03d007c7e5958720e60d8c05ce6fc696672024dca52831b870bfabc5a4e1.png)

## 控制带宽、延迟和丢包

启用网络链路调节器会根据所选配置改变整个系统的网络环境，限制上行或下载[带宽](https://en.wikipedia.org/wiki/Bandwidth_%28computing%29)、[延迟](https://en.wikipedia.org/wiki/Latency_%28engineering%29%23Communication_latency)以及[丢包](https://en.wikipedia.org/wiki/Packet_loss)率。

你可以从以下预设中选择一种：

- 100% 丢包 (100% Loss)
- 3G
- DSL
- EDGE
- 高延迟 DNS (High Latency DNS)
- LTE
- 非常糟糕的网络 (Very Bad Network)
- WiFi
- WiFi 802.11ac

……或者根据你的特定需求创建自己的预设。

![预设](https://nshipster.com/assets/network-link-conditioner-preset-90a1ad42f1dadd577eb4f5ebbeef5e76f9535b520632d3f94792d1020d8e8d1f6e2ba5aa395504e0dd7011371b20fe9eca3233e684e7a67c14409a5c040a358a.png)

---

现在尝试在启用网络链路调节器的情况下运行你的 App：

网络延迟如何影响你的 App 启动？  
带宽对表格视图（table view）滚动性能有何影响？  
你的 App 在 100% 丢包的情况下还能工作吗？

## 在 iOS 设备上启用网络链路调节器

虽然偏好设置面板在模拟器上开发时效果很好，但在真机上进行测试也很重要。幸运的是，网络链路调节器也适用于 iOS。

要在 iOS 上使用网络链路调节器，请将你的设备设置为开发设备：

1. 将你的 iOS 设备连接到 Mac
2. 在 Xcode 中，导航到 Window > Devices & Simulators
3. 在侧边栏中选择你的设备
4. 点击“Use for Development”

![iOS 设备](https://nshipster.com/assets/network-link-conditioner-ios-28f5a485b77714d22a91039b894e51708e0bce5b9a4f8ad4a7235e999519d85bed21d262ccfc53d98e541b0627bf37e65db50107152c1f5a05892662435b99ce.png)

现在你将可以访问“设置”App 中的“开发者 (Developer)”部分。你可以在“设置”>“开发者”>“网络 (Networking)”下启用和配置你的 iOS 设备上的网络链路调节器。（记得测试完成后关闭它！）。
