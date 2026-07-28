---
title: 在使用 Mac Catalyst 构建的 Mac App 中显示复选框
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst
source_url: 'https://developer.apple.com/documentation/uikit/displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.json'
content_hash: 'sha256:ae420f8732f6a32b'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [Mac Catalyst](mac-catalyst.md)

# 在使用 Mac Catalyst 构建的 Mac App 中显示复选框

<sub>文章</sub>

当 App 以 Mac 用户界面惯用方式运行时，将开关控制（switch control）显示为 Mac 风格的复选框。

## 概述

使用 Mac Catalyst 构建且采用 Mac 用户界面惯用方式的 Mac App，会在 [preferredStyle](uiswitch/preferredstyle.md) 值为 [UISwitchStyleAutomatic](uiswitch/style-swift.enum/automatic.md)（默认值）或 [UISwitchStyleCheckbox](uiswitch/style-swift.enum/checkbox.md) 时，将 [UISwitch](uiswitch.md) 显示为复选框。如果你的 App 不使用 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 惯用方式，开关会显示为滑块式开关。要了解更多信息，请参阅[为 Mac App 选择用户界面惯用方式](choosing-a-user-interface-idiom-for-your-mac-app.md)。

### 为复选框添加文本

若要在复选框旁显示文本，请设置 [title](uiswitch/title.md) 属性。

```swift
let showFavoritesAtTop = UISwitch()
showFavoritesAtTop.title = "Always show favorite recipes at the top"
```

### 调整复选框大小

复选框样式的开关默认 frame 大小为零。如果你没有使用 Auto Layout 来确定开关的大小和位置，请调用 [- sizeToFit](<uiview/sizetofit().md>) 调整其大小，使其占用显示复选框及其标题所需的适当空间。

## 另请参阅

### 用户界面

- [UIKit 目录：创建和自定视图与控制](uikit-catalog-creating-and-customizing-views-and-controls.md) — 使用视图和控制自定 App 的用户界面。
- [使用 Mac Catalyst 构建和改进 App](building-and-improving-your-app-with-mac-catalyst.md) — 通过支持原生控制、多个窗口、共享、打印、菜单和键盘快捷键，改进你的 iPadOS App。
- [移除使用 Mac Catalyst 构建的 Mac App 的标题栏](removing-the-title-bar-in-your-mac-app-built-with-mac-catalyst.md) — 通过移除标题栏，显示填满窗口整个高度的内容。
- [工具栏](toolbar.md) — 在窗口标题栏下方和自定内容上方提供用于放置控制的空间。
- [触控栏](../appkit/touch-bar.md) — 在触控栏中显示交互式内容和控制。
