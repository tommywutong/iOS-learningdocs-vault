---
title: Toolbar
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/toolbar
source_url: 'https://developer.apple.com/documentation/uikit/toolbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/toolbar.json'
content_hash: 'sha256:c6e18fdcd940fd37'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Mac Catalyst](mac-catalyst.md)

# Toolbar

<sub>API 集合</sub>

在窗口标题栏下方、你自定义内容上方提供一处放置控制的空间。

## 主题

### View

- [Integrating a Toolbar and Touch Bar into Your App](../appkit/integrating-a-toolbar-and-touch-bar-into-your-app.md) — 让用户可以从工具栏及对应的 Touch Bar 快速访问你 App 的各项特性。
- [NSToolbar](../appkit/nstoolbar.md) — 一个对象，用于管理你 App 自定义内容上方、窗口标题栏下方或与标题栏整合在一起的那部分空间。
- [NSToolbarItemValidation](../appkit/nstoolbaritemvalidation.md) — 对某个工具栏项目的验证。

### Items

- [NSToolbarItem](../appkit/nstoolbaritem.md) — 出现在窗口工具栏中的单个项目。
- [NSToolbarItemGroup](../appkit/nstoolbaritemgroup.md) — 工具栏项目中的一组子项目。
- [NSToolbarItemGroup.ControlRepresentation](../appkit/nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [NSToolbarItemGroup.SelectionMode](../appkit/nstoolbaritemgroup/selectionmode-swift.enum.md) — 一个值，指示某个分组工具栏项目如何选择其子项目。
- [NSMenuToolbarItem](../appkit/nsmenutoolbaritem.md) — 在窗口工具栏中呈现一个菜单的控制。
- [NSSearchToolbarItem](../appkit/nssearchtoolbaritem.md) — 一个包含搜索栏的工具栏项目，针对基于文本的搜索进行了优化。
- [NSTrackingSeparatorToolbarItem](../appkit/nstrackingseparatortoolbaritem.md) — 一个工具栏分隔符，与同一窗口中的垂直拆分视图对齐。
- [NSUIViewToolbarItem](nsuiviewtoolbaritem.md) — 窗口工具栏中承载自定义 UIKit 视图的一个项目。

### Item validation

- [NSCloudSharingValidation](../appkit/nscloudsharingvalidation.md) — 云共享工具栏项目用来获取项目验证的协议。

## 另请参阅

### User interface

- [UIKit Catalog: Creating and customizing views and controls](uikit-catalog-creating-and-customizing-views-and-controls.md) — 使用视图和控制自定义你 App 的用户界面。
- [Building and improving your app with Mac Catalyst](building-and-improving-your-app-with-mac-catalyst.md) — 通过支持原生控制、多窗口、共享、打印、菜单和键盘快捷键，使用 Mac Catalyst 改进你的 iPadOS App。
- [Displaying a checkbox in your Mac app built with Mac Catalyst](displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md) — 当你的 App 在 Mac 用户界面习惯用法下运行时，将切换控制以 Mac 风格的复选框形式呈现。
- [Removing the title bar in your Mac app built with Mac Catalyst](removing-the-title-bar-in-your-mac-app-built-with-mac-catalyst.md) — 通过移除标题栏，显示铺满整个窗口高度的内容。
- [Touch Bar](../appkit/touch-bar.md) — 在 Touch Bar 中显示交互式内容和控制。
