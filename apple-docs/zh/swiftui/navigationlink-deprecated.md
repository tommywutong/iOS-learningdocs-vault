---
title: 已废弃符号
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/navigationlink-deprecated
source_url: 'https://developer.apple.com/documentation/swiftui/navigationlink-deprecated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationlink-deprecated.json'
content_hash: 'sha256:6fd0a51d6861dc51'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [Navigation](navigation.md) · [NavigationLink](navigationlink.md)

# 已废弃符号

<sub>API 集合</sub>

查看已废弃的导览链接初始化方法。

## 概述

有关更新导览符号使用方式的信息，请参阅[迁移到新的导览类型](migrating-to-new-navigation-types.md)。

## 主题

### 使用内容构建器创建链接

- [init(_:isActive:destination:)](<navigationlink/init(__isactive_destination_).md>) — 创建一个导览链接，在激活时呈现目的地视图，并使用该链接从本地化字符串键生成的文本标签。_(已废弃)_
- [init(isActive:destination:label:)](<navigationlink/init(isactive_destination_label_).md>) — 创建一个在激活时呈现目的地视图的导览链接。_(已废弃)_
- [init(_:tag:selection:destination:)](<navigationlink/init(__tag_selection_destination_).md>) — 创建一个导览链接，当绑定的选择变量与你提供的值匹配时呈现目的地视图，并使用该链接从标题字符串生成的文本标签。_(已废弃)_
- [init(tag:selection:destination:label:)](<navigationlink/init(tag_selection_destination_label_).md>) — 创建一个导览链接，当绑定的选择变量等于给定的标签值时呈现目的地视图。_(已废弃)_

### 为 WatchKit 创建链接

- [init(destinationName:isActive:label:)](<navigationlink/init(destinationname_isactive_label_).md>) — 创建一个导览链接，在激活时呈现来自 WatchKit storyboard 的视图。_(已废弃)_
- [init(destinationName:tag:selection:label:)](<navigationlink/init(destinationname_tag_selection_label_).md>) — 创建一个导览链接，当绑定的选择变量与你提供的值匹配时呈现来自 WatchKit storyboard 的视图。_(已废弃)_
- [init(destinationName:label:)](<navigationlink/init(destinationname_label_).md>) — 创建一个呈现来自 WatchKit storyboard 的视图的导览链接。_(已废弃)_

### 使用视图实参创建链接

- [init(_:destination:isActive:)](<navigationlink/init(__destination_isactive_).md>) — 创建一个导览链接，在激活时呈现目的地视图，并使用该链接从本地化字符串键生成的文本标签。_(已废弃)_
- [init(destination:isActive:label:)](<navigationlink/init(destination_isactive_label_).md>) — 创建一个在激活时呈现目的地视图的导览链接。_(已废弃)_
- [init(_:destination:tag:selection:)](<navigationlink/init(__destination_tag_selection_).md>) — 创建一个导览链接，当绑定的选择变量与你提供的值匹配时呈现目的地视图，并使用该链接从标题字符串生成的文本标签。_(已废弃)_
- [init(destination:tag:selection:label:)](<navigationlink/init(destination_tag_selection_label_).md>) — 创建一个导览链接，当绑定的选择变量等于给定的标签值时呈现目的地视图。_(已废弃)_
