---
title: 布局调整
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layout-adjustments
source_url: 'https://developer.apple.com/documentation/swiftui/layout-adjustments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layout-adjustments.json'
content_hash: 'sha256:07dbdf00deb161e8'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 布局调整

<sub>API 集合</sub>

对对齐、间距、内边距和其他布局参数进行精细调整。

## 概述

叠放和网格等布局容器为在 App 的用户界面中排列视图提供了很好的起点。当你需要进行精细调整时，使用布局视图修饰符。你可以调整或约束视图的大小、位置和对齐方式。你还可以在视图周围添加内边距，并指示视图如何与系统定义的安全区交互。

![](../../../attachments/44eb8b59b2583dbb9feab193d65420ee/layout-adjustments-hero@2x.png)

要开始使用基本布局，请参阅[布局基础](layout-fundamentals.md)。有关设计指引，请参阅《人机界面指南》中的[布局](../design/human-interface-guidelines/layout.md)。

## 主题

### 微调布局

- [布局一个简单的视图](laying-out-a-simple-view.md) — 通过调整视图的大小来创建视图布局。
- [检查视图布局](inspecting-view-layout.md) — 使用 Xcode 预览或添加临时边框来确定视图的位置和范围。

### 在视图周围添加内边距

- [padding(_:)](<view/padding(__).md>) — 为该视图的每条边添加不同的内边距量。
- [padding(_:_:)](<view/padding(____).md>) — 为该视图的特定边添加相等的内边距量。
- [padding3D(_:)](<view/padding3d(__).md>) — 使用你指定的边缘嵌入量为此视图添加内边距。
- [padding3D(_:_:)](<view/padding3d(____).md>) — 使用你指定的边缘嵌入量为此视图添加内边距。
- [scenePadding(_:)](<view/scenepadding(__).md>) — 使用适合当前场景的量为该视图的指定边添加内边距。
- [scenePadding(_:edges:)](<view/scenepadding(__edges_).md>) — 使用适合当前场景的量为该视图的指定边添加指定类型的内边距。
- [ScenePadding](scenepadding.md) — 用于将视图与其所在场景隔开的内边距。

### 影响视图的大小

- [frame(width:height:alignment:)](<view/frame(width_height_alignment_).md>) — 将此视图放置在一个具有指定大小的不可见 frame 内。
- [frame(depth:alignment:)](<view/frame(depth_alignment_).md>) — 将此视图放置在一个具有指定深度的不可见 frame 内。
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](<view/frame(minwidth_idealwidth_maxwidth_minheight_idealheight_maxheight_alignment_).md>) — 将此视图放置在一个具有指定大小约束的不可见 frame 内。
- [frame(minDepth:idealDepth:maxDepth:alignment:)](<view/frame(mindepth_idealdepth_maxdepth_alignment_).md>) — 将此视图放置在一个具有指定深度约束的不可见 frame 内。
- [containerRelativeFrame(_:alignment:)](<view/containerrelativeframe(__alignment_).md>) — 将此视图放置在一个大小相对于最近容器的不可见 frame 内。
- [containerRelativeFrame(_:alignment:_:)](<view/containerrelativeframe(__alignment___).md>) — 将此视图放置在一个大小相对于最近容器的不可见 frame 内。
- [containerRelativeFrame(_:count:span:spacing:alignment:)](<view/containerrelativeframe(__count_span_spacing_alignment_).md>) — 将此视图放置在一个大小相对于最近容器的不可见 frame 内。
- [fixedSize()](<view/fixedsize().md>) — 将此视图固定在其理想大小。
- [fixedSize(horizontal:vertical:)](<view/fixedsize(horizontal_vertical_).md>) — 在指定维度上将此视图固定在其理想大小。
- [layoutPriority(_:)](<view/layoutpriority(__).md>) — 设置父布局向此子视图分配空间时使用的优先级。

### 调整视图的位置

- [对视图的位置进行精细调整](making-fine-adjustments-to-a-view-s-position.md) — 通过应用 offset 或 position 修饰符来移动视图的位置。
- [position(_:)](<view/position(__).md>) — 将此视图的中心放置在其父坐标空间中的指定点上。
- [position(x:y:)](<view/position(x_y_).md>) — 将此视图的中心放置在其父坐标空间中的指定坐标上。
- [offset(_:)](<view/offset(__).md>) — 按 offset 参数中指定的水平和垂直量偏移此视图。
- [offset(x:y:)](<view/offset(x_y_).md>) — 按指定的水平和垂直距离偏移此视图。
- [offset(z:)](<view/offset(z_).md>) — 将视图沿 Z 轴向前移动指定的点数距离。

### 对齐视图

- [在叠放内对齐视图](aligning-views-within-a-stack.md) — 使用对齐参考线定位叠放内的视图。
- [跨叠放对齐视图](aligning-views-across-stacks.md) — 创建自定义对齐方式，并用它跨多个叠放对齐视图。
- [alignmentGuide(_:computeValue:)](<view/alignmentguide(__computevalue_).md>) — 设置视图的水平对齐。
- [Alignment](alignment.md) — 两个轴上的对齐。
- [HorizontalAlignment](horizontalalignment.md) — 沿水平轴的对齐位置。
- [VerticalAlignment](verticalalignment.md) — 沿垂直轴的对齐位置。
- [DepthAlignment](depthalignment.md) — 沿深度轴的对齐位置。
- [AlignmentID](alignmentid.md) — 一种用于创建自定义对齐参考线的类型。
- [ViewDimensions](viewdimensions.md) — 视图在其自身坐标空间中的大小和对齐参考线。
- [ViewDimensions3D](viewdimensions3d.md) — 视图在其自身坐标空间中的 3D 大小和对齐参考线。
- [SpatialContainer](spatialcontainer.md) — 一个在 3D 空间中对齐重叠内容的布局容器。

### 设置外边距

- [contentMargins(_:for:)](<view/contentmargins(__for_).md>) — 为给定的位置配置内容外边距。
- [contentMargins(_:_:for:)](<view/contentmargins(____for_).md>) — 为给定的位置配置内容外边距。
- [ContentMarginPlacement](contentmarginplacement.md) — 外边距的位置。

### 保持安全区内

- [ignoresSafeArea(_:edges:)](<view/ignoressafearea(__edges_).md>) — 扩展视图的安全区。
- [ignoresSafeArea(_:edges:alignment:)](<view/ignoressafearea(__edges_alignment_).md>) — 扩展视图的安全区，并使用提供的对齐方式在新边界内对齐内容。 _(beta)_
- [safeAreaInset(edge:alignment:spacing:content:)](<view/safeareainset(edge_alignment_spacing_content_).md>) — 在被修饰的视图旁边显示指定的内容。
- [safeAreaPadding(_:)](<view/safeareapadding(__).md>) — 将提供的嵌入量加入此视图的安全区。
- [safeAreaPadding(_:_:)](<view/safeareapadding(____).md>) — 将提供的嵌入量加入此视图的安全区。
- [SafeAreaRegions](safearearegions.md) — 一组符号化的安全区区域。

### 设置布局方向

- [layoutDirectionBehavior(_:)](<view/layoutdirectionbehavior(__).md>) — 设置此视图对不同布局方向的行为。
- [LayoutDirectionBehavior](layoutdirectionbehavior.md) — 对布局方向改变时应当发生什么的描述。
- [layoutDirection](environmentvalues/layoutdirection.md) — 与当前环境关联的布局方向。
- [LayoutDirection](layoutdirection.md) — SwiftUI 可以用来布局内容的方向。
- [LayoutRotationUnaryLayout](layoutrotationunarylayout.md)

### 响应界面特性

- [isLuminanceReduced](environmentvalues/isluminancereduced.md) — 一个布尔值，指示显示器或环境当前是否要求降低亮度。
- [displayScale](environmentvalues/displayscale.md) — 此环境的显示缩放比例。
- [pixelLength](environmentvalues/pixellength.md) — 屏幕上一个像素的大小。
- [horizontalSizeClass](environmentvalues/horizontalsizeclass.md) — 此环境的水平尺寸类别。
- [verticalSizeClass](environmentvalues/verticalsizeclass.md) — 此环境的垂直尺寸类别。
- [UserInterfaceSizeClass](userinterfacesizeclass.md) — 一组值，指示视图可用的视觉尺寸。

### 访问边缘、区域和布局

- [Edge](edge.md) — 一个枚举，用于指示矩形的某一条边。
- [Edge3D](edge3d.md) — 3D 体积的一条边或一个面。
- [HorizontalEdge](horizontaledge.md) — 水平轴上的一条边。
- [VerticalEdge](verticaledge.md) — 垂直轴上的一条边。
- [EdgeInsets](edgeinsets.md) — 矩形各边的嵌入距离。
- [EdgeInsets3D](edgeinsets3d.md) — 3D 体积各个面的嵌入距离。

## 另请参阅

### 视图布局

- [布局基础](layout-fundamentals.md) — 在叠放和网格等内置布局容器内排列视图。
- [自定义布局](custom-layout.md) — 以自定义安排放置视图，并在布局类型之间创建动画过渡。
- [列表](lists.md) — 显示一个结构化的、可滚动的信息列。
- [表格](tables.md) — 显示按行和列排列的可选择、可排序的数据。
- [视图分组](view-groupings.md) — 在不同类型的专用容器中呈现视图，例如表单或控制组。
- [滚动视图](scroll-views.md) — 让人们能够滚动查看不适合当前显示的内容。
