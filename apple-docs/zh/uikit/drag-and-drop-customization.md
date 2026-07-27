---
title: 拖放自定
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/drag-and-drop-customization
source_url: 'https://developer.apple.com/documentation/uikit/drag-and-drop-customization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/drag-and-drop-customization.json'
content_hash: 'sha256:22567a95dd701789'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [文本显示和字体](text-display-and-fonts.md)

# 拖放自定

<sub>API 集合</sub>

扩展文本视图对拖放（drag and drop）的标准支持，使其包含自定内容类型。

## 概述

[UITextField](uitextfield.md) 和 [UITextView](uitextview.md) 类为拖放文本和图像提供内建支持。你可以通过向视图添加文本拖动委托（delegate）或文本放置委托，将这种支持扩展到自己的自定数据类型。文本拖动委托采用 [UITextDragDelegate](uitextdragdelegate.md) 协议，并负责提供要拖动的项目。文本放置委托采用 [UITextDropDelegate](uitextdropdelegate.md) 协议，并处理包含自定数据类型项目的放置操作。

## 主题

### 文本视图扩展

- [UITextDragDelegate](uitextdragdelegate.md) — 用于自定文本视图拖动活动行为的接口。
- [UITextDropDelegate](uitextdropdelegate.md) — 用于配置文本视图放置行为的接口。
- [UITextDraggable](uitextdraggable.md) — 用于确定文本视图是否为拖动源的接口。
- [UITextDragOptions](uitextdragoptions.md) — 决定可拖动文本视图行为的一组选项。
- [UITextDroppable](uitextdroppable.md) — 用于确定文本视图是否为放置目的地的接口。
- [UITextDropEditability](uitextdropeditability.md) — 不可编辑文本视图的文本放置可编辑性样式。

### 拖动内容

- [UITextDragRequest](uitextdragrequest.md) — 用于描述源自文本视图的拖动活动属性的接口。
- [UITextDragPreviewRenderer](uitextdragpreviewrenderer.md) — 渲染用户所拖文本的预览。

### 放置管理

- [UITextDropRequest](uitextdroprequest.md) — 用于指定文本视图放置请求属性的接口。
- [UITextDropProposal](uitextdropproposal.md) — 文本放置交互行为的建议配置。
- [Action](uitextdropproposal/action.md) — 文本视图的文本放置操作样式。
- [Performer](uitextdropproposal/performer.md) — 负责处理放置操作的执行者。
- [ProgressMode](uitextdropproposal/progressmode.md) — 用于向用户显示进度指示的文本放置进度样式。

### 粘贴板支持

- [UITextPasteItem](uitextpasteitem.md) — 用于获取粘贴或放置文本项的信息并与之交互的接口。
- [UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md) — 支持粘贴令牌的协议。
- [UITextPasteDelegate](uitextpastedelegate.md) — 使用项目提供器处理文本粘贴和放置的接口。
- [UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md) — 供面向文本的响应器对象参与 iOS 统一粘贴和放置系统的接口。

## 另请参阅

### 文本视图

- [UILabel](uilabel.md) — 显示一行或多行信息文本的视图。
- [UITextField](uitextfield.md) — 在界面中显示可编辑文本区域的对象。
- [UITextView](uitextview.md) — 可滚动的多行文本区域。
