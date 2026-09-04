---
title: 为你的 App 添加硬件键盘支持
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, Xcode 12.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adding-hardware-keyboard-support-to-your-app
source_url: 'https://developer.apple.com/documentation/uikit/adding-hardware-keyboard-support-to-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adding-hardware-keyboard-support-to-your-app.json'
content_hash: 'sha256:9764349eab10c9d2'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [键盘与输入](keyboards-and-input.md)

# 为你的 App 添加硬件键盘支持

<sub>文章</sub>

通过处理原始键盘事件、编写自定义键盘快捷键以及配合手势识别器工作，增强与你 App 的交互。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC20 场次 [10109: Hardware Keyboard Best Practices](https://developer.apple.com/wwdc20/10109/)。

## 另请参阅

### 物理键盘

- [处理在物理键盘上进行的按键操作](handling-key-presses-made-on-a-physical-keyboard.md) — 检测用户何时在物理键盘上按下并松开按键。
- [使用键盘导航 App 的用户界面](navigating-an-app-s-user-interface-using-a-keyboard.md) — 在 iPad App 和用 Mac Catalyst 构建的 App 中，使用键盘和可获得焦点的 UI 元素在用户界面元素之间导航。
- [UIKey](uikey.md) — 提供键盘按键状态信息的对象。
- [UIKeyboardHIDUsage](uikeyboardhidusage.md) — 标识 USB 键盘按键的一组 HID 用法码。

## 下载

- [AddingHardwareKeyboardSupportToYourApp.zip](https://docs-assets.developer.apple.com/published/bfc5b86dd67e/AddingHardwareKeyboardSupportToYourApp.zip)
