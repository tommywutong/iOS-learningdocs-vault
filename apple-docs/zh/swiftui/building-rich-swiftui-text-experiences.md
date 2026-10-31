---
title: 构建丰富的 SwiftUI 文本体验
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, Xcode 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/building-rich-swiftui-text-experiences
source_url: 'https://developer.apple.com/documentation/swiftui/building-rich-swiftui-text-experiences'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/building-rich-swiftui-text-experiences.json'
content_hash: 'sha256:d824db1162d714c6'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [文本输入与输出](text-input-and-output.md)

# 构建丰富的 SwiftUI 文本体验

<sub>示例代码</sub>

使用 SwiftUI 文本编辑器视图和属性字符串构建一个用于带格式文本的编辑器。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC25 场次 280：[Code-along: Cook up a rich text experience in SwiftUI with AttributedString](https://developer.apple.com/wwdc25/280/)。

你可以跟随 WWDC25 场次中编写的代码，学习如何将 `TextEditor` 升级为富文本、构建自定义控制，以及约束编辑器提供的格式化选项。

在跟练（code-along）之后，你可以进一步了解如何使用 SwiftData 持久化富文本，以及如何使用 `Transferable` 协议导出富文本文稿。

### 配置示例代码项目

要配置示例代码项目，请在 Xcode 中执行以下操作：

1. 使用最新版本的 Xcode 打开该示例。
2. 设置开发者团队，让 Xcode 自动管理描述文件。更多信息请参阅[设置软件包标识符](../xcode/preparing-your-app-for-distribution.md#Set-the-bundle-ID)和[将项目指定给团队](../xcode/preparing-your-app-for-distribution.md#Assign-the-project-to-a-team)。

## 另请参阅

### 获取文本输入

- [TextField](textfield.md) — 显示可编辑文本界面的控制。
- [textFieldStyle(_:)](<view/textfieldstyle(__).md>) — 设置此视图内文本栏的样式。
- [SecureField](securefield.md) — 人们用来安全输入私密文本的控制。
- [TextEditor](texteditor.md) — 可以显示和编辑长篇文本的视图。

## 下载

- [BuildingRichSwiftUITextExperiences.zip](https://docs-assets.developer.apple.com/published/af5124237a05/BuildingRichSwiftUITextExperiences.zip)
