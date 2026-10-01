---
title: 在你的 App 中添加文稿浏览器
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

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图控制器](view-controllers.md)

# 在你的 App 中添加文稿浏览器

让用户能够在你的 App 内访问他们的本地或远程文稿。

## 概述

当你的 App 的主要用途是浏览和处理文稿时，使用文稿浏览器视图控制器（document browser view controller）作为你 App 视图层级结构（view hierarchy）的根。当用户选择某个文稿时，你从文稿浏览器以模态方式呈现它的视图控制器。

> [!important] 重要
> 务必将 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 指定为你的 App 的根视图控制器。UIKit 不支持把文稿浏览器放进导览控制器（navigation controller）、标签页栏、拆分视图或模态呈现中。
>
> 如果你想从视图层级结构中的其他位置呈现文稿浏览器，请改用 [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md)。

浏览器会自动为用户提供使用 Share 按钮或拖放（drag and drop）操作来共享文稿的选项。它还为浏览和管理文稿提供了一个标准界面。

在首次创建浏览器时，你设置用户可以选择的文稿类型。你还可以设置浏览器的外观、修改其行为，并添加自定义操作。

## 主题

### 配置

- [设置文稿浏览器 App](setting-up-a-document-browser-app.md) — 为你的 App 添加一个文稿浏览器视图控制器。
- [呈现所选文稿](presenting-selected-documents.md) — 在你的浏览器视图控制器之上显示用户选中的文稿。
- [启用文稿共享](enabling-document-sharing.md) — 让用户能够从你的 App 中导入和导出文稿。

### 自定义

- [自定义文稿浏览器](customizing-the-browser.md) — 自定义文稿浏览器的外观和行为。
- [添加自定义操作和活动](adding-custom-actions-and-activities.md) — 添加自定义的文稿浏览器操作、活动和栏条目。

## 另请参阅

### 文稿与目录

- [自定义基于文稿的 App 的启动体验](customizing-a-document-based-app-s-launch-experience.md) — 为你的 App 的文稿启动场景添加独特的元素。
- [提供对目录的访问](providing-access-to-directories.md) — 使用文稿选择器（document picker）访问你的 App 容器之外的目录内容。
- [构建带文稿浏览器的 App](building-an-app-with-a-document-browser.md) — 通过在你的 App 中添加文稿浏览器，提供对设备端和云端文件的访问。
- [为自定义文件格式构建文稿浏览器 App](building-a-document-browser-app-for-custom-file-formats.md) — 实现一个自定义的文稿文件格式，管理用户与不同云存储服务商上文件的交互。
- [UIDocumentViewController](uidocumentviewcontroller.md) — 一个管理和呈现存储在本地或云端的文稿的视图控制器。
- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) — 一个用于浏览你存储在本地和云端的文稿并对其执行操作的视图控制器。
- [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) — 一个提供对你的 App 沙盒之外的文稿或目的地的访问的视图控制器。
- [UIDocumentInteractionController](uidocumentinteractioncontroller.md) — 一个预览、打开或打印你的 App 无法直接处理的文件格式的文件的视图控制器。
