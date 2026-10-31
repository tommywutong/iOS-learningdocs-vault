---
title: 偏好
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/preferences
source_url: 'https://developer.apple.com/documentation/swiftui/preferences'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/preferences.json'
content_hash: 'sha256:568cd4b4cb596236'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 偏好

<sub>API 集合</sub>

从视图向其容器视图指示配置偏好。

## 概述

环境用于配置视图的子视图，而偏好则用于把配置信息从子视图发送给它们的容器。不过，与配置信息沿视图层级结构从一个容器流向多个子视图不同，单一容器需要协调从其众多子视图向上流动的、可能相互冲突的偏好。

![](../../../attachments/868be1f862daf281c185c168365df04f/preferences-hero@2x.png)

当你使用 [PreferenceKey](preferencekey.md) 协议定义自定偏好时，你需要指明如何合并来自多个子视图的偏好。然后，你可以使用 [preference(key:value:)](<view/preference(key_value_).md>) 视图修饰符在某个视图上为该偏好设置值。许多内置修饰符（例如 [navigationTitle(_:)](<view/navigationtitle(__).md>)）都依赖偏好来向其容器发送配置信息。

## 主题

### 设置偏好

- [preference(key:value:)](<view/preference(key_value_).md>) — 为给定的偏好设置值。
- [transformPreference(_:_:)](<view/transformpreference(____).md>) — 对偏好值应用一种变换。

### 创建自定偏好

- [PreferenceKey](preferencekey.md) — 视图产生的一个具名值。

### 基于几何形状设置偏好

- [anchorPreference(key:value:transform:)](<view/anchorpreference(key_value_transform_).md>) — 为指定的偏好键设置值，该值是与当前坐标空间关联的几何值的函数，让该值的读取者能够将该几何值转换为其本地坐标。
- [transformAnchorPreference(key:value:transform:)](<view/transformanchorpreference(key_value_transform_).md>) — 为指定的偏好键设置值，该值是键的当前值和与当前坐标空间关联的几何值的函数，让该值的读取者能够将该几何值转换为其本地坐标。

### 响应偏好变化

- [onPreferenceChange(_:perform:)](<view/onpreferencechange(__perform_).md>) — 添加一个操作，在指定偏好键的值变化时执行。

### 从偏好生成背景和叠层

- [backgroundPreferenceValue(_:_:)](<view/backgroundpreferencevalue(____).md>) — 从视图读取指定的偏好值，用它生成第二个视图，作为背景应用到原视图上。
- [backgroundPreferenceValue(_:alignment:_:)](<view/backgroundpreferencevalue(__alignment___).md>) — 从视图读取指定的偏好值，用它生成第二个视图，作为背景应用到原视图上。
- [overlayPreferenceValue(_:_:)](<view/overlaypreferencevalue(____).md>) — 从视图读取指定的偏好值，用它生成第二个视图，作为叠层应用到原视图上。
- [overlayPreferenceValue(_:alignment:_:)](<view/overlaypreferencevalue(__alignment___).md>) — 从视图读取指定的偏好值，用它生成第二个视图，作为叠层应用到原视图上。

## 另请参阅

### 数据与存储

- [Model data](model-data.md) — 管理 App 用来驱动其界面的数据。
- [Environment values](environment-values.md) — 使用环境在整个视图层级结构中共享数据。
- [Persistent storage](persistent-storage.md) — 存储数据，供 App 的多次会话使用。
