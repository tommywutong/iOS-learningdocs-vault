---
title: 菜单与命令
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/menus-and-commands
source_url: 'https://developer.apple.com/documentation/swiftui/menus-and-commands'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menus-and-commands.json'
content_hash: 'sha256:14c4d516794df3ba'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 菜单与命令

<sub>API 集合</sub>

以节省空间、依赖上下文的方式提供对命令和控制的访问。

## 概述

使用菜单让人们能够便捷地访问常用命令。你可以使用 [commands(content:)](<scene/commands(content_).md>) 场景修饰符向 macOS 或 iPadOS App 的菜单栏添加条目，或者使用 [contextMenu(menuItems:)](<view/contextmenu(menuitems_).md>) 视图修饰符创建上下文菜单，让人们在当前任务附近唤出它。

![](../../../attachments/dfe1ae858d3f19de19a190f122aaf44a/menus-and-commands-hero@2x.png)

通过把 [Menu](menu.md) 实例嵌套在其他实例中来创建子菜单。使用 [Divider](divider.md) 视图在菜单元素之间创建分隔符。

有关设计指引，请参阅《人机界面指南》中的 [Menus](../design/human-interface-guidelines/menus.md)。

## 主题

### 构建菜单栏

- [使用 SwiftUI 构建和自定义菜单栏](building-and-customizing-the-menu-bar-with-swiftui.md) — 通过为 iPadOS 和 macOS 构建原生菜单栏，提供无缝的跨平台用户体验。

### 创建菜单

- [使用自适应控制填充 SwiftUI 菜单](populating-swiftui-menus-with-adaptive-controls.md) — 通过在菜单中填充控制并直观地组织内容，来改进你的 App。
- [Menu](menu.md) — 一个用于呈现操作菜单的控制。
- [menuStyle(_:)](<view/menustyle(__).md>) — 设置此视图内菜单的样式。

### 创建上下文菜单

- [contextMenu(menuItems:)](<view/contextmenu(menuitems_).md>) — 向视图添加上下文菜单。
- [contextMenu(menuItems:preview:)](<view/contextmenu(menuitems_preview_).md>) — 向视图添加带有自定义预览的上下文菜单。
- [contextMenu(forSelectionType:menu:primaryAction:)](<view/contextmenu(forselectiontype_menu_primaryaction_).md>) — 向视图添加基于条目的上下文菜单。

### 定义命令

- [commands(content:)](<scene/commands(content_).md>) — 向场景添加命令。
- [commandsRemoved()](<scene/commandsremoved().md>) — 移除被修饰场景定义的所有命令。
- [commandsReplaced(content:)](<scene/commandsreplaced(content_).md>) — 用构建器中的命令替换被修饰场景定义的所有命令。
- [Commands](commands.md) — 符合该协议的类型代表一组相关的命令，可以在 macOS 上通过主菜单、在 iOS 上通过按键命令暴露给用户。
- [CommandMenu](commandmenu.md) — 命令菜单是独立的顶层容器，用于放置执行相关的、App 特定命令的控制。
- [CommandGroup](commandgroup.md) — 可以添加到现有命令菜单的控制组。
- [CommandsBuilder](commandsbuilder.md) — 从多表达式闭包构建命令集。与 `ContentBuilder` 一样，它支持在闭包体内最多使用十个表达式。
- [CommandGroupPlacement](commandgroupplacement.md) — 可用于放置新命令组的标准位置。

### 获取内置命令组

- [SidebarCommands](sidebarcommands.md) — 一组用于操作窗口边栏的内置命令。
- [TextEditingCommands](texteditingcommands.md) — 一组用于搜索、编辑和变换文本选区的内置命令。
- [TextFormattingCommands](textformattingcommands.md) — 一组用于变换文本选区所应用样式的内置命令。
- [ToolbarCommands](toolbarcommands.md) — 一组用于操作窗口工具栏的内置命令。
- [ImportFromDevicesCommands](importfromdevicescommands.md) — 一组可从附近设备导入内容的内置命令。
- [InspectorCommands](inspectorcommands.md) — 一组用于操作检查器的内置命令。
- [EmptyCommands](emptycommands.md) — 一个空的命令组。

### 显示菜单指示符

- [menuIndicator(_:)](<view/menuindicator(__).md>) — 设置此视图内控制的菜单指示符可见性。
- [menuIndicatorVisibility](environmentvalues/menuindicatorvisibility.md) — 应用到视图内控制的菜单指示符可见性。

### 配置菜单关闭行为

- [menuActionDismissBehavior(_:)](<view/menuactiondismissbehavior(__).md>) — 告知菜单在执行某个操作后是否关闭。
- [MenuActionDismissBehavior](menuactiondismissbehavior.md) — 菜单关闭行为选项的集合。

### 设置首选顺序

- [menuOrder(_:)](<view/menuorder(__).md>) — 为从此视图呈现的菜单设置条目的首选顺序。
- [menuOrder](environmentvalues/menuorder.md) — 从此视图呈现的菜单条目的首选顺序。
- [MenuOrder](menuorder.md) — 菜单呈现其内容的顺序。

### 已废弃类型

- [MenuButton](menubutton.md) — 一个按钮，按下时显示包含选项列表的菜单。 _(已废弃)_
- [PullDownButton](pulldownbutton.md) _(已废弃)_
- [ContextMenu](contextmenu.md) — 一个容器，用于你作为上下文菜单条目呈现的视图。 _(已废弃)_

## 另请参阅

### 视图

- [视图基础](view-fundamentals.md) — 使用视图的层级结构定义 App 的视觉元素。
- [视图配置](view-configuration.md) — 调整层级结构中视图的特性。
- [视图样式](view-styles.md) — 为不同类型的视图应用内置和自定义的外观与行为。
- [动画](animations.md) — 创建流畅的视觉更新，以响应状态变化。
- [文本输入与输出](text-input-and-output.md) — 显示带格式的文本，并获取用户的文本输入。
- [图像](images.md) — 向 App 的用户界面添加图像和符号。
- [控制与指示符](controls-and-indicators.md) — 显示值并获取用户的选择。
- [形状](shapes.md) — 用颜色、渐变或其他图案描摹并填充内置和自定义形状。
- [绘图与图形](drawing-and-graphics.md) — 用图形效果和自定义绘图增强你的视图。
