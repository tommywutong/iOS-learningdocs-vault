---
title: Xcode 资源库自定
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/xcode-library-customization
source_url: 'https://developer.apple.com/documentation/swiftui/xcode-library-customization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/xcode-library-customization.json'
content_hash: 'sha256:74ec64f3faf2e6ff'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# Xcode 资源库自定

在 Xcode 资源库中公开自定义视图和修饰符。

## 概述

你可以将你的自定义 SwiftUI 视图和视图修饰符添加到 Xcode 的资源库（library）中。这让开发你的 App 或采用你的框架的任何人都能通过点按 Xcode 工具栏中的资源库按钮（+）来访问它们。你可以像对待系统提供的条目一样，选中自定义资源库条目并将其拖入代码中。

![](../../../attachments/75621f8df7fbcc9a90dc8e0bf967ef78/xcode-library-customization-hero@2x.png)

要向资源库添加条目，请创建一个符合 [LibraryContentProvider](../developertoolssupport/librarycontentprovider.md) 协议的结构体，并将你要添加的任何条目封装为 [LibraryItem](../developertoolssupport/libraryitem.md) 实例。实现 [views](../developertoolssupport/librarycontentprovider/views.md) 计算属性以添加包含视图的资源库条目。实现 [modifiers(base:)](<../developertoolssupport/librarycontentprovider/modifiers(base_).md>) 方法以添加包含视图修饰符的条目。Xcode 会在你工作时从你项目中的所有资源库内容提供器收集条目，并在其资源库中提供给你使用。

## 主题

### 创建资源库条目

- [LibraryContentProvider](../developertoolssupport/librarycontentprovider.md) — Xcode 资源库和代码补全内容的来源。
- [LibraryItem](../developertoolssupport/libraryitem.md) — 要添加到 Xcode 资源库的单个条目。

## 另请参阅

### 工具支持

- [Xcode 中的预览](previews-in-xcode.md) — 为你的自定义视图生成动态、可交互的预览。
- [性能分析](performance-analysis.md) — 测量并改进你的 App 的响应能力。
