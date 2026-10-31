---
title: 辅助视图修饰符
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-auxiliary-views
source_url: 'https://developer.apple.com/documentation/swiftui/view-auxiliary-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-auxiliary-views.json'
content_hash: 'sha256:b706192e49b3e933'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md) · [View](view.md)

# 辅助视图修饰符

<sub>API 集合</sub>

添加并配置工具栏和上下文菜单等辅助视图。

## 概述

使用这些修饰符来管理呈现特定上下文的控制和信息的辅助视图。例如，你可以向导航栏添加标题和按钮、管理状态栏、创建上下文菜单，以及为多种不同类型的视图添加角标。

## 主题

### 导览标题

- [配置你 App 的导览标题](configure-your-apps-navigation-titles.md) — 使用导览标题显示界面的当前导览状态。
- [navigationTitle(_:)](<view/navigationtitle(__).md>) — 使用本地化字符串资源为导览目的配置视图的标题。
- [navigationSubtitle(_:)](<view/navigationsubtitle(__).md>) — 使用本地化字符串资源为导览目的配置视图的副标题。

### 导览标题配置

- [navigationDocument(_:)](<view/navigationdocument(__).md>) — 为导览目的配置视图的文稿。
- [navigationDocument(_:preview:)](<view/navigationdocument(__preview_).md>) — 为导览目的配置视图的文稿。

### 导航栏

- [navigationBarBackButtonHidden(_:)](<view/navigationbarbackbuttonhidden(__).md>) — 隐藏该视图的导航栏返回按钮。
- [navigationBarTitleDisplayMode(_:)](<view/navigationbartitledisplaymode(__).md>) — 为该视图配置标题显示模式。

### 导览叠放与分栏

- [navigationDestination(for:destination:)](<view/navigationdestination(for_destination_).md>) — 将目的地视图与所呈现的数据类型关联，以便在导览叠放中使用。
- [navigationDestination(isPresented:destination:)](<view/navigationdestination(ispresented_destination_).md>) — 将目的地视图与一个可用于把该视图压入 [NavigationStack](navigationstack.md) 的绑定关联。
- [navigationDestination(item:destination:)](<view/navigationdestination(item_destination_).md>) — 将目的地视图与一个被绑定的值关联，以便在导览叠放或导览分栏视图中使用
- [navigationSplitViewColumnWidth(_:)](<view/navigationsplitviewcolumnwidth(__).md>) — 为包含此视图的栏设置固定的首选宽度。
- [navigationSplitViewColumnWidth(min:ideal:max:)](<view/navigationsplitviewcolumnwidth(min_ideal_max_).md>) — 为包含此视图的栏设置灵活的首选宽度。
- [navigationLinkIndicatorVisibility(_:)](<view/navigationlinkindicatorvisibility(__).md>) — 配置导览链接是否显示显示指示符。
- [navigationTransition(_:)](<view/navigationtransition(__).md>) — 为该视图设置导览过渡样式。

### 滚动视图边缘

- [scrollEdgeEffectStyle(_:for:)](<view/scrolledgeeffectstyle(__for_).md>) — 为此层级结构内的滚动视图配置滚动边缘效果样式。
- [scrollEdgeEffectHidden(_:for:)](<view/scrolledgeeffecthidden(__for_).md>) — 隐藏此层级结构内滚动视图的任何滚动边缘效果。

### 标签页视图

- [defaultAdaptableTabBarPlacement(_:)](<view/defaultadaptabletabbarplacement(__).md>) — 为使用可适配边栏样式的标签页视图中的标签页指定默认位置。
- [defaultTabBarPlacement(_:)](<view/defaulttabbarplacement(__).md>) — 在标签页栏无法在不同表示之间自适应、只能显示一种表示的平台上，为 [sidebarAdaptable](tabviewstyle/sidebaradaptable.md) 样式下 [TabView](tabview.md) 的标签页指定首选位置。 _(beta)_
- [sectionActions(content:)](<view/sectionactions(content_).md>) — 向分区添加自定义操作。
- [tabBarMinimizeBehavior(_:)](<view/tabbarminimizebehavior(__).md>) — 设置标签页栏的最小化行为。
- [tabViewBottomAccessory(content:)](<view/tabviewbottomaccessory(content_).md>) — 将一个视图放置为标签页视图的底部附件。
- [tabViewBottomAccessory(isEnabled:content:)](<view/tabviewbottomaccessory(isenabled_content_).md>) — 将一个视图放置为标签页视图的底部附件。使用此修饰符可动态显示和隐藏附件视图。
- [tabViewCustomization(_:)](<view/tabviewcustomization(__).md>) — 指定要应用到标签页视图边栏表示的自定项。
- [tabViewSearchActivation(_:)](<view/tabviewsearchactivation(__).md>) — 配置搜索标签页中搜索的激活与停用行为。
- [tabViewSidebarHeader(content:)](<view/tabviewsidebarheader(content_).md>) — 向标签页视图的边栏添加自定义标头。
- [tabViewSidebarFooter(content:)](<view/tabviewsidebarfooter(content_).md>) — 向标签页视图的边栏添加自定义页脚。
- [tabViewSidebarBottomBar(content:)](<view/tabviewsidebarbottombar(content_).md>) — 向标签页视图的边栏添加自定义底栏。

### 工具栏

- [toolbar(content:)](<view/toolbar(content_).md>) — 用指定条目填充工具栏或导航栏。
- [toolbar(id:content:)](<view/toolbar(id_content_).md>) — 用指定条目填充工具栏或导航栏，并允许用户自定。
- [toolbar(_:for:)](<view/toolbar(__for_).md>) — 指定由 SwiftUI 管理的某个栏的可见性。
- [contentToolbar(for:content:)](<view/contenttoolbar(for_content_).md>) — 用你提供的视图填充指定内容视图类型的工具栏。
- [toolbar(removing:)](<view/toolbar(removing_).md>) — 移除默认存在的某个工具栏条目
- [toolbarVisibility(_:for:)](<view/toolbarvisibility(__for_).md>) — 指定由 SwiftUI 管理的某个栏的可见性。
- [toolbarBackground(_:for:)](<view/toolbarbackground(__for_).md>) — 指定由 SwiftUI 管理的某个栏的背景的首选形状样式。
- [toolbarBackgroundVisibility(_:for:)](<view/toolbarbackgroundvisibility(__for_).md>) — 指定由 SwiftUI 管理的某个栏上背景的首选可见性。
- [toolbarItemHidden(_:)](<view/toolbaritemhidden(__).md>) — 隐藏控制组工具栏条目中的单个视图。
- [toolbarForegroundStyle(_:for:)](<view/toolbarforegroundstyle(__for_).md>) — 指定由 SwiftUI 管理的各个栏的首选前景样式。
- [toolbarColorScheme(_:for:)](<view/toolbarcolorscheme(__for_).md>) — 指定由 SwiftUI 管理的某个栏的首选颜色方案。
- [toolbarOverflowMenu(content:)](<view/toolbaroverflowmenu(content_).md>) — 配置工具栏的溢出菜单。 _(beta)_
- [toolbarRole(_:)](<view/toolbarrole(__).md>) — 为填充工具栏的内容配置语义角色。
- [toolbarMinimizationBehavior(_:for:)](<view/toolbarminimizationbehavior(__for_).md>) — 为指定的栏设置最小化行为。 _(beta)_
- [toolbarMinimizationRestoration(_:for:)](<view/toolbarminimizationrestoration(__for_).md>) — 为指定的栏在最小化期间设置恢复行为。 _(beta)_
- [toolbarMinimizationSafeAreaAdjustment(_:for:)](<view/toolbarminimizationsafeareaadjustment(__for_).md>) — 为指定的栏在最小化期间设置安全区调整。 _(beta)_
- [toolbarTitleMenu(content:)](<view/toolbartitlemenu(content_).md>) — 配置工具栏的标题菜单。
- [toolbarTitleDisplayMode(_:)](<view/toolbartitledisplaymode(__).md>) — 为该视图配置工具栏标题显示模式。
- [ornament(visibility:attachmentAnchor:contentAlignment:ornament:)](<view/ornament(visibility_attachmentanchor_contentalignment_ornament_).md>) — 呈现一个挂饰。

### 上下文菜单

- [contextMenu(menuItems:)](<view/contextmenu(menuitems_).md>) — 向视图添加上下文菜单。
- [contextMenu(menuItems:preview:)](<view/contextmenu(menuitems_preview_).md>) — 向视图添加带有自定义预览的上下文菜单。
- [contextMenu(forSelectionType:menu:primaryAction:)](<view/contextmenu(forselectiontype_menu_primaryaction_).md>) — 向视图添加基于条目的上下文菜单。

### 角标

- [badge(_:)](<view/badge(__).md>) — 根据本地化字符串资源为视图生成角标。
- [badgeProminence(_:)](<view/badgeprominence(__).md>) — 指定此视图创建的角标的醒目程度。

### 列表

- [sectionIndexLabel(_:)](<view/sectionindexlabel(__).md>) — 设置在分区索引用于指向此分区的标签，通常只有一个字符长。

### 帮助文本

- [help(_:)](<view/help(__).md>) — 使用你提供的本地化字符串资源为视图添加帮助文本。

### 状态栏

- [statusBarHidden(_:)](<view/statusbarhidden(__).md>) — 设置状态栏的可见性。 _(已废弃)_

### 外部显示器

- [sceneAccessory(content:)](<view/sceneaccessory(content_).md>) — 定义与 `self` 关联的任何场景附件。 _(beta)_

### Touch Bar

- [touchBar(content:)](<view/touchbar(content_).md>) — 设置 Touch Bar 显示的内容。
- [touchBar(_:)](<view/touchbar(__).md>) — 设置在适用时显示在 Touch Bar 中的内容。
- [touchBarItemPrincipal(_:)](<view/touchbaritemprincipal(__).md>) — 设置对此 Touch Bar 具有特殊意义的主要视图。
- [touchBarCustomizationLabel(_:)](<view/touchbarcustomizationlabel(__).md>) — 设置一个用户可见的字符串，用于标识该视图的功能。
- [touchBarItemPresence(_:)](<view/touchbaritempresence(__).md>) — 设置用户自定视图的行为。

## 另请参阅

### 配置视图元素

- [辅助功能修饰符](view-accessibility.md) — 让你的 SwiftUI App 对每个人（包括残障人士）都具备辅助功能。
- [外观修饰符](view-appearance.md) — 配置视图的前景和背景样式、控制以及可见性。
- [文本与符号修饰符](view-text-and-symbols.md) — 管理视图中文本的渲染、选择和输入。
- [图表视图修饰符](view-chart-view.md) — 配置你用 Swift Charts 声明的图表。
