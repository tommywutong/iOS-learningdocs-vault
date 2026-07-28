---
title: 配置 macOS App Sandbox
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-the-macos-app-sandbox
source_url: 'https://developer.apple.com/documentation/xcode/configuring-the-macos-app-sandbox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-the-macos-app-sandbox.json'
content_hash: 'sha256:d126e809a9cf25fa'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [能力](capabilities.md)

# 配置 macOS App Sandbox

<sub>文章</sub>

通过限制对文件系统、网络连接等的访问，保护系统资源和用户数据免受受感染 App 的侵害。

## 概述

*App Sandbox（App 沙盒）* 是 macOS 在内核级别提供并强制实施的一种访问控制技术。沙盒的主要功能是限制损害范围，防止用户执行受感染 App 时对系统和用户数据造成破坏。虽然沙盒无法防止针对你 App 的攻击，但它通过将你的 App 限制在其正常运行所需的最小权限集内，来减少成功攻击可能造成的损害。

沙盒化 App 必须明确声明要访问受限资源或受保护文件位置的意图，否则系统会禁止其在运行时的任何尝试。Xcode 的 App Sandbox 能力允许你通过启用 App 所需的权限来声明该意图。

在启用这些权限之前，请先按照[为 App 添加能力](adding-capabilities-to-your-app.md#Add-a-capability)一文中的[添加能力](adding-capabilities-to-your-app.md)步骤，将 App Sandbox 能力添加到你的 macOS App 目标中。

![](../../../attachments/4508cd639720edbd186a90d7a41b5dc0/app-sandbox@2x.png)

<sub>Xcode 能力库的截图，左侧列出了可用能力列表，右侧为信息面板。列表显示了从 App Sandbox 到 FileProvider Testing Mode 的一系列能力，其中 App Sandbox 能力处于选中状态。信息面板上的文字说明 App Sandbox 能力利用操作系统的服务在 App 代码与关键用户数据、网络访问或系统上的其他进程之间建立屏障，并说明沙盒有助于最大限度地降低 App 及其链接框架中不安全代码带来的风险。</sub>

添加 App Sandbox 能力后，Xcode 会自动更新你的 macOS App 的 entitlement 文件，以包含 [App Sandbox Entitlement](../bundleresources/entitlements/com.apple.security.app-sandbox.md)，这是你提交到 Mac App Store 审核的任何 App 都必须满足的 App Store 要求。

为确保 App Sandbox 处于启用状态，请使用 Xcode 启动你的 macOS App。然后，打开 `/Applications/Utilities/Activity Monitor.app`，并选择“显示”>“列”>“沙盒”以显示沙盒列。在运行进程列表中找到你的 App，并确认该列中的值为 `Yes`。

> [!note] 注意
> 当你使用 Mac Catalyst 使你的 iPad App 能够在 macOS 上运行时，Xcode 会自动为 macOS 目标添加 App Sandbox 和强化运行时（Hardened Runtime）能力。有关更多信息，请参阅[创建 iPad App 的 Mac 版本](../uikit/creating-a-mac-version-of-your-ipad-app.md)。

### 启用对受限资源的访问

如果你的 App 需要访问受限或敏感的系统资源（例如网络连接或已连接的蓝牙设备），则必须包含提供这些资源访问权限的相关 entitlement。请按照以下步骤添加这些 entitlement：

1. 在 Xcode 的项目导航器中选择你的项目。
2. 在目标列表中选择你的 macOS App 的目标。
3. 点击项目编辑器中的“签名与能力”标签页。
4. 找到 App Sandbox 能力。
5. 通过勾选相关复选框来启用对一个或多个资源的访问。

![](../../../attachments/746be89f40048d0d503a12469f4f459b/sandbox-resources@2x.png)

<sub>App Sandbox 能力中可用的各种网络、硬件和 App 数据配置选项截图。其中“传出的连接（客户端）”和“相机”选项处于选中状态。</sub>

Xcode 会更新你的 macOS App 的 entitlement 文件，以包含必要的 entitlement，并将这些 entitlement 的值设置为 `true`。

> [!important] 重要
> Entitlement 会向系统告知你的 App 访问相关资源的意图。在大多数情况下，你仍然需要先获得用户的明确许可，系统才会授予该访问权限。有关具体要求，请参阅相关框架的文档。

下表描述了 App Sandbox 支持的资源访问 entitlement：

| 分类 | 名称 | 描述 |
|---|---|---|
| 网络 | 传入连接（服务器） | 你的 App 监听传入的网络连接。有关更多信息，请参阅 [com.apple.security.network.server](../bundleresources/entitlements/com.apple.security.network.server.md) entitlement。 |
|  | 传出连接（客户端） | 你的 App 使用传出网络连接到远程服务器。有关更多信息，请参阅 [com.apple.security.network.client](../bundleresources/entitlements/com.apple.security.network.client.md) entitlement。 |
| 硬件 | 相机 | 你的 App 使用内置和外接摄像头捕捉图像和影片。有关更多信息，请参阅[相机 entitlement](../bundleresources/entitlements/com.apple.security.device.camera.md)。 |
|  | 音频输入 | 你的 App 使用内置和外接麦克风捕捉音频。有关更多信息，请参阅 [com.apple.security.device.microphone](../bundleresources/entitlements/com.apple.security.device.microphone.md) entitlement。 |
|  | USB | 你的 App 与连接的 USB 设备通信。有关更多信息，请参阅 [com.apple.security.device.usb](../bundleresources/entitlements/com.apple.security.device.usb.md) entitlement。 |
|  | 打印 | 你的 App 使用系统配置的打印机打印文稿和媒体。有关更多信息，请参阅 [com.apple.security.print](../bundleresources/entitlements/com.apple.security.print.md) entitlement。 |
|  | 蓝牙 | 你的 App 与连接的蓝牙设备通信。有关更多信息，请参阅 [com.apple.security.device.bluetooth](../bundleresources/entitlements/com.apple.security.device.bluetooth.md) entitlement。 |
| App 数据 | 通讯录 | 你的 App 需要对用户的通讯录数据库进行读写访问。有关更多信息，请参阅[地址簿 entitlement](../bundleresources/entitlements/com.apple.security.personal-information.addressbook.md)。 |
|  | 位置 | 你的 App 使用定位服务确定用户的位置。有关更多信息，请参阅[位置 entitlement](../bundleresources/entitlements/com.apple.security.personal-information.location.md)。 |
|  | 日历 | 你的 App 需要对用户的日历进行读写访问。有关更多信息，请参阅[日历 entitlement](../bundleresources/entitlements/com.apple.security.personal-information.calendars.md)。 |

### 启用托管文件访问

当用户首次启动你的沙盒化 App 时，系统会创建其*容器（container）* ——位于 `~/Library/Containers` 中的一个文件夹，你的 App 对其拥有独占的读写访问权限。

为了最大程度地降低用户数据风险，系统将你的 App 的文件系统访问权限限制在其容器内，但该容器确实包含许多解析为常用用户文件夹（例如 `~/Downloads` 和 `~/Pictures`）的符号链接。但是，系统将这些视为敏感文件夹，要求你的 App 包含特定的 entitlement，才能授予对符号链接解析位置的访问权限。未经授权尝试访问这些文件夹之一会导致“Operation not permitted”错误。

请按照以下步骤添加所需的 entitlement：

1. 在 Xcode 的项目导航器中选择你的项目。
2. 在目标列表中选择你的 macOS App 的目标。
3. 点击项目编辑器中的“签名与能力”标签页。
4. 找到 App Sandbox 能力。
5. 使用每个选项的下拉菜单，根据你的 App 需求选择 None（无）、Read Only（只读）或 Read/Write（读写）。

![](../../../attachments/18c9ce0d1d22951dcecdb1272738019b/sandbox-file-access@2x.png)

<sub>App Sandbox 能力中可用的“文件访问”选项截图。用户“图片”文件夹的权限和访问设置为 Read Only（只读）。“下载”文件夹、“音乐”文件夹、“影片”文件夹和“用户选择的文件”（User Selected File）选项均设置为 None（无）。</sub>

> [!note] 注意
> “用户选择的文件”（User Selected File）选项允许访问用户使用 AppKit 的 [NSOpenPanel](../appkit/nsopenpanel.md) 和 [NSSavePanel](../appkit/nssavepanel.md) 选择的任意位置。

配置完必要的文件访问后，Xcode 会更新你的 App 的 entitlement 文件，以包含对应的 entitlement，并将这些 entitlement 的值设置为 `true`。

## 另请参阅

### 安全

- [配置家长控制](configuring-family-controls.md) — 添加家长控制（Family Controls）entitlement，以在你的 App 及其 Screen Time API App 扩展中启用家长控制功能。
- [配置强化运行时](configuring-the-hardened-runtime.md) — 通过限制对敏感资源的访问和防止常见漏洞利用，来保护 macOS App 的运行时完整性。
- [配置钥匙串共享](configuring-keychain-sharing.md) — 在属于同一开发者的多个 App 之间共享钥匙串项目。
- [在 macOS 上使用容器保护本地 App 数据](protecting-local-app-data-using-containers.md) — 保护你的 App 的本地存储数据免受未经授权的访问和修改。
- [在现有的 macOS App 中访问 App Group 容器](accessing-app-group-containers.md) — 确保你的 App 具有 App Group 容器 entitlement，并且 macOS 可以对其进行授权。
