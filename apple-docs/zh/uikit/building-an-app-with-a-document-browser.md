---
title: 使用文稿浏览器构建 App
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, Xcode 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/building-an-app-with-a-document-browser
source_url: 'https://developer.apple.com/documentation/uikit/building-an-app-with-a-document-browser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/building-an-app-with-a-document-browser.json'
content_hash: 'sha256:fc5a90b0bf47be68'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md)

# 使用文稿浏览器构建 App

<sub>示例代码</sub>

通过向你的 App 添加文稿浏览器，提供对设备上和云端文件的访问。

## 概述

Document Browser 示例代码使用 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 作为 App 的根视图控制器。浏览器定义了 App 的结构，App 在启动时显示浏览器视图。然后某人可以使用浏览器来：

- 浏览某人设备、iCloud Drive 或任何支持的第三方文件提供商上的所有文本文件。
- 创建新的文本文件。
- 打开文本文件。

当某人打开文件时，App 会过渡到编辑器视图。在那里，某人可以编辑并保存文本文件。编辑完成后，App 返回到浏览器，让某人打开或创建另一个文件。

此示例代码项目演示了设置文稿浏览器、与某人文件协作以及启用系统动画所需的所有步骤。以下部分更详细地描述这些步骤。

### 设置文稿浏览器

Document Browser App 执行以下设置和配置步骤：

1. 将 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 子类分配为窗口的 [rootViewController](uiwindow/rootviewcontroller.md)。
2. 指定支持的文稿类型。
3. 自定义文稿浏览器的行为。

基于文稿浏览器的 App 会将 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 实例分配为 App 的 [rootViewController](uiwindow/rootviewcontroller.md)，确保浏览器在 App 的整个生命周期内都保留在内存中。

示例代码定义了一个名为 `DocumentBrowserViewController` 的 `UIDocumentBrowserViewController` 子类。然后它在 `Main.storyboard` storyboard 中将该子类标记为 App 的初始视图控制器，并在启动时显示浏览器视图。

基于文稿浏览器的 App 还声明它们可以打开的文稿类型。示例代码 App 在项目编辑器的 Info 面板中声明对文本文件的支持。有关设置文稿类型的信息，参见 [Setting up a document browser app](setting-up-a-document-browser-app.md)。

最后，示例代码在 `DocumentBrowserViewController` 类的 `viewDidLoad()` 方法中配置文稿浏览器。具体来说，它启用文稿创建，并禁用多选文稿。这允许用户从浏览器创建新文稿，同时也防止他们一次打开多个文稿。

```swift
allowsDocumentCreation = true
allowsPickingMultipleItems = false
```

有关配置文稿浏览器的信息，参见 [Customizing the document browser](customizing-the-browser.md)。

### 创建新文稿

当用户创建新文稿时，系统会调用文稿浏览器 delegate 的 [- documentBrowser:didRequestDocumentCreationWithHandler:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didrequestdocumentcreationwithhandler_).md>) 方法。

```swift
// Create a new document.
func documentBrowser(_ controller: UIDocumentBrowserViewController,
                     didRequestDocumentCreationWithHandler importHandler: @escaping (URL?, UIDocumentBrowserViewController.ImportMode) -> Void) {
    
    os_log("==> Creating A New Document.", log: .default, type: .debug)
    
    let doc = TextDocument()
    let url = doc.fileURL
    
    // Create a new document in a temporary location.
    doc.save(to: url, for: .forCreating) { (saveSuccess) in
        
        // Make sure the document saved successfully.
        guard saveSuccess else {
            os_log("*** Unable to create a new document. ***", log: .default, type: .error)
            
            // Cancel document creation.
            importHandler(nil, .none)
            return
        }
        
        // Close the document.
        doc.close(completionHandler: { (closeSuccess) in
            
            // Make sure the document closed successfully.
            guard closeSuccess else {
                os_log("*** Unable to create a new document. ***", log: .default, type: .error)
                
                // Cancel document creation.
                importHandler(nil, .none)
                return
            }
            
            // Pass the document's temporary URL to the import handler.
            importHandler(url, .move)
        })
    }
}
```

在此方法中，App 创建、保存，然后关闭一个新的文本文稿。如果成功，App 会将 URL 传递给方法的 import handler，请求系统将文稿移动到其最终位置。否则，它会向 import handler 传递 `nil`，取消文稿创建。

### 打开和导入文稿

某人可以以多种方式打开文稿。示例代码处理以下情况：

- 如果 App 导入文稿（包括成功创建新文稿），系统会调用 [- documentBrowser:didImportDocumentAtURL:toDestinationURL:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didimportdocumentat_todestinationurl_).md>) 方法。
- 如果某人从浏览器中选择文稿，系统会调用 [- documentBrowser:didPickDocumentURLs:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didpickdocumenturls_).md>) 方法。
- 如果某人与 App 共享文稿，或拖动文稿到 App 中，系统会调用 App delegate 的 [- application:openURL:options:](<uiapplicationdelegate/application(__open_options_).md>) 方法。

在前两种情况下，App 调用自定义的 `presentDocuments(at:)` 方法。在第三种情况下，App 调用浏览器的 [- revealDocumentAtURL:importIfNeeded:completion:](<uidocumentbrowserviewcontroller/revealdocument(at_importifneeded_completion_).md>) 方法来导入文稿（如果需要）。然后它调用 `presentDocuments(at:)` 方法。

`presentDocuments(at:)` 方法实例化一个 `TextDocumentViewController`，设置文稿的动画，打开文稿，然后通过调用浏览器的 [- presentViewController:animated:completion:](<uiviewcontroller/present(__animated_completion_).md>) 方法呈现该视图控制器。

### 启用动画

文稿浏览器提供两种内置动画：一种用于加载文件，另一种用于过渡到文稿视图和从文稿视图返回。

要启用任一系统提供的文稿浏览器动画，首先需要通过调用 [- transitionControllerForDocumentURL:](<uidocumentbrowserviewcontroller/transitioncontroller(fordocumenturl_).md>) 方法为文稿请求过渡控制器。

```swift
transitionController = transitionController(forDocumentAt: documentURL)
```

要启用加载动画，请在开始加载文稿时为过渡控制器分配一个 [Progress](../foundation/progress.md) 对象。

```swift
// Set up the loading animation.
transitionController!.loadingProgress = doc.loadProgress
```

随着文稿加载递增进度，确保在加载完成后尽快将其标记为完成。为了在示例代码项目中模拟缓慢、增量的加载，取消注释 `TextDocument` 类的 `read(from:)` 方法。

## 另请参阅

### Documents and directories

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md) — 为你的 App 的文稿启动场景添加独特的元素。
- [Adding a document browser to your app](adding-a-document-browser-to-your-app.md) — 让人从你的 App 内访问其本地或远程文稿。
- [Providing access to directories](providing-access-to-directories.md) — 使用文稿选择器访问 App 容器外部的目录内容。
- [Building a document browser app for custom file formats](building-a-document-browser-app-for-custom-file-formats.md) — 实现自定义文稿文件格式，以管理用户与不同云存储提供商上文件的交互。
- [UIDocumentViewController](uidocumentviewcontroller.md) — 管理并呈现存储在本地或云端的文稿的视图控制器。
- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) — 用于浏览和对本地及云端存储的文稿执行操作的视图控制器。
- [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) — 提供对 App 沙盒外部文稿或目标的访问的视图控制器。
- [UIDocumentInteractionController](uidocumentinteractioncontroller.md) — 预览、打开或打印 App 无法直接处理的文件格式的文件的视图控制器。

## 下载

- [BuildingAnAppWithADocumentBrowser.zip](https://docs-assets.developer.apple.com/published/af1183140aac/BuildingAnAppWithADocumentBrowser.zip)
