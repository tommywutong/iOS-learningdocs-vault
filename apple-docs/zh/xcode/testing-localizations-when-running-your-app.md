---
title: 测试运行 App 时的本地化
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/testing-localizations-when-running-your-app
source_url: 'https://developer.apple.com/documentation/xcode/testing-localizations-when-running-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/testing-localizations-when-running-your-app.json'
content_hash: 'sha256:ef3db88282133f49'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [本地化](localization.md)

# 测试运行 App 时的本地化

<sub>文章</sub>

在你自己支持的每种语言和地区运行你的 App，以全面测试 App。

## 概述

在你翻译字符串并针对不同文化和地区适配资源后，通过在 Run 方案（Run scheme）中选择语言和地区来测试 App 中的每一处本地化。

### 在方案中选择语言和地区

要在特定语言和地区测试你的 App：

1. 在 Xcode 中，选择 Product \> Scheme \> Edit Scheme。
2. 在对话框中，选择侧边栏里的 Run，然后点按右侧的 Options。
3. 从 App Language 弹出式菜单中，选择语言；从 App Region 弹出式菜单中，选择地区。
4. 点按 Close。
5. 在项目窗口工具栏中，选择一个运行目标，然后点按 Run。

要使用设备上的“语言与地区”设置，请从弹出式菜单中选择 System Language 和 System Region。

> [!note] 注意
> 如果你更改模拟器或实体设备上的“语言与地区”设置，整个操作系统都会使用这些设置，而不仅仅是你的 App。

## 另请参阅

### 测试

- [预览本地化](previewing-localizations.md) — 在 SwiftUI 预览或 Interface Builder 预览中测试本地化。
