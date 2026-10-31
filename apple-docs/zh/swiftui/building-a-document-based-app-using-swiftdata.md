---
title: 使用 SwiftData 构建基于文稿的 App
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/building-a-document-based-app-using-swiftdata
source_url: 'https://developer.apple.com/documentation/swiftui/building-a-document-based-app-using-swiftdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/building-a-document-based-app-using-swiftdata.json'
content_hash: 'sha256:ce92010c49eb2538'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [文稿](documents.md)

# 使用 SwiftData 构建基于文稿的 App

<sub>示例代码</sub>

跟随 WWDC 演讲者一起使用 SwiftData 改造一个 App。

## 概述

学习如何使用 [`@Query`](../swiftdata/query.md)、[`@Bindable`](bindable.md)、[`.modelContainer`](<view/modelcontainer(__).md>)、[`.modelContext`](environmentvalues/modelcontext.md) 环境变量以及 [`DocumentGroup`](documentgroup.md) 来与 [`SwiftData`](../swiftdata.md) 框架集成。

> [!note] 注意
> 本示例代码项目关联 WWDC23 场次 10154：[Build an app with SwiftData](https://developer.apple.com/wwdc23/10154/)。

## 另请参阅

### 创建文稿

- [创建基于文稿的 App](creating-a-document-based-app.md) — 构建让人们能够使用协调的文件访问来打开、编辑和保存文件的 App。
- [处理高级文稿场景](handling-advanced-document-scenarios.md) — 扩展你的基于文稿的 App，以支持自定义文件格式、按需文件访问和进度报告。
- [更新你的基于文稿的 App](updating-your-document-based-app.md) — 迁移现有 App，以借助 Swift 并发采用基于 URL 的文稿读写。
- [使用 SwiftUI 构建基于文稿的 App](building-a-document-based-app-with-swiftui.md) — 在多平台 App 中创建、保存和打开文稿。
- [DocumentGroup](documentgroup.md) — 一种支持打开、创建和保存文稿的场景。

## 下载

- [BuildingADocumentBasedAppUsingSwiftData.zip](https://docs-assets.developer.apple.com/published/a378001f6c52/BuildingADocumentBasedAppUsingSwiftData.zip)
