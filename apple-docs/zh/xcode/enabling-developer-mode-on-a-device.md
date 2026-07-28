---
title: 在设备上启用开发者模式
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/enabling-developer-mode-on-a-device
source_url: 'https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/enabling-developer-mode-on-a-device.json'
content_hash: 'sha256:8b413ea1d8a852a1'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Device Hub](device-hub.md)

# 在设备上启用开发者模式

<sub>文章</sub>

授予或拒绝本地安装的 App 在 iOS、iPadOS、watchOS 和 visionOS 上运行的权限。

## 概述

在设备上启用开发者模式（Developer Mode），即可通过 Xcode 在该设备上运行你的 App。开发者模式可保护人们免于无意间安装可能有害的软件，并减少因开发者专属功能而暴露的攻击面。

此功能不影响常规安装方式，例如从 App Store 购买 App 或参与 TestFlight 团队。相反，开发者模式专注于从 Xcode 构建并运行 App，或使用 [Apple Configurator](https://support.apple.com/apple-configurator) 安装 `.ipa` 文件等场景。在这些情况下，设备会明确询问使用者，以确认其开发者身份并知晓安装经过开发者签名的软件所伴随的风险。

当你开始配对设备时，若需开启开发者模式，或先前已配对的设备上开发者模式已关闭，Device Hub 会显示一条消息。有关更多信息，请参阅[在 Device Hub 中管理模拟设备与物理设备](managing-your-simulated-and-physical-devices-in-device-hub.md)。

开启开发者模式后，设备上会出现开发者设置，帮助你测试和调试 App。

> [!note] 注意
> 只有当你发起配对或先前已将该设备与 Mac 配对时，开发者模式才会出现在设置中。在 tvOS 中，没有开发者模式。只需使用 Device Hub 配对 Apple TV，设备上就会出现开发者设置。

### 在 iOS、iPadOS、watchOS 和 visionOS 中开启开发者模式

在设备上的隐私与安全性设置中，打开安全性下方的开发者模式开关。会显示一条警告，提示你开发者模式会降低设备的安全性。要继续开启开发者模式，请轻点警告中的“重新启动”按钮。

设备重新启动后，会再次显示一条警告，确认你要开启开发者模式。在 iOS 和 iPadOS 中，向上轻扫，在对话框里轻点“启用”，然后输入设备密码。

在 watchOS 中，轻点“开启”。如果出现后续对话框，请轻点“信任”，然后输入设备密码以确认。

### 关闭开发者模式

要关闭开发者模式，请关闭设置 > 隐私与安全性中的开发者模式开关，然后重新启动设备。关闭开发者模式后，你将无法在该设备上运行来自 Xcode 的 App，直到再次开启开发者模式。

## 另请参阅

### 基础

- [在模拟设备或物理设备上运行你的 App](running-your-app-on-simulated-or-physical-devices.md) — 在模拟的 iOS、iPadOS、tvOS、visionOS 或 watchOS 设备上，或在与你的 Mac 配对的物理设备上启动你的 App。
- [在 Device Hub 中管理模拟设备与物理设备](managing-your-simulated-and-physical-devices-in-device-hub.md) — 添加自定义模拟器并让物理设备与你的 Mac 配对，以便在 Xcode 中选择它们作为运行目标。
