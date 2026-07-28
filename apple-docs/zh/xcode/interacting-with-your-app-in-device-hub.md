---
title: 在 Device Hub 中与 App 交互
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/interacting-with-your-app-in-device-hub
source_url: 'https://developer.apple.com/documentation/xcode/interacting-with-your-app-in-device-hub'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/interacting-with-your-app-in-device-hub.json'
content_hash: 'sha256:128d2807da0b9edc'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Device Hub](device-hub.md)

# 在 Device Hub 中与 App 交互

<sub>文章</sub>

使用 Device Hub 控制与模拟设备和实体设备上 App 的交互。

## 概述

在 Device Hub 画布中显示的模拟设备和实体设备上，你可以使用 Mac 上类似的控制方式与 App 交互。

在模拟设备上启动 App 时，Device Hub 会打开并在紧凑窗口中显示设备屏幕。在实体设备上启动 App 时，Xcode 会在设备上运行 App。若要在 Device Hub 中与设备交互，请在边栏中选择设备，然后点按画布区域中的 View Screen。

Device Hub 会在屏幕内容周围显示类似目标设备的边框。在 visionOS 中，它会显示合成空间，以模拟佩戴设备时的体验。每种设备边框和空间都有支持相应交互的特定控制。

## 在画布中与 iOS 或 iPadOS App 交互

使用 Mac 的指针、触控板或 Magic Mouse、键盘、菜单项和按钮，在模拟的 iOS 或 iPadOS 设备上执行手势。

| 手势 | 模拟方式 |
|---|---|
| 轻点 | 点按。 |
| 轻点两下 | 点按两下。 |
| 触碰并按住 | 点按并按住。 |
| 拖放（drag and drop） | 点按并按住，直到拖动条目出现，然后将条目拖到目标位置。 |
| 激活 Siri | 按住设备边框上的睡眠/唤醒按钮，或选取 Controls \> Siri。 |
| 向左旋转模拟器 | 点按设备边框下方的旋转按钮，或选取 Controls \> Rotate Left。 |
| 向右旋转模拟器 | 按住 Option 键点按设备边框下方的旋转按钮，或选取 Controls \> Rotate Right。 |
| 设置设备方向 | 从 Device \> Orientation 子菜单中选取方向。Face Up 和 Face Down 不会旋转模拟器。 |

通过点按设备边框的相应部分来激活设备按钮：

| 按钮 | 模拟方式 |
|---|---|
| 按下主屏幕按钮 | 点按设备边框下方的主屏幕按钮，或选取 Controls \> Home。 |
| 按下睡眠/唤醒按钮 | 点按设备边框上的睡眠/唤醒按钮，或选取 Controls \> Lock。 |
| 点按或按住调高音量按钮 | 点按或按住设备边框上的调高音量按钮，或选取 Device \> Sound \> Increase Volume。 |
| 点按或按住调低音量按钮 | 点按或按住设备边框上的调低音量按钮，或选取 Device \> Sound \> Decrease Volume。 |
| 按下操作按钮 | 点按设备边框上的操作按钮。 |

## 在画布中与 watchOS App 交互

使用指针、触控板或 Magic Mouse、键盘和菜单项，在模拟的 watchOS 设备上执行手势。

| 手势 | 模拟方式 |
|---|---|
| 轻点 | 点按。 |
| 轻点两下 | 点按两下。 |
| 触碰并按住 | 点按并按住。 |
| 激活 Siri | 按住设备边框上的睡眠/唤醒按钮，或选取 Controls \> Siri。 |

使用菜单项或点按设备边框的相应部分来激活设备按钮：

| 按钮 | 模拟方式 |
|---|---|
| 按下数码表冠 | 点按设备边框上的数码表冠。 |
| 顺时针或逆时针旋转数码表冠 | 将指针移到设备边框上的数码表冠上，然后使用鼠标滚轮或触控板滚动。如果边框已隐藏，请将指针移到模拟器窗口上，然后使用鼠标滚轮或触控板滚动。 |
| 按下侧边按钮 | 点按设备边框上的侧边按钮。 |
| 按下操作按钮 | 点按设备边框上的操作按钮，或选取 Controls \> Action Button。 |

## 在画布中与 tvOS App 交互

使用指针、键盘和菜单项，在模拟的 tvOS 设备上执行手势。

| 手势 | 模拟方式 |
|---|---|
| 将焦点向左移动 | 按下左箭头键。 |
| 将焦点向右移动 | 按下右箭头键。 |
| 将焦点向上移动 | 按下上箭头键。 |
| 将焦点向下移动 | 按下下箭头键。 |
| 触发当前焦点的操作 | 按下 Return 键。 |
| 在导览层级（navigation hierarchy）中向上移动一级 | 按下 Escape 键。 |

## 处理实体设备上的相机和麦克风访问冲突

在 Device Hub 中与实体设备交互时，无法访问相机或麦克风。

开始在 Device Hub 中与实体设备交互前，请退出设备上所有访问相机或麦克风的 App。然后在边栏中选择设备，并点按画布中的 View Screen 与设备交互。

与设备交互期间，访问相机或麦克风的低优先级 App（例如“相机”和“语音备忘录”）无法使用这些传感器，可能会录下静音音频和空白视频。

如果你在设备上启动访问相机或麦克风的高优先级 App（例如“电话”或 FaceTime），Device Hub 会停止交互。若要继续与设备交互，请退出设备上使用相机或麦克风的 App，然后再次点按 Device Hub 中的 View Screen。

## 另请参阅

### 设备交互

- [配置模拟设备的环境](configuring-the-environment-of-a-simulated-device.md) — 修改模拟设备的设置。
- [从设备捕获屏幕截图和视频](capturing-screenshots-and-videos-from-devices.md) — 录制交互并捕获 App 屏幕截图，以便共享、审核或提交到 App Store。
