---
title: 表格
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tables
source_url: 'https://developer.apple.com/documentation/swiftui/tables'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tables.json'
content_hash: 'sha256:4f3e6c98adc77f8e'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 表格

<sub>API 集合</sub>

显示按行和列排列、可选择且可排序的数据。

## 概述

使用表格在元素集合上显示多个值。集合中的每个元素显示在表格的不同行中，而给定元素的每个值显示在不同的列中。狭窄的显示可能会自适应为只显示表格的第一列。

![](../../../attachments/a784f68f4e1b73d07143c7d57ae3f586/tables-hero@2x.png)

创建表格时，你需要提供一个元素集合，然后告诉表格如何为每一列找到所需的值。在简单的情况下，SwiftUI 会为每一行推断元素，但在更复杂的场景中你也可以显式指定行元素。只需少量额外配置，你还可以让表格中的项目可选择、列可排序。

与 [List](list.md) 一样，表格包含隐式的垂直滚动，你可以使用[滚动视图](scroll-views.md)中描述的视图修饰符来配置它。有关设计指引，请参阅《人机界面指南》中的 [Lists and tables](../design/human-interface-guidelines/lists-and-tables.md)。

## 主题

### 创建表格

- [Building a great Mac app with SwiftUI](building-a-great-mac-app-with-swiftui.md) — 通过引入边栏、表格、工具栏和其他几种常用的用户界面元素，创建引人入胜的 SwiftUI Mac App。
- [Table](table.md) — 一种容器，呈现按一列或多列排列的数据行，并可选择提供选定一个或多个成员的能力。
- [tableStyle(_:)](<view/tablestyle(__).md>) — 设置此视图内表格的样式。

### 创建列

- [TableColumn](tablecolumn.md) — 为表格中的每一行显示一个视图的列。
- [TableColumnContent](tablecolumncontent.md) — 用于表示表格中列的一种类型。
- [TableColumnAlignment](tablecolumnalignment.md) — 描述表格列内容的对齐方式。
- [TableColumnBuilder](tablecolumnbuilder.md) — 一种结果构建器，从闭包创建表格列内容。
- [TableColumnForEach](tablecolumnforeach.md) — 一种结构体，根据底层的已标识数据集合按需计算列。

### 自定列

- [tableColumnHeaders(_:)](<view/tablecolumnheaders(__).md>) — 控制 `Table` 的列标头视图的可见性。
- [TableColumnCustomization](tablecolumncustomization.md) — 表格中列的状态的一种表示。
- [TableColumnCustomizationBehavior](tablecolumncustomizationbehavior.md) — 表格可向用户提供的一组列自定行为。

### 创建行

- [TableRow](tablerow.md) — 在表格中表示一个数据值的行。
- [TableRowContent](tablerowcontent.md) — 用于表示表格行的一种类型。
- [TableHeaderRowContent](tableheaderrowcontent.md) — 一种表格行，显示单个视图而不是分列内容。
- [TupleTableRowContent](tupletablerowcontent.md) — 一种表格列内容类型，从 Swift 表格行元组创建表格行。
- [TableForEachContent](tableforeachcontent.md) — 一种表格行内容类型，通过迭代集合创建表格行。
- [EmptyTableRowContent](emptytablerowcontent.md) — 不产生任何行的表格行内容。
- [DynamicTableRowContent](dynamictablerowcontent.md) — 一种表格行内容类型，根据底层数据集合生成表格行。
- [TableRowBuilder](tablerowbuilder.md) — 一种结果构建器，从闭包创建表格行内容。

### 添加渐进式展开

- [DisclosureTableRow](disclosuretablerow.md) — 一种表格行，根据显示控制的状态显示或隐藏额外的行。
- [TableOutlineGroupContent](tableoutlinegroupcontent.md) — 由表格的层级初始化方法创建的一个不透明表格行类型。

## 另请参阅

### 视图布局

- [Layout fundamentals](layout-fundamentals.md) — 在内置布局容器（如叠放和网格）内排列视图。
- [Layout adjustments](layout-adjustments.md) — 微调对齐、间距、内边距 (padding) 和其他布局参数。
- [Custom layout](custom-layout.md) — 以自定义安排放置视图，并在布局类型之间创建动画过渡。
- [Lists](lists.md) — 显示一个结构化的、可滚动的信息列。
- [View groupings](view-groupings.md) — 在不同类型的专用容器中呈现视图，例如表单或控制组。
- [Scroll views](scroll-views.md) — 让人们能够滚动查看不适合当前显示的内容。
