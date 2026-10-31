---
title: 配置你 App 的导览标题
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/configure-your-apps-navigation-titles
source_url: 'https://developer.apple.com/documentation/swiftui/configure-your-apps-navigation-titles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/configure-your-apps-navigation-titles.json'
content_hash: 'sha256:cd1b34c385cce0fd'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md) · [View](view.md) · [Auxiliary view modifiers](view-auxiliary-views.md)

# 配置你 App 的导览标题

<sub>文章</sub>

使用导览标题显示界面的当前导览状态。

## 概述

在 iOS 和 watchOS 上，当视图在导览叠放内被导览到时，导航栏会显示该视图的标题。在 iPadOS 上，主要目的地的导览标题会体现为 App 切换器中窗口的标题。同样，在 macOS 上，系统会把主要目的地的标题用作标题栏、「窗口」菜单和调度中心中的窗口标题。

在最简单的形式下，你可以直接向导览标题修饰符提供一个字符串或本地化字符串键。

```swift
ContentView()
    .navigationTitle("My Title")
```

你 App 工具栏的标题还可以使用其他与导览相关的修饰符进一步自定。例如，你可以使用导览文稿修饰符将一个 [URL](../foundation/url.md) 或你自己符合 [Transferable](../coretransferable/transferable.md) 的类型关联到你的视图。

```swift
ContentView()
    .navigationTitle("My Title")
    .navigationDocument(myURL)
```

在 iOS 和 iPadOS 上，这会构建一个这样的标题：在 App 的导航栏中轻点导览标题即可呈现一个菜单。菜单包含提供与该 URL 相关信息的内容，以及一个用于分享的可拖动图标。

在 macOS 上，此项目会构建一个代理图标，用于操控支撑文稿的文件。

提供可传输类型时，你通常应提供一个 [SharePreview](sharepreview.md)，为在菜单标头中渲染预览提供合适的内容。

```swift
ContentView()
    .navigationTitle("My Title")
    .navigationDocument(
        myDocument, 
        preview: SharePreview(
            "My Preview Title", image: myDocument.image))
```

### 重命名

你可以向导览标题修饰符提供文本绑定，SwiftUI 会自动配置工具栏，允许在 iOS 或 macOS 上编辑导览标题。SwiftUI 会自动将导览标题与提供给文本栏的字符串绑定的值同步。

你可以向导览标题提供字符串绑定来配置标题的文本栏。SwiftUI 会自动在标题菜单中放置一个重命名操作，与源自你 App 命令的操作并列。

```swift
ContentView()
    .navigationTitle($contentTitle)
```

在 iOS 上，当在导览标题中使用文本栏时，SwiftUI 会在工具栏标题中创建一个按钮。触发该按钮后，导览标题会更新为显示一个内嵌文本栏，用户输入时会更新你提供的绑定。

## 另请参阅

### 导览标题

- [navigationTitle(_:)](<view/navigationtitle(__).md>) — 使用本地化字符串资源为导览目的配置视图的标题。
- [navigationSubtitle(_:)](<view/navigationsubtitle(__).md>) — 使用本地化字符串资源为导览目的配置视图的副标题。
