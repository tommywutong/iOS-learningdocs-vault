---
title: 辅助功能修饰符
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-accessibility
source_url: 'https://developer.apple.com/documentation/swiftui/view-accessibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-accessibility.json'
content_hash: 'sha256:8815be0bb893af45'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md) · [View](view.md)

# 辅助功能修饰符

<sub>API 集合</sub>

让你的 SwiftUI App 对每个人都易于访问，包括残障人士。

## 概述

与所有 Apple UI 框架一样，SwiftUI 内置了辅助功能支持。该框架会自省常见元素（如导航视图、列表、文本栏、滑块、按钮等），并默认提供基本的辅助功能标签和值。你无需进行任何额外工作即可启用这些标准辅助功能。

SwiftUI 还提供了一些工具来帮助你增强 App 的辅助功能。例如，你可以使用 [accessibilityLabel(_:)](<view/accessibilitylabel(__).md>) 或 [accessibilityValue(_:)](<view/accessibilityvalue(__).md>) 视图修饰符，显式地为 UI 中的元素添加辅助功能标签。

要进一步了解如何为你的 App 添加辅助功能特性，请参阅[辅助功能基础](accessibility-fundamentals.md)。

## 主题

### 标签

- [accessibilityLabel(_:)](<view/accessibilitylabel(__).md>) — 向视图添加一个描述其内容的标签。
- [accessibilityLabel(_:isEnabled:)](<view/accessibilitylabel(__isenabled_).md>) — 向视图添加一个描述其内容的标签。
- [accessibilityLabel(content:)](<view/accessibilitylabel(content_).md>) — 向视图添加一个描述其内容的标签。
- [accessibilityInputLabels(_:)](<view/accessibilityinputlabels(__).md>) — 设置用户用来识别视图的备用输入标签。
- [accessibilityInputLabels(_:isEnabled:)](<view/accessibilityinputlabels(__isenabled_).md>) — 设置用户用来识别视图的备用输入标签。
- [accessibilityLabeledPair(role:id:in:)](<view/accessibilitylabeledpair(role_id_in_).md>) — 将表示标签的辅助功能元素与匹配内容的元素配对。

### 值

- [accessibilityValue(_:)](<view/accessibilityvalue(__).md>) — 添加视图所包含值的文字描述。
- [accessibilityValue(_:isEnabled:)](<view/accessibilityvalue(__isenabled_).md>) — 添加视图所包含值的文字描述。

### 提示

- [accessibilityHint(_:)](<view/accessibilityhint(__).md>) — 向用户传达执行视图操作后会发生什么。
- [accessibilityHint(_:isEnabled:)](<view/accessibilityhint(__isenabled_).md>) — 向用户传达执行视图操作后会发生什么。

### 操作

- [accessibilityAction(_:_:)](<view/accessibilityaction(____).md>) — 向视图添加一个辅助功能操作。操作允许辅助技术（例如旁白）通过调用该操作来与视图交互。
- [accessibilityActions(_:)](<view/accessibilityactions(__).md>) — 向视图添加多个辅助功能操作。
- [accessibilityActions(category:_:)](<view/accessibilityactions(category___).md>) — 向视图添加多个具有特定类别的辅助功能操作。操作允许辅助技术（例如旁白）通过调用该操作来与视图交互，并按其类别分组。当具有相同类别的多个操作修饰符应用于视图时，这些操作会被合并在一起。
- [accessibilityAction(named:_:)](<view/accessibilityaction(named___).md>) — 向视图添加一个辅助功能操作。操作允许辅助技术（例如旁白）通过调用该操作来与视图交互。
- [accessibilityAction(action:label:)](<view/accessibilityaction(action_label_).md>) — 向视图添加一个辅助功能操作。操作允许辅助技术（例如旁白）通过调用该操作来与视图交互。
- [accessibilityAction(intent:label:)](<view/accessibilityaction(intent_label_).md>) — 向视图添加一个以 `label` 内容为标签的辅助功能操作。操作允许辅助技术（例如旁白）通过调用该操作来与视图交互。执行该操作时，会调用 `intent`。
- [accessibilityAction(_:intent:)](<view/accessibilityaction(__intent_).md>) — 向视图添加一个表示 `actionKind` 的辅助功能操作。操作允许辅助技术（例如旁白）通过调用该操作来与视图交互。执行该操作时，会调用 `intent`。
- [accessibilityAction(named:intent:)](<view/accessibilityaction(named_intent_).md>) — 向视图添加一个标签为 `name` 的辅助功能操作。操作允许辅助技术（例如旁白）通过调用该操作来与视图交互。执行该操作时，会调用 `intent`。
- [accessibilityAdjustableAction(_:)](<view/accessibilityadjustableaction(__).md>) — 向视图添加一个辅助功能可调节操作。操作允许辅助技术（例如旁白）通过调用该操作来与视图交互。
- [accessibilityScrollAction(_:)](<view/accessibilityscrollaction(__).md>) — 向视图添加一个辅助功能滚动操作。操作允许辅助技术（例如旁白）通过调用该操作来与视图交互。
- [accessibilityScrollStatus(_:isEnabled:)](<view/accessibilityscrollstatus(__isenabled_).md>) — 更改用户滚动此视图内的滚动视图时辅助功能技术所提供的播报。

### 手势

- [accessibilityActivationPoint(_:)](<view/accessibilityactivationpoint(__).md>) — 元素的激活点是辅助技术用来启动手势的位置。
- [accessibilityActivationPoint(_:isEnabled:)](<view/accessibilityactivationpoint(__isenabled_).md>) — 元素的激活点是辅助技术用来启动手势的位置。
- [accessibilityDragPoint(_:description:)](<view/accessibilitydragpoint(__description_).md>) — 辅助技术应该用来开始拖拽交互的点。
- [accessibilityDragPoint(_:description:isEnabled:)](<view/accessibilitydragpoint(__description_isenabled_).md>) — 辅助技术应该用来开始拖拽交互的点。
- [accessibilityDropPoint(_:description:)](<view/accessibilitydroppoint(__description_).md>) — 辅助技术应该用来结束拖拽交互的点。
- [accessibilityDropPoint(_:description:isEnabled:)](<view/accessibilitydroppoint(__description_isenabled_).md>) — 辅助技术应该用来结束拖拽交互的点。
- [accessibilityDirectTouch(_:options:)](<view/accessibilitydirecttouch(__options_).md>) — 显式设置此辅助功能元素是否为直接触摸区域。直接触摸区域将触摸事件直接传递给 App，而不是通过辅助技术（例如旁白）处理。该修饰符接受一个可选的 `AccessibilityDirectTouchOptions` 选项集来自定义直接触摸区域的功能。
- [accessibilityZoomAction(_:)](<view/accessibilityzoomaction(__).md>) — 向视图添加一个辅助功能缩放操作。操作允许辅助技术（例如旁白）通过调用该操作来与视图交互。

### 元素

- [accessibilityElement(children:)](<view/accessibilityelement(children_).md>) — 创建一个新的辅助功能元素，或修改现有辅助功能元素的 [AccessibilityChildBehavior](accessibilitychildbehavior.md)。
- [accessibilityChildren(children:)](<view/accessibilitychildren(children_).md>) — 用一个或多个新的合成辅助功能元素替换现有辅助功能元素的子元素。
- [accessibilityHidden(_:)](<view/accessibilityhidden(__).md>) — 指定是否在系统辅助功能中隐藏此视图。
- [accessibilityHidden(_:isEnabled:)](<view/accessibilityhidden(__isenabled_).md>) — 指定是否在系统辅助功能中隐藏此视图。

### 自定义控制

- [accessibilityRepresentation(representation:)](<view/accessibilityrepresentation(representation_).md>) — 用新的辅助功能元素替换此视图的一个或多个辅助功能元素。
- [accessibilityRespondsToUserInteraction(_:)](<view/accessibilityrespondstouserinteraction(__).md>) — 显式设置此辅助功能元素是否响应用户交互，从而会被切换控制、语音控制或完整键盘访问等技术交互。
- [accessibilityRespondsToUserInteraction(_:isEnabled:)](<view/accessibilityrespondstouserinteraction(__isenabled_).md>) — 显式设置此辅助功能元素是否响应用户交互，从而会被切换控制、语音控制或完整键盘访问等技术交互。

### 自定义内容

- [accessibilityCustomContent(_:_:importance:)](<view/accessibilitycustomcontent(____importance_).md>) — 向视图添加额外的辅助功能信息。

### 使用转子

- [accessibilityRotor(_:entries:)](<view/accessibilityrotor(__entries_).md>) — 使用指定的用户可见标签创建一个辅助功能转子（rotor），并使用由内容闭包生成的条目。
- [accessibilityRotor(_:entries:entryID:entryLabel:)](<view/accessibilityrotor(__entries_entryid_entrylabel_).md>) — 使用指定的用户可见标签和条目创建一个辅助功能转子。
- [accessibilityRotor(_:entries:entryLabel:)](<view/accessibilityrotor(__entries_entrylabel_).md>) — 使用指定的用户可见标签和条目创建一个辅助功能转子。
- [accessibilityRotor(_:textRanges:)](<view/accessibilityrotor(__textranges_).md>) — 使用指定的用户可见标签以及为每个指定范围生成的条目创建一个辅助功能转子。该转子将附加到当前辅助功能元素上，并且每个条目将指向该元素的指定范围。

### 配置转子

- [accessibilityRotorEntry(id:in:)](<view/accessibilityrotorentry(id_in_).md>) — 定义一个显式标识符，将此视图的辅助功能元素与辅助功能转子中的一个条目关联起来。
- [accessibilityLinkedGroup(id:in:)](<view/accessibilitylinkedgroup(id_in_).md>) — 链接多个辅助功能元素，使用户能够快速从一个元素导航到另一个元素，即使这些元素在辅助功能层级结构中并不相邻。
- [accessibilitySortPriority(_:)](<view/accessibilitysortpriority(__).md>) — 设置此视图的辅助功能元素相对于同一层级其他元素的排序优先顺序。

### 焦点

- [accessibilityFocused(_:)](<view/accessibilityfocused(__).md>) — 通过将此视图的辅助功能元素的焦点状态绑定到给定的布尔状态值来修改此视图。
- [accessibilityFocused(_:equals:)](<view/accessibilityfocused(__equals_).md>) — 通过将此视图的辅助功能元素的焦点状态绑定到给定的状态值来修改此视图。
- [accessibilityDefaultFocus(_:_:)](<view/accessibilitydefaultfocus(____).md>) — 通过为给定的辅助功能焦点状态绑定赋值，定义一个评估默认辅助功能焦点的区域。

### 特性

- [accessibilityAddTraits(_:)](<view/accessibilityaddtraits(__).md>) — 向视图添加给定的特性。
- [accessibilityRemoveTraits(_:)](<view/accessibilityremovetraits(__).md>) — 从此视图移除给定的特性。

### 身份

- [accessibilityIdentifier(_:)](<view/accessibilityidentifier(__).md>) — 使用你指定的字符串来标识视图。
- [accessibilityIdentifier(_:isEnabled:)](<view/accessibilityidentifier(__isenabled_).md>) — 使用你指定的字符串来标识视图。

### 颜色反转

- [accessibilityIgnoresInvertColors(_:)](<view/accessibilityignoresinvertcolors(__).md>) — 设置此视图是否应忽略系统的智能反转设置。

### 内容描述

- [accessibilityTextContentType(_:)](<view/accessibilitytextcontenttype(__).md>) — 设置一个辅助功能文本内容类型。
- [accessibilityHeading(_:)](<view/accessibilityheading(__).md>) — 设置此标题的辅助功能级别。

### 旁白

- [speechAdjustedPitch(_:)](<view/speechadjustedpitch(__).md>) — 提高或降低朗读文本的音调。
- [speechAlwaysIncludesPunctuation(_:)](<view/speechalwaysincludespunctuation(__).md>) — 设置旁白是否应始终朗读文本视图中的所有标点符号。
- [speechAnnouncementsQueued(_:)](<view/speechannouncementsqueued(__).md>) — 控制是否将待播报的内容排在现有语音之后，而不是打断正在进行的语音。
- [speechSpellsOutCharacters(_:)](<view/speechspellsoutcharacters(__).md>) — 设置旁白是否应逐个字符地朗读文本视图的内容。

### 图表

- [accessibilityChartDescriptor(_:)](<view/accessibilitychartdescriptor(__).md>) — 向表示图表的视图添加一个描述符，使图表内容对所有用户都易于访问。

### 大内容

- [accessibilityShowsLargeContentViewer()](<view/accessibilityshowslargecontentviewer().md>) — 添加一个默认的大内容视图，供大内容查看器显示。
- [accessibilityShowsLargeContentViewer(_:)](<view/accessibilityshowslargecontentviewer(__).md>) — 添加一个自定义的大内容视图，供大内容查看器显示。

### 快捷操作

- [accessibilityQuickAction(style:content:)](<view/accessibilityquickaction(style_content_).md>) — 添加一个在激活时由系统显示的快捷操作。
- [accessibilityQuickAction(style:isActive:content:)](<view/accessibilityquickaction(style_isactive_content_).md>) — 添加一个在激活时由系统显示的快捷操作。

### 使用辅助访问

- [assistiveAccessNavigationIcon(_:)](<view/assistiveaccessnavigationicon(__).md>) — 为导览目的配置视图的图标。
- [assistiveAccessNavigationIcon(systemImage:)](<view/assistiveaccessnavigationicon(systemimage_).md>) — 为导览目的配置视图的图标。

## 另请参阅

### 配置视图元素

- [外观修饰符](view-appearance.md) — 配置视图的前景和背景样式、控制以及可见性。
- [文本和符号修饰符](view-text-and-symbols.md) — 管理视图中文本的渲染、选择和输入。
- [辅助视图修饰符](view-auxiliary-views.md) — 添加并配置支持视图，例如工具栏和上下文菜单。
- [图表视图修饰符](view-chart-view.md) — 配置你用 Swift Charts 声明的图表。
