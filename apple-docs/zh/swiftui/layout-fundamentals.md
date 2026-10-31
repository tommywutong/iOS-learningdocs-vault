---
title: 布局基础
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layout-fundamentals
source_url: 'https://developer.apple.com/documentation/swiftui/layout-fundamentals'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layout-fundamentals.json'
content_hash: 'sha256:d153b7837ff34187'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 布局基础

<sub>API 集合</sub>

在叠放和网格等内置布局容器内排列视图。

## 概述

使用布局容器来排列用户界面的元素。叠放和网格会响应内容或界面尺寸的变化，更新并调整它们所包含子视图的位置。你可以在其他布局容器内以任意深度嵌套布局容器，以实现复杂的布局效果。

![](../../../attachments/9fd862b8214f1de236f13a51187c257f/layout-fundamentals-hero@2x.png)

要微调用布局容器视图构建的布局的位置、对齐和其他元素，请参阅[布局调整](layout-adjustments.md)。要定义自定义布局容器，请参阅[自定义布局](custom-layout.md)。有关设计指引，请参阅《人机界面指南》中的[布局](../design/human-interface-guidelines/layout.md)。

## 主题

### 选择布局

- [为你的内容选择容器视图](picking-container-views-for-your-content.md) — 使用叠放、网格、列表和表单构建灵活的用户界面。

### 在一个维度中静态排列视图

- [用叠放视图构建布局](building-layouts-with-stack-views.md) — 用基础的容器视图组合出复杂的布局。
- [HStack](hstack.md) — 一个把子视图排成水平行的视图。
- [VStack](vstack.md) — 一个把子视图排成垂直列的视图。

### 在一个维度中动态排列视图

- [用惰性叠放视图为数据分组](grouping-data-with-lazy-stack-views.md) — 在惰性叠放视图内把内容划分为多个逻辑分区。
- [创建高性能的可滚动叠放](creating-performant-scrollable-stacks.md) — 使用滚动视图、叠放视图和惰性叠放高效显示大量重复视图。
- [LazyHStack](lazyhstack.md) — 一个把子视图排列在水平方向增长的行中的视图，仅在需要时才创建条目。
- [LazyVStack](lazyvstack.md) — 一个把子视图排列在垂直方向增长的列中的视图，仅在需要时才创建条目。
- [PinnedScrollableViews](pinnedscrollableviews.md) — 一组可以被固定到滚动视图边界的视图类型。

### 在两个维度中静态排列视图

- [Grid](grid.md) — 一个把其他视图排列成二维布局的容器视图。
- [GridRow](gridrow.md) — 二维网格容器中的一个水平行。
- [gridCellColumns(_:)](<view/gridcellcolumns(__).md>) — 告知充当网格单元格的视图横跨指定的列数。
- [gridCellAnchor(_:)](<view/gridcellanchor(__).md>) — 为充当网格单元格的视图指定自定义的对齐锚点。
- [gridCellUnsizedAxes(_:)](<view/gridcellunsizedaxes(__).md>) — 要求网格布局不要在指定轴上为该视图提供额外尺寸。
- [gridColumnAlignment(_:)](<view/gridcolumnalignment(__).md>) — 覆盖该视图所在网格列的默认水平对齐方式。

### 在两个维度中动态排列视图

- [LazyHGrid](lazyhgrid.md) — 一个把子视图排列在水平方向增长的网格中的容器视图，仅在需要时才创建条目。
- [LazyVGrid](lazyvgrid.md) — 一个把子视图排列在垂直方向增长的网格中的容器视图，仅在需要时才创建条目。
- [GridItem](griditem.md) — 对惰性网格中某一行或某一列的描述。

### 层叠视图

- [为视图添加背景](adding-a-background-to-your-view.md) — 在视图后面组合一个背景，并将其延伸到安全区嵌入量之外。
- [ZStack](zstack.md) — 一个覆盖其子视图并在两个轴上对齐它们的视图。
- [zIndex(_:)](<view/zindex(__).md>) — 控制重叠视图的显示顺序。
- [background(alignment:content:)](<view/background(alignment_content_).md>) — 将你指定的视图层叠在此视图后面。
- [background(_:ignoresSafeAreaEdges:)](<view/background(__ignoressafeareaedges_).md>) — 将视图的背景设置为某种样式。
- [background(ignoresSafeAreaEdges:)](<view/background(ignoressafeareaedges_).md>) — 将视图的背景设置为默认背景样式。
- [background(_:in:fillStyle:)](<view/background(__in_fillstyle_).md>) — 将视图的背景设置为一个用某种样式填充的可嵌入形状。
- [background(in:fillStyle:)](<view/background(in_fillstyle_).md>) — 将视图的背景设置为一个用默认背景样式填充的可嵌入形状。
- [overlay(alignment:content:)](<view/overlay(alignment_content_).md>) — 将你指定的视图层叠在此视图前面。
- [overlay(_:ignoresSafeAreaEdges:)](<view/overlay(__ignoressafeareaedges_).md>) — 将指定的样式层叠在此视图前面。
- [overlay(_:in:fillStyle:)](<view/overlay(__in_fillstyle_).md>) — 将你指定的形状层叠在此视图前面。
- [backgroundMaterial](environmentvalues/backgroundmaterial.md) — 当前视图下方的材质。
- [containerBackground(_:for:)](<view/containerbackground(__for_).md>) — 使用视图设置所包含容器的容器背景。
- [containerBackground(for:alignment:content:)](<view/containerbackground(for_alignment_content_).md>) — 使用视图设置所包含容器的容器背景。
- [ContainerBackgroundPlacement](containerbackgroundplacement.md) — 容器背景的位置。

### 自动选择合适的布局

- [ViewThatFits](viewthatfits.md) — 一个通过提供第一个适配的子视图来适应可用空间的视图。

### 分隔

- [Spacer](spacer.md) — 一个灵活的空白区域，沿其所在叠放布局的主轴扩展；如果不在叠放内，则在两个轴上扩展。
- [Divider](divider.md) — 一个可用于分隔其他内容的视觉元素。

## 另请参阅

### 视图布局

- [布局调整](layout-adjustments.md) — 对对齐、间距、内边距和其他布局参数进行精细调整。
- [自定义布局](custom-layout.md) — 以自定义安排放置视图，并在布局类型之间创建动画过渡。
- [列表](lists.md) — 显示一个结构化的、可滚动的信息列。
- [表格](tables.md) — 显示按行和列排列的可选择、可排序的数据。
- [视图分组](view-groupings.md) — 在不同类型的专用容器中呈现视图，例如表单或控制组。
- [滚动视图](scroll-views.md) — 让人们能够滚动查看不适合当前显示的内容。
