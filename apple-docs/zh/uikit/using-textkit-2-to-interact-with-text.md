---
title: 使用 TextKit 2 与文本交互
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, Xcode 14.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/using-textkit-2-to-interact-with-text
source_url: 'https://developer.apple.com/documentation/uikit/using-textkit-2-to-interact-with-text'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/using-textkit-2-to-interact-with-text.json'
content_hash: 'sha256:379b4b12f79ae5f1'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md)

# 使用 TextKit 2 与文本交互

<sub>示例代码</sub>

通过管理文本选择和插入自定文本元素与文本交互。

## 概述

> [!note] 注意
> 此示例代码项目与 WWDC21 场次 [10061：认识 TextKit 2](https://developer.apple.com/wwdc21/10061/) 相关联。

## 另请参阅

### 布局

- [使用自定布局显示文本](display-text-with-a-custom-layout.md) — 在自定形状的容器中排列文本，并应用字形替换。
- [管理文本视图中的视口布局与附件复用](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md) — 在你的文本视图子类中自定布局并保留附件视图。
- [NSTextLayoutManager](nstextlayoutmanager.md) — 用于为自定文本显示管理文本布局和呈现的主要类。
- [NSTextContainer](nstextcontainer.md) — 进行文本布局的区域。
- [NSTextLayoutFragment](nstextlayoutfragment.md) — 表示布局片段的类，该片段通常对应于图层或视图子类等渲染表面。
- [NSTextLineFragment](nstextlinefragment.md) — 表示行片段的类，该行片段是文本布局片段内的单个文本布局与渲染单元。
- [NSTextViewportLayoutController](nstextviewportlayoutcontroller.md) — 与其委托（delegate）交互，管理视口内的布局过程。
- [NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md) — 将视图或图层标识为文本布局片段的可绘制元素的协议。 _(beta)_
- [NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md) — 让你在存储或检索渲染表面时使用对象标识该表面的协议。
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md) — 一组定义对象文本方向的方法。

## 下载

- [UsingTextKit2ToInteractWithText.zip](https://docs-assets.developer.apple.com/published/806998142c63/UsingTextKit2ToInteractWithText.zip)
