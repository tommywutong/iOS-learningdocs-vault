---
title: 辅助功能控制
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessible-controls
source_url: 'https://developer.apple.com/documentation/swiftui/accessible-controls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessible-controls.json'
content_hash: 'sha256:0cb89f7df23b6b91'
translated: true
---

> 导航： [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# 辅助功能控制

<sub>API 集合</sub>

改善对 App 可执行操作的访问。

## 概述

帮助使用辅助技术的人们访问你 App 中的控制。

![](../../../attachments/206dea16b7574c6f5be707477407cfd3/accessible-controls-hero@2x.png)

如需设计指导，参见《人机界面指南》无障碍部分中的[无障碍](../design/human-interface-guidelines/accessibility.md#Buttons-and-controls)。

## 主题

### 为视图添加操作

- [accessibilityAction(_:_:)](<view/accessibilityaction(____).md>) — 为视图添加一个辅助功能操作。操作允许旁白（VoiceOver）等辅助技术通过调用该操作来与视图交互。
- [accessibilityActions(_:)](<view/accessibilityactions(__).md>) — 为视图添加多个辅助功能操作。
- [accessibilityAction(named:_:)](<view/accessibilityaction(named___).md>) — 为视图添加一个辅助功能操作。操作允许旁白（VoiceOver）等辅助技术通过调用该操作来与视图交互。
- [accessibilityAction(action:label:)](<view/accessibilityaction(action_label_).md>) — 为视图添加一个辅助功能操作。操作允许旁白（VoiceOver）等辅助技术通过调用该操作来与视图交互。
- [accessibilityAction(intent:label:)](<view/accessibilityaction(intent_label_).md>) — 为视图添加一个以 `label` 内容作为标签的辅助功能操作。操作允许旁白（VoiceOver）等辅助技术通过调用该操作来与视图交互。当操作被执行时，会调用该 `intent`。
- [accessibilityAction(_:intent:)](<view/accessibilityaction(__intent_).md>) — 为视图添加一个表示 `actionKind` 的辅助功能操作。操作允许旁白（VoiceOver）等辅助技术通过调用该操作来与视图交互。当操作被执行时，会调用该 `intent`。
- [accessibilityAction(named:intent:)](<view/accessibilityaction(named_intent_).md>) — 为视图添加一个标签为 `name` 的辅助功能操作。操作允许旁白（VoiceOver）等辅助技术通过调用该操作来与视图交互。当操作被执行时，会调用该 `intent`。
- [accessibilityAdjustableAction(_:)](<view/accessibilityadjustableaction(__).md>) — 为视图添加一个辅助功能可调节操作。操作允许旁白（VoiceOver）等辅助技术通过调用该操作来与视图交互。
- [accessibilityScrollAction(_:)](<view/accessibilityscrollaction(__).md>) — 为视图添加一个辅助功能滚动操作。操作允许旁白（VoiceOver）等辅助技术通过调用该操作来与视图交互。
- [accessibilityActions(category:_:)](<view/accessibilityactions(category___).md>) — 以特定类别为视图添加多个辅助功能操作。操作允许旁白（VoiceOver）等辅助技术通过调用该操作来与视图交互，并按其类别分组。当多个具有相同类别的操作修饰符应用于视图时，这些操作会被合并在一起。
- [AccessibilityActionKind](accessibilityactionkind.md) — 定义可用辅助功能操作种类的结构体。
- [AccessibilityAdjustmentDirection](accessibilityadjustmentdirection.md) — 进行辅助功能调整时使用的方向指示。
- [AccessibilityActionCategory](accessibilityactioncategory.md) — 指定一个由系统提供并命名的辅助功能操作类别。

### 向人们提供快速操作

- [accessibilityQuickAction(style:content:)](<view/accessibilityquickaction(style_content_).md>) — 添加一个在活跃时由系统显示的快速操作。
- [accessibilityQuickAction(style:isActive:content:)](<view/accessibilityquickaction(style_isactive_content_).md>) — 添加一个在活跃时由系统显示的快速操作。
- [AccessibilityQuickActionStyle](accessibilityquickactionstyle.md) — 一种描述辅助功能快速操作呈现方式的类型。

### 让手势可访问

- [accessibilityActivationPoint(_:)](<view/accessibilityactivationpoint(__).md>) — 元素的激活点是辅助技术用来发起手势的位置。
- [accessibilityActivationPoint(_:isEnabled:)](<view/accessibilityactivationpoint(__isenabled_).md>) — 元素的激活点是辅助技术用来发起手势的位置。
- [accessibilityDragPoint(_:description:)](<view/accessibilitydragpoint(__description_).md>) — 辅助技术用来开始拖拽交互的点。
- [accessibilityDragPoint(_:description:isEnabled:)](<view/accessibilitydragpoint(__description_isenabled_).md>) — 辅助技术用来开始拖拽交互的点。
- [accessibilityDropPoint(_:description:)](<view/accessibilitydroppoint(__description_).md>) — 辅助技术用来结束拖拽交互的点。
- [accessibilityDropPoint(_:description:isEnabled:)](<view/accessibilitydroppoint(__description_isenabled_).md>) — 辅助技术用来结束拖拽交互的点。
- [accessibilityDirectTouch(_:options:)](<view/accessibilitydirecttouch(__options_).md>) — 显式设置此辅助功能元素是否为直接触控区域。直接触控区域会把触控事件直接传递给 App，而不是通过旁白（VoiceOver）等辅助技术来处理。该修饰符接受一个可选的 `AccessibilityDirectTouchOptions` 选项集合来自定直接触控区域的功能。
- [accessibilityZoomAction(_:)](<view/accessibilityzoomaction(__).md>) — 为视图添加一个辅助功能缩放操作。操作允许旁白（VoiceOver）等辅助技术通过调用该操作来与视图交互。
- [AccessibilityDirectTouchOptions](accessibilitydirecttouchoptions.md) — 一个选项集合，定义视图直接触控区域的功能。
- [AccessibilityZoomGestureAction](accessibilityzoomgestureaction.md) — 人们使用旁白（VoiceOver）等辅助技术执行缩放手势时的位置和方向信息。

### 控制焦点

- [accessibilityFocused(_:)](<view/accessibilityfocused(__).md>) — 通过把此视图的辅助功能元素的焦点状态绑定到给定的布尔状态值来修改此视图。
- [accessibilityFocused(_:equals:)](<view/accessibilityfocused(__equals_).md>) — 通过把此视图的辅助功能元素的焦点状态绑定到给定的状态值来修改此视图。
- [AccessibilityFocusState](accessibilityfocusstate.md) — 一种属性包装器类型，可读写一个值，该值会随着任何活跃的辅助技术（例如旁白）的焦点变化而由 SwiftUI 更新。

### 管理交互性

- [accessibilityRespondsToUserInteraction(_:)](<view/accessibilityrespondstouserinteraction(__).md>) — 显式设置此辅助功能元素是否响应用户交互，从而决定切换控制、语音控制或完整键盘访问等技术是否会与之交互。
- [accessibilityRespondsToUserInteraction(_:isEnabled:)](<view/accessibilityrespondstouserinteraction(__isenabled_).md>) — 显式设置此辅助功能元素是否响应用户交互，从而决定切换控制、语音控制或完整键盘访问等技术是否会与之交互。

## 另请参阅

### 辅助功能

- [辅助功能基础](accessibility-fundamentals.md) — 让你的 SwiftUI App 对每个人（包括残障人士）都无障碍可用。
- [辅助功能外观](accessible-appearance.md) — 增强 App 界面中内容的易读性。
- [辅助功能描述](accessible-descriptions.md) — 描述界面元素，帮助人们理解它们代表什么。
- [辅助功能导览](accessible-navigation.md) — 让用户能够使用转子（rotor）导览到特定的用户界面元素。
