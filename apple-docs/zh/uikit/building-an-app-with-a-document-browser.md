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

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图控制器](view-controllers.md)

# 使用文稿浏览器构建 App

<sub>示例代码</sub>

通过为你的 App 添加文稿浏览器，提供对设备端和云端文件的访问。

## 概述

文稿浏览器（Document Browser）示例代码使用 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 作为 App 的根视图控制器。浏览器定义了 App 的结构，App 在启动时会显示浏览器视图。用户随后可以用浏览器：

- 浏览用户设备上、其 iCloud Drive 中以及任何受支持的第三方文件提供方上的所有文本文件。
- 创建新的文本文件。
- 打开文本文件。

当用户打开一个文件时，App 会切换到编辑器视图。用户可以在其中编辑并保存文本文件。编辑完成后，App 会返回浏览器，让用户打开或创建另一个文件。

这份示例代码项目演示了设置文稿浏览器、处理用户文件以及启用系统动画所需的全部步骤。以下各节更详细地描述了这些步骤。

### 设置文稿浏览器

文稿浏览器 App 执行以下设置与配置步骤：

1. 将一个 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 子类指定为窗口的 [rootViewController](uiwindow/rootviewcontroller.md)。
2. 指定支持的文稿类型。
3. 自定义文稿浏览器的行为。

基于文稿浏览器的 App 会将一个 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 实例指定为 App 的 [rootViewController](uiwindow/rootviewcontroller.md)，确保浏览器在整个 App 生命周期内都驻留在内存中。

示例代码定义了一个名为 `DocumentBrowserViewController` 的 `UIDocumentBrowserViewController` 子类。然后，它在 `Main.storyboard` storyboard 中把这个子类标记为 App 的初始视图控制器，并在启动时显示浏览器视图。

基于文稿浏览器的 App 还要声明它们能打开的文稿类型。示例代码 App 在项目编辑器的 Info 面板中声明了对文本文件的支持。有关设置文稿类型的更多信息，请参阅[设置文稿浏览器 App](setting-up-a-document-browser-app.md)。

最后，示例代码在 `DocumentBrowserViewController` 类的 `viewDidLoad()` 方法中配置文稿浏览器。具体来说，它启用了文稿创建，并禁用了多文稿选择。这让用户能够从浏览器创建新文稿，同时防止他们一次打开多个文稿。

```swift
allowsDocumentCreation = true
allowsPickingMultipleItems = false
```

有关配置文稿浏览器的更多信息，请参阅[自定义文稿浏览器](customizing-the-browser.md)。

### 创建新文稿

当用户创建新文稿时，系统会调用文稿浏览器委托（delegate）的 [- documentBrowser:didRequestDocumentCreationWithHandler:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didrequestdocumentcreationwithhandler_).md>) 方法。

```swift
// 创建新文稿。
func documentBrowser(_ controller: UIDocumentBrowserViewController,
                     didRequestDocumentCreationWithHandler importHandler: @escaping (URL?, UIDocumentBrowserViewController.ImportMode) -> Void) {
    
    os_log("==> Creating A New Document.", log: .default, type: .debug)
    
    let doc = TextDocument()
    let url = doc.fileURL
    
    // 在临时位置创建一个新文稿。
    doc.save(to: url, for: .forCreating) { (saveSuccess) in
        
        // 确保文稿已成功保存。
        guard saveSuccess else {
            os_log("*** Unable to create a new document. ***", log: .default, type: .error)
            
            // 取消文稿创建。
            importHandler(nil, .none)
            return
        }
        
        // 关闭文稿。
        doc.close(completionHandler: { (closeSuccess) in
            
            // 确保文稿已成功关闭。
            guard closeSuccess else {
                os_log("*** Unable to create a new document. ***", log: .default, type: .error)
                
                // 取消文稿创建。
                importHandler(nil, .none)
                return
            }
            
            // 把文稿的临时 URL 传递给导入处理程序。
            importHandler(url, .move)
        })
    }
}
```

在这个方法中，App 会创建、保存然后关闭一个新的文本文稿。如果成功，App 会把 URL 传递给该方法的导入处理程序（import handler），请求系统把文稿移动到它的最终位置；否则，它会把 `nil` 传递给导入处理程序，取消文稿创建。

### 打开和导入文稿

用户可以通过多种方式打开文稿。示例代码处理以下几种情况：

- 如果 App 导入了一个文稿（包括成功创建新文稿），系统会调用 [- documentBrowser:didImportDocumentAtURL:toDestinationURL:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didimportdocumentat_todestinationurl_).md>) 方法。
- 如果用户从浏览器中选定了一个文稿，系统会调用 [- documentBrowser:didPickDocumentURLs:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didpickdocumenturls_).md>) 方法。
- 如果用户与 App 共享了一个文稿，或者把文稿拖入 App，系统会调用 App 委托的 [- application:openURL:options:](<uiapplicationdelegate/application(__open_options_).md>) 方法。

在前两种情况下，App 会调用自定义的 `presentDocuments(at:)` 方法。在第三种情况下，App 会调用浏览器的 [- revealDocumentAtURL:importIfNeeded:completion:](<uidocumentbrowserviewcontroller/revealdocument(at_importifneeded_completion_).md>) 方法在需要时导入文稿，然后调用 `presentDocuments(at:)` 方法。

`presentDocuments(at:)` 方法会实例化一个 `TextDocumentViewController`，设置文稿的动画，打开文稿，然后通过调用浏览器的 [- presentViewController:animated:completion:](<uiviewcontroller/present(__animated_completion_).md>) 方法来呈现该视图控制器。

### 启用动画

文稿浏览器提供两种内置动画：一种用于加载文件，另一种用于进入和离开文稿视图的转场。

要启用系统提供的任何一种文稿浏览器动画，首先需要通过调用 [- transitionControllerForDocumentURL:](<uidocumentbrowserviewcontroller/transitioncontroller(fordocumenturl_).md>) 方法为文稿请求一个转场控制器（transition controller）。

```swift
transitionController = transitionController(forDocumentAt: documentURL)
```

要启用加载动画，请在开始加载文稿时把一个 [Progress](../foundation/progress.md) 对象赋给转场控制器。

```swift
// 设置加载动画。
transitionController!.loadingProgress = doc.loadProgress
```

在文稿加载的过程中递增进度，并确保加载一完成就把它标记为已完成。要在示例代码项目中模拟缓慢的渐进式加载，请取消对 `TextDocument` 类的 `read(from:)` 方法的注释。

## 另请参阅

### 文稿与目录

- [自定义基于文稿的 App 的启动体验](customizing-a-document-based-app-s-launch-experience.md) — 为你的 App 的文稿启动场景添加独特元素。
- [在你的 App 中添加文稿浏览器](adding-a-document-browser-to-your-app.md) — 让用户在你的 App 内访问他们的本地或远程文稿。
- [提供对目录的访问](providing-access-to-directories.md) — 使用文稿选择器（document picker）访问你的 App 容器之外的目录内容。
- [为自定义文件格式构建文稿浏览器 App](building-a-document-browser-app-for-custom-file-formats.md) — 实现自定义文稿文件格式，管理用户与不同云存储提供商上文件的交互。
- [UIDocumentViewController](uidocumentviewcontroller.md) — 管理并呈现存储在本地或云端的文稿的视图控制器。
- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) — 用于浏览你存储在本地和云端的文稿并对其执行操作的视图控制器。
- [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) — 提供对你 App 沙盒之外的文稿或目的地的访问的视图控制器。
- [UIDocumentInteractionController](uidocumentinteractioncontroller.md) — 预览、打开或打印其文件格式无法被你的 App 直接处理的文件的视图控制器。

## 下载

- [BuildingAnAppWithADocumentBrowser.zip](https://docs-assets.developer.apple.com/published/af1183140aac/BuildingAnAppWithADocumentBrowser.zip)
