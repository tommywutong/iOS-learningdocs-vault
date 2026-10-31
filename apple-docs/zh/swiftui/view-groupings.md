---
title: 视图分组
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-groupings
source_url: 'https://developer.apple.com/documentation/swiftui/view-groupings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-groupings.json'
content_hash: 'sha256:a42654bc40880870'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 视图分组

<sub>API 集合</sub>

在不同类型的用途驱动容器（如表单或控制组）中呈现视图。

## 概述

你可以创建服务于不同用途的视图分组。

![](../../../attachments/53961e3c03e161d637bf0a08c342c9a4/view-groupings-hero@2x.png)

例如，[Group](group.md) 构造将指定的视图视为一个单元，而不施加任何额外的布局或外观特性。[Form](form.md) 则以适合收集用户输入的特定平台外观呈现一组元素。

有关设计指引，请参阅《人机界面指南》中的 [Layout](../design/human-interface-guidelines/layout.md)。

## 主题

### 将视图分组到容器中

- [Creating custom container views](creating-custom-container-views.md) — 访问各个子视图以组合灵活的容器视图。
- [Group](group.md) — 一种类型，将某个内容类型的多个实例——如视图、场景或命令——收集为单一单元。
- [GroupElementsOfContent](groupelementsofcontent.md) — 将给定视图的子视图变换为结果内容视图。
- [GroupSectionsOfContent](groupsectionsofcontent.md) — 将给定视图的分区变换为结果内容视图。

### 将视图组织成分区

- [Section](section.md) — 一种容器视图，可用于在某些视图内添加层级结构。
- [SectionCollection](sectioncollection.md) — 表示视图分区的一个不透明集合。
- [SectionConfiguration](sectionconfiguration.md) — 指定分区的内容。

### 迭代动态数据

- [ForEach](foreach.md) — 一种结构体，根据底层的已标识数据集合按需计算视图。
- [ForEachSectionCollection](foreachsectioncollection.md) — 一种集合，允许在 for each 循环中将视图视为其分区的集合。
- [ForEachSubviewCollection](foreachsubviewcollection.md) — 一种集合，允许在 for each 循环中将视图视为其子视图的集合。
- [DynamicViewContent](dynamicviewcontent.md) — 一种视图类型，根据底层数据集合生成视图。

### 访问容器的子视图

- [Subview](subview.md) — 表示另一视图的子视图的一个不透明值。
- [SubviewsCollection](subviewscollection.md) — 表示视图子视图的一个不透明集合。
- [SubviewsCollectionSlice](subviewscollectionslice.md) — SubviewsCollection 的一个切片。
- [containerValue(_:_:)](<view/containervalue(____).md>) — 设置视图的某个特定容器值。
- [ContainerValues](containervalues.md) — 与给定视图关联的容器值集合。
- [ContainerValueKey](containervaluekey.md) — 用于访问容器值的键。

### 将视图分组到方框中

- [GroupBox](groupbox.md) — 一种经过样式化的视图，带有可选标签，在视觉上将内容的逻辑分组汇集在一起。
- [groupBoxStyle(_:)](<view/groupboxstyle(__).md>) — 设置此视图内分组框的样式。

### 分组输入

- [Form](form.md) — 一种容器，用于对数据输入所用的控制进行分组，例如在设置或检查器中。
- [formStyle(_:)](<view/formstyle(__).md>) — 设置视图层级结构中表单的样式。
- [LabeledContent](labeledcontent.md) — 一种容器，用于将标签附加到带值的视图。
- [labeledContentStyle(_:)](<view/labeledcontentstyle(__).md>) — 为带标签内容设置样式。

### 呈现一组控制

- [ControlGroup](controlgroup.md) — 一种容器视图，以适合上下文的视觉方式显示语义上相关的控制
- [controlGroupStyle(_:)](<view/controlgroupstyle(__).md>) — 设置此视图内控制组的样式。

## 另请参阅

### 视图布局

- [Layout fundamentals](layout-fundamentals.md) — 在内置布局容器（如叠放和网格）内排列视图。
- [Layout adjustments](layout-adjustments.md) — 微调对齐、间距、内边距 (padding) 和其他布局参数。
- [Custom layout](custom-layout.md) — 以自定义安排放置视图，并在布局类型之间创建动画过渡。
- [Lists](lists.md) — 显示一个结构化的、可滚动的信息列。
- [Tables](tables.md) — 显示按行和列排列的可选择、可排序的数据。
- [Scroll views](scroll-views.md) — 让人们能够滚动查看不适合当前显示的内容。
