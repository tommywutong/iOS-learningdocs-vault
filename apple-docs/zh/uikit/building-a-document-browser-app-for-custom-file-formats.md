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

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图控制器](view-controllers.md)

# 为自定义文件格式构建文稿浏览器 App

<sub>文章</sub>

实现自定义文稿文件格式，管理用户与不同云存储提供商上文件的交互。

## 概述

用户可以把文稿存储在 iCloud Drive 等云存储提供商（file provider）那里。基于文稿浏览器视图控制器（document browser view controller）的 App 让用户无论文稿存储在哪里，都能浏览和访问它们。此外，文稿浏览器视图控制器还让用户能创建新文稿，并充当进入你 App 主用户界面的跳板。

这个示例 App 演示了如何使用文稿浏览器视图控制器。它在系统中注册了一个名为 Particles 的自定义文件格式，允许用户在用户已启用的任何文件提供方上创建新的 Particles 文稿。当用户选定一个文稿时，App 会呈现一个编辑视图，用户可以在其中修改文稿内容。用户完成修改后，系统保存文件，用户回到文稿浏览器视图控制器。

这个 App 还演示了如何用 [UIDocument](uidocument.md) 类正确处理文件，并为 Particles 文件格式构建 Quick Look 预览与缩略图扩展。最后，本示例展示了如何自定义文稿浏览器视图控制器的外观、自定义浏览器操作，以及用自定义缩放转场呈现文稿视图控制器。

[UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 和这个 Particles App 要求至少 iOS 13.2。

### 配置示例代码项目

Xcode 为创建基于文稿的 App 提供了 Document Based App 模板。这个模板自带从零实现一个基于文稿的 App 所需的一切。

选定模板后，项目会提供一个 storyboard，它以一个 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 作为入口。此外，模板会创建一个 [UIDocument](uidocument.md) 子类 Document，在运行时充当你的 App 的文稿的表示。创建新文稿的逻辑已经就位。当用户创建新文稿，或在文稿浏览器视图控制器中轻点文件打开现有文稿时，系统会呈现一个 `DocumentViewController`，它持有一个 `Document` 实例的引用。这个 `DocumentViewController` 充当查看和修改文稿内容的主用户界面。

> [!note] 注意
> 如果你想把现有的基于文稿的 App 迁移为使用 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md)，请确保把文稿浏览器视图控制器全屏呈现，作为用户启动你的 App 时看到的第一个用户界面。并确保实现 [UIDocumentBrowserViewControllerDelegate](uidocumentbrowserviewcontrollerdelegate.md) 协议，把它的一个实例赋给文稿浏览器视图控制器。

接下来，你可以扩展项目以满足自己的需要。在你的 App 导出的统一类型标识符（Uniform Type Identifiers，UTI）中设置一个自定义文件格式，或在导入的 UTI 部分配置一个或多个现有 UTI。App 的文稿类型也需要配置，这样文稿浏览器视图控制器才能向用户显示正确的文件。

再接下来，提供用户创建新文稿时的起始文稿；例如，从 App bundle 中拷贝一个代表新文稿空白版本的文件。通过导入处理程序把这个空白文件交给文稿浏览器视图控制器。为了提供恰当的文稿保存与加载，请为 [UIDocument](uidocument.md) 子类补充正确编码与解码文稿数据所需的逻辑。

最后，你可以配置文稿浏览器视图控制器，在用户一次选中一个或多个文稿，或长按文稿呼出菜单时，向用户显示自定义浏览器操作。

### 为视图控制器转场添加动画

在创建新文稿或选择现有文稿之后呈现文稿视图控制器时，转场控制器可以用优雅的缩放转场为视图控制器切换添加动画。

[UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 类提供了一个获取转场控制器的方法。转场控制器持有对一个文稿的引用，这样它的缩略图就能用作动画的起点或终点。

为文稿视图控制器（显示文稿内容的那个视图控制器）指定一个转场委托对象。转场委托需要遵循 [UIViewControllerTransitioningDelegate](uiviewcontrollertransitioningdelegate.md) 协议。系统即将呈现或关闭该视图控制器时会向委托索要动画控制器。委托返回一个从文稿浏览器视图控制器取得的转场控制器。转场控制器在打开或关闭文稿时显示缩放动画。

### 配置自定义文件格式

本示例引入了一个名为 Particles 的自定义文件格式。Particles 文件使用 `.particles` 扩展名。为了注册这个文件格式，示例在 target 的 Info 面板中同时修改了导出的 UTI 和文稿类型。

- 在导出的 UTI 部分，示例项目把 Particles 文稿定义为遵循 `public.data, public.content`。这一条目向系统注册了该文件格式。
- 在“Additional exported UTI properties”下，示例项目定义了 `UTTypeTagSpecification` 字典，其中 `public.filename-extension` 键的值为 `particles`。这一条目把 `particles` 设为文稿的扩展名。
- 在 Document Types 部分，示例项目同样定义了 Particles 文稿，让 App 的文稿浏览器能够支持 Particles 文稿。
- 由于这个 App 创建了该文件格式，在“Additional document type properties”下，它把 `LSHandlerRank` 设为 `Owner`。

### 预览自定义文稿

本示例提供了两个 Quick Look 扩展：

- `ParticlesPreview` 扩展，生成预览视图。
- `ParticlesThumbnails` 扩展，为新注册文件格式的文件生成缩略图。

为了让 Quick Look 在处理 Particles 文稿时选中这些扩展，两个扩展的 `Info.plist` 文件都配置了 Particles 文件格式数据。

### 应用最佳实践

只要可能，请用 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 和 [UIDocument](uidocument.md) 子类来创建基于文稿的 App。[UIDocument](uidocument.md) 类提供了基于文稿的 App 常见的那些功能，例如保存和加载文稿、异步读写数据、带冲突检测的版本管理等等。此外，[UIDocument](uidocument.md) 还提供了自动协调读写的能力，避免在访问磁盘上可能同时被其他进程读写的文件时出问题。如果要手动访问文件，请使用文件协调（file coordination）以免丢失数据。

避免在为 App 配置的文稿类型中列出高层级 UTI。只列出 App 真正能处理的 UTI。否则，文稿浏览器视图控制器可能在与用户无关的“最近使用”板块、搜索结果或其他位置显示不支持的文件格式的文件。

正确配置 App 的 `Info.plist` 文件中的文稿类型以及导出和导入的 UTI。"最近文稿"这类动态板块、带标签的文稿集合，以及 App 的弹出窗口，都需要这些信息才能正常工作。

最后，重要的是知道何时该使用选择器视图控制器（picker view controller）。[UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) 和 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 是两个不同的视图控制器，各有用途。使用 [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) 让用户快速选取一个现有文件，例如插入当前打开的文稿，或把文稿导出到某个位置。使用 [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) 作为 App 的入口，让用户创建新文稿或选择现有文稿。

## 另请参阅

### 文稿与目录

- [自定义基于文稿的 App 的启动体验](customizing-a-document-based-app-s-launch-experience.md) — 为你的 App 的文稿启动场景添加独特元素。
- [向你的 App 添加文稿浏览器](adding-a-document-browser-to-your-app.md) — 让用户在你的 App 内访问他们的本地或远程文稿。
- [提供对目录的访问](providing-access-to-directories.md) — 使用文稿选择器访问 App 容器之外的目录内容。
- [使用文稿浏览器构建 App](building-an-app-with-a-document-browser.md) — 通过为你的 App 添加文稿浏览器，提供对设备端和云端文件的访问。
- [UIDocumentViewController](uidocumentviewcontroller.md) — 管理并呈现存储在本地或云端的文稿的视图控制器。
- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) — 用于浏览你存储在本地和云端的文稿并对其执行操作的视图控制器。
- [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) — 提供对你 App 沙盒之外的文稿或目的地的访问的视图控制器。
- [UIDocumentInteractionController](uidocumentinteractioncontroller.md) — 预览、打开或打印你的 App 无法直接处理的文件格式的文件的视图控制器。

## 下载

- [BuildingADocumentBrowserAppForCustomFileFormats.zip](https://docs-assets.developer.apple.com/published/25972df8148a/BuildingADocumentBrowserAppForCustomFileFormats.zip)
