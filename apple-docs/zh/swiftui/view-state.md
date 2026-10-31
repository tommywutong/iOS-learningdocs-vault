---
title: 状态修饰符
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-state
source_url: 'https://developer.apple.com/documentation/swiftui/view-state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-state.json'
content_hash: 'sha256:6365e8efde84ca72'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md) · [View](view.md)

# 状态修饰符

<sub>API 集合</sub>

访问存储，并为子视图提供配置数据。

## 概述

SwiftUI 提供了在 App 中管理数据的工具。例如，你可以把值和对象存储在视图层级结构中各视图共享的环境里。任何共享该环境的视图——通常是存储该项的视图的所有后代视图——之后都可以访问存储的项。

有关 SwiftUI 为帮助管理 App 中数据而提供的类型的更多信息，请参阅[模型数据](model-data.md)。

## 主题

### 身份

- [tag(_:includeOptional:)](<view/tag(__includeoptional_).md>) — 设置此视图的唯一标签值。
- [id(_:)](<view/id(__).md>) — 将视图的身份绑定到给定的代理值。
- [equatable()](<view/equatable().md>) — 当视图的新值与旧值相同时，阻止其更新子视图。

### Environment values

- [environment(_:)](<view/environment(__).md>) — 将可观察对象放入视图中。
- [environment(_:_:)](<view/environment(____).md>) — 将指定键路径的环境值设置为给定值。
- [environmentObject(_:)](<view/environmentobject(__).md>) — 向视图的层级结构提供可观察对象。
- [transformEnvironment(_:transform:)](<view/transformenvironment(__transform_).md>) — 用给定的函数变换指定键路径的环境值。

### 偏好

- [preference(key:value:)](<view/preference(key_value_).md>) — 为给定的偏好设置值。
- [transformPreference(_:_:)](<view/transformpreference(____).md>) — 对偏好值应用一种变换。
- [anchorPreference(key:value:transform:)](<view/anchorpreference(key_value_transform_).md>) — 为指定的偏好键设置值，该值是与当前坐标空间关联的几何值的函数，让该值的读取者能够将该几何值转换为其本地坐标。
- [transformAnchorPreference(key:value:transform:)](<view/transformanchorpreference(key_value_transform_).md>) — 为指定的偏好键设置值，该值是键的当前值和与当前坐标空间关联的几何值的函数，让该值的读取者能够将该几何值转换为其本地坐标。
- [onPreferenceChange(_:perform:)](<view/onpreferencechange(__perform_).md>) — 添加一个操作，在指定偏好键的值变化时执行。
- [backgroundPreferenceValue(_:_:)](<view/backgroundpreferencevalue(____).md>) — 从视图读取指定的偏好值，用它生成第二个视图，作为背景应用到原视图上。
- [backgroundPreferenceValue(_:alignment:_:)](<view/backgroundpreferencevalue(__alignment___).md>) — 从视图读取指定的偏好值，用它生成第二个视图，作为背景应用到原视图上。
- [overlayPreferenceValue(_:_:)](<view/overlaypreferencevalue(____).md>) — 从视图读取指定的偏好值，用它生成第二个视图，作为叠层应用到原视图上。
- [overlayPreferenceValue(_:alignment:_:)](<view/overlaypreferencevalue(__alignment___).md>) — 从视图读取指定的偏好值，用它生成第二个视图，作为叠层应用到原视图上。

### 默认存储

- [defaultAppStorage(_:)](<view/defaultappstorage(__).md>) — 视图内 `AppStorage` 使用的默认存储。

### 配置模型

- [modelContext(_:)](<view/modelcontext(__).md>) — 在此视图的环境中设置模型上下文。
- [modelContainer(_:)](<view/modelcontainer(__).md>) — 在此视图的环境中设置模型容器及关联的模型上下文。
- [modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)](<view/modelcontainer(for_inmemory_isautosaveenabled_isundoenabled_onsetup_).md>) — 在此视图中设置用于存储所提供模型类型的模型容器（必要时创建新容器），同时在此视图的环境中为该容器设置模型上下文。

## 另请参阅

### 提供交互性

- [Input and event modifiers](view-input-and-events.md) — 为视图提供响应于用户输入和系统事件而执行的操作。
- [Search modifiers](view-search.md) — 让人们能够在你的 App 中搜索内容。
- [Presentation modifiers](view-presentation.md) — 为视图定义额外要在指定条件下呈现的视图。
