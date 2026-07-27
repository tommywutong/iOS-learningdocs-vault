---
title: 在用户界面中采用菜单和 UIAction
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, Xcode 11.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adopting-menus-and-uiactions-in-your-user-interface
source_url: 'https://developer.apple.com/documentation/uikit/adopting-menus-and-uiactions-in-your-user-interface'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adopting-menus-and-uiactions-in-your-user-interface.json'
content_hash: 'sha256:44c2d77a9b6d032e'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Menus and shortcuts](menus-and-shortcuts.md)

# 在用户界面中采用菜单和 UIAction

<sub>示例代码</sub>

利用内建的按钮和栏按钮条目支持向用户界面添加菜单，并创建自定义菜单体验。

## 概述

> [!note] 注意
> 此示例代码项目对应 WWDC20 的第 10052 场：[Build with iOS Pickers, Menus and Actions](https://developer.apple.com/wwdc20/10052/)。

## 另请参阅

### 菜单元素和键盘快捷键

- [向菜单栏和用户界面添加菜单与快捷键](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — 向使用 Mac Catalyst 构建的 Mac App 添加菜单和键盘快捷键，以便快速访问实用操作。
- [UIMenuElement](uimenuelement.md) — 表示菜单、操作或命令的对象。
- [UIAction](uiaction.md) — 在闭包中执行操作的菜单元素。
- [UICommand](uicommand.md) — 在 selector 中执行操作的菜单元素。
- [UIKeyCommand](uikeycommand.md) — 指定在硬件键盘上执行的按键操作及其结果操作的对象。
- [UIDeferredMenuElement](uideferredmenuelement.md) — 占位菜单元素，系统会用代码块补全处理程序的结果替换它。
- [Provider](uideferredmenuelement/provider.md)
- [Attributes](uimenuelement/attributes.md) — 决定菜单元素样式的属性。
- [State](uimenuelement/state.md) — 表示基于操作或命令的菜单元素状态的常量。
- [UIMenuLeaf](uimenuleaf.md) — 表示没有子元素的菜单元素对象的接口。

## 下载

- [AdoptingMenusAndUIActionsInYourUserInterface.zip](https://docs-assets.developer.apple.com/published/27cc7dd67349/AdoptingMenusAndUIActionsInYourUserInterface.zip)
