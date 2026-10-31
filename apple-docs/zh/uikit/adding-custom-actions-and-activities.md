---
title: 添加自定操作与活动
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

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [Adding a document browser to your app](adding-a-document-browser-to-your-app.md)

# 添加自定操作与活动

<sub>文章</sub>

添加自定文稿浏览器操作、活动与栏项。

## 概述

有三种不同的方式可向文稿浏览器添加自定操作：

- 向导航栏或编辑菜单添加文稿浏览器操作。
- 向活动视图添加活动。
- 向导航栏添加栏项。

### 添加文稿浏览器操作

默认情况下，系统提供复制、移动、重命名、删除和共享等标准操作。要添加自定操作，将 [UIDocumentBrowserAction](uidocumentbrowseraction.md) 对象数组指定给浏览器的 [customActions](uidocumentbrowserviewcontroller/customactions.md) 属性。

文稿浏览器操作可通过两种方式访问：

- _导航栏_操作在某人将浏览器置于选择模式时出现在导航栏中。
- _编辑菜单_操作在某人长按文稿或文件夹时出现。

当某人启动这些操作之一时，操作会收到当前所选项目的 URL。

### 添加活动

当某人点击共享按钮时（例如在某人长按文稿或文件夹并从编辑菜单选择「共享」时），浏览器会显示活动视图。

要向活动视图添加自定活动，请实现你的 [UIDocumentBrowserViewControllerDelegate](uidocumentbrowserviewcontrollerdelegate.md) 对象的 [- documentBrowser:applicationActivitiesForDocumentURLs:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__applicationactivitiesfordocumenturls_).md>) 方法，并返回自定 [UIActivity](uiactivity.md) 对象数组。

委托对象会收到当前所选项目的 URL 数组。你可以在 [UIActivity](uiactivity.md) 子类中存储并使用这些 URL。

有关设计指南，请参阅 Human Interface Guidelines \> [协作与共享](../design/human-interface-guidelines/collaboration-and-sharing.md)。

### 添加栏按钮项

使用 [additionalLeadingNavigationBarButtonItems](uidocumentbrowserviewcontroller/additionalleadingnavigationbarbuttonitems.md) 和 [additionalTrailingNavigationBarButtonItems](uidocumentbrowserviewcontroller/additionaltrailingnavigationbarbuttonitems.md) 属性向导航栏添加按钮。

这些按钮启动的操作无法访问浏览器的内容或所选项目的 URL。请将栏按钮项用于不影响特定文稿或文件夹的操作。

## 另请参阅

### 自定

- [Customizing the document browser](customizing-the-browser.md) — 自定文稿浏览器的外观与行为。
