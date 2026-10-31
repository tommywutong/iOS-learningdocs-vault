---
title: 样式修饰符
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-style-modifiers
source_url: 'https://developer.apple.com/documentation/swiftui/view-style-modifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-style-modifiers.json'
content_hash: 'sha256:9d72df49f3e7ec40'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md) · [View](view.md)

# 样式修饰符

<sub>API 集合</sub>

为不同类型的视图应用内置样式。

## 概述

SwiftUI 为某些类型的视图定义了内置样式，并会针对特定的呈现上下文选择合适的样式。例如，[Label](label.md) 可能显示为图标、字符串标题，或两者兼有，具体取决于平台、视图是否出现在工具栏中等因素。

你可以使用某个样式修饰符来覆盖自动选择的样式。这些修饰符通常会在容器视图中传播，因此你可以将整个视图层级结构包裹在样式修饰符中，从而影响该层级结构内所有给定类型的视图。某些视图类型还允许你创建自定样式，同样使用样式修饰符来应用。

有关设置视图样式的更多信息，请参阅[视图样式](view-styles.md)。

## 主题

### Liquid Glass

- [glassEffect(_:in:)](<view/glasseffect(__in_).md>) — 将 Liquid Glass 效果应用到视图。
- [glassEffectID(_:in:)](<view/glasseffectid(__in_).md>) — 将一个身份值与此视图中定义的 Liquid Glass 效果关联。
- [glassEffectTransition(_:)](<view/glasseffecttransition(__).md>) — 将玻璃效果过渡与此视图中定义的任何玻璃效果关联。
- [glassEffectUnion(id:namespace:)](<view/glasseffectunion(id_namespace_).md>) — 将此视图中定义的任何 Liquid Glass 效果与提供的标识符关联为一个并集。

### 控制

- [buttonStyle(_:)](<view/buttonstyle(__).md>) — 将此视图内按钮的样式设置为具有自定义外观和标准交互行为的按钮样式。
- [buttonSizing(_:)](<view/buttonsizing(__).md>) — 视图层级结构中按钮的首选尺寸调整行为。
- [datePickerStyle(_:)](<view/datepickerstyle(__).md>) — 设置此视图内日期选择器的样式。
- [menuStyle(_:)](<view/menustyle(__).md>) — 设置此视图内菜单的样式。
- [pickerStyle(_:)](<view/pickerstyle(__).md>) — 设置此视图内选择器的样式。
- [toggleStyle(_:)](<view/togglestyle(__).md>) — 设置视图层级结构中切换控件的样式。

### 指示符

- [gaugeStyle(_:)](<view/gaugestyle(__).md>) — 设置此视图内仪表的样式。
- [progressViewStyle(_:)](<view/progressviewstyle(__).md>) — 设置此视图内进度视图的样式。

### 文本

- [labelStyle(_:)](<view/labelstyle(__).md>) — 设置此视图内标签的样式。
- [labeledContentStyle(_:)](<view/labeledcontentstyle(__).md>) — 为带标签内容设置样式。
- [textFieldStyle(_:)](<view/textfieldstyle(__).md>) — 设置此视图内文本栏的样式。
- [textEditorStyle(_:)](<view/texteditorstyle(__).md>) — 设置此视图内文本编辑器的样式。

### 集合

- [listStyle(_:)](<view/liststyle(__).md>) — 设置此视图内列表的样式。
- [tableStyle(_:)](<view/tablestyle(__).md>) — 设置此视图内表格的样式。
- [disclosureGroupStyle(_:)](<view/disclosuregroupstyle(__).md>) — 设置此视图内披露组的样式。

### 呈现

- [navigationSplitViewStyle(_:)](<view/navigationsplitviewstyle(__).md>) — 设置此视图内导览分栏视图的样式。
- [tabViewStyle(_:)](<view/tabviewstyle(__).md>) — 在当前环境中设置标签页视图的样式。
- [presentedWindowStyle(_:)](<view/presentedwindowstyle(__).md>) — 为通过与此视图交互而创建的窗口设置样式。
- [presentedWindowToolbarStyle(_:)](<view/presentedwindowtoolbarstyle(__).md>) — 为通过与此视图交互而创建的窗口中的工具栏设置样式。

### 分组

- [controlGroupStyle(_:)](<view/controlgroupstyle(__).md>) — 设置此视图内控制组的样式。
- [formStyle(_:)](<view/formstyle(__).md>) — 设置视图层级结构中表单的样式。
- [groupBoxStyle(_:)](<view/groupboxstyle(__).md>) — 设置此视图内分组框的样式。
- [indexViewStyle(_:)](<view/indexviewstyle(__).md>) — 在当前环境中设置索引视图的样式。

## 另请参阅

### 绘图视图

- [Layout modifiers](view-layout.md) — 通过调整视图的大小、位置、对齐方式、内边距等，告知视图如何在视图层级结构中安排自身。
- [Graphics and rendering modifiers](view-graphics-and-rendering.md) — 影响系统绘制视图的方式，例如缩放或遮罩视图，或应用图形效果。
