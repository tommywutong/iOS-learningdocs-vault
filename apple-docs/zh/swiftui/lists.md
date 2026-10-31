---
title: 列表
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/lists
source_url: 'https://developer.apple.com/documentation/swiftui/lists'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/lists.json'
content_hash: 'sha256:b5828ee8d4ec7cee'
translated: true
---

> 导航： [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# 列表

<sub>API 集合</sub>

显示一个结构化的、可滚动的信息纵栏。

## 概述

使用列表来显示一维的视图纵向集合。

![](../../../attachments/15c88d97bce9de9704854a5490b6aee5/lists-hero@2x.png)

列表是一种复杂的容器类型，当它大到超出当前显示屏时会自动提供滚动。构建列表的方式是为列表的各个行提供单独的视图，或者使用 [ForEach](foreach.md) 来枚举一组行。你还可以混合使用这两种策略，把任意数量的单独视图和 `ForEach` 构造融合在一起。

使用视图修饰符来配置列表及其行、页眉、分节和分隔线的外观与行为。例如，你可以为列表应用样式、为单个行添加轻扫手势，或让列表可以通过下拉手势刷新。你还可以使用与[滚动视图](scroll-views.md)关联的配置来控制列表的隐式滚动行为。

如需设计指导，参见《人机界面指南》中的[列表与表格](../design/human-interface-guidelines/lists-and-tables.md)。

## 主题

### 创建列表

- [在列表中显示数据](displaying-data-in-lists.md) — 以符合平台的外观将数据集合可视化。
- [List](list.md) — 一种以单列形式呈现数据行的容器，可选择提供选择一个或多个成员的能力。
- [listStyle(_:)](<view/liststyle(__).md>) — 设置此视图内列表的样式。

### 渐进式地披露信息

- [OutlineGroup](outlinegroup.md) — 一种结构体，根据树形结构、有标识的底层数据集合按需计算视图和披露组。
- [DisclosureGroup](disclosuregroup.md) — 一种根据显示控制的显示或隐藏其他内容视图的视图。
- [disclosureGroupStyle(_:)](<view/disclosuregroupstyle(__).md>) — 设置此视图内披露组的样式。

### 配置列表的布局

- [listRowInsets(_:)](<view/listrowinsets(__).md>) — 为列表中的行应用内边距。
- [listRowInsets(_:_:)](<view/listrowinsets(____).md>) — 在指定的边缘上设置列表中行的内边距。
- [defaultMinListRowHeight](environmentvalues/defaultminlistrowheight.md) — 列表中行的默认最小高度。
- [defaultMinListHeaderHeight](environmentvalues/defaultminlistheaderheight.md) — 列表中页眉的默认最小高度。
- [listRowSpacing(_:)](<view/listrowspacing(__).md>) — 设置 List 中两个相邻行之间的垂直间距。
- [listSectionSpacing(_:)](<view/listsectionspacing(__).md>) — 把 [List](list.md) 中相邻分节之间的间距设置为自定值。
- [ListSectionSpacing](listsectionspacing.md) — 列表中两个相邻分节之间的间距选项。
- [listSectionMargins(_:_:)](<view/listsectionmargins(____).md>) — 为特定边缘设置分节外边距。

### 配置行

- [listItemTint(_:)](<view/listitemtint(__).md>) — 为列表中的内容设置固定的着色颜色。
- [ListItemTint](listitemtint.md) — 一种可应用于列表内容的着色效果配置。

### 配置页眉

- [headerProminence(_:)](<view/headerprominence(__).md>) — 为此视图设置页眉的显著程度。
- [headerProminence](environmentvalues/headerprominence.md) — 应用于视图内分节页眉的显著程度。
- [Prominence](prominence.md) — 一种指示视图层级结构显著程度的类型。

### 配置分隔线

- [listRowSeparatorTint(_:edges:)](<view/listrowseparatortint(__edges_).md>) — 设置与某个行关联的着色颜色。
- [listSectionSeparatorTint(_:edges:)](<view/listsectionseparatortint(__edges_).md>) — 设置与某个分节关联的着色颜色。
- [listRowSeparator(_:edges:)](<view/listrowseparator(__edges_).md>) — 设置与此特定行关联的分隔线的显示模式。
- [listSectionSeparator(_:edges:)](<view/listsectionseparator(__edges_).md>) — 设置是否隐藏与列表分节关联的分隔线。

### 配置背景

- [listRowBackground(_:)](<view/listrowbackground(__).md>) — 在列表行项目的背后放置一个自定背景视图。
- [alternatingRowBackgrounds(_:)](<view/alternatingrowbackgrounds(__).md>) — 覆盖此视图中的列表和表格是否使用交替行背景。
- [AlternatingRowBackgroundBehavior](alternatingrowbackgroundbehavior.md) — 视图在交替行背景方面的样式设置。
- [backgroundProminence](environmentvalues/backgroundprominence.md) — 与此环境关联的视图下方背景的显著程度。
- [BackgroundProminence](backgroundprominence.md) — 其他视图下方背景的显著程度。

### 在列表项目上显示徽章

- [badge(_:)](<view/badge(__).md>) — 从本地化的字符串资源为视图生成徽章。
- [badgeProminence(_:)](<view/badgeprominence(__).md>) — 指定此视图创建的徽章的显著程度。
- [badgeProminence](environmentvalues/badgeprominence.md) — 应用于与此环境关联的徽章的显著程度。
- [BadgeProminence](badgeprominence.md) — 徽章的视觉显著程度。

### 配置交互

- [swipeActions(edge:allowsFullSwipe:content:)](<view/swipeactions(edge_allowsfullswipe_content_).md>) — 为列表中的行添加自定轻扫操作。
- [selectionDisabled(_:)](<view/selectiondisabled(__).md>) — 添加一个条件，控制用户能否选择此视图。
- [listRowHoverEffect(_:)](<view/listrowhovereffect(__).md>) — 请求包含此视图的列表行使用提供的悬停效果。
- [listRowHoverEffectDisabled(_:)](<view/listrowhovereffectdisabled(__).md>) — 请求包含此视图的列表行停用其悬停效果。

### 刷新列表内容

- [refreshable(action:)](<view/refreshable(action_).md>) — 添加一个异步处理程序，当用户发起请求（例如下拉刷新）时更新视图显示的数据。
- [refresh](environmentvalues/refresh.md) — 存储在视图环境中的刷新操作。
- [RefreshAction](refreshaction.md) — 发起刷新操作的一种操作。

### 编辑列表

- [moveDisabled(_:)](<view/movedisabled(__).md>) — 添加一个条件，控制视图的视图层级结构是否可移动。
- [deleteDisabled(_:)](<view/deletedisabled(__).md>) — 添加一个条件，控制视图的视图层级结构是否可删除。
- [editMode](environmentvalues/editmode.md) — 指示用户能否编辑与此环境关联的视图内容的标识。
- [EditMode](editmode.md) — 指示用户能否编辑视图内容的模式。
- [EditActions](editactions.md) — 视图可以向用户提供的、针对数据集合的一组编辑操作。
- [EditableCollectionContent](editablecollectioncontent.md) — 一种不透明的包装视图，为列表中的行添加编辑能力。
- [IndexedIdentifierCollection](indexedidentifiercollection.md) — 一种集合包装器，同时迭代集合的索引和标识符。

### 配置分节索引

- [listSectionIndexVisibility(_:)](<view/listsectionindexvisibility(__).md>) — 更改列表分节索引的可见性。
- [sectionIndexLabel(_:)](<view/sectionindexlabel(__).md>) — 设置在分节索引中用于指向此分节的标签，通常只有一个字符长。

## 另请参阅

### 视图布局

- [布局基础](layout-fundamentals.md) — 在叠放、网格等内置布局容器内安排视图。
- [布局调整](layout-adjustments.md) — 对对齐、间距、内边距和其他布局参数进行微调。
- [自定布局](custom-layout.md) — 以自定方式放置视图，并在布局类型之间创建动画过渡。
- [表格](tables.md) — 显示按行列排列的可选择、可排序数据。
- [视图分组](view-groupings.md) — 在不同类型的、以目标为导向的容器（例如表单或控制组）中呈现视图。
- [滚动视图](scroll-views.md) — 让人们能够滚动查看超出当前显示屏的内容。
