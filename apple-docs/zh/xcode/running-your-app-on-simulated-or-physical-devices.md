---
title: 在模拟设备或实体设备上运行你的 App
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/running-your-app-on-simulated-or-physical-devices
source_url: 'https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/running-your-app-on-simulated-or-physical-devices.json'
content_hash: 'sha256:1a325687a1c04d34'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Device Hub](device-hub.md)

# 在模拟设备或实体设备上运行你的 App

<sub>文章</sub>

在模拟的 iOS、iPadOS、tvOS、visionOS 或 watchOS 设备上，或在与 Mac 配对的实体设备上启动你的 App。

## 概述

要测试你的 App，请在模拟设备或实体设备上构建并运行它。使用模拟设备可以在你可能没有的各种硬件上调试你的 App。请注意，模拟器在 Mac 上的 Device Hub 中运行，不会复制实体设备的性能或功能。要验证你的 App 是否完全按预期运行，请在一个或多个实体设备上运行它。

## 选择构建方案和运行目标

在构建和运行你的 App 之前，请选择一个包含 Xcode 中 App 目标的构建方案（build scheme）。_方案_ 是一组项目详细信息和设置，用于告诉 Xcode 如何从你的项目构建和运行产品。在工具栏中，从运行目标左侧的弹出菜单中选取一个方案。

然后，从运行目标弹出菜单中选取一个模拟设备或实体设备。根据你选择的方案，Xcode 会使用可用设备列表（包括常见硬件和最新操作系统的模拟器）填充运行目标菜单。例如，如果方案包含 watchOS App，Xcode 只会显示 watchOS 模拟设备和实体设备作为可用的运行目标。

如果你没有为目标安装平台支持，则无法在设备上构建和运行你的 App。要安装平台支持，请点击 `Any [Platform] Device` 运行目标旁边出现的“获取”按钮。或者，稍后在“组件”设置中管理你的下载（参阅[下载并安装额外的 Xcode 组件](downloading-and-installing-additional-xcode-components.md)）。

要了解有关方案的更多信息，请参阅[自定义项目的构建方案](customizing-the-build-schemes-for-a-project.md)。

> [!important] 重要
> 在 Device Hub 的模拟器中运行 App 时，某些特定于硬件的功能可能不可用。提供对设备特定功能访问权限的框架也会提供 API，以告知你这些功能何时可用。调用这些 API 并处理功能不可用的情况。要测试该功能本身，请在实体设备上运行你的代码。

## 运行 App

要在选定的模拟设备或实体设备上构建并运行 App，请点击工具栏中的“运行”按钮，或选择“产品”>“运行”。在工具栏的活动区域查看构建的状态。

如果构建成功，Xcode 会运行 App，并在调试区域打开一个调试会话。使用调试区域中的控制来逐步执行你的代码、检查变量以及与调试器交互。要在没有调试器的情况下运行 App，请关闭方案编辑器“信息”标签中的“调试可执行文件”选项。

如果你选择模拟器作为运行目标，Device Hub 默认会打开一个紧凑窗口，显示你的 App 在设备屏幕上的运行情况，你可以使用 Mac 与其交互。

![Device Hub 中 Apple Vision Pro 模拟器运行从 Xcode 启动的 App 的紧凑窗口屏幕截图。](../../../attachments/8e9b9eda2e4e79296e703ddf0b9cfb09/device-hub-compact-view@2x.png)

如果你选择实体设备，Xcode 会在该设备上运行 App。要同时使用设备和 Device Hub 与 App 交互，请在侧边栏中选择该设备，然后在画布区域中点击“查看屏幕”。

有关在 Device Hub 中与不同类型设备交互的更多信息，请参阅[在 Device Hub 中与你的 App 交互](interacting-with-your-app-in-device-hub.md)和[配置模拟设备的环境](configuring-the-environment-of-a-simulated-device.md)。

如果构建失败，请点击活动区域中的指示器，在问题导航器中阅读错误或警告消息。或者，选择“视图”>“导航器”>“问题”，或按 Command-5，以查看这些消息。

在 Device Hub 中完成 App 测试后，点击 Xcode 工具栏中的“停止”按钮。

## 为实体设备创建 Provisioning Profile

如果你选择实体设备作为运行目标，请执行以下额外步骤在 Xcode 中创建一个开发 provisioning profile：

- 在 Xcode > 设置 > Apple 账户中，使用你的 Apple Developer Program 或个人 Apple 账户登录。
- 在项目编辑器的“签名与能力”面板中，将你的项目分配给一个团队。
- 在项目编辑器的工具栏中，选择实体设备作为运行目标。

在“签名与能力”面板上的“签名”下，启用默认的“自动管理签名”选项，Xcode 会为你注册设备并创建开发 provisioning profile。否则，如果出现“注册”按钮，请在“签名”下点击它。

> [!note] 注意
> 除非你添加了需要 provisioning 的能力，否则无需配置 Mac 设备来运行你的 macOS App。类似地，要运行 iPad App 的 macOS 版本，请选择“我的 Mac”作为设备。

有关开发者账户的更多信息，请参阅[选择会员资格](https://developer.apple.com/support/compare-memberships/)。

## 另请参阅

### 基础

- [在 Device Hub 中管理你的模拟设备和实体设备](managing-your-simulated-and-physical-devices-in-device-hub.md) — 添加自定义模拟器并将实体设备与 Mac 配对，以便你可以在 Xcode 中将它们选为运行目标。
- [在设备上启用开发者模式](enabling-developer-mode-on-a-device.md) — 允许或拒绝本地安装的 App 在 iOS、iPadOS、watchOS 和 visionOS 中运行。
