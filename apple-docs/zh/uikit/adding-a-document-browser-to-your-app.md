---
title: 为你的 App 添加文稿浏览器
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adding-a-document-browser-to-your-app
source_url: 'https://developer.apple.com/documentation/uikit/adding-a-document-browser-to-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adding-a-document-browser-to-your-app.json'
content_hash: 'sha256:95deb2beaa7c6570'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md)

# 为你的 App 添加文稿浏览器

让用户在你的 App 内访问其本地或远程文稿。

## 概述

当你的 App 的主要目的是浏览和处理文稿时，使用文稿浏览器视图控制器作为 App 视图层级结构的根。当某人选择一个文稿时，你从文稿浏览器模态地呈现其视图控制器。

> [!important] 重要
> 始终将 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 指定为 App 的根视图控制器。UIKit 不支持将文稿浏览器放置在导航控制器、标签页栏、拆分视图或模态呈现中。
>
> 如果你想从视图层级结构中的其他位置呈现文稿浏览器，请改用 [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md)。

浏览器会自动为用户提供通过共享按钮或拖放操作共享文稿的选项。它还提供用于浏览和管理文稿的标准界面。

你在浏览器首次创建时设置某人可选择的文稿类型。你还可以设置浏览器的外观、修改其行为并添加自定操作。

## 主题

### 配置

- [Setting up a document browser app](setting-up-a-document-browser-app.md) — 向 App 添加文稿浏览器视图控制器。
- [Presenting selected documents](presenting-selected-documents.md) — 在浏览器视图控制器之上显示用户选择的文稿。
- [Enabling document sharing](enabling-document-sharing.md) — 让用户能够在 App 中导入和导出文稿。

### 自定

- [Customizing the document browser](customizing-the-browser.md) — 自定文稿浏览器的外观与行为。
- [Adding custom actions and activities](adding-custom-actions-and-activities.md) — 添加自定文稿浏览器操作、活动与栏项。

## 另请参阅

### 文稿与目录

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md) — 为 App 的文稿启动场景添加独特元素。
- [Providing access to directories](providing-access-to-directories.md) — 使用文稿选取器访问 App 容器之外的目录内容。
- [Building an app with a document browser](building-an-app-with-a-document-browser.md) — 通过向 App 添加文稿浏览器来提供对设备端和云端文件的访问。
- [Building a document browser app for custom file formats](building-a-document-browser-app-for-custom-file-formats.md) — 实现自定文稿文件格式，以管理用户与不同云存储提供商上文件的交互。
- [UIDocumentViewController](uidocumentviewcontroller.md) — 管理并呈现存储在本地或云端的文稿的视图控制器。
- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) — 用于浏览和对本地及云端存储的文稿执行操作的视图控制器。
- [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) — 提供对 App 沙盒之外的文稿或目的地的访问的视图控制器。
- [UIDocumentInteractionController](uidocumentinteractioncontroller.md) — 预览、打开或打印 App 无法直接处理的文件格式的视图控制器。
