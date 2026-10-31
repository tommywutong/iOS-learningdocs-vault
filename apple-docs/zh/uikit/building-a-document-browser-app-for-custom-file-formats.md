---
title: 为自定义文件格式构建文稿浏览器 App
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, Xcode 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/building-a-document-browser-app-for-custom-file-formats
source_url: 'https://developer.apple.com/documentation/uikit/building-a-document-browser-app-for-custom-file-formats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/building-a-document-browser-app-for-custom-file-formats.json'
content_hash: 'sha256:00cb84ae07c6ad6d'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md)

# 为自定义文件格式构建文稿浏览器 App

<sub>示例代码</sub>

实现自定义文稿文件格式，以管理用户与不同云存储提供商上文件的交互。

## 概述

用户可以将文稿存储在云存储提供商上，例如 iCloud Drive。基于文稿浏览器视图控制器的 App 允许用户浏览并访问其文稿，无论这些文稿存储在哪里。此外，文稿浏览器视图控制器还允许用户创建新文稿，并作为进入你的 App 主用户界面的跳板。

此示例 App 演示如何使用文稿浏览器视图控制器。它在系统中注册了一种名为 Particles 的自定义文件格式，并允许用户在用户已激活的任何文件提供商上创建新的 Particles 文稿。当用户选择一个文稿时，App 会呈现一个编辑器视图，用户可以在其中修改文稿的内容。当用户完成修改后，系统会保存文件，用户返回到文稿浏览器视图控制器。

该 App 还演示了使用 [UIDocument](uidocument.md) 类进行正确的文件处理，并为 Particles 文件格式构建了 Quick Look 预览和缩略图扩展。最后，此示例演示如何自定义文稿浏览器视图控制器的外观、自定义浏览器操作，以及使用自定义缩放过渡来呈现文稿视图控制器。

[UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 和此 Particles App 至少需要 iOS 13.2。

### 配置示例代码项目

Xcode 提供了 Document Based App 模板，用于创建基于文稿的 App。此模板包含从头实现基于文稿的 App 所需的一切。

选择模板后，项目会提供一个 storyboard，它使用 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 作为入口点。此外，模板会创建一个 [UIDocument](uidocument.md) 子类 Document，它作为你的 App 在运行时的文稿表示。创建新文稿的逻辑已经就位。当用户创建新文稿，或通过在文稿浏览器视图控制器中轻点文件来打开现有文稿时，系统会呈现一个 `DocumentViewController`，它引用一个 `Document` 实例。此 `DocumentViewController` 作为查看和修改文稿内容的主用户界面。

> [!note] 注意
> 如果你想迁移现有的基于文稿的 App 以使用 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md)，请确保在启动 App 时全屏呈现文稿浏览器视图控制器，作为用户看到的第一个用户界面。确保实现 [UIDocumentBrowserViewControllerDelegate](uidocumentbrowserviewcontrollerdelegate.md) 协议，并将其实例分配给文稿浏览器视图控制器。

接下来，你可以扩展项目以满足你的需求。在 App 的导出统一类型标识符（UTI）中设置自定义文件格式，或在导入的 UTI 部分配置一个或多个现有 UTI。App 的文稿类型也需要配置，以便文稿浏览器视图控制器可以向用户显示正确的文件。

接下来，提供用户创建新文稿时的起始文稿；例如，通过从 App bundle 复制一个文件，该文件代表新文稿的空白版本。通过导入处理程序将空白文件交给文稿浏览器视图控制器。为了提供正确的文稿保存和加载，请用正确编码和解码文稿数据所需的逻辑来增强 [UIDocument](uidocument.md) 子类。

最后，你可以配置文稿浏览器视图控制器，在用户同时选择一个或多个文稿时，或长按文稿以显示菜单时，向用户显示自定义浏览器操作。

### 为视图控制器过渡添加动画

在创建新文稿或选择现有文稿后呈现文稿视图控制器时，过渡控制器可以用优雅的缩放过渡来动画化视图控制器的更改。

[UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 类提供了一个方法来获取过渡控制器。过渡控制器引用一个文稿，以便其缩略图可以用作动画的起点或终点。

将过渡 delegate 对象分配给文稿视图控制器（显示文稿内容的视图控制器）。该过渡 delegate 需要符合 [UIViewControllerTransitioningDelegate](uiviewcontrollertransitioningdelegate.md) 协议。当系统即将呈现或关闭视图控制器时，它会询问 delegate 获取动画控制器。delegate 返回从文稿浏览器视图控制器获取的过渡控制器。过渡控制器在打开或关闭文稿时显示缩放动画。

### 配置自定义文件格式

此示例引入了一种名为 Particles 的自定义文件格式。Particles 文件使用 `.particles` 扩展名。为了注册该文件格式，示例修改了目标 Info 面板中的 Exported UTIs 和 Document Types。

- 在 Exported UTIs 部分，示例项目将 Particles 文稿定义为符合 `public.data, public.content`。此条目向系统注册该文件格式。
- 在 “Additional exported UTI properties” 下，示例项目定义了 `UTTypeTagSpecification` 字典，其中包含 `public.filename-extension` 键，值为 `particles`。此条目将 `particles` 设置为文稿的扩展名。
- 在 Document Types 部分，示例项目还定义了 Particles 文稿，从而在 App 的文稿浏览器中启用对 Particle 文稿的支持。
- 因为此 App 创建了该文件格式，在 “Additional document type properties” 下，它将 `LSHandlerRank` 设置为 `Owner`。

### 预览自定义文稿

示例提供了两个 Quick Look 扩展：

- `ParticlesPreview` 扩展，生成预览视图。
- `ParticlesThumbnails` 扩展，为新注册的文件格式的文件生成缩略图。

为了让 Quick Look 在处理 Particles 文稿时选择这些扩展，两个扩展的 `Info.plist` 文件都配置了 Particles 文件格式数据。

### 应用最佳实践

只要可能，就使用 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 和 [UIDocument](uidocument.md) 子类来创建基于文稿的 App。[UIDocument](uidocument.md) 类提供了基于文稿的 App 常见期望的功能，例如保存和加载文稿、数据的异步读写、带冲突检测的版本控制，以及更多。此外，[UIDocument](uidocument.md) 提供了避免在同时可能被其他进程读取或写入的磁盘文件访问时出现问题所需的自动协调读写。要手动访问文件，请使用文件协调以避免数据丢失。

避免在为 App 配置的文稿类型中列出高级别 UTI。只列出 App 实际能处理的 UTI。否则，文稿浏览器视图控制器可能会在 Recents 部分、搜索结果或其他位置显示用户不相关的不支持的文件格式的文件。

在 App 的 `Info.plist` 文件中正确配置文稿类型以及导出和导入的 UTI。Recent Documents 等动态部分、已标记文稿的集合，以及 App 的弹出窗口需要这些信息才能正常工作。

最后，了解何时使用选择器视图控制器很重要。[UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) 和 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 是两个不同的视图控制器，各自有其用途。使用 [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) 让用户快速选择现有文件，例如插入到当前打开的文稿中，或将文稿导出到某个位置。使用 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 作为 App 的入口点，让用户创建新文稿或选择现有文稿。

## 另请参阅

### Documents and directories

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md) — 为你的 App 的文稿启动场景添加独特的元素。
- [Adding a document browser to your app](adding-a-document-browser-to-your-app.md) — 让人从你的 App 内访问其本地或远程文稿。
- [Providing access to directories](providing-access-to-directories.md) — 使用文稿选择器访问 App 容器外部的目录内容。
- [Building an app with a document browser](building-an-app-with-a-document-browser.md) — 通过向你的 App 添加文稿浏览器，提供对设备上和云端文件的访问。
- [UIDocumentViewController](uidocumentviewcontroller.md) — 管理并呈现存储在本地或云端的文稿的视图控制器。
- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) — 用于浏览和对本地及云端存储的文稿执行操作的视图控制器。
- [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) — 提供对 App 沙盒外部文稿或目标的访问的视图控制器。
- [UIDocumentInteractionController](uidocumentinteractioncontroller.md) — 预览、打开或打印 App 无法直接处理的文件格式的文件的视图控制器。

## 下载

- [BuildingADocumentBrowserAppForCustomFileFormats.zip](https://docs-assets.developer.apple.com/published/25972df8148a/BuildingADocumentBrowserAppForCustomFileFormats.zip)
