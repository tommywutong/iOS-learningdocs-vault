---
title: 使用 SwiftUI 创建视觉效果
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, Xcode 16.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/creating-visual-effects-with-swiftui
source_url: 'https://developer.apple.com/documentation/swiftui/creating-visual-effects-with-swiftui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/creating-visual-effects-with-swiftui.json'
content_hash: 'sha256:e84b7ebc21506f30'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [文本输入与输出](text-input-and-output.md)

# 使用 SwiftUI 创建视觉效果

<sub>示例代码</sub>

使用着色器和文本渲染器添加滚动效果、丰富的颜色处理、自定义过渡和高级效果。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC24 场次 10151：[Create custom visual effects in SwiftUI](https://developer.apple.com/wwdc24/10151/)。

## 另请参阅

### 渲染文本

- [TextAttribute](textattribute.md) — 一个可以附加到文本视图上的值，文本渲染器可以查询它。
- [textRenderer(_:)](<view/textrenderer(__).md>) — 返回一个新视图，使其中任何文本视图都使用 `renderer` 来绘制自身。
- [TextRenderer](textrenderer.md) — 一个可以替换默认文本视图绘制行为的值。
- [TextProxy](textproxy.md) — 自定义文本渲染器使用的文本视图代理。

## 下载

- [CreatingVisualEffectsWithSwiftUI.zip](https://docs-assets.developer.apple.com/published/9a15b1cc1a22/CreatingVisualEffectsWithSwiftUI.zip)
