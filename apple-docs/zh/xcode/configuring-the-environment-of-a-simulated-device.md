---
title: 配置模拟设备的环境
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-the-environment-of-a-simulated-device
source_url: 'https://developer.apple.com/documentation/xcode/configuring-the-environment-of-a-simulated-device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-the-environment-of-a-simulated-device.json'
content_hash: 'sha256:728886a525180aac'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Device Hub](device-hub.md)

# 配置模拟设备的环境

<sub>文章</sub>

修改模拟设备的设置。

## 概述

在模拟设备上测试你的 App，使用不同的操作系统设置，例如辅助功能（accessibility）、外观、位置、音频和方向。若要测试你的 App 在新设备上或重启后的加载情况，可以重置或重启模拟设备。

## 更改环境设置

在 Device Hub 中，于边栏中选择一台模拟设备，如有需要，在画布中点击“启动”。在设置检查器中，更改环境设置，例如外观、Liquid Glass 和文本大小。然后在模拟器上运行你的 App，并观察 App 是否相应地调整。

若要在模拟器中运行你的 App，请参阅[在模拟或物理设备上运行你的 App](running-your-app-on-simulated-or-physical-devices.md)。

## 调整画布大小

在展开的窗口中，使用工具栏中的控制调整画布大小。例如，缩放画布以检查 App 中使用的控制、图像和颜色的对齐情况。

- 若要更改画布缩放比例，请点击“缩小”或“放大”按钮。
- 若要将设备缩放到画布大小，请点击“缩放以适合”按钮。
- 若要将画布大小更改为物理设备的屏幕大小，请点击“物理大小”按钮。

对于紧凑窗口，请在工具栏中点击“展开以查看所有控制”以展开窗口并显示调整大小控制，或调整紧凑窗口大小以更改画布缩放比例。

## 更改模拟 iPhone 的屏幕大小

若要快速验证你的界面是否适应不同设备大小，你可以将模拟 iPhone 屏幕调整为任意大小，而无需在多个设备上运行你的 App。

若要进入调整大小模式，请在模拟器上运行你的 App，然后点击画布工具栏中的“进入调整大小模式”按钮。然后拖动模拟器顶部、底部或侧面的手柄来调整屏幕大小。或者，在模拟器下方输入屏幕尺寸。Device Hub 会将屏幕大小吸附到最接近的有效尺寸。完成后，点击“退出调整大小模式”。

![](../../../attachments/f8196d8e075a578565940e4c1f64a548/resize-iphone-canvas@2x.png)

<sub>Device Hub 的屏幕截图，显示 App 在 iPhone 模拟器中运行，调整大小模式已启用，设备四周出现手柄。</sub>

## 设置音频输入和输出

设置模拟设备使用的音频输入和音频输出。

- 若要调整音频音量，请选择“设备”>“声音”>“增大音量”或“设备”>“声音”>“减小音量”。
- 若要设置音频输入，请从“设备”>“声音”>“声音输入”子菜单中选择一个设备。选择“系统”以使用与 Mac 相同的音频输入。
- 若要设置音频输出，请从“设备”>“声音”>“声音输出”子菜单中选择一个设备。选择“系统”以使用与 Mac 相同的音频输出。

或者，使用设置检查器中的“声音”、“输出”和“输入”控制来执行这些操作。

Device Hub 会跟踪最近的输入和输出选择。当当前选定的设备断开连接时，Device Hub 会尝试连接到先前选定的设备。

> [!note] 注意
> 当你选择蓝牙耳机作为输入源时，在模拟器中播放或收听音频会将耳机设置为通话模式，从而降低音频质量。若要以全质量收听声音，请为模拟器选择其他音频输入源。

## 重启或重置模拟设备

重启模拟设备以模拟设备关机和再次开机的过程。点击模拟器上方工具栏中的“更多”按钮 (…)，然后选择“关机”或“重启”。或者，按住 Control 键点击边栏中的设备，然后从上下文菜单中选择“关机”或“重启”。

若要重置模拟设备（擦除所有内容和设置），请先关闭设备，然后选择“设备”>“重置内容和设置”。

## 另请参阅

### 设备交互

- [在 Device Hub 中与你的 App 交互](interacting-with-your-app-in-device-hub.md) — 使用 Device Hub 控制在模拟设备和物理设备上与你 App 的交互。
- [从设备捕获屏幕截图和视频](capturing-screenshots-and-videos-from-devices.md) — 记录交互并捕获你的 App 的屏幕截图，以便共享、审查或提交到 App Store。
