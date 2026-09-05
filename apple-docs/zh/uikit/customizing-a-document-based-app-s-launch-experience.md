---
title: 自定义基于文稿的 App 的启动体验
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/customizing-a-document-based-app-s-launch-experience
source_url: 'https://developer.apple.com/documentation/uikit/customizing-a-document-based-app-s-launch-experience'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/customizing-a-document-based-app-s-launch-experience.json'
content_hash: 'sha256:231bc02c35e53b32'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图控制器](view-controllers.md)

# 自定义基于文稿的 App 的启动体验

<sub>文章</sub>

为你的 App 的文稿启动场景添加独特元素。

## 概述

在 iOS 18 及更高版本中，你可以为你的 App 自定义文稿浏览体验，例如设置标题和操作按钮、配置背景，以及向场景添加自定义素材。

> [!note] SwiftUI 等价实现
> 关于如何在 SwiftUI 中采用基于文稿的启动体验，请阅读[用 SwiftUI 构建基于文稿的 App](../swiftui/building-a-document-based-app-with-swiftui.md)。

### 搭建基于文稿的 App

要创建自定义的文稿启动体验，请按以下步骤操作：

- 在 App target 的 Info 标签页的 Document Types 部分声明你支持的文稿类型。
- 在 Info 标签页的 Custom iOS Target Properties 部分设置 Supports Document Browser 键（`UISupportsDocumentBrowser`）。
- 为你的 App 支持的每种文稿类型创建一个 [UIDocument](uidocument.md) 子类。
- 为你的 App 创建一个 [UIDocumentViewController](uidocumentviewcontroller.md) 子类，并让该子类遵循 [UIDocumentBrowserViewControllerDelegate](uidocumentbrowserviewcontrollerdelegate.md) 协议。
- 把你的文稿视图子类设为 App 的根视图控制器。另一种做法是把你的 [UIDocumentViewController](uidocumentviewcontroller.md) 子类嵌入一个导览控制器，再把它设为根视图控制器。
- 实现你的委托的 [- documentDidOpen](<uidocumentviewcontroller/documentdidopen().md>) 方法来配置你的文稿视图。
- 用文稿视图控制器的 [launchOptions](uidocumentviewcontroller/launchoptions-swift.property.md) 属性配置启动场景。

设置文稿类型时，要提供文稿的名称和统一类型标识符（UTI）。添加 [CFBundleTypeRole](../bundleresources/information-property-list/cfbundledocumenttypes/cfbundletyperole.md) 键，值为 `Viewer`（只读）或 `Editor`（如果你的 App 既读又写该文稿类型）。最后，添加一个 `UIDocumentClass` 键，把它的值设为该文稿类型对应的你的 [UIDocument](uidocument.md) 子类的名称。

![App target 的 Document Type 设置的 Xcode 屏幕快照。](../../../attachments/b3a10e8273a1a7f341470b1c696e8b21/customizing-a-document-based-app-s-launch-experience-1@2x.png)

实现 [- documentDidOpen](<uidocumentviewcontroller/documentdidopen().md>) 方法时，在更新视图之前先确认你持有有效的文稿和有效的视图。更多信息参见 [UIDocumentViewController](uidocumentviewcontroller.md)。

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    // 配置你的启动选项。
    mySetupTextView()
}

override func documentDidOpen() {
    mySetupTextView()
}

func mySetupTextView() {
    
    // 确保你持有有效的文稿。
    guard let document = document as? MyDocument else { return }
            
    // 确保你持有有效的视图。
    guard let view else { return }
    
    // 确保文稿已打开。
    guard !document.documentState.contains(.closed) else { return }

    // 配置视图。
    textView.text = document.text
}
```

### 创建新文稿

文稿查看器使用 app intent 来创建新文稿。它还使用 [CreationIntent](uidocument/creationintent.md) 结构来指定你的 App 创建文稿的各种方式。[UIDocument](uidocument.md) 已经提供了默认 intent 和对应的 `.default` 枚举值。

要添加你自己的 intent，先扩展 [CreationIntent](uidocument/creationintent.md) 并为你的 intent 添加值。

```swift
// 扩展创建 intent 枚举，为文稿创建添加自定义选项。
extension UIDocument.CreationIntent {
    static let template = UIDocument.CreationIntent("template")
}
```

然后调用 [UIDocument](uidocument.md) 类的 [+ createDocumentActionWithIntent:](<uidocumentviewcontroller/launchoptions-swift.class/createdocumentaction(withintent_).md>) 方法来创建该 intent。设置 intent 的标题，并把它赋给你的 [LaunchOptions](uidocumentviewcontroller/launchoptions-swift.class.md) 实例的 [primaryAction](uidocumentviewcontroller/launchoptions-swift.class/primaryaction.md) 或 [secondaryAction](uidocumentviewcontroller/launchoptions-swift.class/secondaryaction.md) 属性。默认情况下，系统会自动把文稿视图控制器的 [primaryAction](uidocumentviewcontroller/launchoptions-swift.class/primaryaction.md) 设为默认的创建文稿操作。

```swift
// 为次要操作提供一个操作。
let templateAction = LaunchOptions.createDocumentAction(withIntent: .template)

// 设置 intent 的标题。
templateAction.title = "Choose a Template"

// 把该 intent 加入一个操作。
launchOptions.secondaryAction = templateAction
```

最后，实现 [UIDocumentBrowserViewControllerDelegate](uidocumentbrowserviewcontrollerdelegate.md) 协议的 [- documentBrowser:didRequestDocumentCreationWithHandler:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didrequestdocumentcreationwithhandler_).md>) 方法。当某个操作触发创建文稿的 intent 时，系统会调用这个方法。在实现中，用控制器的 [activeDocumentCreationIntent](uidocumentbrowserviewcontroller/activedocumentcreationintent.md) 判断是哪个 intent。创建文稿，然后把 URL 和 [ImportMode](uidocumentbrowserviewcontroller/importmode.md) 传给 `intentHandler`。

```swift
override func documentBrowser(_ controller: UIDocumentBrowserViewController, didRequestDocumentCreationWithHandler importHandler: @escaping (URL?, UIDocumentBrowserViewController.ImportMode) -> Void) {

    switch controller.activeDocumentCreationIntent {
    case .template:
        
        // 让用户选择一个模板，并返回
        // 指向该模板的 URL。
        let templateURL = myPresentTemplateSelection()
        
        // 把 URL 传给导入处理程序。
        importHandler(templateURL, .copy)
        
    default:
        
        // 创建默认文稿。
        let newDocumentURL = myCreateEmptyDocument()
        
        // 把 URL 传给导入处理程序。
        importHandler(newDocumentURL, .move )
    }
}
```

### 自定义文稿浏览体验

在 iPad、iPhone 和 Vision Pro（针对兼容的 iPad App）上，系统会显示一个包含标题和各文稿创建按钮的启动场景，并以 sheet 的形式在这个视图之上显示文稿浏览器。使用文稿视图控制器的 [launchOptions](uidocumentviewcontroller/launchoptions-swift.property.md) 属性按如下方式自定义这个场景：

- 设置 [title](uidocumentviewcontroller/launchoptions-swift.class/title.md) 属性来更改标题视图中显示的名称。默认情况下，控制器使用你的 App 的名称。
- 修改 [background](uidocumentviewcontrollerlaunchoptions/background.md) 属性来配置场景的背景。
- 使用 [foregroundAccessoryView](uidocumentviewcontroller/launchoptions-swift.class/foregroundaccessoryview.md) 或 [backgroundAccessoryView](uidocumentviewcontroller/launchoptions-swift.class/backgroundaccessoryview.md) 把 [UIView](uiview.md) 对象放到标题视图的前面或后面。
- 设置 [primaryAction](uidocumentviewcontroller/launchoptions-swift.class/primaryaction.md) 或 [secondaryAction](uidocumentviewcontroller/launchoptions-swift.class/secondaryaction.md) 属性来向标题视图添加按钮。如果你不修改 [primaryAction](uidocumentviewcontroller/launchoptions-swift.class/primaryaction.md) 属性，控制器会添加一个 Create Document 按钮作为默认的主操作。
- 使用 [browserViewController](uidocumentviewcontroller/launchoptions-swift.class/browserviewcontroller.md) 访问并配置文稿浏览器控制器。

通常，你在视图控制器的 [- viewDidLoad](<uiviewcontroller/viewdidload().md>) 方法中配置启动选项。

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    // 把该视图控制器指定为浏览器委托。
    launchOptions.browserViewController.delegate = self
    
    // 自定义启动选项。
    launchOptions.title = "My Text Editor"
    launchOptions.background.backgroundColor = .darkGray
    
    // 为次要操作提供一个操作。
    let templateAction = LaunchOptions.createDocumentAction(withIntent: .template)
    templateAction.title = "Choose a Template"
    launchOptions.secondaryAction = templateAction
    
    mySetupTextView()
}
```

![](../../../attachments/95c56ba509e379d93b1a8858ce0cac70/customizing-a-document-based-app-s-launch-experience-2@2x.png)

<sub>文稿启动场景的屏幕快照，标题设为“My Text Editor”，带有默认主操作和一个自定义次要操作。</sub>

## 另请参阅

### 文稿与目录

- [向你的 App 添加文稿浏览器](adding-a-document-browser-to-your-app.md) — 让用户在你的 App 内访问他们的本地或远程文稿。
- [提供对目录的访问](providing-access-to-directories.md) — 使用文稿选择器（document picker）访问你的 App 容器之外的目录内容。
- [使用文稿浏览器构建 App](building-an-app-with-a-document-browser.md) — 通过为你的 App 添加文稿浏览器，提供对设备端和云端文稿的访问。
- [为自定义文件格式构建文稿浏览器 App](building-a-document-browser-app-for-custom-file-formats.md) — 实现自定义文稿文件格式，管理用户与不同云存储提供商上文件的交互。
- [UIDocumentViewController](uidocumentviewcontroller.md) — 管理并呈现存储在本地或云端的文稿的视图控制器。
- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) — 用于浏览你存储在本地和云端的文稿并对其执行操作的视图控制器。
- [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) — 提供对你 App 沙盒之外的文稿或目的地的访问的视图控制器。
- [UIDocumentInteractionController](uidocumentinteractioncontroller.md) — 预览、打开或打印你的 App 无法直接处理的文件格式的文稿的视图控制器。
