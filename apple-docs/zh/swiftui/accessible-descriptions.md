---
title: 辅助功能描述
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessible-descriptions
source_url: 'https://developer.apple.com/documentation/swiftui/accessible-descriptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessible-descriptions.json'
content_hash: 'sha256:92285d2b49aa63ac'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 辅助功能描述

<sub>API 集合</sub>

描述界面元素，帮助人们理解它们所代表的内容。

## 概述

SwiftUI 通常可以推断出关于你用户界面元素的一些信息，但你可以使用辅助功能修饰符，为有需要的用户提供更多信息。

![](../../../attachments/f52d60c9e7c4a20b6bbd457a3d013a84/accessible-descriptions-hero@2x.png)

有关设计指引，请参阅《人机界面指南》辅助功能部分中的[辅助功能](../design/human-interface-guidelines/accessibility.md#Content-descriptions)。

## 主题

### 应用标签

- [accessibilityLabel(_:)](<view/accessibilitylabel(__).md>) — 向视图添加一个描述其内容的标签。
- [accessibilityLabel(_:isEnabled:)](<view/accessibilitylabel(__isenabled_).md>) — 向视图添加一个描述其内容的标签。
- [accessibilityLabel(content:)](<view/accessibilitylabel(content_).md>) — 向视图添加一个描述其内容的标签。
- [accessibilityInputLabels(_:)](<view/accessibilityinputlabels(__).md>) — 设置用户用来识别视图的备用输入标签。
- [accessibilityInputLabels(_:isEnabled:)](<view/accessibilityinputlabels(__isenabled_).md>) — 设置用户用来识别视图的备用输入标签。
- [accessibilityLabeledPair(role:id:in:)](<view/accessibilitylabeledpair(role_id_in_).md>) — 将表示标签的辅助功能元素与对应内容的元素配对。
- [AccessibilityLabeledPairRole](accessibilitylabeledpairrole.md) — 标签/内容对中辅助功能元素的角色。

### 描述值

- [accessibilityValue(_:)](<view/accessibilityvalue(__).md>) — 添加视图所包含值的文本描述。
- [accessibilityValue(_:isEnabled:)](<view/accessibilityvalue(__isenabled_).md>) — 添加视图所包含值的文本描述。

### 描述内容

- [accessibilityTextContentType(_:)](<view/accessibilitytextcontenttype(__).md>) — 设置一个辅助功能文本内容类型。
- [accessibilityHeading(_:)](<view/accessibilityheading(__).md>) — 设置此标题的辅助功能级别。
- [AccessibilityHeadingLevel](accessibilityheadinglevel.md) — 一个标题相对于其他标题的层级。
- [AccessibilityTextContentType](accessibilitytextcontenttype.md) — 辅助技术可用来改善语音朗读文本呈现效果的文本上下文。

### 描述图表

- [accessibilityChartDescriptor(_:)](<view/accessibilitychartdescriptor(__).md>) — 向表示图表的视图添加一个描述符，使图表的内容对所有用户具备辅助功能。
- [AXChartDescriptorRepresentable](axchartdescriptorrepresentable.md) — 一个用于生成 `AXChartDescriptor` 对象的类型，你用它来为旁白（VoiceOver）或其他辅助技术中的辅助功能体验提供关于图表及其数据的信息。

### 添加自定义描述

- [accessibilityCustomContent(_:_:importance:)](<view/accessibilitycustomcontent(____importance_).md>) — 向视图添加额外的辅助功能信息。
- [AccessibilityCustomContentKey](accessibilitycustomcontentkey.md) — 一个键，用于指定与额外辅助功能信息条目关联的标识符和标签。

### 为内容指定特性

- [accessibilityAddTraits(_:)](<view/accessibilityaddtraits(__).md>) — 向视图添加给定的特性。
- [accessibilityRemoveTraits(_:)](<view/accessibilityremovetraits(__).md>) — 从此视图移除给定的特性。
- [AccessibilityTraits](accessibilitytraits.md) — 一组描述元素行为方式的辅助功能特性。

### 提供提示

- [accessibilityHint(_:)](<view/accessibilityhint(__).md>) — 告知用户执行视图的操作后会发生什么。
- [accessibilityHint(_:isEnabled:)](<view/accessibilityhint(__isenabled_).md>) — 告知用户执行视图的操作后会发生什么。

### 配置旁白

- [speechAdjustedPitch(_:)](<view/speechadjustedpitch(__).md>) — 提高或降低朗读文本的音高。
- [speechAlwaysIncludesPunctuation(_:)](<view/speechalwaysincludespunctuation(__).md>) — 设置旁白是否应始终朗读文本视图中的所有标点。
- [speechAnnouncementsQueued(_:)](<view/speechannouncementsqueued(__).md>) — 控制是否把待播报的公告排在现有语音之后，而不是打断正在进行的语音。
- [speechSpellsOutCharacters(_:)](<view/speechspellsoutcharacters(__).md>) — 设置旁白是否应逐字符朗读文本视图的内容。

## 另请参阅

### 辅助功能

- [辅助功能基础](accessibility-fundamentals.md) — 让你的 SwiftUI App 对每个人（包括残障人士）都具备辅助功能。
- [辅助功能外观](accessible-appearance.md) — 增强你 App 界面中内容的易读性。
- [辅助功能控制](accessible-controls.md) — 改进对你 App 可执行操作的访问。
- [辅助功能导览](accessible-navigation.md) — 让用户能够使用转子（rotor）导览到特定的用户界面元素。
