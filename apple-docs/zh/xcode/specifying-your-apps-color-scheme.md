---
title: 指定你 App 的配色方案
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/specifying-your-apps-color-scheme
source_url: 'https://developer.apple.com/documentation/xcode/specifying-your-apps-color-scheme'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/specifying-your-apps-color-scheme.json'
content_hash: 'sha256:637b499fb4e70e33'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Asset management](asset-management.md)

# 指定你 App 的配色方案

<sub>文章</sub>

通过使用素材目录，为你的 App 设置一个全局强调色。

## 概述

_强调色_（accent color），或称_着色色_（tint color），是一种应用于你 App 中视图和控制的宽泛主题色。使用强调色可以快速为你的 App 打造统一的配色方案。你可以通过在素材目录中指定一种强调色，来为你的 App 设置强调色。

![](../../../attachments/0a0df01d211ef225282e3db8e667bfee/specifying-your-apps-color-scheme-1@2x.png)

<sub>一个设置为最大值 75% 的滑块控制。其轨道左侧代表最小值与当前值之间的区间，被着上了自定的强调色。</sub>

### 创建一个强调色集

当你从模板创建项目时，项目会自动包含一个默认的素材目录（`Assets.xcassets`），其中带有一个 `AccentColor` 颜色集。Xcode 会把你在该颜色集中指定的颜色应用为你 App 的强调色。

如果你的 App 没有 `AccentColor` 颜色集，请手动创建一个颜色集。

1. 在 Project navigator 中，选择一个素材目录。
2. 点击大纲视图底部的添加按钮（+）。
3. 在弹出菜单中，选择 Color Set。大纲视图中会出现一个新的颜色集，并在详情区域打开。
4. 在大纲视图中双击该颜色集的名称，为它重命名一个描述性的名字，然后按 Return 键。
5. 在 Build Settings 中，找到 "Global Accent Color Name" 这项构建设置。双击该构建设置，输入你的强调色集的名称，然后按 Return 键。

### 指定强调色的变体

在选择强调色时，请选择一种在浅色和深色外观下都表现良好的颜色。如有需要，你可以在你的强调色集中为浅色和深色外观指定不同的颜色值。

1. 在 Project navigator 中，选择一个素材目录。
2. 在大纲视图中，选择该强调色集。
3. 打开 Attributes inspector。在 Appearances 字段中，选择你想要为其指定颜色值的外观。详情区域中会为你所指定的各个外观选项出现额外的颜色池。
4. 选择一个颜色池，并通过 Attributes inspector 中的 Content 字段设置颜色。使用 Any Appearance 颜色池来指定 App 在不区分浅色与深色外观的系统上所使用的颜色值。

你还可以通过勾选 High Contrast 复选框，来指定你的颜色的高对比度版本。

### 从代码中访问强调色

默认情况下，你的强调色会应用到你 App 中所有使用着色色的视图和控制上，除非你为视图层级结构中的特定子集覆盖了该颜色。不过，你可能还想把强调色融入到界面中其他不依赖着色色的部分，比如静态文本元素。

要在代码中使用素材目录里的强调色值，请像下面这样加载该颜色：

```swift
// SwiftUI
Text("Accent Color")
    .foregroundStyle(Color.accentColor)

// UIKit
label.textColor = UIColor.tintColor
```

## 另请参阅

### Colors

- [Supporting Dark Mode in your interface](../uikit/supporting-dark-mode-in-your-interface.md) — 更新颜色、图像和行为，让你的 App 在深色模式启用时能自动适配。
