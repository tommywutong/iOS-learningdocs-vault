---
title: 呈现选中的文稿
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/presenting-selected-documents
source_url: 'https://developer.apple.com/documentation/uikit/presenting-selected-documents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/presenting-selected-documents.json'
content_hash: 'sha256:527b1d2989532aef'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [Adding a document browser to your app](adding-a-document-browser-to-your-app.md)

# 呈现选中的文稿

<sub>文章</sub>

在你的浏览器视图控制器之上显示用户选中的文稿。

## 概述

当用户在浏览器视图控制器中选择一个或多个文稿时，系统会调用你的 delegate 的 [- documentBrowser:didPickDocumentURLs:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didpickdocumenturls_).md>) 方法。

### 使用文稿视图控制器显示文稿

在你的 [- documentBrowser:didPickDocumentURLs:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didpickdocumenturls_).md>) 方法实现中，通过调用浏览器的 [- presentViewController:animated:completion:](<uiviewcontroller/present(__animated_completion_).md>) 方法，模态呈现一个视图控制器来显示选中的文稿。

文稿视图应该填充整个屏幕，但它可以拥有自己的拆分视图控制器、导航控制器或标签控制器（视情况而定）。只要用户正在与文稿交互，它就保持在屏幕上。要返回到浏览器，关闭文稿视图控制器。

## 另请参阅

### Configuration

- [Setting up a document browser app](setting-up-a-document-browser-app.md) — 向你的 App 添加文稿浏览器视图控制器。
- [Enabling document sharing](enabling-document-sharing.md) — 给予用户从你的 App 导入和导出文稿的能力。
