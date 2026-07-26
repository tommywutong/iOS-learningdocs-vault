---
title: 启用文稿共享
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/enabling-document-sharing
source_url: 'https://developer.apple.com/documentation/uikit/enabling-document-sharing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/enabling-document-sharing.json'
content_hash: 'sha256:f6f3fe4c64143df7'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [Adding a document browser to your app](adding-a-document-browser-to-your-app.md)

# 启用文稿共享

<sub>文章</sub>

让用户能够从你的 App 中导入和导出文稿。

## 概述

当用户点按分享按钮或执行拖放操作时，文稿浏览器会自动导出用户的文稿。

要导入文稿，你的 App 必须指定它支持的所有文稿类型。你通常在设置文稿浏览器时指定支持的文稿类型。有关更多信息，请参阅[设置支持的文稿类型](setting-up-a-document-browser-app.md#Set-the-supported-document-types)。

### 打开共享的文稿

如果用户从活动视图中选择了你的 App，系统会启动你的 App 并调用你的 App 委托的 [- application:openURL:options:](<uiapplicationdelegate/application(__open_options_).md>) 方法。实现此方法以调用文稿浏览器的 [- revealDocumentAtURL:importIfNeeded:completion:](<uidocumentbrowserviewcontroller/revealdocument(at_importifneeded_completion_).md>) 方法来显示并导入文稿，如以下示例所示：

```swift
func application(_ app: UIApplication, open inputURL: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
    
    // Reveal and import the document at the URL.
    guard let documentBrowserViewController = window?.rootViewController as? DocumentBrowserViewController else {
        fatalError("The root view is not a document browser!")
    }

    documentBrowserViewController.revealDocument(at: inputURL, importIfNeeded: true) { (revealedDocumentURL, error) in
        
        guard error == nil else {
            os_log("Failed to reveal the document at %@. Error: %@",
                   log: OSLog.default,
                   type: .error,
                   inputURL as CVarArg,
                   error! as CVarArg)
            return
        }
        
        guard let url = revealedDocumentURL else {
            os_log("No URL revealed",
                   log: OSLog.default,
                   type: .error)
            
            return
        }
        
        // You can do something
        // with the revealed document here.
        os_log("Revealed URL: %@",
               log: OSLog.default,
               type: .debug,
               url.path)
        
        // Present the Document View Controller for the revealed URL.
        documentBrowserViewController.presentDocument(at: revealedDocumentURL!)
    }

    return true
}    
```

如果导入成功，系统会调用你的文稿浏览器委托的 [- documentBrowser:didImportDocumentAtURL:toDestinationURL:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didimportdocumentat_todestinationurl_).md>) 方法。

## 另请参阅

### 配置

- [设置文稿浏览器 App](setting-up-a-document-browser-app.md) — 为你的 App 添加一个文稿浏览器视图控制器。
- [呈现选定的文稿](presenting-selected-documents.md) — 在你的浏览器视图控制器之上显示用户选定的文稿。
