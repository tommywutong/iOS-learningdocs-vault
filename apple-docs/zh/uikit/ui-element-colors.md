---
title: UI 元素颜色
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/ui-element-colors
source_url: 'https://developer.apple.com/documentation/uikit/ui-element-colors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/ui-element-colors.json'
content_hash: 'sha256:6ec99ceea221266e'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Drawing](drawing.md) · [UIColor](uicolor.md)

# UI 元素颜色

<sub>API 集合</sub>

为标签、文本、背景和链接等 UI 元素选择颜色。

## 概述

UIKit 为你 App 的 UI 元素的前景色和背景色提供了颜色对象。这些颜色对象的名称反映的是其预期用途，而非具体的颜色值。

除非另有说明，当你使用提供的 [UIColor](uicolor.md) 对象时，这些颜色对象会自动适配深色模式的变化。如果你直接、或通过 [CGColor](../coregraphics/cgcolor.md) 等其他类型获取颜色值，则必须自行处理深色模式的变化。有关支持深色模式的更多信息，请参阅[在界面中支持深色模式](supporting-dark-mode-in-your-interface.md)。

## 主题

### 标签颜色

- [labelColor](uicolor/label.md) — 用于包含主要内容的文本标签的颜色。
- [secondaryLabelColor](uicolor/secondarylabel.md) — 用于包含次要内容的文本标签的颜色。
- [tertiaryLabelColor](uicolor/tertiarylabel.md) — 用于包含第三级内容的文本标签的颜色。
- [quaternaryLabelColor](uicolor/quaternarylabel.md) — 用于包含第四级内容的文本标签的颜色。

### 填充颜色

- [systemFillColor](uicolor/systemfill.md) — 用于细小形状的叠加填充颜色。
- [secondarySystemFillColor](uicolor/secondarysystemfill.md) — 用于中等尺寸形状的叠加填充颜色。
- [tertiarySystemFillColor](uicolor/tertiarysystemfill.md) — 用于大尺寸形状的叠加填充颜色。
- [quaternarySystemFillColor](uicolor/quaternarysystemfill.md) — 用于包含复杂内容的大面积区域的叠加填充颜色。

### 文本颜色

- [placeholderTextColor](uicolor/placeholdertext.md) — 用于控制或文本视图中占位符文本的颜色。

### 强调色

- [tintColor](uicolor/tintcolor.md) — 一个在运行时根据 App 或特性层级结构当前强调色进行解析的颜色值。

### 标准内容背景颜色

- [systemBackgroundColor](uicolor/systembackground.md) — 用于界面主背景的颜色。
- [secondarySystemBackgroundColor](uicolor/secondarysystembackground.md) — 用于叠放在主背景之上的内容的颜色。
- [tertiarySystemBackgroundColor](uicolor/tertiarysystembackground.md) — 用于叠放在次要背景之上的内容的颜色。

### 分组内容背景颜色

- [systemGroupedBackgroundColor](uicolor/systemgroupedbackground.md) — 用于分组界面主背景的颜色。
- [secondarySystemGroupedBackgroundColor](uicolor/secondarysystemgroupedbackground.md) — 用于叠放在分组界面主背景之上的内容的颜色。
- [tertiarySystemGroupedBackgroundColor](uicolor/tertiarysystemgroupedbackground.md) — 用于叠放在分组界面次要背景之上的内容的颜色。

### 分隔线颜色

- [separatorColor](uicolor/separator.md) — 用于细边框或分隔线的颜色，可让部分底层内容透出可见。
- [opaqueSeparatorColor](uicolor/opaqueseparator.md) — 用于边框或分隔线的颜色，会遮住任何底层内容。

### 链接颜色

- [linkColor](uicolor/link.md) — 为链接指定的颜色。

### 不可自适应的颜色

- [darkTextColor](uicolor/darktext.md) — 用于浅色背景上文本的不可自适应系统颜色。
- [lightTextColor](uicolor/lighttext.md) — 用于深色背景上文本的不可自适应系统颜色。

### 已废弃的颜色

- [groupTableViewBackgroundColor](uicolor/grouptableviewbackground.md) — 用于分组表格视图背景的系统颜色。 _(已废弃)_

## 另请参阅

### 获取现有颜色

- [Standard colors](standard-colors.md) — 为红色、蓝色、绿色、黑色、白色等特定色调定义标准颜色对象。
- [Color creation](color-creation.md) — 从素材目录加载颜色，或根据原始分量值创建颜色。
