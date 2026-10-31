---
title: 导览
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/navigation
source_url: 'https://developer.apple.com/documentation/swiftui/navigation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigation.json'
content_hash: 'sha256:248d3ec6cf50a9be'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 导览

<sub>API 集合</sub>

让人们能够在场景内移动到你 App 视图层级结构的不同部分。

## 概述

使用导览容器为 App 的用户界面提供结构，让人们能够轻松在你的 App 各部分之间移动。

![](../../../attachments/f89769a3e08273224563454dc8f3ce0d/navigation-hero@2x.png)

例如，人们可以使用 [NavigationStack](navigationstack.md) 在一组叠放的视图中前后移动，或者使用 [TabView](tabview.md) 从标签页栏中选择要显示的视图。

通过向容器添加 [navigationSplitViewStyle(_:)](<view/navigationsplitviewstyle(__).md>) 之类的视图修饰符来配置导览容器。对容器内的视图使用其他修饰符，可以在容器显示该视图时影响容器的行为。例如，你可以在视图上使用 [navigationTitle(_:)](<view/navigationtitle(__).md>) 提供一个工具栏标题，在显示该视图时展示。

## 主题

### 基础

- [了解导览叠放](understanding-the-navigation-stack.md) — 了解导览叠放、链接，以及如何在 App 结构中管理导览类型。

### 在分栏中呈现视图

- [为你的 SwiftUI App 带来健壮的导览结构](bringing-robust-navigation-structure-to-your-swiftui-app.md) — 使用导览链接、叠放、目的地和路径，为所有平台提供流畅的体验，并支持深层链接和状态恢复等行为。
- [迁移到新的导览类型](migrating-to-new-navigation-types.md) — 用导览叠放和导览分栏视图替换导览视图，改进你 App 的导览行为。
- [NavigationSplitView](navigationsplitview.md) — 一个以两栏或三栏呈现视图的视图，其中前导栏中的选择控制后续栏中的呈现。
- [navigationSplitViewStyle(_:)](<view/navigationsplitviewstyle(__).md>) — 设置此视图内导览分栏视图的样式。
- [navigationSplitViewColumnWidth(_:)](<view/navigationsplitviewcolumnwidth(__).md>) — 为包含此视图的栏设置固定的首选宽度。
- [navigationSplitViewColumnWidth(min:ideal:max:)](<view/navigationsplitviewcolumnwidth(min_ideal_max_).md>) — 为包含此视图的栏设置灵活的首选宽度。
- [NavigationSplitViewVisibility](navigationsplitviewvisibility.md) — 导览分栏视图中前导栏的可见性。
- [NavigationLink](navigationlink.md) — 一个控制导览呈现的视图。

### 在单栏中叠放视图

- [NavigationStack](navigationstack.md) — 一个显示根视图并允许你在根视图之上呈现其他视图的视图。
- [NavigationPath](navigationpath.md) — 一个类型擦除的数据列表，表示导览叠放的内容。
- [navigationDestination(for:destination:)](<view/navigationdestination(for_destination_).md>) — 将目的地视图与所呈现的数据类型关联，以便在导览叠放中使用。
- [navigationDestination(isPresented:destination:)](<view/navigationdestination(ispresented_destination_).md>) — 将目的地视图与一个可用于把该视图压入 [NavigationStack](navigationstack.md) 的绑定关联。
- [navigationDestination(item:destination:)](<view/navigationdestination(item_destination_).md>) — 将目的地视图与一个被绑定的值关联，以便在导览叠放或导览分栏视图中使用

### 管理栏折叠

- [NavigationSplitViewColumn](navigationsplitviewcolumn.md) — 一个表示导览分栏视图中某一栏的视图。

### 为导览内容设置标题

- [navigationTitle(_:)](<view/navigationtitle(__).md>) — 使用本地化字符串资源为导览目的配置视图的标题。
- [navigationSubtitle(_:)](<view/navigationsubtitle(__).md>) — 使用本地化字符串资源为导览目的配置视图的副标题。
- [navigationDocument(_:)](<view/navigationdocument(__).md>) — 为导览目的配置视图的文稿。
- [navigationDocument(_:preview:)](<view/navigationdocument(__preview_).md>) — 为导览目的配置视图的文稿。

### 配置导航栏

- [navigationBarBackButtonHidden(_:)](<view/navigationbarbackbuttonhidden(__).md>) — 隐藏该视图的导航栏返回按钮。
- [navigationBarTitleDisplayMode(_:)](<view/navigationbartitledisplaymode(__).md>) — 为该视图配置标题显示模式。
- [NavigationBarItem](navigationbaritem.md) — 导航栏的一种配置，表示位于导览叠放顶部的视图。

### 配置边栏

- [sidebarRowSize](environmentvalues/sidebarrowsize.md) — 边栏行当前的尺寸。
- [SidebarRowSize](sidebarrowsize.md) — 边栏行的标准尺寸。

### 在标签页中呈现视图

- [用标签页导览增强 App 内容](enhancing-your-app-content-with-tab-navigation.md) — 使用标签页栏让 App 内容保持核心地位，同时提供快捷的导览访问。
- [TabView](tabview.md) — 一个使用交互式用户界面元素在多个子视图之间切换的视图。
- [Tab](tab.md) — 标签页视图中的标签页内容及其关联的标签页条目。
- [TabRole](tabrole.md) — 一个定义标签页用途的值。
- [TabSection](tabsection.md) — 一个可用于在标签页视图中添加层级结构的容器。
- [tabViewStyle(_:)](<view/tabviewstyle(__).md>) — 在当前环境中设置标签页视图的样式。

### 配置标签页栏

- [defaultAdaptableTabBarPlacement(_:)](<view/defaultadaptabletabbarplacement(__).md>) — 为使用可适配边栏样式的标签页视图中的标签页指定默认位置。
- [defaultTabBarPlacement(_:)](<view/defaulttabbarplacement(__).md>) — 在标签页栏无法在不同表示之间自适应、只能显示一种表示的平台上，为 [sidebarAdaptable](tabviewstyle/sidebaradaptable.md) 样式下 [TabView](tabview.md) 的标签页指定首选位置。 _(beta)_
- [tabViewSidebarHeader(content:)](<view/tabviewsidebarheader(content_).md>) — 向标签页视图的边栏添加自定义标头。
- [tabViewSidebarFooter(content:)](<view/tabviewsidebarfooter(content_).md>) — 向标签页视图的边栏添加自定义页脚。
- [tabViewSidebarBottomBar(content:)](<view/tabviewsidebarbottombar(content_).md>) — 向标签页视图的边栏添加自定义底栏。
- [AdaptableTabBarPlacement](adaptabletabbarplacement.md) — 使用可适配边栏样式的标签页视图中标签页的位置。
- [tabBarPlacement](environmentvalues/tabbarplacement.md) — 标签页栏当前的位置。
- [TabBarPlacement](tabbarplacement.md) — 标签页视图中标签页的位置。
- [isTabBarShowingSections](environmentvalues/istabbarshowingsections.md) — 一个布尔值，决定标签页视图是否显示某个标签页分区的展开内容。
- [tabBarMinimizeBehavior(_:)](<view/tabbarminimizebehavior(__).md>) — 设置标签页栏的最小化行为。
- [TabBarMinimizeBehavior](tabbarminimizebehavior.md)
- [TabViewBottomAccessoryPlacement](tabviewbottomaccessoryplacement.md) — 标签页视图中底部附件的位置。你可以用它根据位置调整附件视图的内容。

### 配置标签页

- [sectionActions(content:)](<view/sectionactions(content_).md>) — 向分区添加自定义操作。
- [TabPlacement](tabplacement.md) — 标签页可以出现的位置。
- [TabContentBuilder](tabcontentbuilder.md) — 一个结果构建器，为支持编程式选择的标签页视图构建标签页。此构建器要求标签页视图中的所有标签页具有相同的选择类型。
- [TabContent](tabcontent.md) — 一个为标签页视图中可编程选择的标签页提供内容的类型。
- [AnyTabContent](anytabcontent.md) — 类型擦除的标签页内容。

### 启用标签页自定

- [tabViewCustomization(_:)](<view/tabviewcustomization(__).md>) — 指定要应用到标签页视图边栏表示的自定项。
- [TabViewCustomization](tabviewcustomization.md) — 人们对可适配边栏标签页视图所做的自定。
- [TabCustomizationBehavior](tabcustomizationbehavior.md) — 可自定标签页视图内容的自定行为。

### 在多个窗格中显示视图

- [HSplitView](hsplitview.md) — 一个布局容器，将其子视图排列成一条水平线，并允许用户使用放置在它们之间的分隔符调整大小。
- [VSplitView](vsplitview.md) — 一个布局容器，将其子视图排列成一条垂直线，并允许用户使用放置在它们之间的分隔符调整大小。

### 已废弃类型

- [NavigationView](navigationview.md) — 一个用于呈现一组叠放视图的视图，这些视图表示导览层级结构中的可见路径。 _(已废弃)_
- [tabItem(_:)](<view/tabitem(__).md>) — 设置与此视图关联的标签页栏条目。 _(已废弃)_

## 另请参阅

### App 结构

- [App 组织](app-organization.md) — 定义 App 的入口点和顶层结构。
- [场景](scenes.md) — 声明构成 App 各部分的用户界面分组。
- [窗口](windows.md) — 在一个窗口或一组窗口中显示用户界面内容。
- [沉浸式空间](immersive-spaces.md) — 在用户的周围环境中显示无边界内容。
- [文稿](documents.md) — 让人们能够打开和管理文稿。
- [模态呈现方式](modal-presentations.md) — 在提供专注交互的独立视图中呈现内容。
- [工具栏](toolbars.md) — 提供对常用命令和控制的即时访问。
- [搜索](search.md) — 让人们能够在你的 App 中搜索文本或其他内容。
- [App 扩展](app-extensions.md) — 把你 App 的基础功能扩展到系统的其他部分，例如添加小组件。
