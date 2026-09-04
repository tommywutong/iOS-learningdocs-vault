---
title: 添加自定义操作与活动
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adding-custom-actions-and-activities
source_url: 'https://developer.apple.com/documentation/uikit/adding-custom-actions-and-activities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adding-custom-actions-and-activities.json'
content_hash: 'sha256:5125e344701ce3fd'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图控制器](view-controllers.md) · [向你的 App 添加文稿浏览器](adding-a-document-browser-to-your-app.md)

# 添加自定义操作与活动

<sub>文章</sub>

为文稿浏览器添加自定义操作、活动和栏按钮项。

## 概述

向文稿浏览器添加自定义操作有三种不同方式：

- 把文稿浏览器操作加到导航栏或编辑菜单（Edit Menu）。
- 把活动加到活动视图（activity view）。
- 把栏按钮项加到导航栏。

### 添加文稿浏览器操作

默认情况下，系统会提供拷贝、移动、重新命名、删除和共享等标准操作。要添加自定义操作，把一个 [UIDocumentBrowserAction](uidocumentbrowseraction.md) 对象数组赋给浏览器的 [customActions](uidocumentbrowserviewcontroller/customactions.md) 属性。

文稿浏览器操作有两种访问方式：

- _导航栏_操作在用户把浏览器切到选择（Select）模式时出现在导航栏中。
- _编辑菜单_操作在用户长按文档或文件夹时出现。

当用户触发其中某个操作时，该操作会收到当前所选条目的 URL。

### 添加活动

当用户点按共享按钮时（例如长按文档或文件夹并在编辑菜单中选择 Share），浏览器会显示活动视图。

要向活动视图添加自定义活动，实现你的 [UIDocumentBrowserViewControllerDelegate](uidocumentbrowserviewcontrollerdelegate.md) 对象的 [- documentBrowser:applicationActivitiesForDocumentURLs:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__applicationactivitiesfordocumenturls_).md>) 方法，并返回一个自定义 [UIActivity](uiactivity.md) 对象数组。

你的委托对象会收到当前所选条目的 URL 数组。你可以在你的 [UIActivity](uiactivity.md) 子类中存储并使用这些 URL。

设计指南参见 Human Interface Guidelines \> [Collaboration and sharing](../design/human-interface-guidelines/collaboration-and-sharing.md)。

### 添加栏按钮项

使用 [additionalLeadingNavigationBarButtonItems](uidocumentbrowserviewcontroller/additionalleadingnavigationbarbuttonitems.md) 和 [additionalTrailingNavigationBarButtonItems](uidocumentbrowserviewcontroller/additionaltrailingnavigationbarbuttonitems.md) 属性向导航栏添加按钮。

这些按钮发起的操作无法访问浏览器的内容或所选条目的 URL。请把栏按钮项用于不影响特定文档或文件夹的操作。

## 另请参阅

### 自定义

- [自定义文稿浏览器](customizing-the-browser.md) — 自定义文稿浏览器的外观与行为。
