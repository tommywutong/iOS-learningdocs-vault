---
title: 布局修饰符
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-layout
source_url: 'https://developer.apple.com/documentation/swiftui/view-layout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-layout.json'
content_hash: 'sha256:e679cabe1b42139f'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md) · [View](view.md)

# 布局修饰符

<sub>API 集合</sub>

通过调整视图的大小、位置、对齐方式、内边距等，告诉视图如何在视图层级结构中排布自身。

## 概述

使用布局修饰符来微调视图在视图层级结构中的放置位置。你可以调整或约束视图的大小、位置和对齐方式。你还可以在视图周围添加内边距，并指示视图如何与系统定义的安全区交互。

要开始排布视图，请参阅[布局基础](layout-fundamentals.md)。要对基本布局进行调整，请参阅[布局调整](layout-adjustments.md)。

## 主题

### 尺寸

- [frame(width:height:alignment:)](<view/frame(width_height_alignment_).md>) — 将此视图放置在一个具有指定尺寸的不可见框架内。
- [frame(depth:alignment:)](<view/frame(depth_alignment_).md>) — 将此视图放置在一个具有指定深度的不可见框架内。
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](<view/frame(minwidth_idealwidth_maxwidth_minheight_idealheight_maxheight_alignment_).md>) — 将此视图放置在一个具有指定尺寸约束的不可见框架内。
- [frame(minDepth:idealDepth:maxDepth:alignment:)](<view/frame(mindepth_idealdepth_maxdepth_alignment_).md>) — 将此视图放置在一个具有指定深度约束的不可见框架内。
- [containerRelativeFrame(_:alignment:)](<view/containerrelativeframe(__alignment_).md>) — 将此视图放置在一个尺寸相对于最近容器的不可见框架内。
- [containerRelativeFrame(_:alignment:_:)](<view/containerrelativeframe(__alignment___).md>) — 将此视图放置在一个尺寸相对于最近容器的不可见框架内。
- [containerRelativeFrame(_:count:span:spacing:alignment:)](<view/containerrelativeframe(__count_span_spacing_alignment_).md>) — 将此视图放置在一个尺寸相对于最近容器的不可见框架内。
- [fixedSize()](<view/fixedsize().md>) — 将此视图固定在其理想尺寸上。
- [fixedSize(horizontal:vertical:)](<view/fixedsize(horizontal_vertical_).md>) — 在指定维度上将此视图固定在其理想尺寸上。
- [layoutPriority(_:)](<view/layoutpriority(__).md>) — 设置父布局向此子视图分配空间的优先级。
- [containerCornerOffset(_:sizeToFit:)](<view/containercorneroffset(__sizetofit_).md>) — 调整视图的布局，以避开指定边缘上容器视图的圆角内嵌。

### 位置

- [position(_:)](<view/position(__).md>) — 将此视图的中心放置在其父坐标空间中的指定点上。
- [position(x:y:)](<view/position(x_y_).md>) — 将此视图的中心放置在其父坐标空间中的指定坐标上。
- [offset(_:)](<view/offset(__).md>) — 按 offset 参数中指定的水平和垂直量偏移此视图。
- [offset(x:y:)](<view/offset(x_y_).md>) — 按指定的水平和垂直距离偏移此视图。
- [offset(z:)](<view/offset(z_).md>) — 将视图沿 Z 轴向前移动指定的距离（以点为单位）。
- [coordinateSpace(_:)](<view/coordinatespace(__).md>) — 为视图的坐标空间指定一个名称，使其他代码可以基于相对于该命名空间的点、尺寸等维度进行操作。

### 对齐

- [alignmentGuide(_:computeValue:)](<view/alignmentguide(__computevalue_).md>) — 设置视图的水平对齐。

### 内边距与间距

- [padding(_:)](<view/padding(__).md>) — 为此视图的每条边添加不同的内边距量。
- [padding(_:_:)](<view/padding(____).md>) — 为此视图的特定边添加相等的内边距量。
- [padding3D(_:)](<view/padding3d(__).md>) — 使用你指定的边缘内嵌填充此视图。
- [padding3D(_:_:)](<view/padding3d(____).md>) — 使用你指定的边缘内嵌填充此视图。
- [listRowInsets(_:)](<view/listrowinsets(__).md>) — 对列表中的行应用内嵌。
- [listRowInsets(_:_:)](<view/listrowinsets(____).md>) — 在指定边上设置列表中行的内嵌。
- [scenePadding(_:)](<view/scenepadding(__).md>) — 使用适合当前场景的量为该视图的指定边添加内边距。
- [scenePadding(_:edges:)](<view/scenepadding(__edges_).md>) — 使用适合当前场景的量为该视图的指定边添加指定类型的内边距。
- [listRowSpacing(_:)](<view/listrowspacing(__).md>) — 设置列表中两个相邻行之间的垂直间距。
- [listSectionSpacing(_:)](<view/listsectionspacing(__).md>) — 将 [List](list.md) 中相邻分区之间的间距设置为自定义值。
- [listSectionMargins(_:_:)](<view/listsectionmargins(____).md>) — 为特定边设置分区外边距。

### 网格配置

- [gridCellColumns(_:)](<view/gridcellcolumns(__).md>) — 告诉在网格中充当单元格的视图跨越指定的列数。
- [gridCellAnchor(_:)](<view/gridcellanchor(__).md>) — 为充当网格单元格的视图指定自定义对齐锚点。
- [gridCellUnsizedAxes(_:)](<view/gridcellunsizedaxes(__).md>) — 要求网格布局不要在指定轴向上为视图提供额外尺寸。
- [gridColumnAlignment(_:)](<view/gridcolumnalignment(__).md>) — 覆盖该视图所在的网格列的默认水平对齐。

### 安全区与外边距

- [ignoresSafeArea(_:edges:)](<view/ignoressafearea(__edges_).md>) — 扩展视图的安全区。
- [ignoresSafeArea(_:edges:alignment:)](<view/ignoressafearea(__edges_alignment_).md>) — 扩展视图的安全区，并使用提供的对齐方式在新边界内对齐内容。 _(beta)_
- [safeAreaInset(edge:alignment:spacing:content:)](<view/safeareainset(edge_alignment_spacing_content_).md>) — 在被修饰的视图旁边显示指定的内容。
- [safeAreaBar(edge:alignment:spacing:content:)](<view/safeareabar(edge_alignment_spacing_content_).md>) — 将指定的内容作为自定义栏显示在被修饰的视图旁边。
- [safeAreaPadding(_:)](<view/safeareapadding(__).md>) — 将提供的内嵌添加到此视图的安全区中。
- [safeAreaPadding(_:_:)](<view/safeareapadding(____).md>) — 将提供的内嵌添加到此视图的安全区中。
- [contentMargins(_:for:)](<view/contentmargins(__for_).md>) — 为提供的放置位置配置内容外边距。
- [contentMargins(_:_:for:)](<view/contentmargins(____for_).md>) — 为提供的放置位置配置内容外边距。

### 层叠顺序

- [zIndex(_:)](<view/zindex(__).md>) — 控制重叠视图的显示顺序。

### 布局方向

- [layoutDirectionBehavior(_:)](<view/layoutdirectionbehavior(__).md>) — 设置此视图在不同布局方向下的行为。

### 自定义布局特性

- [layoutValue(key:value:)](<view/layoutvalue(key_value_).md>) — 将一个值与自定义布局属性关联起来。
- [containerValue(_:_:)](<view/containervalue(____).md>) — 设置视图的某个特定容器值。

## 另请参阅

### 绘制视图

- [样式修饰符](view-style-modifiers.md) — 为不同类型的视图应用内置样式。
- [图形与渲染修饰符](view-graphics-and-rendering.md) — 影响系统绘制视图的方式，例如缩放或遮罩视图，或应用图形效果。
