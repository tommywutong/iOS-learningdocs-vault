---
title: 工具栏
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbars
source_url: 'https://developer.apple.com/documentation/swiftui/toolbars'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbars.json'
content_hash: 'sha256:c559396034bc4e6f'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 工具栏

<sub>API 集合</sub>

提供对常用命令和控制的即时访问。

## 概述

系统可能会在你的 App 内容的上方或下方呈现工具栏，具体取决于平台和上下文。

![](../../../attachments/16bd7e535a587b44ad58a35c066192d9/toolbars-hero@2x.png)

通过对你的 App 中的视图应用 [toolbar(content:)](<view/toolbar(content_).md>) 视图修饰符来向工具栏添加条目。你还可以使用视图修饰符来配置工具栏。例如，你可以使用 [toolbar(_:for:)](<view/toolbar(__for_).md>) 修饰符设置工具栏的可见性。

有关设计指引，请参阅《人机界面指南》中的[工具栏](../design/human-interface-guidelines/toolbars.md)。

## 主题

### 填充工具栏

- [toolbar(content:)](<view/toolbar(content_).md>) — 用指定的条目填充工具栏或导航栏。
- [ToolbarItem](toolbaritem.md) — 一种模型，表示可以放置在工具栏或导航栏中的条目。
- [ToolbarItemGroup](toolbaritemgroup.md) — 一种模型，表示一组可以放置在工具栏或导航栏中的 `ToolbarItem`。
- [ToolbarItemPlacement](toolbaritemplacement.md) — 一种定义工具栏条目放置位置的结构。
- [toolbarOverflowMenu(content:)](<view/toolbaroverflowmenu(content_).md>) — 配置工具栏的溢出菜单。 _(beta)_
- [ToolbarOverflowMenu](toolbaroverflowmenu.md) — 工具栏的溢出菜单。 _(beta)_
- [ToolbarContent](toolbarcontent.md) — 遵循该协议的类型表示可以放置在工具栏各个位置中的条目。
- [ToolbarContentBuilder](toolbarcontentbuilder.md) — 从多表达式闭包构建工具栏条目集合。
- [ToolbarSpacer](toolbarspacer.md) — 工具栏中的标准空白条目。
- [DefaultToolbarItem](defaulttoolbaritem.md) — 表示系统组件的工具栏条目。

### 填充可自定的工具栏

- [toolbar(id:content:)](<view/toolbar(id_content_).md>) — 用指定的条目填充工具栏或导航栏，并允许用户自定。
- [toolbarItemHidden(_:)](<view/toolbaritemhidden(__).md>) — 隐藏控制组工具栏条目内的单个视图。
- [CustomizableToolbarContent](customizabletoolbarcontent.md) — 遵循该协议的类型表示可以放置在可自定工具栏各个位置中的条目。
- [ToolbarCustomizationBehavior](toolbarcustomizationbehavior.md) — 可自定工具栏内容的自定行为。
- [ToolbarCustomizationOptions](toolbarcustomizationoptions.md) — 影响可自定工具栏内容默认自定行为的选项。
- [SearchToolbarBehavior](searchtoolbarbehavior.md) — 工具栏中搜索栏的行为。

### 移除默认条目

- [toolbar(removing:)](<view/toolbar(removing_).md>) — 移除默认存在的工具栏条目
- [ToolbarDefaultItemKind](toolbardefaultitemkind.md) — `View` 默认添加的一种工具栏条目类型。

### 设置工具栏可见性

- [toolbar(_:for:)](<view/toolbar(__for_).md>) — 指定由 SwiftUI 管理的栏的可见性。
- [toolbarVisibility(_:for:)](<view/toolbarvisibility(__for_).md>) — 指定由 SwiftUI 管理的栏的可见性。
- [toolbarBackgroundVisibility(_:for:)](<view/toolbarbackgroundvisibility(__for_).md>) — 指定由 SwiftUI 管理的栏的背景的首选可见性。
- [ToolbarPlacement](toolbarplacement.md) — 工具栏的放置位置。
- [ContentToolbarPlacement](contenttoolbarplacement.md)

### 指定工具栏内容的角色

- [toolbarRole(_:)](<view/toolbarrole(__).md>) — 为填充工具栏的内容配置语义角色。
- [ToolbarRole](toolbarrole.md) — 填充工具栏的内容的用途。

### 设置工具栏样式

- [toolbarBackground(_:for:)](<view/toolbarbackground(__for_).md>) — 指定由 SwiftUI 管理的栏的背景的首选形状样式。
- [toolbarColorScheme(_:for:)](<view/toolbarcolorscheme(__for_).md>) — 指定由 SwiftUI 管理的栏的首选配色方案。
- [toolbarForegroundStyle(_:for:)](<view/toolbarforegroundstyle(__for_).md>) — 指定由 SwiftUI 管理的栏的首选前景样式。
- [windowToolbarStyle(_:)](<scene/windowtoolbarstyle(__).md>) — 设置在此场景中定义的工具栏的样式。
- [WindowToolbarStyle](windowtoolbarstyle.md) — 窗口工具栏外观和行为的规格说明。
- [toolbarLabelStyle](environmentvalues/toolbarlabelstyle.md) — 要应用于工具栏内控制的标签样式。
- [ToolbarLabelStyle](toolbarlabelstyle.md) — 工具栏的标签样式。
- [SpacerSizing](spacersizing.md) — 一种定义空白项应如何调整自身尺寸的类型。

### 配置工具栏标题显示模式

- [toolbarTitleDisplayMode(_:)](<view/toolbartitledisplaymode(__).md>) — 为此视图配置工具栏标题显示模式。
- [ToolbarTitleDisplayMode](toolbartitledisplaymode.md) — 一种定义工具栏标题行为的类型。

### 设置工具栏标题菜单

- [toolbarTitleMenu(content:)](<view/toolbartitlemenu(content_).md>) — 配置工具栏的标题菜单。
- [ToolbarTitleMenu](toolbartitlemenu.md) — 工具栏的标题菜单。

### 创建挂饰

- [ornament(visibility:attachmentAnchor:contentAlignment:ornament:)](<view/ornament(visibility_attachmentanchor_contentalignment_ornament_).md>) — 呈现一个挂饰。
- [OrnamentAttachmentAnchor](ornamentattachmentanchor.md) — 挂饰的附加锚点。

### 控制条目可见性

- [visibilityPriority(_:)](<toolbarcontent/visibilitypriority(__).md>) — 定义工具栏条目的可见性优先级。
- [ToolbarItemVisibilityPriority](toolbaritemvisibilitypriority.md) — 定义工具栏条目可见性优先级的值。

### 最小化工具栏

- [toolbarMinimizationBehavior(_:for:)](<view/toolbarminimizationbehavior(__for_).md>) — 为指定的栏设置最小化行为。 _(beta)_
- [ToolbarMinimizationBehavior](toolbarminimizationbehavior.md) — 工具栏的最小化行为。 _(beta)_
- [toolbarMinimizationRestoration(_:for:)](<view/toolbarminimizationrestoration(__for_).md>) — 为指定的栏设置最小化期间的状态恢复行为。 _(beta)_
- [ToolbarMinimizationRestoration](toolbarminimizationrestoration.md) — 工具栏最小化期间的状态恢复行为。 _(beta)_
- [toolbarMinimizationSafeAreaAdjustment(_:for:)](<view/toolbarminimizationsafeareaadjustment(__for_).md>) — 为指定的栏设置最小化期间的安全区调整。 _(beta)_
- [ToolbarMinimizationSafeAreaAdjustment](toolbarminimizationsafeareaadjustment.md) — 工具栏最小化期间的安全区调整。 _(beta)_

## 另请参阅

### App 结构

- [App 组织](app-organization.md) — 定义 App 的入口点和顶层结构。
- [场景](scenes.md) — 声明构成 App 各个部分的用户界面分组。
- [窗口](windows.md) — 在一个窗口或一组窗口中显示用户界面内容。
- [沉浸式空间](immersive-spaces.md) — 在用户周围显示无边界的内容。
- [文稿](documents.md) — 让人们能够打开和管理文稿。
- [导航](navigation.md) — 使用户能够在场景内你的 App 视图层级结构的不同部分之间移动。
- [模态呈现方式](modal-presentations.md) — 在提供专注交互的独立视图中呈现内容。
- [搜索](search.md) — 让人们能够搜索你的 App 内的文本或其他内容。
- [App 扩展](app-extensions.md) — 将你的 App 的基本功能扩展到系统的其他部分，例如添加小组件。
