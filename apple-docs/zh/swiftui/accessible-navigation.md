---
title: 辅助功能导览
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessible-navigation
source_url: 'https://developer.apple.com/documentation/swiftui/accessible-navigation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessible-navigation.json'
content_hash: 'sha256:ada39cb31d4e8ad6'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 辅助功能导览

<sub>API 集合</sub>

让用户能够使用转子导览到特定的用户界面元素。

## 概述

辅助功能转子是一种快捷方式，让用户能够快速导览到用户界面的特定元素，并且可选地导览到这些元素内文本的特定范围。

![](../../../attachments/5ceef0267b3475033df3fcff2a12dd25/accessible-navigation-hero@2x.png)

系统会自动为许多可导览的元素提供转子，但你可以为特定目的提供额外的转子，或者在系统转子没有自动拾取屏幕外元素时（例如 [LazyVStack](lazyvstack.md) 或 [List](list.md) 中深处远端的元素）替换系统转子。

有关设计指引，请参阅《人机界面指南》辅助功能部分中的 [Accessibility](../design/human-interface-guidelines/accessibility.md#Navigation)。

## 主题

### 使用转子

- [accessibilityRotor(_:entries:)](<view/accessibilityrotor(__entries_).md>) — 使用指定的用户可见标签创建一个辅助功能转子（rotor），并使用由内容闭包生成的条目。
- [accessibilityRotor(_:entries:entryID:entryLabel:)](<view/accessibilityrotor(__entries_entryid_entrylabel_).md>) — 使用指定的用户可见标签和条目创建一个辅助功能转子。
- [accessibilityRotor(_:entries:entryLabel:)](<view/accessibilityrotor(__entries_entrylabel_).md>) — 使用指定的用户可见标签和条目创建一个辅助功能转子。
- [accessibilityRotor(_:textRanges:)](<view/accessibilityrotor(__textranges_).md>) — 使用指定的用户可见标签以及为每个指定范围生成的条目创建一个辅助功能转子。该转子将附加到当前辅助功能元素上，并且每个条目将指向该元素的指定范围。

### 创建转子

- [AccessibilityRotorContent](accessibilityrotorcontent.md) — 辅助功能转子中的内容。
- [AccessibilityRotorContentBuilder](accessibilityrotorcontentbuilder.md) — 用于生成转子条目内容的结果构建器。
- [AccessibilityRotorEntry](accessibilityrotorentry.md) — 表示辅助功能转子中一个条目的结构体。

### 替换系统转子

- [AccessibilitySystemRotor](accessibilitysystemrotor.md) — 指定一个转子，用一个开发者提供的转子替换自动生成的系统转子之一。

### 配置转子

- [accessibilityRotorEntry(id:in:)](<view/accessibilityrotorentry(id_in_).md>) — 定义一个显式标识符，将此视图的辅助功能元素与辅助功能转子中的一个条目关联起来。
- [accessibilityLinkedGroup(id:in:)](<view/accessibilitylinkedgroup(id_in_).md>) — 链接多个辅助功能元素，使用户能够快速从一个元素导航到另一个元素，即使这些元素在辅助功能层级结构中并不相邻。
- [accessibilitySortPriority(_:)](<view/accessibilitysortpriority(__).md>) — 设置此视图的辅助功能元素相对于同一层级其他元素的排序优先顺序。

## 另请参阅

### Accessibility

- [Accessibility fundamentals](accessibility-fundamentals.md) — 让你的 SwiftUI App 对每个人（包括残障人士）都无障碍可用。
- [Accessible appearance](accessible-appearance.md) — 增强 App 界面中内容的易读性。
- [Accessible controls](accessible-controls.md) — 改善对 App 可执行操作的访问。
- [Accessible descriptions](accessible-descriptions.md) — 描述界面元素，帮助人们理解它们代表什么。
