---
title: 为你的 SwiftUI App 带来健壮的导航结构
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, Xcode 16.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/bringing-robust-navigation-structure-to-your-swiftui-app
source_url: 'https://developer.apple.com/documentation/swiftui/bringing-robust-navigation-structure-to-your-swiftui-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/bringing-robust-navigation-structure-to-your-swiftui-app.json'
content_hash: 'sha256:0a9d015516c7dff3'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [导航](navigation.md)

# 为你的 SwiftUI App 带来健壮的导航结构

<sub>示例代码</sub>

使用导航链接、叠放、目的地和路径来为所有平台提供精简的体验，并支持深层链接和状态恢复等行为。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC22 场次 [10054: The SwiftUI cookbook for navigation](https://developer.apple.com/wwdc22/10054/)。

## 另请参阅

### 以分栏形式呈现视图

- [迁移到新的导航类型](migrating-to-new-navigation-types.md) — 用导航叠放和导航拆分视图替换导航视图，改善你的 App 的导航行为。
- [NavigationSplitView](navigationsplitview.md) — 以两栏或三栏呈现视图的视图，其中前导栏中的选择控制后续栏中的呈现。
- [navigationSplitViewStyle(_:)](<view/navigationsplitviewstyle(__).md>) — 设置此视图内导航拆分视图的样式。
- [navigationSplitViewColumnWidth(_:)](<view/navigationsplitviewcolumnwidth(__).md>) — 为包含此视图的栏设置固定的首选宽度。
- [navigationSplitViewColumnWidth(min:ideal:max:)](<view/navigationsplitviewcolumnwidth(min_ideal_max_).md>) — 为包含此视图的栏设置灵活的首选宽度。
- [NavigationSplitViewVisibility](navigationsplitviewvisibility.md) — 导航拆分视图中前导栏的可见性。
- [NavigationLink](navigationlink.md) — 控制导航呈现的视图。

## 下载

- [BringingRobustNavigationStructureToYourSwiftUIApp.zip](https://docs-assets.developer.apple.com/published/45511f40934b/BringingRobustNavigationStructureToYourSwiftUIApp.zip)
