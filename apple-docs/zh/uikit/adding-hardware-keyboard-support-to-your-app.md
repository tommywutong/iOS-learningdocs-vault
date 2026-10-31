---
title: 为你的 App 添加硬件键盘支持
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, Xcode 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/adding-hardware-keyboard-support-to-your-app
source_url: 'https://developer.apple.com/documentation/uikit/adding-hardware-keyboard-support-to-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adding-hardware-keyboard-support-to-your-app.json'
content_hash: 'sha256:9764349eab10c9d2'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Keyboards and input](keyboards-and-input.md)

# 为你的 App 添加硬件键盘支持

<sub>示例代码</sub>

通过处理原始键盘事件、编写自定键盘快捷键以及使用手势识别器，增强与 App 的交互。

## 概述

> [!note] 注意
> 此示例代码项目与 WWDC20 会话 [10109: Hardware Keyboard Best Practices](https://developer.apple.com/wwdc20/10109/) 相关联。

## 另请参阅

### 物理键盘

- [Handling key presses made on a physical keyboard](handling-key-presses-made-on-a-physical-keyboard.md) — 检测某人何时在物理键盘上按下与释放按键。
- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md) — 在 iPad App 与使用 Mac Catalyst 构建的 App 中，使用键盘与可聚焦 UI 元素在用户界面元素间导航。
- [UIKey](uikey.md) — 一个提供键盘按键状态信息的对象。
- [UIKeyboardHIDUsage](uikeyboardhidusage.md) — 一组标识 USB 键盘按键的 HID 使用码。

## 下载

- [AddingHardwareKeyboardSupportToYourApp.zip](https://docs-assets.developer.apple.com/published/bfc5b86dd67e/AddingHardwareKeyboardSupportToYourApp.zip)
