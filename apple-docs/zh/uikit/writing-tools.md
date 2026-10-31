---
title: 写作工具（Writing Tools）
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/writing-tools
source_url: 'https://developer.apple.com/documentation/uikit/writing-tools'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/writing-tools.json'
content_hash: 'sha256:736bc7b2c019f18b'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md)

# Writing Tools

<sub>API 集合</sub>

为 App 的文本视图添加 Writing Tools 支持。

## 概述

Writing Tools 为人们提供了一种使用你的 App 改善所写内容的简单方式。支持 Writing Tools 的文本视图能够借助系统提供的大语言模型（LLM）和 Apple Intelligence 进行校对、重写、总结或撰写内容。

Writing Tools 支持标准的系统视图以及你创建的自定文本视图。[UITextView](uitextview.md) 和 [UITextField](uitextfield.md) 类自动支持 Writing Tools，但你可以自定该支持以满足 App 的需求。你还可以为 App 中包含文本的任何 [UIView](uiview.md) 添加 Writing Tools 支持。

## 主题

### 配置

- [Customizing Writing Tools behavior for UIKit views](customizing-writing-tools-behavior-for-system-views.md) — 修改标准 iOS 文本视图中 Writing Tools 的行为，并在该功能激活时调整 App 的行为。
- [UIWritingToolsBehavior](uiwritingtoolsbehavior.md) — 指定底层视图 Writing Tools 体验的常量。
- [UIWritingToolsResultOptions](uiwritingtoolsresultoptions.md) — 指定在 Writing Tools 建议或重写中允许的内容类型的常量。

### 自定视图的 Writing Tools

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md) — 为包含文本的自定 iOS 视图添加 Writing Tools 支持，包括内联替换动画支持。
- [UIWritingToolsCoordinator](uiwritingtoolscoordinator.md) — 管理 Writing Tools 与自定文本视图之间交互的对象。
- [Delegate](uiwritingtoolscoordinator/delegate-swift.protocol.md) — 用于管理 Writing Tools 与自定文本视图之间交互的接口。
- [Context](uiwritingtoolscoordinator/context.md) — 用于与 Writing Tools 共享自定视图文本的数据对象。
- [AnimationParameters](uiwritingtoolscoordinator/animationparameters.md) — 用于配置与 Writing Tools 动画并行运行的额外任务或动画的对象。

### 文本预览

- [UITargetedPreview](uitargetedpreview.md) — 描述在预览相关动画期间使用的视图的对象。
- [UIPreviewParameters](uipreviewparameters.md) — 动画预览界面时使用的额外参数。
- [UIPreviewTarget](uipreviewtarget.md) — 指定动画所用容器视图的对象。

## 另请参阅

### 文本

- [Text display and fonts](text-display-and-fonts.md) — 显示文本、管理字体并检查拼写。
- [TextKit](textkit.md) — 管理文本存储并执行 App 视图中文本内容的自定布局。
- [Keyboards and input](keyboards-and-input.md) — 配置系统键盘、创建自己的键盘来处理输入，或检测物理键盘上的按键。
- [Handwriting recognition](handwriting-recognition.md) — 配置接受文本的文本栏和自定视图，以处理来自 Apple Pencil 的输入。
