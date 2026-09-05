---
title: 手写识别
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/handwriting-recognition
source_url: 'https://developer.apple.com/documentation/uikit/handwriting-recognition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/handwriting-recognition.json'
content_hash: 'sha256:838e7c1c481d942c'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md)

# 手写识别（Handwriting recognition）

<sub>API 集合</sub>

配置接受文本的文本字段和自定义视图，以处理来自 Apple Pencil 的输入。

## 主题

### 基础

- [通过交互自定义随手写](../pencilkit/customizing-scribble-with-interactions.md) — 通过添加交互，在非文本输入视图上启用书写。

### 文本字段

- [UIScribbleInteraction](uiscribbleinteraction.md) — 用于自定义随手写（Scribble）在文本输入视图上的行为、或在特定情况下完全抑制它的交互。
- [UIScribbleInteractionDelegate](uiscribbleinteractiondelegate.md) — 用于自定义或抑制文本输入视图中随手写行为的方法。

### 自定义视图

- [UIIndirectScribbleInteraction](uiindirectscribbleinteraction-1nfjm.md) — 通过在并非正式文本输入的视图上书写、从而使用随手写输入文本的交互。
- [UIIndirectScribbleInteractionDelegate](uiindirectscribbleinteractiondelegate-hdh.md) — 在并非正式文本输入视图的视图上自定义行为的方法。
- [ElementIdentifier](uiindirectscribbleinteractiondelegate-hdh/elementidentifier.md) — 随手写交互中非文本字段控件的唯一标识符。

## 另请参阅

### 文本

- [文本显示与字体](text-display-and-fonts.md) — 显示文本、管理字体并检查拼写。
- [TextKit](textkit.md) — 管理文本存储，并在你的 App 的视图中对基于文本的内容执行自定义布局。
- [键盘与输入](keyboards-and-input.md) — 配置系统键盘、创建你自己的键盘来处理输入，或检测物理键盘上的按键。
- [Writing Tools](writing-tools.md) — 为你的 App 的文本视图添加 Writing Tools 支持。
