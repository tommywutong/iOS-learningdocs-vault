---
title: 图表视图修饰符
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-chart-view
source_url: 'https://developer.apple.com/documentation/swiftui/view-chart-view'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-chart-view.json'
content_hash: 'sha256:0e487fe8c76f7ece'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md) · [View](view.md)

# 图表视图修饰符

<sub>API 集合</sub>

配置你用 Swift Charts 声明的图表。

## 概述

使用这些修饰符来配置你添加到 SwiftUI App 中的 [Chart](../charts/chart.md) 视图。

## 主题

### 样式

- [chartBackground(alignment:content:)](<view/chartbackground(alignment_content_).md>) — 为包含图表的视图添加背景。
- [chartForegroundStyleScale(_:)](<view/chartforegroundstylescale(__).md>) — 为图表配置前景样式比例。
- [chartForegroundStyleScale(domain:range:type:)](<view/chartforegroundstylescale(domain_range_type_).md>) — 为图表配置前景样式比例。
- [chartForegroundStyleScale(domain:type:)](<view/chartforegroundstylescale(domain_type_).md>) — 为图表配置前景样式比例。
- [chartForegroundStyleScale(domain:mapping:)](<view/chartforegroundstylescale(domain_mapping_).md>) — 为图表配置前景样式比例。
- [chartForegroundStyleScale(mapping:)](<view/chartforegroundstylescale(mapping_).md>) — 为图表配置前景样式比例。
- [chartForegroundStyleScale(range:type:)](<view/chartforegroundstylescale(range_type_).md>) — 为图表配置前景样式比例。
- [chartForegroundStyleScale(type:)](<view/chartforegroundstylescale(type_).md>) — 为图表配置前景样式比例。
- [chartPlotStyle(content:)](<view/chartplotstyle(content_).md>) — 配置图表的绘图区。

### 3D 配置

- [chart3DCameraProjection(_:)](<view/chart3dcameraprojection(__).md>)
- [chart3DPose(_:)](<view/chart3dpose(__).md>) — 关联一个绑定，当 3D 图表的姿态因交互而改变时更新该绑定。
- [chart3DRenderingStyle(_:)](<view/chart3drenderingstyle(__).md>)

### 图例

- [chartLegend(_:)](<view/chartlegend(__).md>) — 为图表配置图例。
- [chartLegend(position:alignment:spacing:)](<view/chartlegend(position_alignment_spacing_).md>) — 为图表配置图例。
- [chartLegend(position:alignment:spacing:content:)](<view/chartlegend(position_alignment_spacing_content_).md>) — 为图表配置图例。

### 覆盖层

- [chartOverlay(alignment:content:)](<view/chartoverlay(alignment_content_).md>) — 为包含图表的视图添加覆盖层。

### 坐标轴

- [chartXAxis(_:)](<view/chartxaxis(__).md>) — 设置 x 轴的可见性。
- [chartXAxis(content:)](<view/chartxaxis(content_).md>) — 为视图中的图表配置 x 轴。
- [chartXAxisStyle(content:)](<view/chartxaxisstyle(content_).md>) — 配置图表的 x 轴内容。
- [chartYAxis(_:)](<view/chartyaxis(__).md>) — 设置 y 轴的可见性。
- [chartYAxis(content:)](<view/chartyaxis(content_).md>) — 为视图中的图表配置 y 轴。
- [chartYAxisStyle(content:)](<view/chartyaxisstyle(content_).md>) — 配置图表的 y 轴内容。
- [chartZAxis(_:)](<view/chartzaxis(__).md>) — 设置 z 轴的可见性。
- [chartZAxis(content:)](<view/chartzaxis(content_).md>) — 为视图中的 3D 图表配置 z 轴。

### 坐标轴标签

- [chartXAxisLabel(_:position:alignment:spacing:)](<view/chartxaxislabel(__position_alignment_spacing_).md>) — 为视图中的图表添加 x 轴标签。
- [chartXAxisLabel(position:alignment:spacing:content:)](<view/chartxaxislabel(position_alignment_spacing_content_).md>) — 为视图中的图表添加 x 轴标签。
- [chartYAxisLabel(_:position:alignment:spacing:)](<view/chartyaxislabel(__position_alignment_spacing_).md>) — 为视图中的图表添加 y 轴标签。
- [chartYAxisLabel(position:alignment:spacing:content:)](<view/chartyaxislabel(position_alignment_spacing_content_).md>) — 为视图中的图表添加 y 轴标签。
- [chartZAxisLabel(_:position:alignment:spacing:)](<view/chartzaxislabel(__position_alignment_spacing_).md>) — 为视图中的图表添加 z 轴标签。仅影响 3D 图表。

### 坐标轴比例

- [chartXScale(domain:range:type:)](<view/chartxscale(domain_range_type_).md>) — 为图表配置 x 轴比例。
- [chartXScale(domain:type:)](<view/chartxscale(domain_type_).md>) — 为图表配置 x 轴比例。
- [chartXScale(range:type:)](<view/chartxscale(range_type_).md>) — 为图表配置 x 轴比例。
- [chartXScale(type:)](<view/chartxscale(type_).md>) — 为图表配置 x 轴比例。
- [chartYScale(domain:range:type:)](<view/chartyscale(domain_range_type_).md>) — 为图表配置 y 轴比例。
- [chartYScale(domain:type:)](<view/chartyscale(domain_type_).md>) — 为图表配置 y 轴比例。
- [chartYScale(range:type:)](<view/chartyscale(range_type_).md>) — 为图表配置 y 轴比例。
- [chartYScale(type:)](<view/chartyscale(type_).md>) — 为图表配置 y 轴比例。
- [chartZScale(domain:range:type:)](<view/chartzscale(domain_range_type_).md>) — 为 3D 图表配置 z 轴比例。
- [chartZScale(domain:type:)](<view/chartzscale(domain_type_).md>) — 为 3D 图表配置 z 轴比例。
- [chartZScale(range:type:)](<view/chartzscale(range_type_).md>) — 为 3D 图表配置 z 轴比例。

### 符号比例

- [chartSymbolScale(_:)](<view/chartsymbolscale(__).md>) — 为图表配置符号比例。
- [chartSymbolScale(domain:)](<view/chartsymbolscale(domain_).md>) — 为图表配置符号样式比例。
- [chartSymbolScale(domain:range:)](<view/chartsymbolscale(domain_range_).md>) — 为图表配置符号样式比例。
- [chartSymbolScale(domain:mapping:)](<view/chartsymbolscale(domain_mapping_).md>) — 为图表配置符号比例。
- [chartSymbolScale(mapping:)](<view/chartsymbolscale(mapping_).md>) — 为图表配置符号比例。
- [chartSymbolScale(range:)](<view/chartsymbolscale(range_).md>) — 为图表配置符号样式比例。

### 符号大小比例

- [chartSymbolSizeScale(_:)](<view/chartsymbolsizescale(__).md>) — 为图表配置符号大小比例。
- [chartSymbolSizeScale(domain:range:type:)](<view/chartsymbolsizescale(domain_range_type_).md>) — 为图表配置符号大小比例。
- [chartSymbolSizeScale(domain:type:)](<view/chartsymbolsizescale(domain_type_).md>) — 为图表配置符号大小比例。
- [chartSymbolSizeScale(domain:mapping:)](<view/chartsymbolsizescale(domain_mapping_).md>) — 为图表配置符号大小比例。
- [chartSymbolSizeScale(mapping:)](<view/chartsymbolsizescale(mapping_).md>) — 为图表配置符号大小比例。
- [chartSymbolSizeScale(range:type:)](<view/chartsymbolsizescale(range_type_).md>) — 为图表配置符号大小比例。
- [chartSymbolSizeScale(type:)](<view/chartsymbolsizescale(type_).md>) — 为图表配置符号大小比例。

### 线条样式比例

- [chartLineStyleScale(_:)](<view/chartlinestylescale(__).md>) — 为图表配置线条样式比例。
- [chartLineStyleScale(domain:)](<view/chartlinestylescale(domain_).md>) — 为图表配置线条样式比例。
- [chartLineStyleScale(domain:range:)](<view/chartlinestylescale(domain_range_).md>) — 为图表配置线条样式比例。
- [chartLineStyleScale(range:)](<view/chartlinestylescale(range_).md>) — 为图表配置线条样式比例。
- [chartLineStyleScale(domain:mapping:)](<view/chartlinestylescale(domain_mapping_).md>) — 为图表配置线条样式比例。
- [chartLineStyleScale(mapping:)](<view/chartlinestylescale(mapping_).md>) — 为图表配置线条样式比例。

### 滚动

- [chartScrollPosition(initialX:)](<view/chartscrollposition(initialx_).md>) — 设置沿 x 轴的初始滚动位置。一旦用户滚动了滚动视图，提供给此修饰符的值将不再起作用。
- [chartScrollPosition(initialY:)](<view/chartscrollposition(initialy_).md>) — 设置沿 y 轴的初始滚动位置。一旦用户滚动了滚动视图，提供给此修饰符的值将不再起作用。
- [chartScrollPosition(x:)](<view/chartscrollposition(x_).md>) — 关联一个绑定，当图表沿 x 轴滚动时更新该绑定。
- [chartScrollPosition(y:)](<view/chartscrollposition(y_).md>) — 关联一个绑定，当图表沿 y 轴滚动时更新该绑定。
- [chartScrollTargetBehavior(_:)](<view/chartscrolltargetbehavior(__).md>) — 设置可滚动图表的滚动行为。
- [chartScrollableAxes(_:)](<view/chartscrollableaxes(__).md>) — 配置此视图中图表的可滚动行为。

### 选择

- [chartXSelection(range:)](<view/chartxselection(range_).md>)
- [chartXSelection(value:)](<view/chartxselection(value_).md>)
- [chartYSelection(range:)](<view/chartyselection(range_).md>)
- [chartYSelection(value:)](<view/chartyselection(value_).md>)
- [chartZSelection(range:)](<view/chartzselection(range_).md>)
- [chartZSelection(value:)](<view/chartzselection(value_).md>)
- [chartAngleSelection(value:)](<view/chartangleselection(value_).md>)

### 可见域

- [chartXVisibleDomain(length:)](<view/chartxvisibledomain(length_).md>) — 设置 X 维度中可见域的长度。
- [chartYVisibleDomain(length:)](<view/chartyvisibledomain(length_).md>) — 设置 Y 维度中可见域的长度。

### 交互

- [chartGesture(_:)](<view/chartgesture(__).md>)

## 另请参阅

### 配置视图元素

- [辅助功能修饰符](view-accessibility.md) — 让你的 SwiftUI App 对每个人（包括残障人士）都具备辅助功能。
- [外观修饰符](view-appearance.md) — 配置视图的前景和背景样式、控制以及可见性。
- [文本与符号修饰符](view-text-and-symbols.md) — 管理视图中文本的渲染、选择和输入。
- [辅助视图修饰符](view-auxiliary-views.md) — 添加并配置工具栏和上下文菜单等辅助视图。
