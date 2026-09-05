---
title: 自定义文稿浏览器
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/customizing-the-browser
source_url: 'https://developer.apple.com/documentation/uikit/customizing-the-browser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/customizing-the-browser.json'
content_hash: 'sha256:1ccbde8dc9f6d171'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图控制器](view-controllers.md) · [在你的 App 中添加文稿浏览器](adding-a-document-browser-to-your-app.md)

# 自定义文稿浏览器

<sub>文章</sub>

自定义文稿浏览器的外观与行为。

## 概述

你可以设置浏览器的外观、创建文稿缩略图，并修改浏览器的行为。

### 设置浏览器的外观

通过设置 [browserUserInterfaceStyle](uidocumentbrowserviewcontroller/browseruserinterfacestyle-swift.property.md) 属性来更改浏览器的外观。文稿浏览器视图控制器支持白色、浅色与深色三种外观。

### 创建文稿缩略图或图标

系统会自动为受支持的文稿类型提供缩略图或图标。如果你的 App 使用自定义或第三方的文稿类型，你可以为该类型创建一个 Thumbnail 扩展。更多信息参见 [QLThumbnailProvider](../quicklookthumbnailing/qlthumbnailprovider.md)。

如果你没有提供 Thumbnail 扩展，系统可以基于你的 App 图标创建一个文稿图标。要启用自动图标创建，前往项目导航器，选择 target，点按 Info，然后执行以下操作：

1. 在 Document Type 部分声明对该文稿的统一类型标识符（UTI）的支持。
2. 对你创建的任何自定义文稿类型，在 Exported Type Identifiers 部分导出该统一类型标识符。
3. 对你的 App 使用的任何第三方文稿类型，在 Imported Type Identifiers 部分导入该统一类型标识符。

更多信息参见[设置支持的文稿类型](setting-up-a-document-browser-app.md#Set-the-supported-document-types)。

只有当以下条件全部成立时，你的 App 图标才会出现在文件 App 或文稿浏览器中：

- 系统没有为该统一类型标识符自动提供缩略图。
- 系统尚未为该统一类型标识符提供图标。
- 用户没有为该统一类型标识符安装 Thumbnail 扩展。
- 你的 App 既声明了对该统一类型标识符的文稿类型支持，又把它声明为导出或导入的类型。

### 添加文稿预览

系统会自动为受支持的文稿类型提供预览。如果你的 App 使用自定义或第三方的文稿类型，你可以为该类型创建一个 Preview 扩展。

更多信息参见 [Quick Look](../quartz/quick-look.md)。

### 修改浏览器的行为

你可以控制以下行为：

- 浏览器打开的文稿类型
- 浏览器是否同时打开多个文件
- 浏览器是否创建新文稿

#### 设置允许的文稿类型

允许的文稿类型列表在你创建浏览器时设置。把统一类型标识符字符串组成的数组传给 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 类的 [- initForOpeningFilesWithContentTypes:](<uidocumentbrowserviewcontroller/init(foropeningfileswithcontenttypes_).md>) 方法。如果你传 `nil`，浏览器会使用 App 的 `Info.plist` 文件中 [CFBundleDocumentTypes](../bundleresources/information-property-list/cfbundledocumenttypes.md) 键指定的文稿类型。

关于设置 [CFBundleDocumentTypes](../bundleresources/information-property-list/cfbundledocumenttypes.md) 键的详细说明，参见[设置支持的文稿类型](setting-up-a-document-browser-app.md#Set-the-supported-document-types)。

下面的示例以编程方式创建一个面向 `.txt` 文件的文稿浏览器：

```swift
let browser = UIDocumentBrowserViewController(forOpeningFilesWithContentTypes: ["public.plain-text"])
```

#### 启用多选文稿

默认情况下，用户一次只能选择一个条目。要启用多选文稿，把文稿浏览器的 [allowsPickingMultipleItems](uidocumentbrowserviewcontroller/allowspickingmultipleitems.md) 属性设为 [true](../swift/true.md)。

#### 启用新文稿创建

要让用户创建新文稿，你必须做到以下两点：

- 把浏览器的 [allowsDocumentCreation](uidocumentbrowserviewcontroller/allowsdocumentcreation.md) 属性设为 [true](../swift/true.md)（默认值）。
- 实现 [UIDocumentBrowserViewControllerDelegate](uidocumentbrowserviewcontrollerdelegate.md) 对象的 [- documentBrowser:didRequestDocumentCreationWithHandler:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didrequestdocumentcreationwithhandler_).md>) 方法。

这些步骤完成后，系统会自动在文稿浏览器的导航栏中放入一个添加按钮 (+)。

当用户轻点添加按钮时，系统会调用 [- documentBrowser:didRequestDocumentCreationWithHandler:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didrequestdocumentcreationwithhandler_).md>) 方法。在实现中，你可以呈现一个自定义用户界面，让用户配置文稿。例如，你可以显示一个文稿模板列表。

创建一个新文稿并把它保存到临时位置。文稿一经保存，立即调用提供的 `importHandler`。要确认请求，传入文稿的临时 URL 和导入模式（[UIDocumentBrowserImportModeCopy](uidocumentbrowserviewcontroller/importmode/copy.md) 或 [UIDocumentBrowserImportModeMove](uidocumentbrowserviewcontroller/importmode/move.md)）。要取消请求，传入 `nil` 和 [UIDocumentBrowserImportModeNone](uidocumentbrowserviewcontroller/importmode/none.md)。

> [!important] 重要
> 你必须始终调用 `importHandler`。如果无法创建新文稿，URL 传入 `nil`，导入模式传入 [UIDocumentBrowserImportModeNone](uidocumentbrowserviewcontroller/importmode/none.md)。

## 另请参阅

### 自定义

- [添加自定义操作与活动](adding-custom-actions-and-activities.md) — 添加自定义文稿浏览器操作、活动和栏按钮项。
